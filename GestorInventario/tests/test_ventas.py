import pytest
from modelos.venta import Venta
from módulos.gestor_ventas import GestorVentas
from módulos.gestor_inventario import GestorInventario
from modelos.producto import Producto
def test_registrar_venta1():
    producto1=Producto(1,"lapiz",500,1,"escolares",10)
    producto2=Producto(2,"cuaderno",1500,2,"escolares",10)
    gestor_inventario=GestorInventario()
    gestor_inventario.agregar_producto(producto1)
    gestor_inventario.agregar_producto(producto2)
    productos_vendidos=[producto1,producto2]
    venta=Venta(1,"04/03/25",productos_vendidos,3500,1)
    gestor_ventas=GestorVentas()
    gestor_ventas.registrar_venta(venta)
    assert len(gestor_ventas.historial_ventas)==1


def test_validar_stock_gestor_venta():
    producto1=Producto(1,"lapiz",500,10,"escolares",1)
    producto2=Producto(2,"cuaderno",1500,20,"escolares",1)
    gestor_inventario=GestorInventario()
    gestor_inventario.agregar_producto(producto1)
    gestor_inventario.agregar_producto(producto2)
    venta1=Venta(1,"04/03/25",producto1,2,1)
    venta2=Venta(2,"05/03/25",producto2,3,1)
    gestor_ventas=GestorVentas()
    gestor_ventas.registrar_venta(venta1)
    gestor_ventas.registrar_venta(venta2)
    assert gestor_ventas.validar_stock_venta(1,8)==True and gestor_ventas.validar_stock_venta(2,17)==True


def test_registrar_venta2():
    producto1=Producto(1,"lapiz",500,10,"escolares",1)
    producto2=Producto(2,"cuaderno",1500,20,"escolares",1)
    producto3=Producto(3,"corrector",1000,30,"escolares",1)
    gestor_inventario=GestorInventario()
    gestor_inventario.agregar_producto(producto1)
    gestor_inventario.agregar_producto(producto2)
    gestor_inventario.agregar_producto(producto3)
    venta1=Venta(1,"04/03/25",producto1,500,1)
    venta2=Venta(2,"05/03/25",producto2,3000,1)
    venta3=Venta(2,"05/03/25",producto3,3000,2)
    gestor_ventas=GestorVentas()
    gestor_ventas.registrar_venta(venta1)
    gestor_ventas.registrar_venta(venta2)
    gestor_ventas.registrar_venta(venta3)
    assert len(gestor_ventas.historial_ventas)==3
    

def test_calcular_total():
    producto=Producto(34,"lapiz",500,10,"escolar",1)
    gestor_inventario=GestorInventario()
    gestor_inventario.agregar_producto(producto)
    venta=Venta(1,"03/03/25",producto,1,1)
    assert venta.calcular_total(producto,2)==1000


def test_validar_stock_venta():
    producto1=Producto(1,"lapiz",500,10,"escolares",1)
    producto2=Producto(2,"cuaderno",1500,20,"escolares",1)
    producto3=Producto(3,"corrector",1000,30,"escolares",1)
    gestor_inventario=GestorInventario()
    gestor_inventario.agregar_producto(producto1)
    gestor_inventario.agregar_producto(producto2)
    gestor_inventario.agregar_producto(producto3)
    venta1=Venta(1,"03/05/25",producto1,2,1)
    venta2=Venta(1,"03/05/25",producto2,6,1)
    venta3=Venta(1,"03/05/25",producto3,1,1)
    assert (venta1.validar_stock(producto1)==9 and venta2.validar_stock(producto2)==14 and venta3.validar_stock(producto3)==29)


def test_generar_historial():
    producto=Producto(1,"lapiz",500,10,"escolar",1)
    gestor_inventario=GestorInventario()
    gestor_inventario.agregar_producto(producto)
    venta=Venta(1,"03/04/25",producto,2,1)
    gestor_venta=GestorVentas()
    gestor_venta.registrar_venta(venta)
    assert gestor_venta.generar_historial()==venta