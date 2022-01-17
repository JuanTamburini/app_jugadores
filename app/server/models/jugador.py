from typing import Optional
from pydantic import BaseModel, Field, constr, conint

class SchemaDeJugador(BaseModel):
    nombre: constr(strict=True) = Field(...)
    apellido: constr(strict=True) = Field(...)
    nacionalidad: constr(strict=True) = Field(...)
    club_actual: constr(strict=True) = Field(...)
    edad: conint(strict=True, gt=0) = Field(...)
    activo: bool = Field(...)

    class config:
        schema_extra = {
            "ejemplo": {
                "nombre": "Diego",
                "apellido": "Maradona", 
                "nacionalidad": "Argentina",
                "club_actual": "San Lorenzo",
                "edad": 70, 
                "activo": False 
            }
        }


class UpdateDeJugador(BaseModel):
    nombre: Optional[constr(strict=True)]
    apellido: Optional[constr(strict=True)]
    nacionalidad: Optional[constr(strict=True)]
    club_actual: Optional[constr(strict=True)]
    edad: Optional[conint(strict=True, gt=0)]
    activo: Optional[bool]

    class config:
        schema_extra = {
            "ejemplo": {
                "nombre": "Diego",
                "apellido": "Maradona", 
                "nacionalidad": "Argentina",
                "club_actual": "San Lorenzo",
                "edad": 70, 
                "activo": False 
            }
        }

def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }