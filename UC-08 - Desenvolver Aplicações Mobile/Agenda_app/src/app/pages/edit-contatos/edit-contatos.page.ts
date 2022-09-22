import { Component, OnInit } from '@angular/core';
import { DadosContatosServiceService } from 'src/app/dadosContatos/dados-contatos-service.service'
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-edit-contatos',
  templateUrl: './edit-contatos.page.html',
  styleUrls: ['./edit-contatos.page.scss'],
})
export class EditContatosPage implements OnInit {

  public janela = true
  public dados: any

  constructor( private dadosContats: DadosContatosServiceService,
    private route: ActivatedRoute) { }

  editar() {
    this.janela = false
  }

  mostrar(){
    this.janela = true
  }

  ngOnInit() {
    const id: number = Number(this.route.snapshot.paramMap.get('id'))
    this.dados = this.dadosContats.Filtrar(id)
  }

}
