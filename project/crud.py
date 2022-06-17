from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from project.models import Rol, Equipo, Seleccion, Integrante, Usuario
from project.schemas import RolBaseModel, EquipoBaseModel, SeleccionBaseModel, IntegranteBaseModel, UsuarioBaseModel

from project.utils import hash_password


# ================================
#           ROL
# ================================
def get_rol(db: Session, rol_id: int):
    """ Get a Rol object from our database given an id :rol_id:

    Args:
        db (Session): The database Session.
        rol_id (int): The Rol id.

    Returns:
        Rol object if found, None otherwise.
    """
    return db.query(Rol).filter(Rol.id == rol_id).first()


def get_roles(db: Session):
    """ Get all Rol objects from our database.

        Args:
            db (Session): The database Session.

        Returns:
            Rol objects if found, empty list otherwise.
        """
    return db.query(Rol).all()


def create_rol(db: Session, rol: RolBaseModel):
    """ Create a Rol in our database given the values in the :rol: param.

    Args:
        db (Session): The database Session.
        rol (RolBaseModel): The RolBaseModel to create a Rol in our database.

    Returns:
        Created Rol object.
    """
    db_rol = Rol(titulo=rol.titulo)
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)

    return db_rol


def update_rol(db: Session, rol: RolBaseModel, rol_id: int):
    """ Update a Rol in our database given the values in the :rol: param.

        Args:
            db (Session): The database Session.
            rol (RolBaseModel): The RolBaseModel to update a Rol in our database.
            rol_id (int): The Rol id passed as url param.

        Returns:
            Updated Rol object if found, None otherwise.
        """
    db_rol = db.get(Rol, rol_id)

    if db_rol is None:
        return db_rol

    db_rol.titulo = rol.titulo
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)

    return db_rol


def delete_rol(db: Session, rol_id: int):
    """ Delete a Rol in our database given an id :rol_id:

        Args:
            db (Session): The database Session.
            rol_id (int): The Rol id.

        Returns:
            Deleted Rol object if found, None otherwise.
        """
    db_rol = db.get(Rol, rol_id)

    if db_rol is None:
        return db_rol

    db.delete(db_rol)
    db.commit()

    return db_rol


# ================================
#           EQUIPO
# ================================
def get_equipo(db: Session, equipo_id: int):
    """ Get an Equipo object from our database given an id :equipo_id:

    Args:
        db (Session): The database Session.
        equipo_id (int): The Equipo id.

    Returns:
        Equipo object if found, None otherwise.
    """
    return db.query(Equipo).filter(Equipo.id == equipo_id).first()


def get_equipos(db: Session):
    """ Get all Equipo objects from our database.

        Args:
            db (Session): The database Session.

        Returns:
            Equipo objects if found, Empty List otherwise.
        """
    return db.query(Equipo).all()


def create_equipo(db: Session, equipo: EquipoBaseModel):
    """ Create a Equipo in our database given the values in the :equipo: param.

    Args:
        db (Session): The database Session.
        equipo (EquipoBaseModel): The EquipoBaseModel to create a Equipo in our database.

    Returns:
        Created Equipo object.
    """
    db_equipo = Equipo(nombre=equipo.nombre)
    db.add(db_equipo)
    db.commit()
    db.refresh(db_equipo)

    return db_equipo


def update_equipo(db: Session, equipo: EquipoBaseModel, equipo_id: int):
    """ Update an Equipo in our database given the values in the :equipo: param.

    Args:
        db (Session): The database Session.
        equipo (EquipoBaseModel): The EquipoBaseModel to update an Equipo in our database.
        equipo_id (int): The Equipo id passed as url param.

    Returns:
        Updated Equipo object if found, None otherwise.
    """
    db_equipo = db.get(Equipo, equipo_id)

    if db_equipo is None:
        return db_equipo

    db_equipo.nombre = equipo.nombre
    db.add(db_equipo)
    db.commit()
    db.refresh(db_equipo)

    return db_equipo


def delete_equipo(db: Session, equipo_id: int):
    """ Delete an Equipo in our database given an id :equipo_id:

        Args:
            db (Session): The database Session.
            equipo_id (int): The Equipo id.

        Returns:
            Deleted Equipo object if found, None otherwise.
        """
    db_equipo = db.get(Equipo, equipo_id)

    if db_equipo is None:
        return db_equipo

    db.delete(db_equipo)
    db.commit()

    return db_equipo


# ================================
#           SELECCION
# ================================
def get_seleccion(db: Session, seleccion_id: int):
    """ Get a Seleccion object from our database given an id :seleccion_id:

    Args:
        db (Session): The database Session.
        seleccion_id (int): The Seleccion id.

    Returns:
        Seleccion object if found, None otherwise.
    """
    return db.query(Seleccion).filter(Seleccion.id == seleccion_id).first()


def get_selecciones(db: Session):
    """ Get all Seleccion objects from our database.

        Args:
            db (Session): The database Session.

        Returns:
            Seleccion objects list if found, empty list otherwise.
        """
    return db.query(Seleccion).all()


def create_seleccion(db: Session, seleccion: SeleccionBaseModel):
    """ Create a Seleccion in our database given the values in the :seleccion: param.

        Args:
            db (Session): The database Session.
            seleccion (SeleccionBaseModel): The SeleccionBaseModel to create a Seleccion in our database.

        Returns:
            Created Seleccion object.
        """
    db_seleccion = Seleccion(pais=seleccion.pais)
    db.add(db_seleccion)
    db.commit()
    db.refresh(db_seleccion)

    return db_seleccion


def update_seleccion(db: Session, seleccion: SeleccionBaseModel, seleccion_id: int):
    """ Update an Seleccion in our database given the values in the :seleccion: param.

    Args:
        db (Session): The database Session.
        seleccion (SeleccionBaseModel): The SeleccionBaseModel to update an Seleccion in our database.
        seleccion_id (int): The Seleccion id passed as url param.

    Returns:
        Updated Seleccion object if found, None otherwise.
    """
    db_seleccion = db.get(Seleccion, seleccion_id)

    if db_seleccion is None:
        return db_seleccion

    db_seleccion.pais = seleccion.pais
    db.add(db_seleccion)
    db.commit()
    db.refresh(db_seleccion)

    return db_seleccion


def delete_seleccion(db: Session, seleccion_id: int):
    """ Delete a Seleccion in our database given an id :seleccion_id:

        Args:
            db (Session): The database Session.
            seleccion_id (int): The Seleccion id.

        Returns:
            Deleted Seleccion object if found, None otherwise.
        """
    db_seleccion = db.get(Seleccion, seleccion_id)

    if db_seleccion is None:
        return db_seleccion

    db.delete(db_seleccion)
    db.commit()

    return db_seleccion


# ================================
#           INTEGRANTE
# ================================
def get_integrante(db: Session, integrante_id: int):
    """ Get an Integrante object from our database given an id :integrante_id:

    Args:
        db (Session): The database Session.
        integrante_id (int): The Integrante id.

    Returns:
        Integrante object if found, None otherwise.
    """
    return db.query(Integrante).filter(Integrante.id == integrante_id).first()


def get_integrantes(db: Session):
    """ Get all Integrante objects from our database.

        Args:
            db (Session): The database Session.

        Returns:
            Integrantes list if found, Empty List otherwise.
        """
    return db.query(Integrante).all()


def create_integrante(db: Session, integrante: IntegranteBaseModel):
    """ Create an Integrante in our database given the values in the :integrante: param.

        Args:
            db (Session): The database Session.
            integrante (IntegranteBaseModel): The IntegranteBaseModel to create a Integrante in our database.

        Returns:
            Created Integrante object.
        """
    db_integrante = Integrante(nombre=integrante.nombre,
                               apodo=integrante.apodo,
                               apellido=integrante.apellido,
                               edad=integrante.edad,
                               num_camiseta=integrante.num_camiseta,
                               seleccion_id=integrante.seleccion_id,
                               equipo_id=integrante.equipo_id,
                               rol_id=integrante.rol_id)
    db.add(db_integrante)
    db.commit()
    db.refresh(db_integrante)

    return db_integrante


def update_integrante(db: Session, integrante: IntegranteBaseModel, integrante_id: int):
    """ Update an Integrante in our database given the values in the :integrante: param.

    Args:
        db (Session): The database Session.
        integrante (IntegranteBaseModel): The IntegranteBaseModel to update an Integrante in our database.
        integrante_id (int): The Integrante id passed as url param.

    Returns:
        Updated Integrante object if found, None otherwise.
    """
    db_integrante = db.get(Integrante, integrante_id)

    if db_integrante is None:
        return db_integrante

    db_integrante.nombre = integrante.nombre
    db_integrante.apodo = integrante.apodo
    db_integrante.apellido = integrante.apellido
    db_integrante.edad = integrante.edad
    db_integrante.num_camiseta = integrante.num_camiseta
    db_integrante.seleccion_id = integrante.seleccion_id
    db_integrante.equipo_id = integrante.equipo_id
    db_integrante.rol_id = integrante.rol_id

    db.add(db_integrante)
    db.commit()
    db.refresh(db_integrante)

    return db_integrante


def delete_integrante(db: Session, integrante_id: int):
    """ Delete an Integrante in our database given an id :integrante_id:

        Args:
            db (Session): The database Session.
            integrante_id (int): The Integrante id.

        Returns:
            Deleted Integrante object if found, None otherwise.
        """
    db_integrante = db.get(Integrante, integrante_id)

    if db_integrante is None:
        return db_integrante

    db.delete(db_integrante)
    db.commit()

    return {"OK": f"Integrante con id: {integrante_id} eliminado exitosamente"}


# ================================
#           USUARIO
# ================================
def get_usuario(db: Session, usuario_id: int):
    """ Get an Usuario object from our database given an id :usuario_id:

    Args:
        db (Session): The database Session.
        usuario_id (int): The Usuario id.

    Returns:
        Usuario object if found, None otherwise.
    """
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def get_usuarios(db: Session):
    """ Get all Usuario objects from our database

    Args:
        db (Session): The database Session.

    Returns:
        Usuario objects list if found, empty list otherwise.
    """
    return db.query(Usuario).all()


def create_usuario(db: Session, usuario: UsuarioBaseModel):
    """ Create an Usuario in our database given the values in the :usuario: param.

            Args:
                db (Session): The database Session.
                usuario (UsuarioBaseModel): The UsuarioBaseModel to create an Usuario in our database.

            Returns:
                Created Usuario object.
            """
    db_usuario = Usuario(email=usuario.email,
                         password=hash_password(usuario.password))
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)

    return db_usuario


def update_usuario(db: Session, usuario: UsuarioBaseModel, usuario_id: int):
    """ Update an Usuario in our database given the values in the :usuario: param.

    Args:
        db (Session): The database Session.
        usuario (UsuarioBaseModel): The UsuarioBaseModel to update an Usuario in our database.
        usuario_id (int): The Usuario id passed as url param.

    Returns:
        Updated Usuario object if found, None otherwise.
    """
    db_usuario = db.get(Usuario, usuario_id)

    if db_usuario is None:
        return db_usuario

    db_usuario.email = usuario.email
    db_usuario.password = hash_password(usuario.password)

    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)

    return db_usuario


def delete_usuario(db: Session, usuario_id: int):
    """ Delete an Usuario in our database given an id :usuario_id:

        Args:
            db (Session): The database Session.
            usuario_id (int): The Usuario id.

        Returns:
            Message if Usuario is found, None otherwise.
        """
    db_usuario = db.get(Usuario, usuario_id)

    if db_usuario is None:
        return db_usuario

    db.delete(db_usuario)
    db.commit()

    return {"OK": f"Usuario con id: {usuario_id} eliminado exitosamente"}


def get_usuario_by_email(db: Session, usuario: OAuth2PasswordRequestForm):

    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.username).first()

    return db_usuario
