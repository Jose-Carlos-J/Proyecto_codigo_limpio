import pytest
from modelos.producto import Producto
from módulos.inventario import Inventario
from errores.productoduplicado import ProductoDuplicadoError
from errores.productonoencontrado import ProductoNoEncontradoError
from errores.productoinvalido import ProductoInvalidoError
from errores.stockinvalido import StockInvalidoError
from errores.nohayproductos import NoHayProductosError
#Tests caso normal

def test_agregar_producto_a_inventario():
    producto=Producto(1,"lapiz",500,10,"escolar",1)
    inventario=Inventario()
    inventario.agregar_producto(producto)
    assert len(inventario.productos)==1


def test_eliminar_producto_de_inventario():
    producto=Producto(1,"lapiz",8500,10,"escolar",1)
    inventario=Inventario()
    inventario.agregar_producto(producto)
    assert inventario.eliminar_producto(1) == "el producto: lapiz se a elminado con exito"


def test_actualizar_stock():
    producto=Producto(1,"lapiz",500,10,"escolar",1)
    inventario=Inventario()
    inventario.agregar_producto(producto)
    assert inventario.actualizar_stock(1,10)=="la cantidad de: lapiz se a actualizado a: 20"


def test_filtrar_stock_bajo():
    producto=Producto(1,"lapiz",500,10,"escolar",1)
    producto2=Producto(2,"cuaderno",1500,20,"escolar",1)
    gestor_inventario=Inventario()
    gestor_inventario.agregar_producto(producto)
    gestor_inventario.agregar_producto(producto2)
    assert gestor_inventario.filtrar_por_stock_bajo()==producto


def test_eliminar_producto2():
    producto=Producto(1,"lapiz",500,10,"escolar",1)
    producto2=Producto(2,"cuaderno",1500,20,"escolar",1)
    gestor_inventario=Inventario()
    gestor_inventario.agregar_producto(producto)
    gestor_inventario.agregar_producto(producto2)
    gestor_inventario.eliminar_producto(1)
    assert len(gestor_inventario.productos)==1

def test_actualizar_stock_producto():
    producto=Producto(1,"lapiz",500,5,"escolar",1)
    producto.actualizar_stock(5)
    assert producto.cantidad==10


#Test caso Error
def test_agregar_producto_duplicado():
    producto = Producto(1, "lapiz", 500, 10, "escolar", 1)
    gestor_inventario = Inventario()
    gestor_inventario.agregar_producto(producto)
    with pytest.raises(ProductoDuplicadoError):
        gestor_inventario.agregar_producto(producto)


def test_eliminar_producto_inexistente():
    gestor_inventario = Inventario()
    with pytest.raises(ProductoNoEncontradoError):
        gestor_inventario.eliminar_producto(99)  # ID que no existe


def test_actualizar_stock_cantidad_negativa():
    producto = Producto(1, "lapiz", 500, 10, "escolar", 1)
    gestor_inventario = GestorInventario()
    gestor_inventario.agregar_producto(producto)
    with pytest.raises(StockInvalidoError):
        gestor_inventario.actualizar_stock(1, -5)  # Stock negativo


def test_filtrar_stock_sin_productos():
    gestor_inventario = Inventario()
    with pytest.raises(NoHayProductosError):
        gestor_inventario.filtrar_por_stock_bajo()


def test_producto_invalido_nombre_vacio():
    with pytest.raises(ProductoInvalidoError):
        producto = Producto(1, "", 500, 10, "escolar", 1)  # Nombre vacío debería ser inválido


def test_actualizar_stock_producto_inexistente():
    gestor_inventario = Inventario()
    with pytest.raises(ProductoNoEncontradoError):
        gestor_inventario.actualizar_stock(99, 5)  # Producto con ID 99 no existe