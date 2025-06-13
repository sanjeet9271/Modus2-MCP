-----
applyTo: "*.ts, *.html"
-----

# Modus Angular Component Patterns

> **Important Note**: These instructions only **apply to** Angular Projects.
> **LEAD LEVEL GUIDANCE**: This document provides Angular-specific patterns for implementing Modus components effectively.

## Component Implementation Patterns

### ModusButton

```typescript
import { Component, ViewChild, ElementRef, AfterViewInit, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-button',
  template: `
    <modus-button
      #modusButton
      color="primary"
      type="button"
    >
      Click Me
    </modus-button>
  `
})
export class ButtonComponent implements AfterViewInit, OnDestroy {
  @ViewChild('modusButton') modusButtonRef!: ElementRef;
  
  ngAfterViewInit() {
    if (this.modusButtonRef && this.modusButtonRef.nativeElement) {
      this.modusButtonRef.nativeElement.addEventListener('buttonClick', this.handleClick);
    }
  }
  
  ngOnDestroy() {
    if (this.modusButtonRef && this.modusButtonRef.nativeElement) {
      this.modusButtonRef.nativeElement.removeEventListener('buttonClick', this.handleClick);
    }
  }
  
  handleClick = () => {
    console.log('Button clicked');
  };
}
```

### ModusNavbar

```typescript
import { Component, ViewChild, ElementRef, AfterViewInit, OnDestroy } from '@angular/core';
import { NavigationService } from '../../services/navigation.service';

@Component({
  selector: 'app-navbar',
  template: `
    <modus-navbar
      #modusNavbar
      appName="My Application"
      [showMainMenu]="true"
      logoUrl="https://modus.trimble.com/img/trimble-logo.svg"
    >
    </modus-navbar>
  `
})
export class NavbarComponent implements AfterViewInit, OnDestroy {
  @ViewChild('modusNavbar') modusNavbarRef!: ElementRef;
  
  constructor(private navigationService: NavigationService) {}
  
  ngAfterViewInit() {
    if (this.modusNavbarRef && this.modusNavbarRef.nativeElement) {
      this.modusNavbarRef.nativeElement.addEventListener('mainMenuClick', this.toggleSidenav);
    }
  }
  
  ngOnDestroy() {
    if (this.modusNavbarRef && this.modusNavbarRef.nativeElement) {
      this.modusNavbarRef.nativeElement.removeEventListener('mainMenuClick', this.toggleSidenav);
    }
  }
  
  toggleSidenav = () => {
    this.navigationService.toggleSidenav();
  };
}
```

### ModusSideNavigation

```typescript
import { Component, ViewChild, ElementRef, AfterViewInit, Input, OnChanges, SimpleChanges } from '@angular/core';
import { NavigationService } from '../../services/navigation.service';

@Component({
  selector: 'app-sidebar',
  template: `
    <modus-side-navigation
      #modusSidenav
      [expanded]="isExpanded"
      mode="push"
      targetContent="#main-content"
      style="height: calc(100vh - 56px);"
    >
    </modus-side-navigation>
  `
})
export class SidebarComponent implements AfterViewInit, OnChanges {
  @ViewChild('modusSidenav') sidenavRef!: ElementRef;
  @Input() isExpanded: boolean = false;
  @Input() navItems: any[] = [];
  
  constructor(private navigationService: NavigationService) {}
  
  ngAfterViewInit() {
    this.updateSidenavItems();
  }
  
  ngOnChanges(changes: SimpleChanges) {
    if (changes['navItems'] && !changes['navItems'].firstChange) {
      this.updateSidenavItems();
    }
  }
  
  updateSidenavItems() {
    if (this.sidenavRef && this.sidenavRef.nativeElement) {
      if (this.sidenavRef.nativeElement.initialized) {
        this.sidenavRef.nativeElement.items = this.navItems;
      }
    }
  }
}
```

### ModusTabs

```typescript
import { Component, ViewChild, ElementRef, AfterViewInit, OnDestroy, OnInit } from '@angular/core';

@Component({
  selector: 'app-tabs',
  template: `
    <div #tabsContainer style="width: 100%;">
      <modus-tabs></modus-tabs>
      <div style="padding: 16px;">
        Content for tab {{ activeTab }}
      </div>
    </div>
  `
})
export class TabsComponent implements OnInit, AfterViewInit, OnDestroy {
  @ViewChild('tabsContainer') tabsContainerRef!: ElementRef;
  activeTab: number = 0;
  
  tabData = [
    { id: 0, label: 'Tab 1', icon: 'sun' },
    { id: 1, label: 'Tab 2' },
    { id: 2, label: 'Tab 3', icon: 'moon' },
  ];
  
  ngOnInit() {
    // Initialize component state if needed
  }
  
  ngAfterViewInit() {
    const modusTabs = this.tabsContainerRef.nativeElement.querySelector('modus-tabs');
    if (modusTabs) {
      modusTabs.tabs = this.tabData.map(tab => ({
        id: tab.id,
        label: tab.label,
        leftIcon: tab.icon,
      }));
      
      modusTabs.addEventListener('tabChange', this.handleTabChange);
    }
  }
  
  ngOnDestroy() {
    const modusTabs = this.tabsContainerRef?.nativeElement.querySelector('modus-tabs');
    if (modusTabs) {
      modusTabs.removeEventListener('tabChange', this.handleTabChange);
    }
  }
  
  handleTabChange = (event: CustomEvent) => {
    this.activeTab = event.detail;
  };
}
```

### ModusAccordion with Items

```typescript
import { Component, ViewChild, ElementRef, AfterViewInit, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-accordion',
  template: `
    <modus-accordion #modusAccordion>
      <modus-accordion-item header="Section 1">
        Content for section 1
      </modus-accordion-item>
      <modus-accordion-item header="Section 2">
        Content for section 2
      </modus-accordion-item>
      <modus-accordion-item header="Section 3">
        Content for section 3
      </modus-accordion-item>
    </modus-accordion>
  `
})
export class AccordionComponent implements AfterViewInit, OnDestroy {
  @ViewChild('modusAccordion') accordionRef!: ElementRef;
  
  ngAfterViewInit() {
    if (this.accordionRef && this.accordionRef.nativeElement) {
      this.accordionRef.nativeElement.addEventListener('accordionItemSelect', this.handleItemSelect);
    }
  }
  
  ngOnDestroy() {
    if (this.accordionRef && this.accordionRef.nativeElement) {
      this.accordionRef.nativeElement.removeEventListener('accordionItemSelect', this.handleItemSelect);
    }
  }
  
  handleItemSelect = (event: CustomEvent) => {
    console.log('Item selected:', event.detail);
  };
}
```

### ModusDatePicker with ModusDateInput

```typescript
import { Component, ViewChild, ElementRef, AfterViewInit, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-date-selector',
  template: `
    <modus-date-picker>
      <modus-date-input
        #modusDateInput
        [showCalendarIcon]="true"
        placeholder="Select a date"
      >
      </modus-date-input>
    </modus-date-picker>
  `
})
export class DateSelectorComponent implements AfterViewInit, OnDestroy {
  @ViewChild('modusDateInput') dateInputRef!: ElementRef;
  selectedDate: string = '';
  
  ngAfterViewInit() {
    if (this.dateInputRef && this.dateInputRef.nativeElement) {
      this.dateInputRef.nativeElement.addEventListener('dateSelect', this.handleDateSelect);
    }
  }
  
  ngOnDestroy() {
    if (this.dateInputRef && this.dateInputRef.nativeElement) {
      this.dateInputRef.nativeElement.removeEventListener('dateSelect', this.handleDateSelect);
    }
  }
  
  handleDateSelect = (event: CustomEvent) => {
    this.selectedDate = event.detail;
  };
}
```

### Layout with Navbar and SideNavigation

```typescript
import { Component, ViewChild, ElementRef, AfterViewInit, OnDestroy } from '@angular/core';
import { NavigationService } from '../../services/navigation.service';

@Component({
  selector: 'app-layout',
  template: `
    <div class="app-container">
      <modus-navbar
        #modusNavbar
        appName="My Application"
        [showMainMenu]="true"
        logoUrl="https://modus.trimble.com/img/trimble-logo.svg"
      >
      </modus-navbar>
      <div class="content-container">
        <modus-side-navigation
          #modusSidenav
          [expanded]="isExpanded"
          mode="push"
          targetContent="#main-content"
          style="height: calc(100vh - 56px);"
        >
        </modus-side-navigation>
        <main id="main-content">
          <ng-content></ng-content>
        </main>
      </div>
    </div>
  `,
  styles: [`
    .app-container {
      display: flex;
      flex-direction: column;
      height: 100vh;
    }
    .content-container {
      display: flex;
      flex: 1;
      position: relative;
    }
    #main-content {
      flex: 1;
      padding: 16px;
      overflow: auto;
    }
  `]
})
export class LayoutComponent implements AfterViewInit, OnDestroy {
  @ViewChild('modusNavbar') navbarRef!: ElementRef;
  @ViewChild('modusSidenav') sidenavRef!: ElementRef;
  
  isExpanded: boolean = false;
  
  constructor(private navigationService: NavigationService) {
    this.navigationService.sidenavState.subscribe(
      (expanded: boolean) => this.isExpanded = expanded
    );
  }
  
  ngAfterViewInit() {
    if (this.navbarRef && this.navbarRef.nativeElement) {
      this.navbarRef.nativeElement.addEventListener('mainMenuClick', this.toggleSidenav);
    }
  }
  
  ngOnDestroy() {
    if (this.navbarRef && this.navbarRef.nativeElement) {
      this.navbarRef.nativeElement.removeEventListener('mainMenuClick', this.toggleSidenav);
    }
  }
  
  toggleSidenav = () => {
    this.navigationService.toggleSidenav();
  };
}
```
