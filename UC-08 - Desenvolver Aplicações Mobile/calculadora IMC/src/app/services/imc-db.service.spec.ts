import { TestBed } from '@angular/core/testing';

import { ImcDbService } from './imc-db.service';

describe('ImcDbService', () => {
  let service: ImcDbService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ImcDbService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
