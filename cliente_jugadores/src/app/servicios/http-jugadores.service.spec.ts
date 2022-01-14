import { TestBed } from '@angular/core/testing';

import { HttpJugadoresService } from './http-jugadores.service';

describe('HttpJugadoresService', () => {
  let service: HttpJugadoresService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HttpJugadoresService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
