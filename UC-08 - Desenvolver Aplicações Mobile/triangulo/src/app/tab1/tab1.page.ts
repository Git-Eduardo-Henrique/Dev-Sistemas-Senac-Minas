import { Component } from '@angular/core';
import { AlertController } from '@ionic/angular';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss', '../explore-container/explore-container.component.scss']
})
export class Tab1Page {
  ladoA: string
  ladoB: string
  ladoC: string
  exibidor: string
  imagem: any = 'assets/icon/favicon.png'

  constructor(private alertController: AlertController) {}

  async presentAlert() {
    const alert = await this.alertController.create({
      header: 'TRIANGULO NÃO EXISTE',
      subHeader: 'tente novamente com outros valores',
      buttons: ['fechar'],
    })
    await alert.present()
  }

  veri() {
    var veri1 = Number(this.ladoA + this.ladoB > this.ladoC)
    var veri2 = Number(this.ladoA + this.ladoC > this.ladoB)
    var veri3 = Number(this.ladoB + this.ladoC > this.ladoA)
    if (veri1 && veri2 && veri3){

      var lA = Number(this.ladoA)
      var lB = Number(this.ladoB)
      var lC = Number(this.ladoC)

      if (lA == lB && lB == lC) {
        this.exibidor = 'triangulo equilátero'
        this.imagem = 'assets/icon/tri_equi.png'
      }
      else if (lA != lB && lB != lC) {
        this.exibidor = 'triangulo escaleno'
        this.imagem = 'assets/icon/tri_esca.png'
      }
      else {
        this.exibidor = 'triangulo isósceles'
        this.imagem = 'assets/icon/tri_isos.png'
      }
    }
    else {
      this.presentAlert()
      this.imagem = 'assets/icon/favicon.png'
    }
  }

}
