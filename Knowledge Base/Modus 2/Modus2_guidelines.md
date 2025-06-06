# Modus Web Components 2.0 - Framework Documentation

## Metadata
- **Library Name**: @trimble-oss/moduswebcomponents
- **Version**: 2.0
- **Repository**: [GitHub Repository](https://github.com/trimble-oss/modus-wc-2.0)
- **Documentation**: [Modus Web Components Documentation](https://modus-web-components.trimble.com/)
- **CSS Variables**: [Available CSS Variables](https://github.com/trimble-oss/modus-wc-2.0/blob/main/src/styles/variables.scss)

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Basic Setup](#basic-setup)
   - [Styling Setup](#styling-setup)
   - [Theme Configuration](#theme-configuration)
   - [Component Registration](#component-registration)
4. [Component Usage](#component-usage)
5. [TypeScript Support](#typescript-support)
6. [Framework Integration](#framework-integration)
7. [Icon System](#icon-system)
8. [Styling Options](#styling-options)
9. [Form Input Patterns](#form-input-patterns)
10. [Component Reference](#component-reference)

## Introduction <a name="introduction"></a>

Modus Web Components 2.0 is a library of reusable UI components built with Web Components technology. These components are framework-agnostic and can be used in any web application regardless of the technology stack. The library provides a consistent design system following Trimble's Modus Design guidelines.

Key features:
- Framework-agnostic components
- TypeScript support
- Multiple theming options
- Accessibility compliance
- Responsive design
- Shadow DOM disabled by default for easier styling

## Installation <a name="installation"></a>

Install the Modus Web Components package using npm:

```bash
# It's recommended to lock the version to avoid unintended breakages
npm install @trimble-oss/moduswebcomponents@2.0.0
```

## Basic Setup <a name="basic-setup"></a>

### Styling Setup <a name="styling-setup"></a>

Import the Modus Web Components styles in your main JavaScript or CSS file:

```js
// JavaScript import
import '@trimble-oss/moduswebcomponents/modus-wc-styles.css';
```

```css
/* CSS import */
@import '@trimble-oss/moduswebcomponents/modus-wc-styles.css';
```

### Theme Configuration <a name="theme-configuration"></a>

The available themes are:

- `modus-classic-light`
- `modus-classic-dark`
- `modus-modern-light` (default)
- `modus-modern-dark`

### Component Registration <a name="component-registration"></a>

Register the custom elements in your application:

```javascript
// JavaScript/React
import { defineCustomElements } from '@trimble-oss/moduswebcomponents/loader';

// Call during the initial loading of your application
const Root = () => {
  defineCustomElements();

  return <App />;
};
```

## Component Usage <a name="component-usage"></a>

Once registered, components can be used directly in your HTML:

```html
<!-- HTML usage -->
<modus-wc-button variant="primary">Click me</modus-wc-button>
```

```jsx
// React usage
<ModusWcButton variant="primary">Click me</ModusWcButton>
```

```typescript
// Angular usage
<modus-wc-button variant="primary">Click me</modus-wc-button>
```

## TypeScript Support <a name="typescript-support"></a>

Modus Web Components provides comprehensive TypeScript definitions for all components, giving you type safety and enhanced developer experience.

```typescript
// TypeScript example
import { ISelectOption, ModusWcSelectCustomEvent } from '@trimble-oss/moduswebcomponents';

// Typed component props
const options: ISelectOption[] = [
  {
    label: 'Option 1',
    value: '1',
  },
  {
    label: 'Option 2',
    value: '2',
  },
];

// Typed event handlers
const handleEvent = (e: ModusWcSelectCustomEvent<ISelectOption>) => {
  // Type-safe access to event details
  console.log(e.detail.value);
}
```

## Framework Integration <a name="framework-integration"></a>

Modus Web Components can be integrated with various JavaScript frameworks:

### Angular Integration

Angular provides built-in support for Web Components. See the [detailed Angular integration guide](?path=/docs/documentation-frameworks-angular--docs).

### React Integration

React can work with Web Components using appropriate wrappers. See the [detailed React integration guide](?path=/docs/documentation-frameworks-react--docs).

---

## Icon System <a name="icon-system"></a>

### Modus Icons Integration

Many components in the library require [Modus icons](https://modus-icons.trimble.com) to be installed in the host application. 

#### Online Usage

To install icons with CDN, add the following to your application's HTML:

```html
<head>
  <!-- Preload for performance -->
  <link
    rel="preload"
    href="https://cdn.jsdelivr.net/npm/@trimble-oss/modus-icons@latest/dist/modus-outlined/fonts/modus-icons.css"
    as="style"
    crossorigin="anonymous"
  />
  <!-- Actual stylesheet -->
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/@trimble-oss/modus-icons@latest/dist/modus-outlined/fonts/modus-icons.css"
  />
</head>
```

> **Important:** Modus (font) icons currently only supports the usage of one icon set (outlined, filled, transportation) per application. If you require multiple sets, reach out to [Modus Design](https://mail.google.com/chat/u/0/#chat/space/AAAAexugR1k) and comment on this [GitHub Issue](https://github.com/trimble-oss/modus-icons/issues/363).

### Offline Usage

For applications requiring offline capability or improved performance, you can bundle Modus icons directly with your app:

1. **Install the package:**

   ```bash
   npm install @trimble-oss/modus-icons
   ```

2. **Copy the required font files and styles:**
   - Source: `node_modules/@trimble-oss/modus-icons/dist/modus-outlined/fonts/`
   - Files to copy:
     - `modus-icons.css`
     - Font files (.woff, .woff2, etc.)
   - Destination: A publicly accessible directory in your app (e.g., `/public/fonts/`)

3. **Reference the local stylesheet:**

   ```html
   <head>
     <!-- Preload font for performance -->
     <link
       rel="preload"
       href="/path-to-your-local-modus-icons-font.woff2"
       as="font"
       type="font/woff2"
       crossorigin="anonymous"
     />
     <!-- Reference the CSS -->
     <link rel="stylesheet" href="/path-to-your-local-modus-icons.css" />
   </head>
   ```

---

## Styling Options <a name="styling-options"></a>

The Modus Web Components library provides several standardized approaches to customize component appearances.

### Theme Application

Components come with four preloaded themes based on the Modus Design System. All available themes can be found in the [tailwind.config.ts](https://github.com/trimble-oss/modus-wc-2.0/blob/main/tailwind.config.ts) file under the `daisyui.themes` array.

#### Method 1: Using the ThemeSwitcher Component

```html
<!-- HTML -->
<modus-wc-theme-provider initial-theme='{ "theme": "modus-modern-light" }'>
  <modus-wc-theme-switcher aria-label="Toggle theme" />
</modus-wc-theme-provider>
```

The ThemeSwitcher component:
- Automatically handles theme switching via the theme store
- Stores theme preferences in local storage (`modus-theme-config` key)
- Provides an accessible UI for users to change themes

#### Method 2: Manual HTML Attributes

```html
<!-- Light theme application -->
<html class="light" data-theme="modus-modern-light" data-mode="light">
  ...
</html>

<!-- Dark theme application -->
<html class="dark" data-theme="modus-modern-dark" data-mode="dark">
  ...
</html>
```

### CSS Custom Properties

Components use CSS custom properties (variables) which can be overridden at global or component level.

```css
/* Global variable overrides */
:root {
  --modus-wc-primary-color: purple;       /* Change primary color */
  --modus-wc-color-info: green;           /* Change info color */
  --modus-wc-font-weight-normal: 500;     /* Adjust normal font weight */
}
```

```css
/* Component-specific overrides */
.modus-wc-btn {
  --modus-wc-border-radius-md: 20px;      /* Rounded buttons */
}
```

A complete reference of all available CSS variables is available in the [variables.scss file](https://github.com/trimble-oss/modus-wc-2.0/blob/main/src/styles/variables.scss).

### Custom CSS Classes

Most components accept a `custom-class` attribute that allows adding custom CSS:

```html
<!-- HTML with custom class -->
<modus-wc-button
  label="Custom Button"
  custom-class="my-custom-button"
></modus-wc-button>
```

```css
/* CSS for custom class */
.my-custom-button {
  background-color: purple;
  border-color: purple;
}
```

### Direct CSS Targeting

Since Shadow DOM is disabled by default in Modus Web Components, you can directly target component classes:

```css
/* Direct component styling */
.modus-wc-btn {
  background-color: yellow;
  color: black;
}
```

All component classes are prefixed with `modus-wc-` to avoid collisions with other CSS in your application.

### CSS Reset System

Modus Web Components uses Tailwind's CSS reset (preflight) that normalizes browser styles for consistent rendering across browsers. This reset is automatically loaded when you import the main CSS file.

Key points about the CSS reset:
- Modus-specific overrides are provided in `styles/tailwind.css`
- These overrides maintain compatibility with the Modus Design System
- The overrides are not exhaustive

If you need additional style adjustments:
- Add custom CSS overrides in your application
- Create a GitHub issue describing the needed override (contributions welcome)

---

## Form Input Patterns <a name="form-input-patterns"></a>

### Controlled Input Pattern

The controlled input pattern is where form element values are controlled by application state rather than DOM element state.

**Key Benefits:**
- Single source of truth for input values
- Real-time validation and transformation of data
- Simplified form state management
- Improved testability and debugging

#### Implementation in Different Frameworks

##### Angular Implementation

Angular uses its two-way data binding to implement controlled inputs:

```typescript
// Angular controlled input example
import { Component } from '@angular/core';

@Component({
  selector: 'controlled-text-input',
  template: `
    <modus-wc-text-input
      (inputChange)="onInputChange($event)"
      [value]="inputValue"
    >
    </modus-wc-text-input>
  `,
})
export class ControlledTextInput {
  inputValue: string = '';

  onInputChange(event: CustomEvent) {
    this.inputValue = event.detail.target.value;
    
    // Validation or transformation logic can be added here
  }
}
```

##### React Implementation

React implements controlled inputs using state hooks:

```jsx
// React controlled input example
import { useState } from 'react';

function ControlledTextInput() {
  const [value, setValue] = useState('');

  // Handle input changes
  const handleChange = (event: CustomEvent) => {
    setValue(event.detail.target.value);
    
    // Additional logic can be added here
  };

  return <ModusWcTextInput onInputChange={handleChange} value={value} />;
}
```

##### Vanilla JS Implementation

Without a framework, you can manually implement the controlled input pattern:

```javascript
// Vanilla JS controlled input example
const textInput = document.getElementById('first-name');
let inputValue = ''; // State lives in the parent application

// Set initial value
textInput.value = inputValue;

// Listen for changes
textInput.addEventListener('inputChange', (event) => {
  // Update our state
  inputValue = event.detail.target.value;
  
  // Optional validation/transformation
  // inputValue = inputValue.toUpperCase();
  
  // Update the input with possibly transformed value
  textInput.value = inputValue;
});
```

## Component Reference <a name="component-reference"></a>

Below is a reference of common Modus Web Components:

| Component | Tag | Description |
|-----------|-----|-------------|
| Button | `<modus-wc-button>` | Standard, actionable button element |
| Text Input | `<modus-wc-text-input>` | Single-line text entry field |
| Select | `<modus-wc-select>` | Dropdown selection component |
| Checkbox | `<modus-wc-checkbox>` | Boolean selection control |
| Radio | `<modus-wc-radio>` | Single selection from multiple options |
| Modal | `<modus-wc-modal>` | Dialog/popup component |
| Card | `<modus-wc-card>` | Container for related content |
| Tabs | `<modus-wc-tabs>` | Tabbed interface component |
| Toast | `<modus-wc-toast>` | Temporary notification |
| ThemeSwitcher | `<modus-wc-theme-switcher>` | UI for changing themes |

For complete API documentation, please refer to the [Modus Web Components Documentation](https://modus-web-components.trimble.com/).



# React Framework Integration

This guide will help you get started with consuming the Modus React Web Component library in your React project.

We highly recommend using the Modus React Components library for React based projects.
These components are automatically generated using the Stencil React Framework Integration.

Follow the steps outlined below to integrate and use Modus React Web Components effectively.

Please refer to the [official stencil documentation](https://stenciljs.com/docs/react#consumer-usage) for more information on how to integrate with your React project.

## Usage

Modus React Components have a peer dependency with Modus Web Components and require the
installation of both packages.

### 1. Install `modus-wc-react`:

Ensure that you specify the target version of React for the `modus-wc-react` package (e.g., `react18` for React 18).

<b>
  Lock the installed package versions to avoid unintended breakages on future
  npm installs.
</b>

```bash
npm install @trimble-oss/moduswebcomponents-react@<latest-version>-react<target-version>
# e.g.,
npm install @trimble-oss/moduswebcomponents-react@1.0.0-react18
```

### 2. Set up the styling:

You will need to import our styling in your main JavaScript or CSS file:

```js
import '@trimble-oss/moduswebcomponents/modus-wc-styles.css';
```

### 3. Use the component library as normal.

```tsx
import { ModusWcBadge } from '@trimble-oss/moduswebcomponents-react';

<ModusWcBadge aria-label="Badge" content="Words" />;
```

### Using the Controlled Input Pattern

The controlled input pattern involves maintaining the state of the input's value within the React application or
component. The [React Docs](https://react.dev/reference/react-dom/components/input#controlling-an-input-with-a-state-variable)
describe this in more detail.

```tsx
import React, { useState } from 'react';
import { ModusWcTextInput } from '@trimble-oss/moduswebcomponents-react';

interface Props extends React.ComponentProps<typeof ModusWcTextInput> {}

const MyComponent: React.FC<Props> = (props) => {
  const [value, setValue] = useState('');

  const handleInputChange = (
    e: CustomEvent<HTMLModusWcTextInputElementEventMap['inputChange']>
  ) => {
    const value = e.detail.target.value;
    setValue(value);
  };

  return (
    <ModusWcTextInput
      {...props}
      onInputChange={handleInputChange}
      value={value}
    />
  );
};

export default MyComponent;
```

### Wrapping Components

When using Modus React Components directly, it is recommended to wrap it in corresponding React components within your application.
This will abstract away from the library dependency, allowing more flexibility for you and your application in the future.

Wrapped Modus component example:

```tsx
import React from 'react';
import { ModusWcAvatar } from '@trimble-oss/moduswebcomponents-react';

interface Props extends React.ComponentProps<typeof ModusWcAvatar> {}

const Avatar: React.FC<Props> = (props) => {
  return <ModusWcAvatar {...props} />;
};

export default Avatar;
```

or, a more complex wrapper:

```tsx
import React from 'react';
import { ModusWcTextInput } from '@trimble-oss/moduswebcomponents-react';

interface Props
  extends Omit<React.ComponentProps<typeof ModusWcTextInput>, 'inputChange'> {
  onValueChange: (value: string) => void;
}

const TextInput: React.FC<Props> = (props) => {
  const handleInputChange = (
    e: CustomEvent<HTMLModusWcTextInputElementEventMap['inputChange']>
  ) => {
    const value = e.detail.target.value;
    props.onValueChange(value);
  };

  return <ModusWcTextInput {...props} onInputChange={handleInputChange} />;
};

export default TextInput;
```

# Angular Framework Integration

This guide will help you get started with consuming the Modus Angular Web Component library in your Angular project.

We highly recommend using the Modus Angular Components library for Angular based projects.
These components are automatically generated using the Stencil Angular Framework Integration.

Follow the steps outlined below to integrate and use Modus Angular Web Components effectively.

Please refer to the [official stencil documentation](https://stenciljs.com/docs/angular#consumer-usage) for more information on how to integrate with your Angular project.

## Angular with modules

Modus Angular Components have a peer dependency with Modus Web Components and require the
installation of both packages.

### 1. Install both `modus-wc` and `modus-wc-angular` dependencies:

Ensure that you specify the target version of Angular for the `modus-wc-angular` package (e.g., `ng18` for Angular 18).

<b>
  Lock the installed package versions to avoid unintended breakages on future
  npm installs.
</b>

```bash
npm install @trimble-oss/moduswebcomponents @trimble-oss/moduswebcomponents-angular@<latest-version>-ng<target-version>
```

### 2. Set up the styling:

You will need to import our styling in your main JavaScript or CSS file:

```js
import '@trimble-oss/moduswebcomponents/modus-wc-styles.css';
```

### 3. Import Modus Angular Web Components library into your Angular app's module:

```ts
// app.module.ts
import { ModusAngularComponentsModule } from '@trimble-oss/moduswebcomponents-angular';

@NgModule({
  ...
  imports: [ComponentLibraryModule],
  ...
})
export class AppModule {}
```

### 4. Use Modus Angular Web Components while leveraging Angular template binding syntax:

```ts
// app.component.html
<modus-wc-button label="Click Me" />
```

## Angular with standalone components

Modus Angular Components have a peer dependency with Modus Web Components and require the
installation of both packages.

### 1. Install both `modus-wc` and `modus-wc-angular` dependencies:

Ensure that you specify the target version of Angular for the `modus-wc-angular` package (e.g., `ng18` for Angular 18).

<b>
  Lock the installed package versions to avoid unintended breakages on future
  npm installs.
</b>

```bash
npm install @trimble-oss/moduswebcomponents @trimble-oss/moduswebcomponents-angular@<latest-version>-ng<target-version>
```

### 2. Set up the styling:

You will need to import our styling in your main JavaScript or CSS file:

```js
import '@trimble-oss/moduswebcomponents/modus-wc-styles.css';
```

### 3. Import your component library into your component.

You must distribute your components through a primary `NgModule` to use your components in a standalone component.

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

### 4. Use Modus Angular Web Components while leveraging Angular template binding syntax:

```ts
// app.component.html
<modus-wc-button label="Click Me" />
```

### Custom Elements Schema

In the `app.module.ts` file, you need to tell angular that you are using custom element schemas
so that it does not throw errors when unknown element names are used in the markup.

Import `CUSTOM_ELEMENTS_SCHEMA` and add it to your `@NgModule`'s schemas:

```ts
import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';

@NgModule({
  ...
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
  ...
})
```

### Wrapping Components

When using Modus Web Components directly, it is recommended to wrap it in corresponding Angular components within your application. This will abstract away from the library dependency, allowing more flexibility for you and your application in the future. Each part of the component is able to be abstracted, leaving you with an Angular-native component.

Notice Angular allows `[]` and `()` markup syntax for the web component's inputs and outputs, respectively.

Wrapped Modus Button Example:

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

### Reactive Forms

Working with a web component's inputs/outputs works great but these components do not integrate with Angular's reactive forms quite as easily. Since web components do not know about Angular's form APIs, we must extend form-compatible components' behavior with simple directives. These directives are applied to the web component selectors, giving the components Angular form functionality.

Let's take a look at a directive implementation for a Modus Select's form functionality.

#### Wrapper

You'll notice the `modus-select` in the markup is taking extra inputs, such as `formControl` and `optionsDisplayProp`, these inputs are provided by the directive below. Here is what our wrapper looks like:

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

#### Directive

Moving onto the directive, there are a few things to keep in mind.

- The directive's selector is set to the web component's tag, not the wrapper's.
- Implementing the `ControlValueAccessor` interface helps Angular understand when the form control has been updated or changed.
  - When the value is set, `onChange()` notifies that the control has been updated.
  - Calling `onTouched()` lets Angular know the component has been touched, which is needed for form validation.
- The `get value()`, and `set value()` are used by Angular's form control.
- Using the `@HostListener` decorator lets you listen to events from the web component, and execute appropriate logic.

Here is what our directive looks like:

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

Now adding the Modus Select as a form control is as easy as:

```ts
<select-component
  [formControl]="$any(form).controls['select1']"
  [label]="'Select Form Demo'"
  [options]="options"
  [optionsDisplayProp]="'display'">
</select-component>
```