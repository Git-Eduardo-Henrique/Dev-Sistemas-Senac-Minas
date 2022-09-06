import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AlertController } from '@ionic/angular';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.page.html',
  styleUrls: ['./formulario.page.scss'],
})
export class FormularioPage implements OnInit {
  pessoa = {}
  pessoaForm: FormGroup


  constructor(private formularioBuilder: FormBuilder, private alertController: AlertController) { }

  async presentAlert() {
    const alert = await this.alertController.create({
      header: 'Dados Invalidos',
      subHeader: 'Siga a orientação certa ',
      buttons: ['fechar'],
    })
    await alert.present()
  }

  submit() {
    if (this.pessoaForm.valid){
      console.log(this.pessoa)
    }
    else {
      this.presentAlert()
    }
  }

  ngOnInit() {
    this.pessoaForm = this.formularioBuilder.group({
      nome: ['', Validators.compose([Validators.required, Validators.maxLength(45), Validators.minLength(3)])],
      email: ['', Validators.compose([Validators.required, Validators.maxLength(45), Validators.email])],
      tele: ['', Validators.compose([Validators.required, Validators.maxLength(11), Validators.minLength(11)])],
      cpf: ['', Validators.compose([Validators.required, Validators.minLength(14)])]
    })
  }

}
