import pytest
from jose import jwt

EQUIPOS_URL = "/api/v1/equipos"


class TestEquipoClass:

    def test_create_equipo(self, client, admin_login):
        response = client.post(f"{EQUIPOS_URL}/",
                               json={"nombre": "equipo_test"},
                               headers={
                                   'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        new_equipo = response.json()
        assert response.status_code == 200
        assert new_equipo.get("nombre") == "equipo_test"

    def test_get_equipo(self, client, equipo_test):
        response = client.get(f"{EQUIPOS_URL}/{equipo_test.get('id')}")

        equipo = response.json()
        assert response.status_code == 200
        assert equipo.get("id") == equipo_test.get("id")
        assert equipo.get("nombre") == equipo_test.get("nombre")

    def test_get_equipo_error404(self, client):
        response = client.get(f"{EQUIPOS_URL}/99999")

        assert response.status_code == 404
        assert response.json().get("detail") == "Equipo no encontrado."

    def test_get_equipos(self, client, equipo_test):
        response = client.get(f"{EQUIPOS_URL}")

        assert response.status_code == 200
        assert len(response.json()) == 1
        assert equipo_test in response.json()

    @pytest.mark.parametrize("updated_nombre, status_code", [
        ("equipo_test_updated", 200),
        ("", 422),
        (None, 422),
    ])
    def test_update_equipo(self, client, equipo_test, admin_login, updated_nombre, status_code):
        response = client.put(f"{EQUIPOS_URL}/{equipo_test.get('id')}",
                              json={"nombre": updated_nombre},
                              headers={
                                  'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        assert response.status_code == status_code

    def test_update_equipo_error404(self, client, admin_login):
        response = client.put(f"{EQUIPOS_URL}/99999",
                              json={"nombre": "asdaasdasd"},
                              headers={
                                  'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        assert response.status_code == 404
        assert response.json().get("detail") == "Equipo no encontrado."

    def test_delete_equipo(self, client, equipo_test, admin_login):
        response = client.delete(f"{EQUIPOS_URL}/{equipo_test.get('id')}",
                                 headers={
                                     'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        assert response.status_code == 200
        assert response.json() == equipo_test

    def test_delete_equipo_error404(self, client, admin_login):
        response = client.delete(f"{EQUIPOS_URL}/99999",
                                 headers={
                                     'Authorization': f'{admin_login.token_type} {admin_login.access_token}'})

        assert response.status_code == 404
        assert response.json().get('detail') == "Equipo no encontrado."
