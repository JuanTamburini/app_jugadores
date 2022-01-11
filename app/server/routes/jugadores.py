from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    solicitar_jugadores,
    agregar_jugador,
    actualizar_jugador,
    buscar_jugador,
    eliminar_jugador,
)
from server.models.jugador import (
    ErrorResponseModel,
    ResponseModel,
    SchemaDeJugador,
    UpdateDeJugador,
)

router = APIRouter()

@router.post("/", response_description="Jugador agregado a la base de datos")
async def add_jugador(jugador: SchemaDeJugador = Body(...)):
    jugador = jsonable_encoder(jugador)
    nuevo_jugador = await agregar_jugador(jugador)
    return ResponseModel(nuevo_jugador, "Jugador agregado.")

@router.get("/", response_description="Jugadores recibidos")
async def get_jugadores():
    jugadores = await solicitar_jugadores()
    if jugadores:
        return ResponseModel(jugadores, "jugadores recibidos")
    return ResponseModel(jugadores, "No se encontraron jugadores")


@router.get("/{id}", response_description="jugador recibido")
async def get_data_jugador(id):
    jugador = await buscar_jugador(id)
    if jugador:
        return ResponseModel(jugador, "Se consiguieron los datos del jugador")
    return ErrorResponseModel("Ocurrió un error", 404, "El jugador no existe.")

@router.put("/{id}")
async def put_data_jugador(id: str, req: UpdateDeJugador = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    jugador_actualizado = await actualizar_jugador(id, req)
    if jugador_actualizado:
        return ResponseModel(
            "Se pudo actualizar el jugador con el ID: {} ".format(id), "Jugador actualizado correctamente"
        )
    return ErrorResponseModel(
        "Ocurrió un error",
        404,
        "Hubo una falla actualizando los datos del jugador",
    )

@router.delete("/{id}", response_description="Jugador eliminado de la base de datos")
async def delete_jugador(id: str):
    jugador_eliminado = await eliminar_jugador(id)
    if jugador_eliminado:
        return ResponseModel(
            "Jugador con ID {} borrado".format(id), "Jugador borrado exitosamente"
        )
    return ErrorResponseModel(
        "Hubo un error", 404, "Socio con id {0} no existe".format(id)
    )