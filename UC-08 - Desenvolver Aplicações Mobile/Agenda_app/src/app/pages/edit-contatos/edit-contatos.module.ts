import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { EditContatosPageRoutingModule } from './edit-contatos-routing.module';

import { EditContatosPage } from './edit-contatos.page';

import { SimpleMaskModule } from 'ngx-ion-simple-mask'

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    EditContatosPageRoutingModule,
    ReactiveFormsModule,
    SimpleMaskModule
  ],
  declarations: [EditContatosPage]
})
export class EditContatosPageModule {}
