import { Component } from '@angular/core';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page {
  a: string
  b: string
  c: string
  resul: string

  constructor() {}

  calcular(){
    var a = Number(this.a)
    var b = Number(this.b)
    var c = Number(this.c)
    var p = Number((a + b + c) / 2)
    var r =  Math.sqrt(p * (p - a) * (p - b) * (p - c))
    if (a + b > c && a + c > b && b + c > a){
      this.resul = 'a area é: ' + r.toFixed(2)
    }
    else{
      this.resul = 'esse triangulo nao existe'
    }
  } 

}
