# State Management in Modus 2.0 React Projects

> **LEAD LEVEL GUIDANCE**: This document provides best practices for managing state in Modus 2.0 React applications using Web Components.

## State Management Principles

### 1. Component State Isolation

- Use local state for component-specific UI states
- Leverage Modus Web Components' internal state management
- Handle state updates through component events

### 2. Context-Based Shared State

- Use React Context for cross-component state sharing
- Create separate contexts for different domains (theme, navigation, etc.)
- Place providers strategically in the component tree

### 3. Event Handling with Web Components

- Listen to Modus Web Component events using proper event handling
- Ensure proper cleanup of event listeners
- Use TypeScript event types for type safety

## Implementation Patterns

### Theme Provider Example (Modus 2.0)

```jsx
// context/ThemeContext.js
import { createContext, useState, useContext, useEffect } from 'react';

const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('modus-modern-light');
  
  useEffect(() => {
    // Apply theme to html element as per Modus 2.0 guidelines
    document.documentElement.setAttribute('data-theme', theme);
    document.documentElement.setAttribute('data-mode', theme.includes('dark') ? 'dark' : 'light');
  }, [theme]);
  
  const toggleTheme = () => {
    setTheme(prev => 
      prev.includes('light') ? 'modus-modern-dark' : 'modus-modern-light'
    );
  };
  
  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => useContext(ThemeContext);
```

### Form State Management (Modus 2.0)

```tsx
import { useState } from 'react';
import { ModusWcTextInput, ModusWcButton } from '@trimble-oss/moduswebcomponents-react';
import type { ModusWcTextInputCustomEvent, ModusWcButtonCustomEvent } from '@trimble-oss/moduswebcomponents-react';

const LoginForm = () => {
  const [formState, setFormState] = useState({
    username: '',
    password: ''
  });
  
  const handleInputChange = (e: ModusWcTextInputCustomEvent<string>) => {
    const { target, detail } = e;
    const inputName = (target as HTMLElement).getAttribute('name');
    setFormState(prev => ({ ...prev, [inputName]: detail }));
  };
  
  const handleSubmit = (e: ModusWcButtonCustomEvent) => {
    e.preventDefault();
    console.log('Form submitted:', formState);
  };
  
  return (
    <form>
      <ModusWcTextInput
        name="username"
        label="Username"
        value={formState.username}
        onValueChange={handleInputChange}
      />
      <ModusWcTextInput
        name="password"
        label="Password"
        type="password"
        value={formState.password}
        onValueChange={handleInputChange}
      />
      <ModusWcButton
        variant="primary"
        type="submit"
        onClick={handleSubmit}
      >
        Login
      </ModusWcButton>
    </form>
  );
};
```

### Navigation State (Modus 2.0)

```tsx
import { createContext, useState, useContext } from 'react';
import { ModusWcSideNavigation } from '@trimble-oss/moduswebcomponents-react';
import type { ModusWcSideNavigationCustomEvent } from '@trimble-oss/moduswebcomponents-react';

const NavigationContext = createContext<any>(null);

export const NavigationProvider = ({ children }) => {
  const [expanded, setExpanded] = useState(false);
  
  const handleExpandChange = (e: ModusWcSideNavigationCustomEvent<boolean>) => {
    setExpanded(e.detail);
  };
  
  const navItems = [
    { id: 'dashboard', text: 'Dashboard', icon: 'mi-dashboard', route: '/' },
    { id: 'profile', text: 'Profile', icon: 'mi-person', route: '/profile' },
    { id: 'settings', text: 'Settings', icon: 'mi-settings', route: '/settings' }
  ];
  
  return (
    <NavigationContext.Provider value={{ expanded, navItems }}>
      <ModusWcSideNavigation
        expanded={expanded}
        onExpandedChange={handleExpandChange}
      >
        {children}
      </ModusWcSideNavigation>
    </NavigationContext.Provider>
  );
};
```

## Best Practices for Modus 2.0

1. **TypeScript Integration**
   - Use TypeScript types provided by Modus Web Components
   - Properly type custom events and component props
   - Leverage interface definitions for component properties

2. **Event Handling**
   - Use the onEventName pattern for Modus Web Component events
   - Properly type event handlers using provided TypeScript types
   - Clean up event listeners when components unmount

3. **State Management Guidelines**
   - Keep component state local when possible
   - Use Context for shared state across components
   - Leverage Modus Web Components' built-in state management
   - Use TypeScript for type-safe state management

## Common Anti-Patterns to Avoid

1. **Manual Event Binding**: Use the provided React event handlers instead of addEventListener
2. **Ref-based Event Handling**: Prefer the onEventName props over ref-based event handling
3. **Improper Type Usage**: Always use the provided TypeScript types for events and props
4. **State Duplication**: Don't duplicate state that's already managed by Modus components
5. **Direct DOM Manipulation**: Use component props and events instead of direct DOM access
