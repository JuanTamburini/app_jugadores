from fastapi import FastAPI
from server.routes.jugadores import router as JugadorRouter

app = FastAPI()

app.include_router(JugadorRouter, tags=["Jugador"], prefix="/jugadores")

@app.get("/", tags=['root'])
async def read_root():
    return {"message": "Bienvenides a esta fantástica aplicación"}