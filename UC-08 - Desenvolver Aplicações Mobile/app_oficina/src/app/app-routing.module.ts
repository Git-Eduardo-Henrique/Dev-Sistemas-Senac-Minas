import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: 'home',
    loadChildren: () => import('./home/home.module').then( m => m.HomePageModule)
  },
  {
    path: '',
    redirectTo: 'listagem-servicos',
    pathMatch: 'full'
  },
  {
    path: 'listagem-servicos',
    loadChildren: () => import('./pages/listagem-servicos/listagem-servicos.module').then( m => m.ListagemServicosPageModule)
  },
  {
    path: 'detalhes-servicos/:id',
    loadChildren: () => import('./pages/detalhes-servicos/detalhes-servicos.module').then( m => m.DetalhesServicosPageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
