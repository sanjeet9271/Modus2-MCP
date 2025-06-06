# React Best Practices for Modus Projects

> **LEAD LEVEL GUIDANCE**: This document provides React-specific implementation guidance for Modus projects. It assumes you have already read the core principles.

## Project Structure

### Directory Organization

- **Modular Organization**: Each component should have its own directory containing:
  - `index.tsx` for the main component file
  - `styles.css` or `styles.module.css` for component-specific styles
  - `utils` directory for helper functions

### Standard Project Structure

```
src/
├── components/           # Reusable components
│   ├── layout/          # Layout components (Navbar, Sidebar, Footer)
│   ├── shared/          # Shared components used across features
│   └── feature/         # Feature-specific components
├── pages/               # Page components that use reusable components
├── context/             # Context providers for state management
├── hooks/               # Custom React hooks
├── routes/              # Routing configuration
├── utils/               # Utility functions
└── assets/              # Static assets
```

## Component Implementation

### Component Creation Guidelines

1. **Single Responsibility**: Each component should have a single responsibility
2. **Prop Documentation**: Document all props with JSDoc comments
3. **Default Props**: Provide default values for optional props
4. **Prop Validation**: Use PropTypes or TypeScript for prop validation
5. **Forward Refs**: Use forwardRef for components that need refs passed to them

### Event Handling Pattern

**ALWAYS** use this pattern for event handling:

```jsx
const buttonRef = useRef(null);

useEffect(() => {
  if (buttonRef.current) {
    buttonRef.current.addEventListener('buttonClick', handleClick);
    return () => {
      buttonRef.current?.removeEventListener('buttonClick', handleClick);
    };
  }
}, []);

const handleClick = (event) => {
  // Handle event
};

return <ModusButton ref={buttonRef}>Button Text</ModusButton>;
```

## State Management

### Local Component State
- Use `useState` for component-specific state
- Avoid prop drilling by extracting common state to context

### Application State
- Use React Context for shared state across components
- Create separate contexts for different domains (e.g., navigation, authentication)
- Implement context providers at the appropriate level of the component tree

## Routing

- Use React Router for navigation
- Define routes in a central location (`AppRoutes.tsx`)
- Use layout components for consistent UI across routes

## Component-Specific Guidelines

### Navbar Implementation
- Choose between `blue` and `default` variants
- Use the correct logo URL based on variant:
  - Blue variant: `https://modus-bootstrap.trimble.com/img/trimble-logo-rev.svg`
  - Default variant: `https://modus.trimble.com/img/trimble-logo.svg`
- Include hamburger menu and proper event handling

### SideNavigation Implementation
- Implement in Layout component for persistence across pages
- Use context to manage expanded state
- Use "push" mode with proper targetContent selector
- Set height with `calc(100vh - 56px)` to account for navbar

### Form Components
- Always use Modus form components instead of HTML elements
- Handle validation through component properties when available
