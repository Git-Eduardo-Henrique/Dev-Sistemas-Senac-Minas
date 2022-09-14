import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { DetalhesServicosPageRoutingModule } from './detalhes-servicos-routing.module';

import { DetalhesServicosPage } from './detalhes-servicos.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    DetalhesServicosPageRoutingModule
  ],
  declarations: [DetalhesServicosPage]
})
export class DetalhesServicosPageModule {}
