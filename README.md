# API La ScalonetApp - Desplegada en [Heroku](https://api-scalonetapp.herokuapp.com/docs)

API para la aplicación web La ScalonetApp. Desarrollada en Python con el framework FastAPI y utilizando una base de datos relacional PostgreSQL.

## Modelos

* ### Selecciones
* ### Equipos
* ### Integrantes
* ### Roles
* ### Usuarios


## Seleciones

Representa a los países/selecciones que irán al mundial Qatar 2022.

* Atributos:
  * id (numero)
  * pais (texto)

* Métodos HTTP:
  * GET
  * POST (Protegido - Rol: Usuario Admin)
  * PUT (Protegido - Rol: Usuario Admin)
  * DELETE (Protegido - Rol: Usuario Admin)

## Equipos

Representa a los equipos de los integrantes de las selecciones.

* Atributos:
  * id (numero)
  * nombre (texto)

* Métodos HTTP:
  * GET
  * POST (Protegido - Rol: Usuario Admin)
  * PUT (Protegido - Rol: Usuario Admin)
  * DELETE (Protegido - Rol: Usuario Admin)

## Roles

Representa los roles de cada integrante de las selecciones.

* Atributos:
  * id (numero)
  * titulo (texto)

* Métodos HTTP:
  * GET
  * POST (Protegido - Rol: Usuario Admin)
  * PUT (Protegido - Rol: Usuario Admin)
  * DELETE (Protegido - Rol: Usuario Admin)

## Integrantes

Representa a los integrantes de las selecciones.

* Atributos:
  * id (numero)
  * nombre (texto)
  * apodo (texto)
  * apellido (texto)
  * edad (numero)
  * num_camiseta (numero)
  * seleccion (Seleccion)
  * equipo (Equipo)
  * rol (Rol)

* Métodos HTTP:
  * GET
  * POST (Protegido - Rol: Usuario Admin)
  * PUT (Protegido - Rol: Usuario Admin)
  * DELETE (Protegido - Rol: Usuario Admin)

## Usuarios

Representa a los usuarios de nuestra aplicación. La autenticación de los usuarios está implementada a través de Bearer Token con JWT con OAuth2

* Atributos:
  * id (numero)
  * email (texto)
  * password (texto - hashed)
  * is_admin (bool - default = False)
  * created_at (timestamp)

* Métodos HTTP:
  * GET
  * POST (Protegido - Rol: Usuario Admin)
  * PUT (Protegido - Rol: Usuario Admin)
  * DELETE (Protegido - Rol: Usuario Admin)