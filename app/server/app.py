from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags=['root'])
async def read_root():
    return {"message": "Bienvenides a esta fantástica aplicación"}