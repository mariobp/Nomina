import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { CargoComponent, CargoListComponent, EditCargoComponent } from './cargo/cargo.component';
import { GeneralComponent } from './general/general.component';
import { TipocontratoComponent, TipoContratoListComponent, EditTipoContratoComponent } from './tipocontrato/tipocontrato.component';
import { CargoService } from './cargo/cargo.service';
import { TipoContratoService } from './tipocontrato/tipocontrato.service';

export const ConfiguracionRoutes: Routes = [
  {
    path: '', children: [
      { path: 'cargos', component: CargoComponent, children: [
        { path: '', component: CargoListComponent },
        { path: ':id/edit', component: EditCargoComponent, resolve: { item: CargoService} }
      ] },
      { path: 'general', component: GeneralComponent },
      { path: 'tipo/contrato', component: TipocontratoComponent, children: [
        { path: '', component: TipoContratoListComponent },
        { path: ':id/edit', component: EditTipoContratoComponent, resolve: { item: TipoContratoService} }
      ] }
    ]
  }
]

export const ConfiguracionMenuMeta: MenuMeta[] = [
  { title: 'Cargos', url: '/configuracion/cargos', icon: 'extension' },
  { title: 'Tipos de Contrato', url: '/configuracion/tipo/contrato', icon: 'extension' },
  { title: 'Configuración General', url: '/configuracion/general', icon: 'extension' }
]
