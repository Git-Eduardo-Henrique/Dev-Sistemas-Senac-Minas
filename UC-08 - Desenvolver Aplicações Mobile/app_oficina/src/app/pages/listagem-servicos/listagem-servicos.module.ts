import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ListagemServicosPageRoutingModule } from './listagem-servicos-routing.module';

import { ListagemServicosPage } from './listagem-servicos.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ListagemServicosPageRoutingModule
  ],
  declarations: [ListagemServicosPage]
})
export class ListagemServicosPageModule {}
