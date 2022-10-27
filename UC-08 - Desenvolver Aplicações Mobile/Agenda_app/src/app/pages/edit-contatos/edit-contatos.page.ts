import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AlertController } from '@ionic/angular';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { Guid } from "guid-typescript";
import { Contatos } from 'src/app/models/contatos.model';
import { DadosContatosServiceService } from 'src/app/dadosContatos/dados-contatos-service.service'

@Component({
  selector: 'app-edit-contatos',
  templateUrl: './edit-contatos.page.html',
  styleUrls: ['./edit-contatos.page.scss'],
})
export class EditContatosPage implements OnInit {

  public janela = true
  public delete = false

  private contato: Contatos
  public contatoForm: FormGroup

  constructor( 
    private route: ActivatedRoute,
    private alerta: AlertController,
    private _router: Router,

    private dadosContats: DadosContatosServiceService,
    private formulario: FormBuilder) { }

 // ==============================================================================================================

  // async Excluir_contato() {
  //    const alert = await this.alerta.create({
  //     header: 'Atenção',
  //     subHeader: '',
  //     message: 'Este contato sera excluido e não podera mais ser resgatado!',
  //     buttons: [{text: 'Cancelar', role: 'cancel',
  //                handler: ()=> {}}, 
  //               {text: 'Deletar', role: 'confirm', 
  //               handler: ()=> {this.deletar_id(), this._router.navigate(['/home'])}}],
  //   });
  //    await alert.present();
  //   }

   async Erro() {
     const alert = await this.alerta.create({
      header: 'contato não validado!',
      subHeader: '',
      message: 'preencha cada campo com a formatação certa!',
      buttons: ['OK'],
    });
     await alert.present();
    }

  // ==============================================================================================================

  editar() {
    this.janela = false
  }

  submit(){
    var id: any = String(this.route.snapshot.paramMap.get('id'))
    if (this.contatoForm.valid){
      if (id = 'edit') {
        this.dadosContats.adicionar(this.contatoForm.value)
        this.janela = true
        this._router.navigate(['/home'])
      }
      else {
        this.janela = true
      }
    }
    else {
      this.Erro()
    }
  }

  // deletar_id(){
  //   this.dadosContats.deletar(this.dados)
  // }

  ngOnInit() {

    var id: any =  String(this.route.snapshot.paramMap.get('id'))

    if (id = 'edit'){
      // this.dados = {id, nome: '', sobrenome: '', tipo_num: '',num: '', email: ''}
      this.contato = {id: Guid.createEmpty(), nome: '', sobrenome: '', tipo_num: '', num: '', email: ''}

      this.janela = false
      this.delete = true
    }
    else {
      // this.dados = this.dadosContats.Filtrar(id)
      this.delete = false
    }

    this.contatoForm = this.formulario.group({
      nome: [this.contato.nome, Validators.compose([Validators.required, Validators.minLength(3), Validators.maxLength(15)])],
      sobrenome: [this.contato.sobrenome, Validators.compose([Validators.minLength(3), Validators.maxLength(15)])],
      email: [this.contato.tipo_num, Validators.compose([Validators.maxLength(45), Validators.email])],
      num: [this.contato.num, Validators.compose([Validators.required, Validators.maxLength(17)])],  
      tipo_num: [this.contato.email, Validators.required]
    })
  }

}
