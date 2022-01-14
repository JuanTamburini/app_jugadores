import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { ListaDeJugadoresComponent } from './lista-de-jugadores/lista-de-jugadores.component';
import { HttpJugadoresService } from './servicios/http-jugadores.service';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    ListaDeJugadoresComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [HttpJugadoresService],
  bootstrap: [AppComponent]
})
export class AppModule { }
