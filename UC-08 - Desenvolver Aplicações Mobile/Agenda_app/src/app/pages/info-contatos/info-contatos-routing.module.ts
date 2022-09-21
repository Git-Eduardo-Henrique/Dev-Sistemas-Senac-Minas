import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { InfoContatosPage } from './info-contatos.page';

const routes: Routes = [
  {
    path: '',
    component: InfoContatosPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class InfoContatosPageRoutingModule {}
