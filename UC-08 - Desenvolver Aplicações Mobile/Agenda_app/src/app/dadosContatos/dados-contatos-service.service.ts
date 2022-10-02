import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DadosContatosServiceService {

  private Contatos = [
    {id: 1, 
      nome: 'Eduardo', 
      sobrenome: 'Henrique', 
      tipo_num: 'trabalho',
      num: '(035) 9 4002-8922', 
      email: 'taty@gmail.com'}
  ]

  constructor() { }

  retorno() {
    return this.Contatos
  }

  adicionar(novo_contato: any) {
    novo_contato.id = this.Contatos.length + 1
    this.Contatos.push(novo_contato)
  }
  
  deletar(remover){
    const index = this.Contatos.indexOf(remover)
    this.Contatos.splice(index, 1)
  }

  Filtrar(id : any) {
    const selecionaProdu = this.Contatos.filter(produto => produto.id === id)
    return selecionaProdu[0]
  }
}
