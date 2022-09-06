import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { FormularioPageRoutingModule } from './formulario-routing.module';

import { FormularioPage } from './formulario.page';

import { SimpleMaskModule } from 'ngx-ion-simple-mask'

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    FormularioPageRoutingModule,
    ReactiveFormsModule,
    SimpleMaskModule
  ],
  declarations: [FormularioPage]
})
export class FormularioPageModule {}
