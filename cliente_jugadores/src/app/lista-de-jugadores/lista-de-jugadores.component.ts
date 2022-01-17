import { Component, OnInit } from '@angular/core';
import { ApiJson, Jugador } from '../models/jugador';
import { HttpJugadoresService } from '../servicios/http-jugadores.service';

@Component({
  selector: 'app-lista-de-jugadores',
  templateUrl: './lista-de-jugadores.component.html',
  styleUrls: ['./lista-de-jugadores.component.css']
})
export class ListaDeJugadoresComponent implements OnInit {

  apiGet: ApiJson = {
    data: [],
    code: 0,
    message: ''
  }
  jugadores: Array<Jugador> = [];

  constructor(private httpService: HttpJugadoresService) { }

  ngOnInit(): void {
    this.httpService.getJugadores().subscribe((jugadoresApi)=>{
      this.apiGet.data = jugadoresApi.data
      this.apiGet.code = jugadoresApi.code
      this.apiGet.message = jugadoresApi.message
      this.jugadores = this.apiGet.data
      console.log(this.apiGet)
      console.log(this.jugadores)
    })
  }

}
