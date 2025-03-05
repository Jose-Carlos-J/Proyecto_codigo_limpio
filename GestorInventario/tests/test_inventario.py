import pytest
from modelos.producto import Producto
from módulos.gestor_inventario import GestorInventario


def test_agregar_producto_a_inventario():
    producto=Producto(1,"lapiz",500,10,"escolar",1)
    gestor_inventario=GestorInventario()
    gestor_inventario.agregar_producto(producto)
    assert len(gestor_inventario.productos)==1


def test_eliminar_producto_de_inventario():
    producto=Producto(1,"lapiz",8500,10,"escolar",1)
    gestor_inventario=GestorInventario()
    gestor_inventario.agregar_producto(producto)
    assert gestor_inventario.eliminar_producto(1) == "el producto: lapiz se a elminado con exito"


def test_actualizar_stock():
    producto=Producto(1,"lapiz",500,10,"escolar",1)
    gestor_inventario=GestorInventario()
    gestor_inventario.agregar_producto(producto)
    assert gestor_inventario.actualizar_stock(1,10)=="la cantidad de: lapiz se a actualizado a: 20"


def test_filtrar_stock_bajo():
    producto=Producto(1,"lapiz",500,10,"escolar",1)
    producto2=Producto(2,"cuaderno",1500,20,"escolar",1)
    gestor_inventario=GestorInventario()
    gestor_inventario.agregar_producto(producto)
    gestor_inventario.agregar_producto(producto2)
    assert gestor_inventario.filtrar_por_stock_bajo()==producto


def test_eliminar_producto2():
    producto=Producto(1,"lapiz",500,10,"escolar",1)
    producto2=Producto(2,"cuaderno",1500,20,"escolar",1)
    gestor_inventario=GestorInventario()
    gestor_inventario.agregar_producto(producto)
    gestor_inventario.agregar_producto(producto2)
    gestor_inventario.eliminar_producto(1)
    assert len(gestor_inventario.productos)==1

def test_actualizar_stock_producto():
    producto=Producto(1,"lapiz",500,5,"escolar",1)
    producto.actualizar_stock(5)
    assert producto.cantidad==10