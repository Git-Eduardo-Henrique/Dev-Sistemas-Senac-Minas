import { Injectable } from '@angular/core';

// banco de dados
import { Guid } from "guid-typescript";
import { Storage } from '@ionic/storage-angular';
import { Contatos } from '../models/contatos.model';


@Injectable({
  providedIn: 'root'
})
export class DadosContatosServiceService {

  constructor(
    private storage: Storage) { }

  Atualizar(id : any, arg: Contatos){
    arg.id = Guid.parse(id)
    this.storage.set(arg.id.toString(), JSON.stringify(arg))
  
  }
 
  adicionar(arg : Contatos) {
    arg.id = Guid.create()
    this.storage.set(arg.id.toString(), JSON.stringify(arg))

  }
  deletar(id: any){
    this.storage.remove(id)
  }

  async retorno(){
    let arraycontato: Contatos [] = []

    await this.storage.forEach((value: string) => 
        {const contato: Contatos = JSON.parse(value); arraycontato.push(contato)})

    return arraycontato
  }

  async Filtrar(id : any) {
    const user = JSON.parse(await this.storage.get(id))
    return user
  }
 }
