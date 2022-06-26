import pytest

ROLES_URL = "/api/v1/roles"


class TestRolClass:

    def test_create_rol(self, client, admin_login):
        response = client.post(f"{ROLES_URL}/", json={"titulo": "rol_test"},
                               headers={
                                   'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        assert response.status_code == 200
        assert response.json().get('titulo') == "rol_test"

    def test_get_rol(self, client, rol_test):
        response = client.get(f"{ROLES_URL}/{rol_test.get('id')}")

        assert response.status_code == 200
        assert response.json().get("id") == rol_test.get("id")
        assert response.json().get("titulo") == rol_test.get("titulo")

    def test_get_rol_error404(self, client):
        response = client.get(f"{ROLES_URL}/99999")

        assert response.status_code == 404
        assert response.json().get("detail") == "Rol no encontrado."

    def test_get_roles(self, client, rol_test):
        response = client.get(f"{ROLES_URL}/")

        assert response.status_code == 200
        assert len(response.json()) == 1
        assert rol_test in response.json()

    @pytest.mark.parametrize("updated_role, status_code", [
        ("pais_test_updated", 200),
        (None, 422),
    ])
    def test_update_rol(self, client, rol_test, admin_login, updated_role, status_code):
        response = client.put(f"{ROLES_URL}/{rol_test.get('id')}",
                              json={"titulo": updated_role},
                              headers={
                                  'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        assert response.status_code == status_code

    def test_update_rol_error404(self, client, admin_login):
        response = client.put(f"{ROLES_URL}/99999",
                              json={"titulo": "updated_role"},
                              headers={
                                  'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        assert response.status_code == 404
        assert response.json().get("detail") == "Rol no encontrado."

    def test_delete_rol(self, client, rol_test, admin_login):
        response = client.delete(f"{ROLES_URL}/{rol_test.get('id')}",
                                 headers={
                                     'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        assert response.status_code == 200
        assert response.json().get("id") == rol_test.get("id")
        assert response.json().get("titulo") == rol_test.get("titulo")

    def test_delete_rol_error404(self, client, admin_login):
        response = client.delete(f"{ROLES_URL}/99999",
                                 headers={
                                     'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        assert response.status_code == 404
        assert response.json().get("detail") == "Rol no encontrado."
