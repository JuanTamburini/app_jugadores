import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaDeJugadoresComponent } from './lista-de-jugadores.component';

describe('ListaDeJugadoresComponent', () => {
  let component: ListaDeJugadoresComponent;
  let fixture: ComponentFixture<ListaDeJugadoresComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListaDeJugadoresComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ListaDeJugadoresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
