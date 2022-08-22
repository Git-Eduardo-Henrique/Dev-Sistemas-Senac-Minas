import { Component } from '@angular/core';
import { SubjectSubscriber } from 'rxjs/internal/Subject';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})

export class HomePage {
  // variaveis
  resultado: String
  n1: String
  n2: String
  constructor() {}

  // uma função em js
  adicao(){  
    var n1 = Number(this.n1) // variavel
    var n2 = Number(this.n2)
    var soma = n1 + n2
    this.resultado = soma.toString()
  }

  subtracao(){  
    var n1 = Number(this.n1) // variavel
    var n2 = Number(this.n2)
    var sub = n1 - n2
    this.resultado = sub.toString()
  }

  mult(){  
    var n1 = Number(this.n1) // variavel
    var n2 = Number(this.n2)
    var multi = n1 * n2
    this.resultado = multi.toString() 
  }

  divi(){  
    var n1 = Number(this.n1) // variavel
    var n2 = Number(this.n2)
    
    if (n2 != 0) {
      var divi = n1 / n2
      this.resultado = divi.toString()
    }
    else {
      this.resultado = 'NÃO VAI DAAAR'.toString()
    }
  }
}
