import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DadosProdutosService {

  private Produtos = [
    {id: 1, nome: 'Figurinha da copa', valor: 4},
    {id: 2, nome: 'Boneco AmongUS', valor: 50},
    {id: 3, nome: 'Rtx 3090', valor: 2500},
    {id: 4, nome: 'Redmi note 12', valor: 2000},
    {id: 5, nome: 'Manga HTML e CSS', valor: 75},
    {id: 6, nome: 'Pão de queijo', valor: 3}
  ]

  constructor() { }

  EnviarDados() {
    return this.Produtos
  }
  RecebeDados(dadosRecebidos : any){
    dadosRecebidos.id = this.Produtos.length + 1
    this.Produtos.push(dadosRecebidos)
  }

  RemoverDados(item : any){
    const index = this.Produtos.indexOf(item)
    this.Produtos.splice(index, 1)
  }

  FiltrarDados(id: number) {
    const selecionaProdu = this.Produtos.filter(produto => produto.id === id)
    return selecionaProdu[0]
  }
}
