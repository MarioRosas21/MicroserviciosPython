from fastapi import FastAPI, HTTPException
from app.models.usuario import Usuario
from app.db import get_connection

app = FastAPI()

@app.post("/usuarios")
def agregar_usuario(usuario: Usuario):
    conn = None 
    cursor = None
    try:
        
        conn = get_connection()

        cursor = conn.cursor()

        query = "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)"
        print("Valores:", (usuario.nombre, usuario.correo))

        cursor.execute(query, (usuario.nombre, usuario.correo))
        conn.commit()

        print("Usuario insertado correctamente")
        return {"mensaje": "Usuario agregado correctamente"}
    except Exception as e:
        print("Error en el servidor:", e)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

from fastapi import FastAPI, HTTPException
from app.models.usuario import Usuario
from app.db import get_connection


# DELETE por ID
@app.delete("/usuarios/id/{user_id}")
def eliminar_usuario_por_id(user_id: int):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(query, (user_id,))
        conn.commit()
        
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        return {"mensaje": f"Usuario con id {user_id} eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# DELETE por nombre
@app.delete("/usuarios/nombre/{nombre}")
def eliminar_usuario_por_nombre(nombre: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM usuarios WHERE nombre = %s"
        cursor.execute(query, (nombre,))
        conn.commit()
        
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        return {"mensaje": f"Usuario con nombre '{nombre}' eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
