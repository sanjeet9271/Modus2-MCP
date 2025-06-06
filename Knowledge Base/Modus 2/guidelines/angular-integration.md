# Angular Framework Integration with Modus Web Components 2.0

This guide will help you get started with consuming the Modus Angular Web Component library in your Angular project.

## Introduction

We highly recommend using the Modus Angular Components library for Angular-based projects.
These components are automatically generated using the Stencil Angular Framework Integration.

Follow the steps outlined below to integrate and use Modus Angular Web Components effectively.

## Setup for Angular with Modules

Modus Angular Components have a peer dependency with Modus Web Components and require the
installation of both packages.

### 1. Install Required Packages

Ensure that you specify the target version of Angular for the `modus-wc-angular` package (e.g., `ng18` for Angular 18).

<b>
  Lock the installed package versions to avoid unintended breakages on future
  npm installs.
</b>

```bash
npm install @trimble-oss/moduswebcomponents @trimble-oss/moduswebcomponents-angular@<latest-version>-ng<target-version>
```

### 2. Set up the Styling

Import Modus styles in your main JavaScript or CSS file:

```js
import '@trimble-oss/moduswebcomponents/modus-wc-styles.css';
```

### 3. Import the Component Library

Add the Modus Angular Web Components library to your Angular app's module:

```ts
// app.module.ts
import { ModusAngularComponentsModule } from '@trimble-oss/moduswebcomponents-angular';

@NgModule({
  ...
  imports: [ModusAngularComponentsModule],
  ...
})
export class AppModule {}
```

### 4. Configure Custom Elements Schema

In the `app.module.ts` file, you need to tell Angular that you are using custom element schemas
so that it does not throw errors when unknown element names are used in the markup:

```ts
import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';

@NgModule({
  ...
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
  ...
})
```

### 5. Use the Components

Use Modus Angular Web Components while leveraging Angular template binding syntax:

```html
<!-- app.component.html -->
<modus-wc-button label="Click Me"></modus-wc-button>
```

## Setup for Angular with Standalone Components

### 1. Install Required Packages

Same as with modules:

```bash
npm install @trimble-oss/moduswebcomponents @trimble-oss/moduswebcomponents-angular@<latest-version>-ng<target-version>
```

### 2. Set up the Styling

```js
import '@trimble-oss/moduswebcomponents/modus-wc-styles.css';
```

### 3. Import into Standalone Component

You must distribute your components through a primary `NgModule` to use your components in a standalone component:

```ts
// app.component.ts
import { Component } from '@angular/core';
import { ModusAngularComponentsModule } from '@trimble-oss/moduswebcomponents-angular';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ModusAngularComponentsModule],
  templateUrl: './app.component.html',
})
export class AppComponent {}
```

### 4. Use the Components

```html
<!-- app.component.html -->
<modus-wc-button label="Click Me"></modus-wc-button>
```

## Best Practice: Wrapping Components

When using Modus Web Components directly, it is recommended to wrap it in corresponding Angular components within your application. This will abstract away from the library dependency, allowing more flexibility for you and your application in the future.

Notice Angular allows `[]` and `()` markup syntax for the web component's inputs and outputs, respectively.

### Wrapped Button Example:

```ts
import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'button-component',
  template: `
    <modus-wc-button
      [buttonStyle]="buttonStyle"
      [color]="color"
      [disabled]="disabled"
      [size]="size"
      (buttonClick)="onButtonClick.emit()"
    >
      <ng-content></ng-content>
    </modus-wc-button>
  `,
})
export class ButtonComponent {
  @Input() buttonStyle: 'borderless' | 'fill' | 'outline' = 'fill';
  @Input() color: 'danger' | 'default' | 'primary' | 'secondary' | 'warning' =
    'default';
  @Input() disabled: boolean;
  @Input() size: 'small' | 'medium' | 'large' = 'medium';

  @Output() onButtonClick = new EventEmitter();
}
```

## Reactive Forms Integration

Working with web component inputs/outputs works great, but these components do not integrate with Angular's reactive forms as easily. Since web components don't know about Angular's form APIs, we must extend form-compatible components' behavior with directives.

### Component Wrapper Example

```ts
import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'select-component',
  template: `
    <modus-wc-select
      #select
      [disabled]="disabled"
      [errorText]="errorText"
      [formControl]="formControl"
      [helperText]="helperText"
      [label]="label"
      [options]="options"
      [optionsDisplayProp]="optionsDisplayProp"
      [required]="required"
      [selectValue]="value"
      [size]="size"
      [validText]="validText"
      (valueChange)="onSelectValueChange.emit(select.value)"
    >
    </modus-wc-select>
  `,
})
export class SelectComponent {
  @Input() disabled: boolean;
  @Input() errorText: string;
  @Input() formControl: FormControl;
  @Input() helperText: string;
  @Input() label: string;
  @Input() options: unknown[] = [];
  @Input() optionsDisplayProp: string;
  @Input() required: boolean;
  @Input() size: 'medium' | 'large' = 'medium';
  @Input() validText: string;
  @Input() value: unknown;

  @Output() onSelectValueChange = new EventEmitter<unknown>();
}
```

### Directive Implementation

The directive makes the web component work with Angular's form controls:

```ts
import {
  Directive,
  forwardRef,
  ElementRef,
  HostListener,
  Input,
  OnInit,
  Output,
  EventEmitter,
} from '@angular/core';
import {
  ControlValueAccessor,
  FormControl,
  NG_VALUE_ACCESSOR,
} from '@angular/forms';

@Directive({
  selector: 'modus-wc-select',
  providers: [
    {
      provide: NG_VALUE_ACCESSOR,
      useExisting: forwardRef(() => ModusSelectDirective),
      multi: true,
    },
  ],
})
export class ModusSelectDirective implements ControlValueAccessor, OnInit {
  @Input() disabled: boolean;
  @Input() errorText: string;
  @Input() formControl: FormControl;
  @Input() helperText: string;
  @Input() label: string;
  @Input() options: unknown[];
  @Input() optionsDisplayProp: string;
  @Input() required: boolean;
  @Input() selectValue: unknown;
  @Input() size: 'medium' | 'large';
  @Input() validText: string;

  @Output() valueChange = new EventEmitter<string>();

  onChange: any = () => {};
  onTouched: any = () => {};

  private _value: string;

  get value() {
    return this._value;
  }

  set value(value) {
    if (value !== this._value) {
      this._value = value;
      this.onChange(this._value);
      this.onTouched();
      this.elementRef.nativeElement.value = value;
    }
  }

  constructor(private elementRef: ElementRef) {}

  ngOnInit(): void {
    const modusSelect = this.elementRef.nativeElement as HTMLModusSelectElement;
    modusSelect.disabled = this.disabled;
    modusSelect.errorText = this.errorText;
    modusSelect.helperText = this.helperText;
    modusSelect.label = this.label;
    modusSelect.options = this.options;
    modusSelect.optionsDisplayProp = this.optionsDisplayProp;
    modusSelect.required = this.required;
    modusSelect.size = this.size;
    modusSelect.validText = this.validText;
    modusSelect.value = this.selectValue;

    if (!this.formControl) {
      this.formControl = new FormControl(null);
    }
  }

  @HostListener('valueChange', ['$event.detail'])
  listenForValueChange(value: string): void {
    this.value = value;
  }

  registerOnChange(fn: Function): void {
    this.onChange = fn;
  }

  registerOnTouched(fn: Function): void {
    this.onTouched = fn;
  }

  setDisabledState(isDisabled: boolean): void {
    this.disabled = isDisabled;
  }

  writeValue(value: string): void {
    if (value) {
      this.value = value;
    }
  }
}
```

### Using the Form-enabled Component

```html
<select-component
  [formControl]="$any(form).controls['select1']"
  [label]="'Select Form Demo'"
  [options]="options"
  [optionsDisplayProp]="'display'">
</select-component>
```

## Key Points for Angular Integration

1. **Custom Elements Schema**: Always include `CUSTOM_ELEMENTS_SCHEMA` in your NgModule to avoid template errors
2. **Angular Syntax**: Use Angular binding syntax (`[property]` for inputs, `(event)` for outputs)
3. **Reactive Forms**: Create directives implementing `ControlValueAccessor` for form integration
4. **Component Wrapping**: Abstract library dependencies through wrapper components
5. **Event Handling**: Use Angular's `@HostListener` to handle custom events from web components

## Additional Resources

For more information on using Modus Web Components with Angular, refer to:
- [Modus Web Components Documentation](https://modus-web-components.trimble.com/)
- [Stencil.js Angular Integration Documentation](https://stenciljs.com/docs/angular)
