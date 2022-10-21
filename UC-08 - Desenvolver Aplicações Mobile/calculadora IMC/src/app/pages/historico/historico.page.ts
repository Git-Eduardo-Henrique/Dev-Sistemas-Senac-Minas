import { Component, OnInit } from '@angular/core';
import { ImcDbService } from 'src/app/services/imc-db.service';

@Component({
  selector: 'app-historico',
  templateUrl: './historico.page.html',
  styleUrls: ['./historico.page.scss'],
})
export class HistoricoPage implements OnInit {
  private service: ImcDbService
  public arrayImc: any 

  constructor() { }

  ngOnInit() {
    this.service.lista().then(arrayall => {this.arrayImc = arrayall})
  }

}
