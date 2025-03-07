#algunos comandos que debes usar antes de hacer las pruebas
    python3 -m venv venv
    source venv/bin/activate
    export PYTHONPATH=$(pwd)
    pip install pytest   


# Proyecto_codigo_limpio

# 📦 Gestor de Inventario y Ventas  
Sistema para gestionar productos, ventas y usuarios en un entorno retail. Permite:  
- **Control de inventario**: Agregar, eliminar y actualizar productos.  
- **Registro de ventas**: Validar stock y generar historial.  
- **Gestión de usuarios**: Roles (Admin/Empleado) y autenticación segura.  

---

## 🧪 Casos de Prueba  

### **Módulo de Inventario** (`test_inventario.py`)  
1. **Agregar producto**: Verifica que un producto se añade correctamente al inventario.  
2. **Eliminar producto**: Confirma la eliminación física/lógica de un producto.  
3. **Actualizar stock**: Valida el ajuste de cantidades en un producto existente.  
4. **Filtrar stock bajo**: Comprueba que se detectan productos con stock mínimo.  
5. **Eliminar múltiples productos**: Asegura que solo se elimina el producto especificado.  
6. **Actualizar stock desde clase**: Verifica el método interno de actualización.  

### **Módulo de Usuarios** (`test_usuarios.py`)  
1. **Crear usuario**: Valida el registro de nuevos usuarios.  
2. **Validar rol**: Confirma que los roles se asignan correctamente.  
3. **Eliminar usuario**: Asegura la eliminación de cuentas por ID.  
4. **Iniciar sesión**: Verifica autenticación con contraseña correcta.  
5. **Cambiar contraseña**: Confirma la actualización de credenciales.  
6. **Iniciar sesión fallido**: Valida el rechazo de contraseñas incorrectas.  

### **Módulo de Ventas** (`test_ventas.py`)  
1. **Registrar venta simple**: Verifica que una venta se añade al historial.  
2. **Validar stock en venta**: Confirma que no se venda sin stock suficiente.  
3. **Registrar múltiples ventas**: Asegura el correcto conteo de transacciones.  
4. **Calcular total**: Valida el monto total de una venta.  
5. **Validar stock post-venta**: Comprueba el descuento automático de stock.  
6. **Generar historial**: Confirma que se recuperan todas las ventas registradas.  

---
