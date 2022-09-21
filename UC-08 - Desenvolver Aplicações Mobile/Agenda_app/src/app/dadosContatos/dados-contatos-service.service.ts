import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DadosContatosServiceService {

  private Contatos = [
    {id: 0, nome: 'Mãe', num: '(35) 9985-2009', email: 'socapanoff@gmail.com'}
  ]

  constructor() { }

  retorno() {
    return this.Contatos
  }

  Filtrar(id : any) {
    const selecionaProdu = this.Contatos.filter(produto => produto.id === id)
    return selecionaProdu[0]
  }
}
