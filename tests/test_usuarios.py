import pytest
from decouple import config
from jose import jwt

from project.oauth2 import SECRET_KEY, ALGORITHM

from project.schemas import UsuarioResponseModel, Token
from project.utils import hash_password

ADMIN_EMAIL = config("ADMIN_EMAIL")
ADMIN_PASSWORD = hash_password(config("ADMIN_PASSWORD"))

USUARIOS_URL = "/api/v1/usuarios"
AUTH_URL = "/api/v1/auth/login"


class TestUsuarioClass:

    def test_create_usuario(self, client):
        response = client.post(f"{USUARIOS_URL}/", json={"email": "test2@email.com",
                                                         "password": "password"})
        new_usuario = UsuarioResponseModel(**response.json())
        assert response.status_code == 200
        assert new_usuario.email == "test2@email.com"

    def test_authenticate_usuario(self, client, usuario_test):
        response = client.post(f"{AUTH_URL}", data={"username": usuario_test.get("email"),
                                                    "password": usuario_test.get("password")})

        login_res = Token(**response.json())
        payload = jwt.decode(login_res.access_token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id = payload.get("usuario_id")

        assert response.status_code == 200
        assert login_res.token_type == "Bearer"
        assert usuario_id == usuario_test.get("id")

    @pytest.mark.parametrize("email, password, status_code", [
        ("wrong-email@email.com", "password123", 403),
        ("test@email.com", "wrong-password", 403),
        ("wrongemail@email.com", "wrong-password", 403),
        (None, "password123", 422),
        ("test@email.com", None, 422)
    ])
    def test_authenticate_usuario_failed(self, client, usuario_test, email, password, status_code):
        response = client.post(f"{AUTH_URL}", data={"username": email,
                                                    "password": password})
        assert response.status_code == status_code

    def test_get_usuario(self, client, usuario_test):
        response = client.get(f"{USUARIOS_URL}/{usuario_test.get('id')}")
        assert response.status_code == 200
        assert response.json().get("id") == usuario_test.get("id")
        assert response.json().get("email") == usuario_test.get("email")

    def test_get_usuario_error404(self, client):
        response = client.get(f"{USUARIOS_URL}/99999")
        assert response.status_code == 404
        assert response.json().get("detail") == "Usuario inexistente."

    @pytest.mark.parametrize("updated_email, updated_password", [
        ("updated-email@email.com", "password123"),
        ("test@email.com", "123password"),
        ("updated-email@email.com", "123password"),
    ])
    def test_update_usuario(self, client, usuario_test, usuario_login,
                            updated_email, updated_password):
        response = client.put(f"{USUARIOS_URL}/{usuario_test.get('id')}",
                              json={"email": updated_email, "password": updated_password},
                              headers={
                                  'Authorization': f'{usuario_login.token_type} {usuario_login.access_token}'})
        assert response.status_code == 200
        assert response.json().get("email") == updated_email
        assert response.json().get("id") == usuario_test.get("id")

    @pytest.mark.parametrize("email, password, status_code", [
        ("new-email@email.com", "password123", 200),
        ("test@email.com", "new-password", 200),
        ("new-email@email.com", "new-password", 200),
        (None, "password123", 422),
        ("test@email.com", None, 422)
    ])
    def test_update_usuario_error(self, client, usuario_test, usuario_login, email, password, status_code):
        response = client.put(f"{USUARIOS_URL}/{usuario_test.get('id')}",
                              json={"email": email, "password": password},
                              headers={
                                  'Authorization': f'{usuario_login.token_type} {usuario_login.access_token}'}
                              )
        assert response.status_code == status_code

    def test_delete_usuario(self, client, usuario_test, usuario_login):
        response = client.delete(f"{USUARIOS_URL}/{usuario_test.get('id')}",
                                 headers={
                                     'Authorization': f'{usuario_login.token_type} {usuario_login.access_token}'}
                                 )

        assert response.status_code == 200
        assert response.json() == {"OK": f"Usuario con id: {usuario_test.get('id')} eliminado exitosamente"}

    def test_delete_usuario_error404(self, client, usuario_test, usuario_login):
        response = client.delete(f"{USUARIOS_URL}/99999",
                                 headers={
                                     'Authorization': f'{usuario_login.token_type} {usuario_login.access_token}'}
                                 )

        assert response.status_code == 404
