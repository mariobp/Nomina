import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CompensacionComponent } from './compensacion.component';

describe('CompensacionComponent', () => {
  let component: CompensacionComponent;
  let fixture: ComponentFixture<CompensacionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CompensacionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CompensacionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
