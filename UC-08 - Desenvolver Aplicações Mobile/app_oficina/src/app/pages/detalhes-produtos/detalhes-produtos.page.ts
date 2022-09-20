import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DadosProdutosService} from 'src/app/products/dados-produtos.service'

@Component({
  selector: 'app-detalhes-produtos',
  templateUrl: './detalhes-produtos.page.html',
  styleUrls: ['./detalhes-produtos.page.scss'],
})
export class DetalhesProdutosPage implements OnInit {

  public dadoseleciona: any
  public altera = false

  constructor(
    private ObjProdu:  DadosProdutosService,
    private route: ActivatedRoute
  ) { }

  encerrarEdicao() {
    const id: number = Number(this.route.snapshot.paramMap.get('id'))
    if (id > 0) {
      this.altera = false
    }
    else {
      this.ObjProdu.RecebeDados(this.dadoseleciona)
      this.altera = false
    }
  }

  Editar(){
    this.altera = true
  }

  RemoverProdu(){
    const id: number = Number(this.route.snapshot.paramMap.get('id'))
    this.dadoseleciona = this.ObjProdu.FiltrarDados(id)
    this.ObjProdu.RemoverDados(this.dadoseleciona)
  }

  ngOnInit() {
    const id: number = Number(this.route.snapshot.paramMap.get('id'))
    if (id > 0) {
      this.dadoseleciona = this.ObjProdu.FiltrarDados(id)
    }
    else{
      this.dadoseleciona = {id, nome: '', valor: ''}
      this.altera = true
    }
  }

}
