import pytest

from project.schemas import SeleccionResponseModel

SELECCIONES_URL = "/api/v1/selecciones"


class TestSeleccionClass:

    def test_create_seleccion(self, client, admin_login):
        response = client.post(f"{SELECCIONES_URL}/", json={"pais": "pais_test"},
                               headers={
                                   'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        new_seleccion = response.json()
        assert response.status_code == 200
        assert new_seleccion.get("pais") == "pais_test"

    def test_get_seleccion(self, client, seleccion_test):
        response = client.get(f"{SELECCIONES_URL}/{seleccion_test.get('id')}")

        seleccion = response.json()
        assert response.status_code == 200
        assert seleccion.get("id") == seleccion_test.get('id')
        assert seleccion.get("pais") == seleccion_test.get('pais')

    def test_get_seleccion_error404(self, client):
        response = client.get(f"{SELECCIONES_URL}/99999")

        assert response.status_code == 404
        assert response.json().get("detail") == "Selección no encontrada"

    def test_get_selecciones(self, client, seleccion_test):
        response = client.get(f"{SELECCIONES_URL}/")

        assert response.status_code == 200
        assert len(response.json()) == 1
        assert seleccion_test in response.json()

    @pytest.mark.parametrize("updated_pais, status_code", [
        ("pais_test_updated", 200),
        ("", 422),
        (None, 422),
    ])
    def test_update_seleccion(self, client, seleccion_test, admin_login, updated_pais, status_code):
        response = client.put(f"{SELECCIONES_URL}/{seleccion_test.get('id')}",
                              json={"pais": updated_pais},
                              headers={
                                  'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})
        assert response.status_code == status_code

    def test_update_seleccion_error404(self, client, admin_login):
        response = client.put(f"{SELECCIONES_URL}/99999",
                              json={"pais": "updated_pais"},
                              headers={
                                  'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})
        assert response.status_code == 404
        assert response.json().get("detail") == "Selección no encontrada"

    def test_delete_seleccion(self, client, seleccion_test, admin_login):
        response = client.delete(f"{SELECCIONES_URL}/{seleccion_test.get('id')}",
                                 headers={
                                     'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        assert response.status_code == 200
        assert response.json().get("id") == seleccion_test.get("id")
        assert response.json().get("pais") == seleccion_test.get("pais")

    def test_delete_seleccion_error404(self, client, admin_login):
        response = client.delete(f"{SELECCIONES_URL}/99999",
                                 headers={
                                     'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        assert response.status_code == 404
        assert response.json().get("detail") == "Selección no encontrada"
