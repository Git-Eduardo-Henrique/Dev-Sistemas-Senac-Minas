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
  public altera = true

  constructor(
    private ObjProdu:  DadosProdutosService,
    private route: ActivatedRoute
  ) { }

  ngOnInit() {
    const id: number = Number(this.route.snapshot.paramMap.get('id'))
    this.dadoseleciona = this.ObjProdu.FiltrarDados(id)
  }

}
