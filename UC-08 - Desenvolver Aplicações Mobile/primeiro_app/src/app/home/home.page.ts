import { Component } from '@angular/core';
import { SubjectSubscriber } from 'rxjs/internal/Subject';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  resultado: string
  escreva: string
  constructor() {}
  escreval(){
    this.resultado = this.escreva.toString()
  }

}
