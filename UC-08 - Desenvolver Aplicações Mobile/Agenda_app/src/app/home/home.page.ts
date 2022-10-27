import { Component, OnInit} from '@angular/core';
import { DadosContatosServiceService } from 'src/app/dadosContatos/dados-contatos-service.service'; 

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit{

  public mostrar: any

  constructor( private TodosContatos : DadosContatosServiceService) {}


ngOnInit(){
  this.TodosContatos.retorno().then(arraycontato => {this.mostrar = arraycontato})
  console.log()
}

}
