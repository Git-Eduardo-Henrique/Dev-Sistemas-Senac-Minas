import { Injectable } from '@angular/core';

// banco de dados
import { Guid } from "guid-typescript";
import { Storage } from '@ionic/storage-angular';
import { Contatos } from '../models/contatos.model';

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

  constructor(private storage: Storage) { }

  retorno() {
    return this.Contatos
  }

  adicionar(arg : Contatos) {
    arg.id = Guid.create()
    this.storage.set(arg.id.toString(), JSON.stringify(arg))

    // novo_contato.id = this.Contatos.length + 1
    // this.Contatos.push(novo_contato)
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
