import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Route } from '@angular/router';
import { DadosContatosServiceService } from 'src/app/dadosContatos/dados-contatos-service.service';

@Component({
  selector: 'app-info-contatos',
  templateUrl: './info-contatos.page.html',
  styleUrls: ['./info-contatos.page.scss'],
})
export class InfoContatosPage implements OnInit {

  public dadoContato : any

  constructor( 
    private ObjContato : DadosContatosServiceService,
    private route : ActivatedRoute) {

     }

  ngOnInit() {
    const id: number = Number(this.route.snapshot.paramMap.get('id'))
    this.dadoContato = this.ObjContato.Filtrar(id)
  }

}
