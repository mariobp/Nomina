import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { CargoComponent, CargoListComponent } from './cargo/cargo.component';
import { GeneralComponent } from './general/general.component';
import { TipocontratoComponent } from './tipocontrato/tipocontrato.component';

export const ConfiguracionRoutes: Routes = [
  {
    path: '', children: [
      { path: 'cargos', component: CargoComponent, children: [
        { path: '', component: CargoListComponent }
      ] },
      { path: 'general', component: GeneralComponent },
      { path: 'tipos', component: TipocontratoComponent }
    ]
  }
]

export const ConfiguracionMenuMeta: MenuMeta[] = [
  { title: 'Cargos', url: '/configuracion/cargos', icon: 'extension' },
  { title: 'Tipos de Contrato', url: '/configuracion/tipos', icon: 'extension' },
  { title: 'Configuración General', url: '/configuracion/general', icon: 'extension' }
]
