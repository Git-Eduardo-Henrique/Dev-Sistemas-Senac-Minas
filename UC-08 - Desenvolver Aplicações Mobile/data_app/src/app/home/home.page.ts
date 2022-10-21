import { Component, OnInit} from '@angular/core';
//impots
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Guid } from 'guid-typescript';
import { Nomes } from '../models/nomes.model';
import { NomeService } from '../servics/nome.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit{

  private nome: Nomes
  public nome_form: FormGroup
  public arraynome: any

  constructor(
    private  formBuilder: FormBuilder,
    private nomeservice: NomeService
  ) {}

  submit(){
    if (this.nome_form.valid){
      this.nomeservice.insert(this.nome_form.value)
    }
  }


  ngOnInit() {
    this.nome = {
      id: Guid.createEmpty(), nome: ''
    }

    this.nome_form = this.formBuilder.group(
      {id: [this.nome.id], nome: [this.nome.nome, Validators.required]}
    )

    this.nomeservice.list().then(arrayPessoa => {this.arraynome = arrayPessoa})
  }
}
