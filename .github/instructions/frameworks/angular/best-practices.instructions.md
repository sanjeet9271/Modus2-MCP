-----
applyTo: "*.ts, *.html"
-----

# Angular Best Practices for Modus Components

> **Important Note**: These instructions only **apply to** Angular Projects.
> **LEAD LEVEL GUIDANCE**: This document provides Angular-specific best practices for implementing Modus components effectively.

## Component Architecture

1. **Component Organization**
   - Follow the Angular module pattern for organizing components
   - Structure components into feature modules
   - Keep presentational and container components separate
   - Implement a clean folder structure with feature-based organization

2. **Component Communication**
   - Use `@Input()` and `@Output()` for parent-child communication
   - Use services and RxJS BehaviorSubject/Observable for cross-component communication
   - Avoid excessive nesting of components to prevent prop drilling

3. **ViewChild for Modus Components**
   - Use `@ViewChild` to get references to Modus web components in the DOM
   - Access component references only in or after `ngAfterViewInit` lifecycle hook
   - Always check if references exist before accessing their properties or methods

4. **Lifecycle Management**
   - Initialize event listeners in `ngAfterViewInit`
   - Clean up event listeners in `ngOnDestroy` to prevent memory leaks
   - Use `implements AfterViewInit, OnDestroy` to enforce lifecycle method implementation

## Event Handling

1. **Event Listeners**
   - Use arrow functions for event handlers to preserve `this` context
   - Add event listeners in `ngAfterViewInit` and remove them in `ngOnDestroy`
   - Follow this pattern for adding event listeners:
     ```typescript
     ngAfterViewInit() {
       if (this.componentRef?.nativeElement) {
         this.componentRef.nativeElement.addEventListener('eventName', this.handleEvent);
       }
     }
     
     ngOnDestroy() {
       if (this.componentRef?.nativeElement) {
         this.componentRef.nativeElement.removeEventListener('eventName', this.handleEvent);
       }
     }
     
     handleEvent = (event: CustomEvent) => {
       // Handle the event
     }
     ```

2. **Custom Events**
   - Use Angular `@Output()` and `EventEmitter` to emit events from Angular components
   - For Modus components, listen to their native events using `addEventListener`
   - Create typed event interfaces for complex event data structures

## Change Detection and Performance

1. **Change Detection Strategy**
   - Use `ChangeDetectionStrategy.OnPush` for better performance when possible
   - Avoid frequent updates to complex component properties
   - Use pure pipes for transforming data in templates

2. **Modus Component Initialization**
   - Initialize Modus component properties only after checking if the component is ready:
     ```typescript
     if (this.componentRef?.nativeElement?.initialized) {
       this.componentRef.nativeElement.property = value;
     }
     ```

3. **Performance Considerations**
   - Avoid manipulating the DOM directly outside of Modus components
   - Unsubscribe from all observables in `ngOnDestroy`
   - Use trackBy function with *ngFor for better rendering performance

## Form Integration

1. **Reactive Forms**
   - Use Angular's Reactive Forms approach with Modus form components
   - Implement custom form controls with `ControlValueAccessor` to wrap Modus inputs
   - Handle form validation through Angular's form validation mechanism

2. **Form Events**
   - Listen to Modus input events and update form controls accordingly
   - Provide appropriate validation feedback using Modus validation states
   - Example:
     ```typescript
     ngAfterViewInit() {
       if (this.inputRef?.nativeElement) {
         this.inputRef.nativeElement.addEventListener('valueChange', (e: CustomEvent) => {
           this.form.get('field')?.setValue(e.detail);
         });
       }
     }
     ```

## Testing

1. **Component Testing**
   - Create TestBed configurations that include Modus components
   - Implement appropriate mocks for Modus component functionality
   - Use `fixture.detectChanges()` after setup of components

2. **Event Testing**
   - Test event handlers by triggering custom events on component elements
   - Verify component state changes after event handling
   - Example:
     ```typescript
     it('should handle button click', () => {
       const buttonElement = fixture.debugElement.query(By.css('modus-button')).nativeElement;
       
       // Create and dispatch a custom event
       const customEvent = new CustomEvent('buttonClick', { detail: {} });
       buttonElement.dispatchEvent(customEvent);
       
       fixture.detectChanges();
       
       expect(component.handleButtonClickCalled).toBeTrue();
     });
     ```

## Styling

1. **Component Styling**
   - Use component-specific styles with `styles` or `styleUrls` in component decorators
   - Avoid global styles that might conflict with Modus components
   - Use Angular's view encapsulation to prevent style leakage

2. **Modus Themes**
   - Apply Modus themes consistently across the application
   - Set global theme at the application root level
   - Override theme variables using Angular's style inclusion mechanism

## Project Setup

1. **Module Configuration**
   - Include CUSTOM_ELEMENTS_SCHEMA in NgModule to support Modus web components
   - Import and define components in appropriate feature modules
   - Example:
     ```typescript
     @NgModule({
       declarations: [
         AppComponent,
         // other components
       ],
       imports: [
         BrowserModule,
         // other modules
       ],
       schemas: [CUSTOM_ELEMENTS_SCHEMA], // Required for Modus web components
       providers: [],
       bootstrap: [AppComponent]
     })
     export class AppModule { }
     ```

2. **Initialization**
   - Initialize Modus components in the main.ts or app.module.ts file:
     ```typescript
     import { defineCustomElements } from '@trimble-oss/modus-web-components/loader';
     
     defineCustomElements().then(() => {
       // Optional: any code that should run after Modus components are defined
     });
     ```
