import { TestBed } from '@angular/core/testing';

import { DadosContatosServiceService } from './dados-contatos-service.service';

describe('DadosContatosServiceService', () => {
  let service: DadosContatosServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DadosContatosServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
