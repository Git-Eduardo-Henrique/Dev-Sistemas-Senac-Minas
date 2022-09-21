import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { InfoContatosPageRoutingModule } from './info-contatos-routing.module';

import { InfoContatosPage } from './info-contatos.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    InfoContatosPageRoutingModule
  ],
  declarations: [InfoContatosPage]
})
export class InfoContatosPageModule {}
