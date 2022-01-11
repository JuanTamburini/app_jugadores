import os
import motor.motor_asyncio
from bson.objectid import ObjectId


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])

database = client.jugadores

jugador_collection = database.get_collection("jugadores_collections")

def jugador_helper(jugador) -> dict:
    return {
        "id": str(jugador["_id"]),
        "nombre": jugador["nombre"],
        "apellido": jugador["apellido"],
        "nacionalidad": jugador["nacionalidad"],
        "club_actual": jugador["club_actual"],
        "edad": jugador["edad"],
        "activo": jugador["activo"]
    }

async def request_jugadores():
    
    jugadores = []

    async for jugador in jugador_collection.find():
        jugadores.append(jugador_helper(jugador))

    return jugadores

async def agregar_jugador(data: dict) -> dict:
    jugador = await jugador_collection.insert_one(data)
    nuevo_jugador = await jugador_collection.find_one({"_id": jugador.inserted_id})
    return jugador_helper(nuevo_jugador)

async def buscar_jugador(id: str) -> dict:
    jugador = await jugador_collection.find_one({"_id": ObjectId(id)})
    if jugador:
        return jugador_helper(jugador)

async def actualizar_jugador(id: str, data: dict):
    if len(data) < 1:
        return False

    jugador = await jugador_collection.find_one({"_id": ObjectId(id)})
    if jugador:
        jugador_actualizado = await jugador_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    if jugador_actualizado:
        return True
    return False

async def eliminar_jugador(id: str):
    jugador = await jugador_collection.find_one({"_id": ObjectId(id)})

    if jugador:
        await jugador_collection.delete_one({"_id": ObjectId(id)})
        return True



    
