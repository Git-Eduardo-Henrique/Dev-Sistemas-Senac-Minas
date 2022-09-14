import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DadosServicosService } from 'src/app/services/dados-servicos.service'

@Component({
  selector: 'app-detalhes-servicos',
  templateUrl: './detalhes-servicos.page.html',
  styleUrls: ['./detalhes-servicos.page.scss'],
})
export class DetalhesServicosPage implements OnInit {

  public dadoSeleciona: any

  constructor(
    private objDados: DadosServicosService, 
    private route: ActivatedRoute
    ) {

    }

  ngOnInit() {
    const id: number = Number(this.route.snapshot.paramMap.get('id'))
    this.dadoSeleciona = this.objDados.FiltrarDadosId(id)
  }

}
