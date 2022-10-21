import { Injectable } from '@angular/core';

import { imc } from '../models/imc.model';
import { Guid } from 'guid-typescript';
import { Storage } from '@ionic/storage-angular';

@Injectable({
  providedIn: 'root'
})
export class ImcDbService {

  constructor(
    private storage: Storage
  ) { }

  insert(arg: imc){  // inserir no db
    arg.id = Guid.create()
    this.storage.set(arg.id.toString(), JSON.stringify(arg))
  }
  
  async lista() {
    let arrayall: imc [] = [];

    await this.storage.forEach((value: string) => 
    {const pessoa: imc = JSON.parse(value); arrayall.push(pessoa)}) 

    return arrayall
  }
}
