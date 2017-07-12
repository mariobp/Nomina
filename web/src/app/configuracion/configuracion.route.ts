import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { CargoComponent, CargoListComponent, EditCargoComponent } from './cargo/cargo.component';
import { GeneralComponent, EditGeneralComponent } from './general/general.component';
import { TipocontratoComponent, TipoContratoListComponent, EditTipoContratoComponent } from './tipocontrato/tipocontrato.component';
import { TarifarioComponent, TarifarioListComponent, EditTarifarioComponent } from './tarifario/tarifario.component';
import { UnidadproduccionComponent, EditUnidadProduccionComponent, UnidadProduccionListComponent} from './unidadproduccion/unidadproduccion.component';
import { BancoComponent, BancoListComponent, EditBancoComponent } from './banco/banco.component';
import { CargoService } from './cargo/cargo.service';
import { TipoContratoService } from './tipocontrato/tipocontrato.service';
import { UnidadProduccionService } from './unidadproduccion/unidadproduccion.service';
import { TarifarioService } from './tarifario/tarifario.service';
import { BancoService } from './banco/banco.service';

export const ConfiguracionRoutes: Routes = [
    {
        path: '', children: [
            {
                path: 'cargos', component: CargoComponent, data: { miga: 'Cargos' }, children: [
                    { path: '', component: CargoListComponent },
                    { path: ':id/edit', component: EditCargoComponent, data: { miga: 'Editar' }, resolve: { item: CargoService } }
                ]
            },
            {
                path: 'general', component: GeneralComponent, children: [
                    { path: '', component: EditGeneralComponent }
                ]
            },
            {
                path: 'tipo/contrato', component: TipocontratoComponent, data: { miga: 'Tipos de contratos' }, children: [
                    { path: '', component: TipoContratoListComponent },
                    { path: ':id/edit', component: EditTipoContratoComponent, data: { miga: 'Editar' }, resolve: { item: TipoContratoService } }
                ]
            },
            {
                path: 'unidad/produccion', component: UnidadproduccionComponent, data: { miga: 'Unidades de producción' }, children: [
                    { path: '', component: UnidadProduccionListComponent },
                    { path: ':id/edit', component: EditUnidadProduccionComponent, data: { miga: 'Editar' }, resolve: { item: UnidadProduccionService } }
                ]
            },
            {
                path: 'tarifario', component: TarifarioComponent, data: { miga: 'Tarifario' }, children: [
                    { path: '', component: TarifarioListComponent },
                    { path: ':id/edit', component: EditTarifarioComponent, data: { miga: 'Editar' }, resolve: { item: TarifarioService } }

                ]
            },

            {
                path: 'banco', component: BancoComponent, data: { miga: 'Bancos' }, children: [
                    { path: '', component: BancoListComponent },
                    { path: ':id/edit', component: EditBancoComponent, data: { miga: 'Editar' }, resolve: { item: BancoService } }

                ]
            }
        ]
    }
]

export const ConfiguracionMenuMeta: MenuMeta[] = [
    { title: 'Banco', url: '/configuracion/banco', icon: 'extension' },
    { title: 'Cargos', url: '/configuracion/cargos', icon: 'extension' },
    { title: 'Tipos de Contrato', url: '/configuracion/tipo/contrato', icon: 'extension' },
    { title: 'Unidad de producción', url: '/configuracion/unidad/produccion', icon: 'extension' },
    { title: 'Tarifario', url: '/configuracion/tarifario', icon: 'extension' },
    { title: 'Configuración General', url: '/configuracion/general', icon: 'extension' },
]
