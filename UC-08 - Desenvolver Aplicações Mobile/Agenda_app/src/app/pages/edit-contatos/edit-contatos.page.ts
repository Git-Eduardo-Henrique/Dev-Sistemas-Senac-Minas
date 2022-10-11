import { Component, OnInit } from '@angular/core';
import { DadosContatosServiceService } from 'src/app/dadosContatos/dados-contatos-service.service'
import { ActivatedRoute, Router } from '@angular/router';
import { AlertController } from '@ionic/angular';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-edit-contatos',
  templateUrl: './edit-contatos.page.html',
  styleUrls: ['./edit-contatos.page.scss'],
})
export class EditContatosPage implements OnInit {

  public janela = true
  public delete = false
  dados: any
  contatoForm: FormGroup


  constructor( 
    private dadosContats: DadosContatosServiceService,
    private route: ActivatedRoute,
    private alerta: AlertController,
    private formulario: FormBuilder,
    private _router: Router) { }

  async Excluir_contato() {
     const alert = await this.alerta.create({
      header: 'Atenção',
      subHeader: '',
      message: 'Este contato sera excluido e não podera mais ser resgatado!',
      buttons: [{text: 'Cancelar', role: 'cancel',
                 handler: ()=> {}}, 
                {text: 'Deletar', role: 'confirm', 
                handler: ()=> {this.deletar_id(), this._router.navigate(['/home'])}}],
    });
     await alert.present();
    }

   async Erro() {
     const alert = await this.alerta.create({
      header: 'contato não validado!',
      subHeader: '',
      message: 'preencha cada campo com a formatação certa!',
      buttons: ['OK'],
    });
     await alert.present();
    }

  editar() {
    this.janela = false
  }

  submit(){
    const id: number = Number(this.route.snapshot.paramMap.get('id'))
    if (this.contatoForm.valid){
      if (id > 0) {
        this.janela = true
      }
      else {
        this.dadosContats.adicionar(this.dados)
        this.janela = true
        this._router.navigate(['/home'])
      }
    }
    else {
      this.Erro()
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
      this.dados = {id, nome: '', sobrenome: '', tipo_num: '',num: '', email: ''}
      this.janela = false
      this.delete = true
    }

    this.contatoForm = this.formulario.group({
      nome: ['', Validators.compose([Validators.required, Validators.minLength(3), Validators.maxLength(15)])],
      sobrenome: ['', Validators.compose([Validators.minLength(3), Validators.maxLength(15)])],
      email: ['', Validators.compose([Validators.maxLength(45), Validators.email])],
      num: ['', Validators.compose([Validators.required, Validators.maxLength(17)])],  
      tipo_num: ['', Validators.required]
    })
  }

}
