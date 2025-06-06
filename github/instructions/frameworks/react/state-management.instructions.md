# State Management in Modus React Projects

> **LEAD LEVEL GUIDANCE**: This document provides best practices for managing state in Modus React applications.

## State Management Principles

### 1. Component State Isolation

- Isolate state to the smallest possible component scope
- Avoid state leakage between unrelated components
- Use local state for UI-specific concerns (e.g., form inputs, toggle states)

### 2. Context-Based Shared State

- Use React Context for sharing state across component hierarchies
- Create domain-specific contexts rather than a single global state
- Place providers at the appropriate level in the component tree

### 3. Event Isolation

- Isolate event handling to prevent interference between components
- Use proper event cleanup in useEffect returns
- Avoid double event binding

## Implementation Patterns

### Navigation Context Example

```jsx
// context/NavigationContext.js
import { createContext, useState, useContext, useCallback } from 'react';

const NavigationContext = createContext();

export const NavigationProvider = ({ children }) => {
  const [isExpanded, setIsExpanded] = useState(false);
  
  const toggleSidenav = useCallback(() => {
    setIsExpanded(prev => !prev);
  }, []);
  
  const navItems = [
    { id: 'dashboard', text: 'Dashboard', icon: 'dashboard', route: '/' },
    { id: 'profile', text: 'Profile', icon: 'person', route: '/profile' },
    { id: 'settings', text: 'Settings', icon: 'gear', route: '/settings' },
  ];
  
  return (
    <NavigationContext.Provider value={{ isExpanded, toggleSidenav, navItems }}>
      {children}
    </NavigationContext.Provider>
  );
};

export const useNavigation = () => useContext(NavigationContext);
```

### Form State Management Pattern

```jsx
import { useState, useRef, useEffect } from 'react';
import { ModusTextInput, ModusButton } from '@trimble-oss/modus-react-components';

const LoginForm = () => {
  const [formState, setFormState] = useState({
    username: '',
    password: ''
  });
  
  const usernameRef = useRef(null);
  const passwordRef = useRef(null);
  const submitRef = useRef(null);
  
  useEffect(() => {
    if (usernameRef.current) {
      usernameRef.current.addEventListener('valueChange', (e) => {
        setFormState(prev => ({ ...prev, username: e.detail }));
      });
      return () => {
        usernameRef.current?.removeEventListener('valueChange', (e) => {
          setFormState(prev => ({ ...prev, username: e.detail }));
        });
      };
    }
  }, []);
  
  useEffect(() => {
    if (passwordRef.current) {
      passwordRef.current.addEventListener('valueChange', (e) => {
        setFormState(prev => ({ ...prev, password: e.detail }));
      });
      return () => {
        passwordRef.current?.removeEventListener('valueChange', (e) => {
          setFormState(prev => ({ ...prev, password: e.detail }));
        });
      };
    }
  }, []);
  
  useEffect(() => {
    if (submitRef.current) {
      submitRef.current.addEventListener('buttonClick', handleSubmit);
      return () => {
        submitRef.current?.removeEventListener('buttonClick', handleSubmit);
      };
    }
  }, [formState]);
  
  const handleSubmit = () => {
    console.log('Form submitted:', formState);
  };
  
  return (
    <form>
      <ModusTextInput
        ref={usernameRef}
        label="Username"
        value={formState.username}
      />
      <ModusTextInput
        ref={passwordRef}
        label="Password"
        type="password"
        value={formState.password}
      />
      <ModusButton
        ref={submitRef}
        color="primary"
        type="button"
      >
        Login
      </ModusButton>
    </form>
  );
};
```

### Theme Context Example

```jsx
// context/ThemeContext.js
import { createContext, useState, useContext } from 'react';

const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');
  
  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };
  
  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => useContext(ThemeContext);
```

## Common Anti-Patterns to Avoid

1. **Global State Overuse**: Not everything needs to be in global state. Use local state for component-specific concerns.
2. **Prop Drilling**: If you're passing props through multiple layers, consider using context instead.
3. **Event Listener Leaks**: Always clean up event listeners in useEffect returns.
4. **Redundant State**: Don't duplicate state that could be derived from existing state.
5. **Inconsistent State Updates**: Use functional updates (`setCount(prev => prev + 1)`) when new state depends on previous state.
