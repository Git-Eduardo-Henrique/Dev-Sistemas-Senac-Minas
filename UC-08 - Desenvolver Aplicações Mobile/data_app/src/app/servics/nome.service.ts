
import { Injectable } from '@angular/core';
// imports

import { Nomes } from '../models/nomes.model';
import { Guid } from 'guid-typescript';
import { Storage } from '@ionic/storage-angular';

@Injectable({
  providedIn: 'root'
})
export class NomeService {

  constructor(private home_storage: Storage) { }

  insert(arg: Nomes){  // inserir no db
    arg.id = Guid.create()
    this.home_storage.set(arg.id.toString(), JSON.stringify(arg))
  }

  async list() {
    let arrayPessoa: Nomes [] = [];

    await this.home_storage.forEach((value: string) => 
    {const pessoa: Nomes = JSON.parse(value); arrayPessoa.push(pessoa)}) 

    return arrayPessoa
  }
}
