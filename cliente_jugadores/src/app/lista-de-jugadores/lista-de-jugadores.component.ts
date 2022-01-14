import { Component, OnInit } from '@angular/core';
import { Jugador, Usuario } from '../models/jugador';
import { HttpJugadoresService } from '../servicios/http-jugadores.service';

@Component({
  selector: 'app-lista-de-jugadores',
  templateUrl: './lista-de-jugadores.component.html',
  styleUrls: ['./lista-de-jugadores.component.css']
})
export class ListaDeJugadoresComponent implements OnInit {

  jugadores: Array<Jugador> = []
  usuarios: Array<Usuario> = []


  constructor(private httpService: HttpJugadoresService) { }

  ngOnInit(): void {
    this.httpService.getJugadores().subscribe((jugadoresApi)=>{
      this.usuarios = jugadoresApi
    })
  }

}
