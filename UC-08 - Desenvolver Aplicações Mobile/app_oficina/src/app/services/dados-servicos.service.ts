import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DadosServicosService {

  private Servicos = [
    {id: 1, nome:'Alinhamento', valor: 69.98}, 
    {id: 2, nome: 'Balanceamento', valor: 59.98},
    {id: 3, nome: 'Troca de Oleo', valor: 119.98}, 
    {id: 4, nome: 'Troca de Pneu', valor: 99.98}
  ]

  constructor() { }

  
  EnviarDados() {
    return this.Servicos
  }

  FiltrarDadosId(id:number){
    const servicoSeleciona = this.Servicos.filter(servico => servico.id === id)
    return servicoSeleciona[0]
  }
}
