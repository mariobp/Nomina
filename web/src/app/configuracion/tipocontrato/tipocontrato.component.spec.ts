import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TipocontratoComponent } from './tipocontrato.component';

describe('TipocontratoComponent', () => {
  let component: TipocontratoComponent;
  let fixture: ComponentFixture<TipocontratoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TipocontratoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TipocontratoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
