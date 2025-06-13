# Modus Web Components 2.0 - Framework Documentation

## Table of Contents
1. [Overview](#overview)
2. [General Setup](#general-setup)
3. [React Implementation](#react-implementation)
4. [Angular Implementation](#angular-implementation)
5. [Event Handling Guide](#event-handling-guide)
6. [Component Reference](#component-reference)

---

## Overview

### Metadata
- **Library Name**: @trimble-oss/moduswebcomponents
- **Version**: 2.0

### Introduction

Modus Web Components 2.0 is a library of reusable UI components built with Web Components technology. These components are framework-agnostic and can be used in any web application regardless of the technology stack. The library provides a consistent design system following Trimble's Modus Design guidelines.

**Key Features:**
- Framework-agnostic components
- TypeScript support
- Multiple theming options
- Accessibility compliance
- Responsive design
- Shadow DOM disabled by default for easier styling

---

## General Setup

### Base Installation

Install the core Modus Web Components package:

```powershell
npm install @trimble-oss/moduswebcomponents
```

### Icon System Integration

Many components in the library require Modus Icons to be installed in the host application.

#### CDN Integration (Recommended)

Add the following to your application's HTML head section:

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

---

## React Implementation

### React-Specific Installation

```powershell
npm install @trimble-oss/moduswebcomponents-react
```

### Component Registration

Register the custom elements in your React application:

```javascript
// JavaScript/React
import { defineCustomElements } from '@trimble-oss/moduswebcomponents/loader';

// Call during the initial loading of your application
const Root = () => {
  defineCustomElements();

  return <App />;
};
```

### Basic React Usage

```jsx
// React usage
<ModusWcButton variant="primary">Click me</ModusWcButton>
```

### React TypeScript Support

```typescript
// TypeScript example with React
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

### React Controlled Input Pattern

The controlled input pattern involves maintaining the state of the input's value within the React application or component.

**Key Benefits:**
- Single source of truth for input values
- Real-time validation and transformation of data
- Simplified form state management
- Improved testability and debugging

#### Basic React Controlled Input

```jsx
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

#### Alternative React Controlled Input

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

### React Component Wrapping Patterns

When using Modus React Components directly, it is recommended to wrap it in corresponding React components within your application. This will abstract away from the library dependency, allowing more flexibility for you and your application in the future.

#### Simple React Wrapper

```tsx
import React from 'react';
import { ModusWcAvatar } from '@trimble-oss/moduswebcomponents-react';

interface Props extends React.ComponentProps<typeof ModusWcAvatar> {}

const Avatar: React.FC<Props> = (props) => {
  return <ModusWcAvatar {...props} />;
};

export default Avatar;
```

#### Complex React Wrapper

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

### Using React Component Library

```tsx
import { ModusWcBadge } from '@trimble-oss/moduswebcomponents-react';

<ModusWcBadge aria-label="Badge" content="Words" />;
```

---

## Angular Implementation

### Angular-Specific Installation

```powershell
npm install @trimble-oss/moduswebcomponents @trimble-oss/moduswebcomponents-angular
```

### Basic Angular Usage

```typescript
// Angular usage
<modus-wc-button variant="primary">Click me</modus-wc-button>
```

### Angular Controlled Input Pattern

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

---

## Event Handling Guide

### When to Use `e.detail.value` vs `event.detail.target.value`

> **⚠️ CRITICAL EVENT HANDLING GUIDE ⚠️**

Understanding when to use `e.detail.value` versus `event.detail.target.value` is crucial for proper event handling in Modus Web Components.

#### Use `e.detail.value` when:
- Working with **SELECT components** and similar dropdown/choice components
- The event provides a direct value in the detail object
- Component documentation specifically mentions `detail.value`

```typescript
// Example: Select component event handling
const handleSelectEvent = (e: ModusWcSelectCustomEvent<ISelectOption>) => {
  console.log(e.detail.value); // ✅ Correct for select components
}
```

#### Use `event.detail.target.value` when:
- Working with **INPUT components** (text inputs, number inputs, etc.)
- The event detail contains a target object with the value
- Component documentation mentions `detail.target.value`

```typescript
// Example: Text input event handling
const handleInputChange = (event: CustomEvent) => {
  setValue(event.detail.target.value); // ✅ Correct for input components
}
```

#### Quick Reference Table

| Component Type | Event Property | Example |
|---------------|----------------|---------|
| `modus-wc-select` | `e.detail.value` | Select dropdowns |
| `modus-wc-text-input` | `event.detail.target.value` | Text inputs |
| `modus-wc-number-input` | `event.detail.target.value` | Number inputs |
| `modus-wc-textarea` | `event.detail.target.value` | Text areas |
| `modus-wc-checkbox` | `event.detail.target.checked` | Checkboxes |
| `modus-wc-radio` | `event.detail.target.value` | Radio buttons |

---

## Component Reference

Below is a reference of common Modus Web Components:

| Component | Tag | Description | Framework Usage |
|-----------|-----|-------------|-----------------|
| Button | `<modus-wc-button>` | Standard, actionable button element | React: `<ModusWcButton>` |
| Text Input | `<modus-wc-text-input>` | Single-line text entry field | React: `<ModusWcTextInput>` |
| Select | `<modus-wc-select>` | Dropdown selection component | React: `<ModusWcSelect>` |
| Checkbox | `<modus-wc-checkbox>` | Boolean selection control | React: `<ModusWcCheckbox>` |
| Radio | `<modus-wc-radio>` | Single selection from multiple options | React: `<ModusWcRadio>` |
| Modal | `<modus-wc-modal>` | Dialog/popup component | React: `<ModusWcModal>` |
| Card | `<modus-wc-card>` | Container for related content | React: `<ModusWcCard>` |
| Tabs | `<modus-wc-tabs>` | Tabbed interface component | React: `<ModusWcTabs>` |
| Toast | `<modus-wc-toast>` | Temporary notification | React: `<ModusWcToast>` |
| ThemeSwitcher | `<modus-wc-theme-switcher>` | UI for changing themes | React: `<ModusWcThemeSwitcher>` |

### HTML Usage (Framework Agnostic)

```html
<!-- HTML usage -->
<modus-wc-button variant="primary">Click me</modus-wc-button>
```

---
