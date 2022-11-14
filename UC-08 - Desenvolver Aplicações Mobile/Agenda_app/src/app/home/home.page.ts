import { Component} from '@angular/core';
import { DadosContatosServiceService } from 'src/app/dadosContatos/dados-contatos-service.service'; 

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage{

  public mostrar: any []

  constructor( private TodosContatos : DadosContatosServiceService) {
    this.TodosContatos.retorno().then(arraycontato => {this.mostrar = arraycontato})
  }

ionViewDidEnter(){ //executa toda vez que o pagina é carregada
  this.TodosContatos.retorno().then(arraycontato => {this.mostrar = arraycontato})
}

handleChange(event){
  const resul1 = event.target.value.toLowerCase()

  if (resul1 != ''){
    this.mostrar = this.mostrar.filter(item => item.nome.toLowerCase().indexOf(resul1) > -1)
  }

  else {
    this.TodosContatos.retorno().then(arraycontato => {this.mostrar = arraycontato})
  }

}
}
