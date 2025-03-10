import httpx

from fastapi import FastAPI, HTTPException
from api.db import db
from api.models import Aplicacion
from api.config import postgres_config
import psycopg2
import psycopg2.extras


app = FastAPI()


@app.get("/aplicaciones")
async def get_all_aplicaciones():
    return db


@app.get("/aplicacion/{aplicacion_nombre}", response_model=Aplicacion)
async def get_aplicacion(aplicacion_nombre: str):
    for aplicacion in db:
        if aplicacion.nombre == aplicacion_nombre:
            return aplicacion
    raise HTTPException(status_code=404, detail="Aplicacion not found")


@app.post("/aplicacion/", response_model=Aplicacion)
async def create_aplicacion(aplicacion: Aplicacion):
    db.append(aplicacion)
    return aplicacion


@app.put("/aplicacion/{aplicacion_nombre}", response_model=Aplicacion)
async def update_aplicacion(aplicacion_nombre: str, aplicacion: Aplicacion):
    for idx, b in enumerate(db):
        if b.nombre == aplicacion_nombre:
            db[idx] = aplicacion
            return aplicacion
    raise HTTPException(status_code=404, detail="Aplicacion not found")


@app.delete("/aplicacion/{aplicacion_nombre}", response_model=dict)
async def delete_aplicacion(aplicacion_nombre: str):
    for idx, aplicacion in enumerate(db):
        if aplicacion.nombre == aplicacion_nombre:
            del db[idx]
            return {"message": "Aplicacion deleted successfully"}
    raise HTTPException(status_code=404, detail="Aplicacion not found")


@app.get("/test_sql_query")
def test_sql_query():
    conn = None
    try:
        params = postgres_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        sql_stmt = f"SELECT * FROM test_user;"
        cur.execute(sql_stmt)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return {"results": results}
    except (Exception, psycopg2.DatabaseError) as error:
        if conn is not None:
            conn.close()
        return {"error": str(error)}
    finally:
        if conn is not None:
            conn.close()