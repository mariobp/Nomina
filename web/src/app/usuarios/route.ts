import { Routes } from '@angular/router';
import { MenuMeta } from '../app.routing';
import { AsistenteComponent, AsistenteEditComponent, AsistenteListComponent } from './asistente/asistente.component';
import { AdminComponent } from './admin/admin.component';
import { AsistenteResolver } from './asistente/asistente.service';

export const UsuariosRoutes: Routes = [
    {
        path: '', children: [
            { path: 'admin', component: AdminComponent },
            { path: 'asistente', component: AsistenteComponent, children: [
                { path: '', component: AsistenteListComponent},
                { path: ':id/edit', component: AsistenteEditComponent, resolve: { asistente: AsistenteResolver }}
            ]},
        ]
    }

];

export const UsuariosMenuMeta: MenuMeta[] = [
    { title: 'Administrador', url: '/usuarios/admin', icon: 'account_box' },
    { title: 'Asistente', url: '/usuarios/asistente', icon: 'supervisor_account' },
];
