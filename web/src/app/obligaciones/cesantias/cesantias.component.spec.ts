import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CesantiasComponent } from './cesantias.component';

describe('CesantiasComponent', () => {
  let component: CesantiasComponent;
  let fixture: ComponentFixture<CesantiasComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CesantiasComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CesantiasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
