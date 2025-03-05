import json
with open('data/inventario.json','r') as file:
    inventario = json.load(file)
class Venta():
    def __init__(self,id:int,fecha:str,productos_vendidos:list[dict],total:float,id_empleado:int):
        pass
    def calcular_total(inventario:dict):
        pass
    def validar_stock(inventario:dict):
        pass
