import { Injectable } from '@angular/core';

// banco de dados
import { Guid } from "guid-typescript";
import { Storage } from '@ionic/storage-angular';
import { Contatos } from '../models/contatos.model';


@Injectable({
  providedIn: 'root'
})
export class DadosContatosServiceService {


  public array: any

  constructor(
    private storage: Storage) { }

  adicionar(arg : Contatos) {
    arg.id = Guid.create()
    this.storage.set(arg.id.toString(), JSON.stringify(arg))

  }

  async retorno(){
    let arraycontato: Contatos [] = []

    await this.storage.forEach((value: string) => 
        {const contato: Contatos = JSON.parse(value); arraycontato.push(contato)})

    return arraycontato
  }
  
  
 }

