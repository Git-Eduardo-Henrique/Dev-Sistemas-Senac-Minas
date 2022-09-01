import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-formulario',
  templateUrl: './formulario.page.html',
  styleUrls: ['./formulario.page.scss'],
})
export class FormularioPage implements OnInit {
  pessoa = {}
  pessoaForm: FormGroup


  constructor(private formularioBuilder: FormBuilder) { }

  submit() {
    console.log('ui')
  }

  ngOnInit() {
    this.pessoaForm = this.formularioBuilder.group({
      nome: ['', Validators.required],
      tele: ['', Validators.required],
      cpf: ['', Validators.required]
    })
  }

}
