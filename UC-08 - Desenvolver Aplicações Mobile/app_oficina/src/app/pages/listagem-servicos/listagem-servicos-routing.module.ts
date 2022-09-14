import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ListagemServicosPage } from './listagem-servicos.page';

const routes: Routes = [
  {
    path: '',
    component: ListagemServicosPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ListagemServicosPageRoutingModule {}
