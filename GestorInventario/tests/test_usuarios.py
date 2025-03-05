import pytest
from modelos.usuario import Usuario
from módulos.gestor_usuarios import GestorUsuarios


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
    