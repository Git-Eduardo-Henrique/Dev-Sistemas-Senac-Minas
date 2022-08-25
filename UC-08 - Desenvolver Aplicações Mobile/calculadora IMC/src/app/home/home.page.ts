import { Component } from '@angular/core';
import { AlertController } from '@ionic/angular';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  sexo_opt: string
  altura: string
  peso: string
  resul: string
  msg: string
  imagem: any = 'assets/icon/favicon.png'

  constructor(private alertController: AlertController) {}

  async presentAlert() {
    const alert = await this.alertController.create({
      header: 'RESULTADO DO IMC',
      subHeader: this.resul,
      message: this.msg,
      buttons: ['fechar'],
    })
    await alert.present()
  }

  imc() {
    if (this.sexo_opt == null) {
      this.msg = 'selecione um sexo!!!'
    } 

    else {
      var p = parseFloat(this.peso)
      var a = parseFloat(this.altura)
      var imc = p / a**2
      this.resul = imc.toFixed(2)

      if (this.sexo_opt == 'f'){
        if (imc <= 19) {
          this.msg = 'abaixo do peso'
          this.imagem = 'assets/icon/alerta.png'
        }
        else if (imc > 19 && imc <=27.3) {
          this.msg = 'peso normal'
          this.imagem = 'assets/icon/normal.png'
        } 
        else {
          this.msg = 'acima do peso'
          this.imagem = 'assets/icon/alerta_vermelho.png'
        }
      }

      if (this.sexo_opt == 'm'){
        if (imc <= 20.7) {
          this.msg = 'abaixo do peso'
          this.imagem = 'assets/icon/alerta.png'
        }
        else if (imc > 20.7 && imc <=27.8) {
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

}
