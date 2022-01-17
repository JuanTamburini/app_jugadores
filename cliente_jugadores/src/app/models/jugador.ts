export interface Jugador {
    id: string;
    nombre: string;
    apellido: string;
    nacionalidad: string;
    club_actual: string;
    edad: number;
    activo: boolean
}

export interface ApiJson {
    data: Array<Jugador>;
    code: number;
    message: string
}