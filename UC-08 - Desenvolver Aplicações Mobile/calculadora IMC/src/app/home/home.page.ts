import { Component, OnInit} from '@angular/core';
import { AlertController } from '@ionic/angular';

import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Guid } from 'guid-typescript';
import { imc } from '../models/imc.model';
import { ImcDbService } from '../services/imc-db.service'; 

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {

  private imcs: imc

  public vetor: any
  public imc: any

  public formG: FormGroup

  sexo_opt: string
  altura: string
  peso: string
  resul: string
  msg: string
  imagem: any = 'assets/icon/favicon.png'

  constructor(
    private alertController: AlertController,
    private formbuild: FormBuilder,
    private service: ImcDbService
  ) {}

  async presentAlert() {
    const alert = await this.alertController.create({
      header: 'RESULTADO DO IMC',
      subHeader: this.resul,
      message: this.msg,
      buttons: ['fechar'],
    })
    await alert.present()
  }

  imcc() {
    if (this.sexo_opt == null) {
      this.msg = 'selecione um sexo!!!'
    } 

    else {
      var p = parseFloat(this.peso)
      var a = parseFloat(this.altura)
      this.imc = p / a**2
      this.resul = this.imc.toFixed(2)

      if (this.sexo_opt == 'f'){
        if (this.imc <= 19) {
          this.msg = 'abaixo do peso'
          this.imagem = 'assets/icon/alerta.png'
        }
        else if (this.imc > 19 && this.imc <=27.3) {
          this.msg = 'peso normal'
          this.imagem = 'assets/icon/normal.png'
        } 
        else {
          this.msg = 'acima do peso'
          this.imagem = 'assets/icon/alerta_vermelho.png'
        }
      }

      if (this.sexo_opt == 'm'){
        if (this.imc <= 20.7) {
          this.msg = 'abaixo do peso'
          this.imagem = 'assets/icon/alerta.png'
        }
        else if (this.imc > 20.7 && this.imc <=27.8) {
          this.msg = 'peso normal'
          this.imagem = 'assets/icon/normal.png'
        } 
        else {
          this.msg = 'acima do peso'
          this.imagem = 'assets/icon/alerta_vermelho.png'
          
        }
      }
    }
    this.presentAlert()
  }

  submit(){
    if (this.formG.valid){

      // guarda o formulario em uma variavel
      this.vetor = this.formG.value
      this.vetor.imc = this.imc
      this.vetor.resul = this.msg

      this.service.insert(this.vetor)
    }
  }

  ngOnInit() {
    this.imcs = {id: Guid.createEmpty(), sexo:'', altura: '', peso: '', imc: '', resul: ''}

    this.formG = this.formbuild.group({
      id: [this.imcs.id],
      sexo: [this.imcs.sexo, Validators.required],
      altura: [this.imcs.altura, Validators.required],
      peso: [this.imcs.peso, Validators.required],
      imc: [this.imcs.imc],
      resul: [this.imcs.resul]
    })
  }

}
