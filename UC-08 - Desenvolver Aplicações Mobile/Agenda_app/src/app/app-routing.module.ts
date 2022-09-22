import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'home',
    loadChildren: () => import('./home/home.module').then( m => m.HomePageModule)
  },
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'info-contatos',
    loadChildren: () => import('./pages/info-contatos/info-contatos.module').then( m => m.InfoContatosPageModule)
  },
  {
    path: 'edit-contatos/:id',
    loadChildren: () => import('./pages/edit-contatos/edit-contatos.module').then( m => m.EditContatosPageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
