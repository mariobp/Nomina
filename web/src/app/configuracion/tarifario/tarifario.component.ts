import { Component, ViewChild, AfterViewInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { FormComponent, TableComponent, RenderInput } from '../../../lib/components'
import { TarifarioService } from './tarifario.service';


@Component({
    template: '<router-outlet></router-outlet>'

})
export class TarifarioComponent { }
