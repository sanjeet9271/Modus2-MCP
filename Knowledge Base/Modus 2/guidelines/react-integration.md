# React Framework Integration with Modus Web Components 2.0

This guide will help you get started with consuming the Modus React Web Component library in your React project.

## Introduction

We highly recommend using the Modus React Components library for React-based projects.
These components are automatically generated using the Stencil React Framework Integration.

Follow the steps outlined below to integrate and use Modus React Web Components effectively.

## Setup and Installation

Modus React Components have a peer dependency with Modus Web Components and require the
installation of both packages.

### 1. Install the Required Packages

```bash
npm install @trimble-oss/moduswebcomponents-react
# e.g.,
npm install @trimble-oss/moduswebcomponents-react
```

### 2. Set up the Styling

You need to import Modus styles in your main JavaScript or CSS file:

```js
import '@trimble-oss/moduswebcomponents/modus-wc-styles.css';
```

### 3. Component Registration

For React applications, the component registration is handled automatically by the React wrappers. In your application root:

```jsx
import { defineCustomElements } from '@trimble-oss/moduswebcomponents/loader';

// Call during the initial loading of your application
const Root = () => {
  defineCustomElements();

  return <App />;
};
```

## Using Components

Import and use components directly in your React components:

```tsx
import { ModusWcBadge } from '@trimble-oss/moduswebcomponents-react';

function MyComponent() {
  return <ModusWcBadge aria-label="Badge" content="Words" />;
}
```

## Using the Controlled Input Pattern

The controlled input pattern involves maintaining the state of the input's value within the React application or component. The [React Docs](https://react.dev/reference/react-dom/components/input#controlling-an-input-with-a-state-variable) describe this in more detail.

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

## Best Practice: Wrapping Components

When using Modus React Components directly, it is recommended to wrap them in corresponding React components within your application. This will abstract away from the library dependency, allowing more flexibility for you and your application in the future.

### Simple Wrapper Example

```tsx
import React from 'react';
import { ModusWcAvatar } from '@trimble-oss/moduswebcomponents-react';

interface Props extends React.ComponentProps<typeof ModusWcAvatar> {}

const Avatar: React.FC<Props> = (props) => {
  return <ModusWcAvatar {...props} />;
};

export default Avatar;
```

### Advanced Wrapper Example

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

## Benefits of Using React Wrappers

1. **Type Safety**: Full TypeScript support for component props and event handling
2. **React Integration**: Components behave like native React components
3. **Standard Patterns**: Support for controlled components and React patterns
4. **Performance**: Optimized rendering with React's virtual DOM
5. **Maintenance**: Easier to maintain as you can update the component library without changing component usage

## Common Patterns

### Working with Forms

React forms work well with Modus Web Components by applying the controlled input pattern:

```tsx
import React, { useState, FormEvent } from 'react';
import { ModusWcTextInput, ModusWcButton } from '@trimble-oss/moduswebcomponents-react';

const FormExample: React.FC = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: ''
  });

  const handleInputChange = (field: string) => (
    e: CustomEvent<any>
  ) => {
    setFormData({
      ...formData,
      [field]: e.detail.target.value
    });
  };

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    console.log('Form submitted with:', formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <ModusWcTextInput
        label="First Name"
        value={formData.firstName}
        onInputChange={handleInputChange('firstName')}
      />
      <ModusWcTextInput
        label="Last Name"
        value={formData.lastName}
        onInputChange={handleInputChange('lastName')}
      />
      <ModusWcButton type="submit">Submit</ModusWcButton>
    </form>
  );
};
```
