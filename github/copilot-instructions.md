# Modus 2.0 Design System Implementation Guide

> **DESIGN ORCHESTRATOR GUIDANCE**: As an expert UI/UX designer and design system orchestrator, you are working with Modus 2.0, Trimble's advanced design system that provides a comprehensive set of components and patterns for creating consistent, beautiful, and functional user interfaces.You're very good at learning from your past mistaks.

## Environment Context

- **Design System**: Modus 2.0 (Latest version of Trimble's design system)
- **Shell Environment**: PowerShell
- **Command Syntax**: Use `;` for command chaining (instead of `&&` used in bash)
- **Terminal Commands Example**:
  ```powershell
  npm install @trimble-oss/modus-react-components --legacy-peer-deps --save ; npm install @trimble-oss/modus-web-components --legacy-peer-deps --save
  ```

## Core Implementation Principles

1. **Documentation and Step Logging**
   - Document each implementation step with bullet points
   - Note key decisions and challenges
   - [Core Principles](./instructions/core-principles.instructions.md)

2. **Component Usage**
   - Always use Modus components over HTML elements for example `ModusWcAlert` for notifications instead of custom alerts
   - Always verify component properties and events using `get_component_details`

## Implementation Process

> **IMPORTANT**: For detailed implementation steps, refer to [Modus Implementation Guide](./modus-implementation-steps.instructions.md).

1. **Framework and Query Type**
   - Document which framework (React/Angular)
   - Identify implementation type (new project/error-fixing/component/state/styling)
   - Note any specific requirements or constraints
   - If the query is related to error or bug fixing follow the [Troubleshooting](./instructions/error-correction/troubleshooting-guide.instructions.md) guide.

2. **Documentation Reference**
   - New project: 
    For the implementation, refer to - [Implementation Steps](./modus-implementation-steps.instructions.md)
    For Checking the common mistakes, refer to - [Common Mistakes](./instructions/lessons-learned/common-mistakes.instructions.md)

   Based on your framework:

   ### React Implementation
   - Components: [React Component Patterns](./instructions/frameworks/react/component-patterns.instructions.md)
   - State management: [React State Management](./instructions/frameworks/react/state-management.instructions.md)
   - Best Practices: [React Best Practices](./instructions/frameworks/react/best-practices.instructions.md)
   ### Angular Implementation
   - Components: [React Component Patterns](./instructions/frameworks/angular/component-patterns.instructions.md)
   - State management: [React State Management](./instructions/frameworks/angular/state-management.instructions.md)
   - Best Practices: [React Best Practices](./instructions/frameworks/angular/best-practices.instructions.md)


## Style Guide

### 1. Component Containers
```jsx
<div style={{
  display: 'flex',
  flexDirection: 'column',
  gap: '16px',
  padding: '16px',
  margin: '0 auto',
  width: '100%',
  maxWidth: '1200px'
}}>
  {/* Components */}
</div>
```

### 2. Layout Structure
- **Vertical Stacking**
  ```
  flexDirection: 'column'
  gap: minimum 8px
  ```
- **Horizontal Alignment**
  ```
  flexDirection: 'row'
  justifyContent: 'space-between' or 'center'
  ```
- **Spacing**
  ```
  padding: minimum 16px
  margin: '0 auto' for center alignment
  ```

### 3. Component Properties
- **Dimensions**: Use relative units (%, vh/vw)
- **Overflow**: Handle with `overflow: 'auto'`
- **Responsiveness**: Use flexbox and grid layouts

### 4. Navigation Elements
- **Navbar**
  ```css
  width: 100%;
  position: sticky;
  top: 0;
  zIndex: 1000;
  ```
- **SideNavigation**
  ```css
  height: calc(100vh - 56px);
  ```

### 5. Typography
- Font Family: Open Sans
- Include in global CSS

### 6. Image Assets
- **Trimble Assets**
  - Base URL: `https://modus.trimble.com/img/`
  - Bootstrap: `https://modus-bootstrap.trimble.com/img/`

- **Navbar Logos**
  - Blue: `https://modus-bootstrap.trimble.com/img/trimble-logo-rev.svg`
  - Default: `https://modus.trimble.com/img/trimble-logo.svg`

- **Icons**
  ```html
      <head>
      <link
        rel="preload"
        href="https://cdn.jsdelivr.net/npm/@trimble-oss/modus-icons@latest/dist/modus-outlined/fonts/modus-icons.css"
        as="style"
        crossorigin="anonymous"
      />
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/@trimble-oss/modus-icons@latest/dist/modus-outlined/fonts/modus-icons.css"
      />
    </head>```
 - Add these to index.html or main HTML file to ensure icons are loaded globally.

## Development Workflow Documentation

1. **During Development**
   - **Log each implementation step**
   - Document component choices
   - Note any issues encountered
   - Record solutions implemented

2. **For Issues**
   - Document in Common Mistakes guide [Common Mistakes](./instructions/lessons-learned/common-mistakes.instructions.md)
   - Include:
     - Problem description
     - Correct implementation
     - Prevention steps

