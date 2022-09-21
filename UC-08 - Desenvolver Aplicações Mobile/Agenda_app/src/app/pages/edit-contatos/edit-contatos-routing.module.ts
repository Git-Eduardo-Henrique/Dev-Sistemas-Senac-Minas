import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { EditContatosPage } from './edit-contatos.page';

const routes: Routes = [
  {
    path: '',
    component: EditContatosPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class EditContatosPageRoutingModule {}
