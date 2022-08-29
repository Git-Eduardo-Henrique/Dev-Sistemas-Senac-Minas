import { Component } from '@angular/core';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss']
})
export class Tab3Page {
  Base: string
  Altura: string
  resul: string

  constructor() {}

  calcular(){
    var base = Number(this.Base)
    var altura = Number(this.Altura)
    var resul = (base * altura) / 2
    if (this.Base && this.Altura) {
      this.resul = 'a area é: ' + resul.toFixed(2)
    }
    else {
      this.resul = 'triangulo não existe'
    }
  }
}
