class Producto():
    def __init__(self,id:int,nombre:str,precio:float,cantidad:int,categoria:str,stock_minimo:int):
        self.stock=cantidad+stock_minimo
        pass
    def actualizar_stock(self,cantidad):
        'Producto.stock'=self.stock+cantidad