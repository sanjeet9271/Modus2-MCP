# Modus Web Components 2.0 Documentation Generator

## Overview
This document provides instructions for generating structured documentation for Modus Web Components 2.0. You'll be processing component documentation and creating two output files:
1. A Directory named `components-modus2` containing all the Modus Web Components inside this there would be directories named after components e.g. `modus-wc-switch`, `modus-wc-button`, etc.
2. Inside each component directory, there will be two files:
   - `<component_name>.json`: A JSON database containing structured information about the component's properties and events.
   - `<component_name>.md`: A Markdown file containing practical guidance on using the component, including example questions and answers.

## Input Structure
Each component will be provided in the following Markdown format in the combined_modus2.md file:

```markdown
# modus-wc-component

<!-- Auto Generated Below -->

## Overview
<!-- Component overview and description -->

## Properties
| Property | Attribute | Description | Type | Default |
| -------- | --------- | ----------- | ---- | ------- |
| ... | ... | ... | ... | ... |

## Events
| Event | Description | Type |
| ----- | ----------- | ---- |
| ... | ... | ... |

<!-- Additional sections like Dependencies may be present -->
```

## Step-by-Step Instructions

### Step 1: Understand Component Structure
For each component in the source file:
1. Extract the component name (e.g., `modus-wc-button`)
2. Analyze the provided overview to understand component purpose and usage
3. Identify properties and their details (name, type, description, default value)
4. Identify DOM events and their details (name, description, emitted value type)
5. Note any dependencies on other components

### Step 2: Create JSON Database
Create the corresponding component's JSON file with structured component information following this format:

```json
{
  "ModusWcComponentName": {
    "description": "Brief component description from Overview",
    "properties": [
      {
        "name": "propertyName",
        "type": "propertyType",
        "description": "Property description",
        "default": "defaultValue"
      }
    ],
    "events": [
      {
        "name": "eventName",
        "description": "Event description",
        "emits": "emittedValueType"
      }
    ],
    "dependencies": {
      "usedBy": ["component1", "component2"],
      "uses": ["component3", "component4"]
    },
    "componentName": "ModusWcComponentName"
  }
}
```

Example:
```json
"ModusWcButton": {
  "description": "A customizable button component used for user interactions",
  "properties": [
    {
      "name": "color",
      "type": "\"danger\" | \"primary\" | \"secondary\" | \"tertiary\" | \"warning\"",
      "description": "The color variant of the button",
      "default": "primary"
    },
    {
      "name": "customClass",
      "type": "string",
      "description": "Custom CSS class to apply to the button element",
      "default": ""
    },
    {
      "name": "disabled",
      "type": "boolean",
      "description": "If true, the button will be disabled",
      "default": "false"
    },
    {
      "name": "fullWidth",
      "type": "boolean",
      "description": "If true, the button will take the full width of its container",
      "default": "false"
    },
    {
      "name": "pressed",
      "type": "boolean",
      "description": "If true, the button will be in a pressed state (for toggle buttons)",
      "default": "false"
    },
    {
      "name": "shape",
      "type": "\"circle\" | \"rectangle\" | \"square\"",
      "description": "The shape of the button",
      "default": "rectangle"
    },
    {
      "name": "size",
      "type": "\"lg\" | \"md\" | \"sm\" | \"xs\"",
      "description": "The size of the button",
      "default": "md"
    },
    {
      "name": "type",
      "type": "\"button\" | \"reset\" | \"submit\"",
      "description": "The type of the button",
      "default": "button"
    },
    {
      "name": "variant",
      "type": "\"borderless\" | \"filled\" | \"outlined\"",
      "description": "The variant of the button",
      "default": "filled"
    }
  ],
  "events": [
    {
      "name": "buttonClick",
      "description": "Event emitted when the button is clicked or activated via keyboard",
      "emits": "KeyboardEvent | MouseEvent"
    }
  ],
  "dependencies": {
    "usedBy": ["modus-wc-alert", "modus-wc-modal", "modus-wc-navbar"]
  },
  "componentName": "ModusWcButton"
}
```

### Step 3: Create Knowledge Base
Create the corresponding component's markdown file with practical guidance on using each component:

1. Start the file with:
   ```markdown
   # Working with Modus Web Components 2.0
   
   This knowledge base demonstrates how to use Modus Web Components 2.0 in web applications following an agentic approach, with a focus on React integration for AI assistance.
   ```

2. For each component, add structured documentation:
   ```markdown
   # <ModusWcComponentName>
   
   ## Prompt 1
   **User Question:** [Formulate a relevant question based on the component's purpose and properties]
   
   **Agent Answer:**
   References:
   [Add your analysis of the component's properties, events, and usage patterns]
   
   ```html
   <!-- Add HTML code demonstrating component usage -->
   ```
   
   ```typescript
   // Add TypeScript code demonstrating component usage
   ```
   
   Note to keep in mind: 
    - Keep the code examples concise and don't include styles unless extremely necessary.
    - Ensure the code is relevant to the question asked.
    - Provide both HTML and TypeScript code blocks separately.
    - If multiple examples are needed, limit to 1-2 focused examples.
   ```

3. Include at least one practical question and answer for each component that demonstrates:
   - Component initialization
   - Setting key properties
   - Handling events
   - Framework-agnostic usage patterns (with optional framework-specific examples for React/Angular)
   
4. Format code examples as follows:
   - Provide separate HTML and TypeScript blocks
   - HTML should include the component with appropriate attributes and container elements
   - TypeScript should show event handling and interaction with the component
   - Follow this pattern:
   
   ```html
   <div id="component-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
     <modus-wc-component attribute="value"></modus-wc-component>
   </div>
   ```
   
   ```typescript
   const component = document.querySelector('#component-id');
   if (component) {
     component.addEventListener('eventName', (event) => {
       console.log('Event occurred:', event.detail);
     });
   }
   ```
   
5. When appropriate, include framework-specific usage examples (focusing primarily on React with vanilla JS as base):
   
   - **Framework-agnostic (vanilla JS):**
   ```typescript
   // Framework-agnostic example
   const button = document.querySelector('#action-button');
   if (button) {
     button.addEventListener('buttonClick', (event) => {
       console.log('Button clicked:', event.detail);
       // Perform action based on button click
       performAction();
     });
   }
   ```
   
   - **React example:**
   ```typescript
   // React example with component pattern
   import React from 'react';
   import { ModusWcButton } from '@trimble-oss/moduswebcomponents-react';
   
   function ButtonExample() {
     const handleButtonClick = (e) => {
       console.log('Button clicked:', e.detail);
       // Perform action based on button click
       performAction();
     };
     
     return (
       <ModusWcButton
         color="primary"
         variant="filled"
         size="md"
         onButtonClick={handleButtonClick}>
         Submit
       </ModusWcButton>
     );
   }
   ```
   ```

### Step 4: Guidelines for Creating Quality Documentation

When creating your documentation:

1. **Understand the Web Component's design philosophy**:
   - Modus Web Components are framework-agnostic custom elements
   - Shadow DOM is disabled by default for easier styling
   - Components can be used with or without frameworks
   - TypeScript definitions are provided for all components

2. **Analyze component properties thoroughly** to understand:
   - Required vs. optional properties
   - Default values and behaviors
   - Property types and constraints
   - How properties affect component behavior

3. **Formulate relevant questions** that developers might ask about the component:
   - "How do I initialize a basic [component]?"
   - "How can I handle events from [component]?"
   - "How do I customize the appearance of [component]?"
   - "How do I integrate [component] with a form?"

4. **Provide comprehensive answers** that include:
   - Component purpose and use cases
   - Key properties and their impact
   - Event handling strategies
   - HTML and TypeScript code examples as separate blocks
   - React framework integration examples for agentic coding use cases

5. **In the references section:**
   - Explain your thought process
   - Detail why specific properties were chosen
   - Provide context for implementation decisions
   
6. **For code examples:**
   - Always use the HTML and TypeScript format shown in the example pattern
   - Include proper element IDs and descriptive container elements
   - Demonstrate proper event handling
   - Include minimal but sufficient styling for clarity
   - Focus on the component's functionality, not excessive styling

## Example Documentation Pattern

```markdown

# ModusWcButton

## Prompt 1
**User Question:** How do I create a primary button in my app that submits a form and shows a loading state?

**Agent Answer:**
References:
I analyzed the ModusWcButton properties and determined that the important properties to implement here are `variant`, `color`, `type`, and handling the `buttonClick` event. For form submission with loading state, we'll need to combine this with some state management.

The ModusWcButton component is versatile with different variants (filled, outlined, borderless), colors (primary, secondary, danger, etc.), and shapes. Since this is for form submission, I'm using the "submit" type and primary color to indicate its importance in the UI.

```html
<div id="form-container" style="display: flex; flex-direction: column; gap: 16px; padding: 16px;">
  <form id="my-form">
    <!-- Form fields would go here -->
    <modus-wc-button
      id="submit-button"
      variant="filled"
      color="primary"
      type="submit">
      Submit Form
    </modus-wc-button>
  </form>
</div>
```

```typescript
const form = document.getElementById('my-form');
const submitButton = document.querySelector('#submit-button');

if (form && submitButton) {
  let isLoading = false;

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    
    if (isLoading) return;
    
    // Set loading state
    isLoading = true;
    submitButton.disabled = true;
    submitButton.textContent = 'Submitting...';
    
    try {
      // Simulate form submission
      await submitFormData(new FormData(form));
      console.log('Form submitted successfully');
    } catch (error) {
      console.error('Form submission error:', error);
    } finally {
      // Reset button state
      isLoading = false;
      submitButton.disabled = false;
      submitButton.textContent = 'Submit Form';
    }
  });
}

async function submitFormData(formData) {
  // Simulate API call
  return new Promise(resolve => setTimeout(resolve, 2000));
}
```

For React applications, here's how you would implement the same functionality with state management:

```tsx
import React, { useState } from 'react';
import { ModusWcButton } from '@trimble-oss/moduswebcomponents-react';

function FormWithSubmitButton() {
  const [isLoading, setIsLoading] = useState(false);
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (isLoading) return;
    
    setIsLoading(true);
    
    try {
      // Simulate form submission
      await new Promise(resolve => setTimeout(resolve, 2000));
      console.log('Form submitted successfully');
    } catch (error) {
      console.error('Form submission error:', error);
    } finally {
      setIsLoading(false);
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      {/* Form fields would go here */}
      <ModusWcButton
        variant="filled"
        color="primary"
        type="submit"
        disabled={isLoading}>
        {isLoading ? 'Submitting...' : 'Submit Form'}
      </ModusWcButton>
    </form>
  );
}
```
```
