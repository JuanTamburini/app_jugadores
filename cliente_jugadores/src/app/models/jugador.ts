export interface Jugador {
    id: string;
    nombre: string;
    apellido: string;
    nacionalidad: string;
    club_actual: string;
    edad: number;
    activo: boolean
}

export interface Usuario {
    userId: number,
    id: number,
    title: string,
    body: string
}