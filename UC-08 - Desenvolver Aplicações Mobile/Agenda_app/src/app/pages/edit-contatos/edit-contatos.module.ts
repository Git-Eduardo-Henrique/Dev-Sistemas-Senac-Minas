import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { EditContatosPageRoutingModule } from './edit-contatos-routing.module';

import { EditContatosPage } from './edit-contatos.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    EditContatosPageRoutingModule
  ],
  declarations: [EditContatosPage]
})
export class EditContatosPageModule {}
