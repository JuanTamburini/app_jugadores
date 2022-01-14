import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Jugador, Usuario } from '../models/jugador';

@Injectable({
  providedIn: 'root'
})
export class HttpJugadoresService {

  api_route: string = 'https://jsonplaceholder.typicode.com/posts'

  constructor(private http: HttpClient) { }

  getJugadores(): Observable<Usuario[]>
  {
    return this.http.get<Usuario[]>(this.api_route)
  }
}
