import { Component, OnInit } from '@angular/core';
import { ImcDbService } from 'src/app/services/imc-db.service';

@Component({
  selector: 'app-historico',
  templateUrl: './historico.page.html',
  styleUrls: ['./historico.page.scss'],
})
export class HistoricoPage implements OnInit {
  public arrayImc: any 

  constructor(private service: ImcDbService) { }

  ngOnInit() {
    this.service.lista().then(arrayall => {this.arrayImc = arrayall})
  }

}
