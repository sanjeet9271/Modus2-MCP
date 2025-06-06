# Modus Web Components 2.0 - General Guidelines

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
6. [Icon System](#icon-system)
7. [Styling Options](#styling-options)
8. [Form Input Patterns](#form-input-patterns)
9. [Component Reference](#component-reference)

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
// JavaScript
import { defineCustomElements } from '@trimble-oss/moduswebcomponents/loader';

// Call during the initial loading of your application
defineCustomElements();
```

## Component Usage <a name="component-usage"></a>

Once registered, components can be used directly in your HTML:

```html
<!-- HTML usage -->
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

## Form Input Patterns <a name="form-input-patterns"></a>

### Controlled Input Pattern

The controlled input pattern is where form element values are controlled by application state rather than DOM element state.

**Key Benefits:**
- Single source of truth for input values
- Real-time validation and transformation of data
- Simplified form state management
- Improved testability and debugging

#### Vanilla JS Implementation

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
