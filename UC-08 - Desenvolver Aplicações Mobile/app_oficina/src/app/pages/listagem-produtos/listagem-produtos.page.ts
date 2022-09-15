import { Component, OnInit } from '@angular/core';
import {DadosProdutosService} from 'src/app/products/dados-produtos.service'

@Component({
  selector: 'app-listagem-produtos',
  templateUrl: './listagem-produtos.page.html',
  styleUrls: ['./listagem-produtos.page.scss'],
})
export class ListagemProdutosPage implements OnInit {

  public Produtos: any

  constructor( private Objprodutos: DadosProdutosService) { 
    this.Produtos = Objprodutos.EnviarDados()
  }

  ngOnInit() {
  }

}
