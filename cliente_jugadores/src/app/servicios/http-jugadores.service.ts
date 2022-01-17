import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiJson, Jugador } from '../models/jugador';

@Injectable({
  providedIn: 'root'
})
export class HttpJugadoresService {

  api_route: string = 'http://localhost:8000/jugadores/'

  constructor(private http: HttpClient) { }

  getJugadores(): Observable<ApiJson>
  {
    return this.http.get<ApiJson>(this.api_route)
  }
}
