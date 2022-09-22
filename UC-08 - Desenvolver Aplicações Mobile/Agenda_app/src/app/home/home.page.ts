import { Component } from '@angular/core';
import { DadosContatosServiceService } from 'src/app/dadosContatos/dados-contatos-service.service'; 

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  public mostrar : any

  constructor( private TodosContatos : DadosContatosServiceService) {
    this.mostrar = TodosContatos.retorno()
  }

}
