import { Injectable } from '@angular/core';

// banco de dados
import { Guid } from "guid-typescript";
import { Storage } from '@ionic/storage-angular';
import { Contatos } from '../models/contatos.model';


@Injectable({
  providedIn: 'root'
})
export class DadosContatosServiceService {

  
  // private Contatos = [
  //   {id: 1, 
  //     nome: 'Eduardo', 
  //     sobrenome: 'Henrique', 
  //     tipo_num: 'trabalho',
  //     num: '(035) 9 4002-8922', 
  //     email: 'taty@gmail.com'}
  // ]


  public array: any

  constructor(
    private storage: Storage) { }

  // update
  adicionar(arg : Contatos) {
    arg.id = Guid.create()
    this.storage.set(arg.id.toString(), JSON.stringify(arg))

    // novo_contato.id = this.Contatos.length + 1
    // this.Contatos.push(novo_contato)
  }

  async retorno(){
    let arraycontato: Contatos [] = []

    await this.storage.forEach((value: string) => 
        {const contato: Contatos = JSON.parse(value); arraycontato.push(contato)})

    return arraycontato
  }
  
  // deletar(remover){
  //   const index = this.Contatos.indexOf(remover)
  //   this.Contatos.splice(index, 1)
  // }

  // async Filtrar(id : any) {
  //   let arraycontato: Contatos [] = []

  //   await this.storage.forEach((value: string) => 
  //       {const contato: Contatos = JSON.parse(value); arraycontato.push(contato)})
    
    
  //   for (var sus in arraycontato){
  //     console.log('array = ', arraycontato[sus].id)
  //   }
  //   return arraycontato.filter(servico => servico.id === id)
 
    //========================
    // let arraycontato: Contatos [] = []

    // await this.storage.forEach((value: string) => 
    //     {const contato: Contatos = JSON.parse(value); arraycontato.push(contato)})
   
    // for (var single in arraycontato) {
    //   if (arraycontato[single].id == id) {

    //     console.log('foi')

    //     var receba = arraycontato[single]

    //     return receba
    //   }

    //   else {
    //     console.log("nao foi")
    //   }
  //   }
 }

