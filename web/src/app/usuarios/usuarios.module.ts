import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AsistenteComponent } from './asistente/asistente.component';
import { AdminComponent } from './admin/admin.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [AsistenteComponent, AdminComponent]
})
export class UsuariosModule { }
