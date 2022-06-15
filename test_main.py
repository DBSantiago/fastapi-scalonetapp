import pytest

from project import app

from fastapi.testclient import TestClient

client = TestClient(app)

# ===========================================
#                 ROLES
# ===========================================
ROLES_URL = "/api/v1/roles"


class TestRolesClass:
    rol = {
        "titulo": "test_role_2"
    }

    def test_post_role(self):
        response = client.post(f"{ROLES_URL}/", json=TestRolesClass.rol)
        assert response.status_code == 200
        assert "titulo" in response.json()
        assert "test_role_2" in response.json().values()
        TestRolesClass.rol = response.json()

    def test_get_role(self):
        response = client.get(f"{ROLES_URL}/{TestRolesClass.rol['id']}")
        assert response.status_code == 200
        assert TestRolesClass.rol == response.json()

    def test_get_role_error404(self):
        response = client.get(f"{ROLES_URL}/99999")
        assert response.status_code == 404

    def test_get_roles(self):
        response = client.get(f"{ROLES_URL}/")
        assert response.status_code == 200
        assert TestRolesClass.rol in response.json()

    def test_update_role(self):
        updated_role = {
            "titulo": "test_role_changed"
        }
        response = client.put(f"{ROLES_URL}/{TestRolesClass.rol['id']}", json=updated_role)
        assert response.status_code == 200
        assert response.json()['id'] == TestRolesClass.rol['id']
        assert "test_role_changed" in response.json().values()

        TestRolesClass.rol = response.json()

    def test_update_role_error404(self):
        updated_role = {
            "titulo": "test_role_changed"
        }
        response = client.put(f"{ROLES_URL}/99999", json=updated_role)
        assert response.status_code == 404

    def test_delete_role(self):
        response = client.delete(f"{ROLES_URL}/{TestRolesClass.rol['id']}")
        assert response.status_code == 200
        assert response.json() == TestRolesClass.rol

    def test_delete_role_error404(self):
        response = client.delete(f"{ROLES_URL}/99999")
        assert response.status_code == 404


# ===========================================
#                 EQUIPOS
# ===========================================
EQUIPOS_URL = "/api/v1/equipos"


class TestEquiposClass:
    equipo = {
        "nombre": "equipo_test"
    }

    def test_create_equipo(self):
        response = client.post(f"{EQUIPOS_URL}/", json=TestEquiposClass.equipo)
        assert response.status_code == 200
        assert "nombre" in response.json()
        assert "equipo_test" in response.json().values()
        TestEquiposClass.equipo = response.json()

    def test_get_equipos(self):
        response = client.get(f"{EQUIPOS_URL}/")
        assert response.status_code == 200
        assert TestEquiposClass.equipo in response.json()

    def test_get_equipo(self):
        response = client.get(f"{EQUIPOS_URL}/{TestEquiposClass.equipo['id']}")
        assert response.status_code == 200
        assert TestEquiposClass.equipo == response.json()

    def test_get_equipo_error404(self):
        response = client.get(f"{EQUIPOS_URL}/99999")
        assert response.status_code == 404

    def test_update_equipo(self):
        updated_equipo = {
            "nombre": "equipo_test_changed"
        }
        response = client.put(f"{EQUIPOS_URL}/{TestEquiposClass.equipo['id']}", json=updated_equipo)
        assert response.status_code == 200
        assert TestEquiposClass.equipo['id'] == response.json()['id']
        assert "equipo_test_changed" == response.json()['nombre']
        TestEquiposClass.equipo = response.json()

    def test_update_equipo_error404(self):
        updated_equipo = {
            "nombre": "equipo_test_changed"
        }
        response = client.put(f"{EQUIPOS_URL}/99999", json=updated_equipo)
        assert response.status_code == 404

    def test_delete_equipo(self):
        response = client.delete(f"{EQUIPOS_URL}/{TestEquiposClass.equipo['id']}")
        assert response.status_code == 200
        assert TestEquiposClass.equipo == response.json()

    def test_delete_equipo_error404(self):
        response = client.delete(f"{EQUIPOS_URL}/99999")
        assert response.status_code == 404


# ===========================================
#                 SELECCIONES
# ===========================================
SELECCIONES_URL = "/api/v1/selecciones"


class TestSeleccionesClass:
    seleccion = {
        "pais": "seleccion_test"
    }

    def test_create_seleccion(self):
        response = client.post(f"{SELECCIONES_URL}/", json=TestSeleccionesClass.seleccion)
        assert response.status_code == 200
        assert "pais" in response.json()
        assert "seleccion_test" in response.json().values()
        TestSeleccionesClass.seleccion = response.json()

    def test_get_selecciones(self):
        response = client.get(f"{SELECCIONES_URL}/")
        assert response.status_code == 200
        assert TestSeleccionesClass.seleccion in response.json()

    def test_get_seleccion(self):
        response = client.get(f"{SELECCIONES_URL}/{TestSeleccionesClass.seleccion['id']}")
        assert response.status_code == 200
        assert TestSeleccionesClass.seleccion == response.json()

    def test_get_seleccion_error404(self):
        response = client.get(f"{SELECCIONES_URL}/99999")
        assert response.status_code == 404

    def test_update_seleccion(self):
        updated_seleccion = {
            "pais": "seleccion_test_changed"
        }
        response = client.put(f"{SELECCIONES_URL}/{TestSeleccionesClass.seleccion['id']}", json=updated_seleccion)
        assert response.status_code == 200
        assert TestSeleccionesClass.seleccion['id'] == response.json()['id']
        assert "seleccion_test_changed" == response.json()['pais']
        TestSeleccionesClass.seleccion = response.json()

    def test_update_seleccion_error404(self):
        updated_seleccion = {
            "pais": "seleccion_test_changed"
        }
        response = client.put(f"{SELECCIONES_URL}/99999", json=updated_seleccion)
        assert response.status_code == 404

    def test_delete_seleccion(self):
        response = client.delete(f"{SELECCIONES_URL}/{TestSeleccionesClass.seleccion['id']}")
        assert response.status_code == 200
        assert TestSeleccionesClass.seleccion == response.json()

    def test_delete_seleccion_error404(self):
        response = client.delete(f"{SELECCIONES_URL}/99999")
        assert response.status_code == 404


# ===========================================
#                 INTEGRANTES
# ===========================================
INTEGRANTES_URL = "/api/v1/integrantes"


class TestIntegrantesClass:
    integrante = {
        "nombre": "test_nombre",
        "apodo": "test_apodo",
        "apellido": "test_apellido",
        "edad": 30,
        "num_camiseta": 10,
        "seleccion_id": 1,
        "equipo_id": 1,
        "rol_id": 1
    }

    def test_create_integrante(self):
        response = client.post(f"{INTEGRANTES_URL}/", json=TestIntegrantesClass.integrante)
        assert response.status_code == 200
        assert "nombre" in response.json()
        assert "apodo" in response.json()
        assert "apellido" in response.json()
        assert "edad" in response.json()
        assert "num_camiseta" in response.json()
        assert "seleccion" in response.json()
        assert response.json()["seleccion"] is not None
        assert "equipo" in response.json()
        assert response.json()["equipo"] is not None
        assert "rol" in response.json()
        assert response.json()["rol"] is not None
        assert "test_nombre" in response.json().values()
        assert "test_apodo" in response.json().values()
        assert "test_apellido" in response.json().values()
        TestIntegrantesClass.integrante = response.json()

    def test_get_integrantes(self):
        response = client.get(f"{INTEGRANTES_URL}/")
        assert response.status_code == 200
        assert TestIntegrantesClass.integrante in response.json()

    def test_get_integrante(self):
        response = client.get(f"{INTEGRANTES_URL}/{TestIntegrantesClass.integrante['id']}")
        assert response.status_code == 200
        assert TestIntegrantesClass.integrante == response.json()

    def test_get_integrante_error404(self):
        response = client.get(f"{SELECCIONES_URL}/99999")
        assert response.status_code == 404

    def test_update_integrante(self):
        updated_integrante = {
            "nombre": "test_nombre_changed",
            "apodo": "test_apodo_changed",
            "apellido": "test_apellido_changed",
            "edad": 40,
            "num_camiseta": 0,
            "seleccion_id": 1,
            "equipo_id": 1,
            "rol_id": 1
        }
        response = client.put(f"{INTEGRANTES_URL}/{TestIntegrantesClass.integrante['id']}", json=updated_integrante)
        assert response.status_code == 200
        assert TestIntegrantesClass.integrante['id'] == response.json()['id']
        assert "test_nombre_changed" == response.json()['nombre']
        assert "test_apodo_changed" == response.json()['apodo']
        assert "test_apellido_changed" == response.json()['apellido']
        assert 40 == response.json()['edad']
        assert 0 == response.json()['num_camiseta']
        TestIntegrantesClass.integrante = response.json()

    def test_update_integrante_error404(self):
        updated_integrante = {
            "nombre": "test_nombre_changed",
            "apodo": "test_apodo_changed",
            "apellido": "test_apellido_changed",
            "edad": 40,
            "num_camiseta": 0,
            "seleccion_id": 1,
            "equipo_id": 1,
            "rol_id": 1
        }
        response = client.put(f"{INTEGRANTES_URL}/99999", json=updated_integrante)
        assert response.status_code == 404

    def test_delete_integrante(self):
        response = client.delete(f"{INTEGRANTES_URL}/{TestIntegrantesClass.integrante['id']}")
        assert response.status_code == 200

    def test_delete_integrante_error404(self):
        response = client.delete(f"{INTEGRANTES_URL}/99999")
        assert response.status_code == 404
