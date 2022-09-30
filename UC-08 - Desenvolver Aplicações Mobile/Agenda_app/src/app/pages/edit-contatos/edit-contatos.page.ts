import { Component, OnInit } from '@angular/core';
import { DadosContatosServiceService } from 'src/app/dadosContatos/dados-contatos-service.service'
import { ActivatedRoute } from '@angular/router';
import { AlertController } from '@ionic/angular';

@Component({
  selector: 'app-edit-contatos',
  templateUrl: './edit-contatos.page.html',
  styleUrls: ['./edit-contatos.page.scss'],
})
export class EditContatosPage implements OnInit {

  public janela = true
  public delete = false
  public dados: any

  constructor( 
    private dadosContats: DadosContatosServiceService,
    private route: ActivatedRoute,
    private alerta: AlertController) { }

  async presentAlert() {
     const alert = await this.alerta.create({
      header: 'Atenção',
      subHeader: '',
      message: 'Este contato sera excluido e não podera mais ser resgatado!',
      buttons: [{text: 'Cancelar', role: 'cancel'}, 
                {text: 'Deletar', role: 'confirm', 
                handler: ()=> this.deletar_id()}],
    });
     await alert.present();
    }

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
  mostrar_alert(){
    this.presentAlert()
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
      this.dados = {id, nome: '', sobrenome: '', tipo_num: '',num: '', email: ''}
      this.janela = false
      this.delete = true
    }
  }

}
