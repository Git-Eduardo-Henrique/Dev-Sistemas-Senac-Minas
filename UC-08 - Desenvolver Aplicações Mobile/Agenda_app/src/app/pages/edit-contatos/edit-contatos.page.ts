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
  public delete = false
  public dados: any

  constructor( private dadosContats: DadosContatosServiceService,
    private route: ActivatedRoute) { }

  editar() {
    this.janela = false
  }

  mostrar(){
    const id: number = Number(this.route.snapshot.paramMap.get('id'))
    if (id > 0) {
      this.janela = true
    }
    else {
      this.dadosContats.adicionar(this.dados)
      this.janela = true
    }
  }
  
  deletar_id(){
    this.dadosContats.deletar(this.dados)
  }

  ngOnInit() {
    const id: number = Number(this.route.snapshot.paramMap.get('id'))
    if (id > 0){
      this.dados = this.dadosContats.Filtrar(id)
      this.delete = false
    }
    else {
      this.dados = {id, nome: '', num: '', email: ''}
      this.janela = false
      this.delete = true
    }
  }

}
