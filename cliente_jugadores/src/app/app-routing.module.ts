import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListaDeJugadoresComponent } from './lista-de-jugadores/lista-de-jugadores.component';

const routes: Routes = [
  { 
    path: '', component: ListaDeJugadoresComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }