import pytest
from modelos.usuario import Usuario
from módulos.gestor_usuarios import GestorUsuarios
from errores.usuarioduplicado import UsuarioDuplicadoError
from errores.usuarionoencontrado import UsuarioNoEncontradoError
from errores.credencialesinvalidos import CredencialesInvalidasError
from errores.contraseñainvalida import ContraseñaInvalidaError


def test_crear_usuario():
    gestor_usuario=GestorUsuarios()
    usuario=Usuario(1,"jose","empleado","1234")
    assert gestor_usuario.crear_usuario(usuario) == "el usuario se creo con exito"

def test_usuario_validar_rol():
    gestor_usuario=GestorUsuarios()
    usuario=Usuario(1,"jose","empleado","1234")
    gestor_usuario.crear_usuario(usuario)
    assert gestor_usuario.validar_rol(1,"empleado")==True


def test_eliminar_usuario3():
    gestor_usuario=GestorUsuarios()
    usuario=Usuario(1,"jose","empleado","1234")
    usuario2=Usuario(2,"alejandro","empleado","4321")
    usuario3=Usuario(3,"pepe","empleado","9876")
    gestor_usuario.crear_usuario(usuario)
    gestor_usuario.crear_usuario(usuario2)
    gestor_usuario.crear_usuario(usuario3)
    assert gestor_usuario.eliminar_usuario(3)=="el usuario pepe ha sido eliminado"


def test_iniciar_sesion():
    usuario=Usuario(1,"jose","empleado","1234")
    assert usuario.iniciar_sesion("1234")==True


def test_cambiar_contraseña():
    usuario=Usuario(1,"jose","empleado","1234")
    assert usuario.cambiar_contraseña("4321")== "4321"


def test_iniciar_sesion2():
    usuario=Usuario(1,"jose","empleado","1234")
    assert usuario.iniciar_sesion("4321")==False
    

def test_crear_usuario_duplicado():
    gestor_usuario = GestorUsuarios()
    usuario = Usuario(1, "jose", "empleado", "1234")
    gestor_usuario.crear_usuario(usuario)

    with pytest.raises(UsuarioDuplicadoError, match="El usuario con ID 1 ya existe"):
        gestor_usuario.crear_usuario(usuario)


def test_validar_rol_usuario_no_existente():
    gestor_usuario = GestorUsuarios()

    with pytest.raises(UsuarioNoEncontradoError, match="El usuario con ID 99 no existe"):
        gestor_usuario.validar_rol(99, "empleado")


def test_eliminar_usuario_inexistente():
    gestor_usuario = GestorUsuarios()

    with pytest.raises(UsuarioNoEncontradoError, match="El usuario con ID 99 no existe"):
        gestor_usuario.eliminar_usuario(99)


def test_crear_usuario_contraseña_invalida():
    with pytest.raises(ContraseñaInvalidaError, match="La contraseña no cumple con los requisitos mínimos"):
        Usuario(1, "jose", "empleado", "")


def test_iniciar_sesion_fallida():
    usuario = Usuario(1, "jose", "empleado", "1234")

    with pytest.raises(CredencialesInvalidasError, match="Credenciales incorrectas"):
        usuario.iniciar_sesion("0000")


def test_cambiar_contraseña_invalida():
    usuario = Usuario(1, "jose", "empleado", "1234")

    with pytest.raises(ContraseñaInvalidaError, match="La contraseña no cumple con los requisitos mínimos"):
        usuario.cambiar_contraseña("")