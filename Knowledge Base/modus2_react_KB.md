# ModusWcAccordion

## Prompt 1
**User Question:** How do I create an accordion component with configurable collapsible sections that include icons and descriptions?

**Agent Answer:**
References:
I analyzed the ModusWcAccordion component and found that it's designed as a container for collapsible content sections. The accordion itself has minimal properties, with its main functionality coming from the nested `modus-wc-collapse` elements that you place inside it as children. The accordion emits an `expandedChange` event when sections are expanded or collapsed, which is useful for tracking user interactions.

Each collapse component can be configured with an options object that provides rich customization including title, description, icon, and more. This makes it easy to create professional-looking accordions with consistent styling.

```tsx
import React, { useState } from 'react';
import { ModusWcAccordion, ModusWcCollapse } from '@trimble-oss/moduswebcomponents-react';

function AccordionExample() {
  // Define collapse options
  const collapseOptions = [
    {
      description: 'Item one description',
      icon: 'alert',
      iconAriaLabel: 'Alert',
      title: 'Item One',
    },
    {
      description: 'Item two description',
      icon: 'alert',
      iconAriaLabel: 'Alert',
      title: 'Item Two',
    },
    {
      description: 'Item three description',
      icon: 'alert',
      iconAriaLabel: 'Alert',
      title: 'Item Three',
    },
  ];
  const [expandedSection, setExpandedSection] = useState(null);
  
  const handleExpandedChange = (e) => {
    const { expanded, index } = e.detail;
    setExpandedSection(expanded ? index : null);
    
    // You can perform additional actions based on which section was toggled
    if (expanded && index === 1) {
      // Do something special when section 2 is expanded
      console.log('Loading additional content for section 2...');
    }
  };
  
  return (
    <ModusWcAccordion onExpandedChange={handleExpandedChange} customClass="demo-accordion">
      <ModusWcCollapse options={collapseOptions[0]}>
        <div slot="content">This is the content for the first section of the accordion.</div>
      </ModusWcCollapse>
      
      <ModusWcCollapse options={collapseOptions[1]}>
        <div slot="content">
          <p>Content for section 2 goes here.</p>
          <ul>
            <li>List item 1</li>
            <li>List item 2</li>
          </ul>
        </div>
      </ModusWcCollapse>
      
      <ModusWcCollapse options={collapseOptions[2]}>
        <div slot="content">This is the third section content.</div>
      </ModusWcCollapse>
    </ModusWcAccordion>
  );
}
```

Note to keep in mind: 
- The accordion component itself doesn't manage which sections are open or closed; that functionality is handled by the individual collapse components.
- You can customize the appearance by adding a custom CSS class to the accordion via the `custom-class` property.
- The new accordion in Modus 2.0 uses collapse components instead of accordion-item components used in 1.0.
- Collapse components support rich configuration through the options object, allowing for titles, descriptions, icons, and more.
- For accessibility, the component automatically handles appropriate ARIA attributes for expandable content.
- The content should be placed in elements with the `slot="content"` attribute to properly display in the collapse component.

---

# ModusWcAlert

## Prompt 1
**User Question:** How do I create a basic alert notification with the Modus Alert component?

**Agent Answer:**
References:
- **Properties**:
  - `alert-title` (string, required): Main message text displayed in the alert
  - `alert-description` (string, optional): Additional descriptive text for the alert
  - `variant` ('error' | 'info' | 'success' | 'warning'): Visual style of the alert
  - `role` ('alert' | 'log' | 'marquee' | 'status' | 'timer'): ARIA role for accessibility
  - `dismissible` (boolean): Whether the alert can be dismissed by the user
  - `icon` (string, optional): Custom icon to display in the alert
  - `custom-class` (string, optional): Additional CSS class(es) to apply

- **Events**:
  - `dismissClick`: Emitted when the user clicks the dismiss button

- **Usage Patterns**: Alerts are commonly used to provide feedback messages, notifications, or status updates to users.

**TypeScript Example:**
```tsx
import React, { useRef, useEffect } from 'react';
import { ModusWcAlert } from '@trimble-oss/moduswebcomponents-react';

const BasicAlert: React.FC = () => {
  const alertRef = useRef<HTMLModusWcAlertElement>(null);
  
  useEffect(() => {
    const element = alertRef.current;
    if (element) {
      const handleDismiss = (e: CustomEvent) => {
        console.log('Alert dismissed');
      };
      
      element.addEventListener('dismissClick', handleDismiss);
      
      return () => {
        element.removeEventListener('dismissClick', handleDismiss);
      };
    }
  }, []);
  
  return (
    <ModusWcAlert
      ref={alertRef}
      alert-title="New message!"
      alert-description="You have 3 new messages."
      variant="info"
      role="status"
      dismissible={true}
    />
  );
};

export default BasicAlert;
```

**Notes:**
- The `alert-title` prop is required for the alert to display properly
- For accessibility, ensure you set the appropriate `role` attribute
- Default variant is 'info' if not specified

## Prompt 2
**User Question:** How can I add a custom button or content to a Modus Alert component?

**Agent Answer:**
References:
- **Slots**:
  - `button`: For adding a custom button to the alert
  - `content`: For adding custom HTML content to replace the default title/description

- **Usage Patterns**: Custom buttons are useful for providing actionable alerts, while custom content allows for more complex alert messages.

**TypeScript Example:**
```tsx
import React, { useState } from 'react';
import { ModusWcAlert, ModusWcButton } from '@trimble-oss/moduswebcomponents-react';

const AlertWithCustomElements: React.FC = () => {
  const [showAlert, setShowAlert] = useState(true);
  
  const handleDismiss = () => {
    setShowAlert(false);
  };
  
  const handleViewAction = () => {
    console.log('View documents action triggered');
    // Navigation or other action logic
  };
  
  if (!showAlert) return null;
  
  return (
    <>
      {/* Alert with custom button */}
      <ModusWcAlert
        alert-title="Action Required"
        alert-description="Please review the new documents"
        variant="warning"
        role="alert"
        dismissible={true}
        onDismissClick={handleDismiss}
      >
        <ModusWcButton
          slot="button"
          color="secondary"
          variant="outlined"
          aria-label="View documents"
          onClick={handleViewAction}
        >
          View Documents
        </ModusWcButton>
      </ModusWcAlert>
      
      {/* Alert with custom content */}
      <ModusWcAlert
        variant="success"
        role="status"
        dismissible={true}
        onDismissClick={handleDismiss}
        style={{ marginTop: '16px' }}
      >
        <div slot="content">
          <strong>Success!</strong> Your profile has been updated.
        </div>
      </ModusWcAlert>
    </>
  );
};

export default AlertWithCustomElements;
```

**Notes:**
- When using the `content` slot, the `alert-title` and `alert-description` props are ignored
- Custom buttons should include proper accessibility attributes (aria-label)
- You can handle both the dismiss event and custom button actions independently
- The button slot allows you to provide any action relevant to the alert message

---

# ModusWcAutocomplete

## Prompt 1
**User Question:** How do I implement a basic autocomplete search component with Modus?

**Agent Answer:**
References:
- **Properties**:
  - `items` (IAutocompleteItem[], required): Array of items to display in the dropdown
  - `value` (string): Current input value
  - `label` (string, optional): Label for the input field
  - `placeholder` (string, optional): Placeholder text for the input
  - `min-chars` (number): Minimum characters before showing suggestions (default: 0)
  - `size` ('sm' | 'md' | 'lg'): Size of the component (default: 'md')
  - `bordered` (boolean): Whether to show a border around the input (default: true)
  - `disabled` (boolean): Whether the component is disabled
  - `required` (boolean): Whether the component is required
  - `read-only` (boolean): Whether the component is read-only
  - `debounce-ms` (number): Milliseconds to wait before triggering input events (default: 300)
  - `no-results` (IAutocompleteNoResults): Configuration for no results message
  - `show-spinner` (boolean): Whether to show a loading spinner

- **Events**:
  - `inputChange`: Emitted when the input value changes
  - `inputFocus`: Emitted when the input gains focus
  - `inputBlur`: Emitted when the input loses focus
  - `itemSelect`: Emitted when an item is selected
  - `chipRemove`: Emitted when a chip is removed (in multi-select mode)

- **Usage Patterns**: Autocomplete components are used for search functionalities with suggestion lists, enabling users to quickly find and select from a pre-populated list of values.

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcAutocomplete } from '@trimble-oss/moduswebcomponents-react';

interface IAutocompleteItem {
  label: string;
  value: string;
  visibleInMenu: boolean;
  focused?: boolean;
  disabled?: boolean;
  selected?: boolean;
}

const BasicAutocomplete: React.FC = () => {
  // Sample items for autocomplete
  const [items, setItems] = useState<IAutocompleteItem[]>([
    { label: 'Apple', value: 'apple', visibleInMenu: true },
    { label: 'Banana', value: 'banana', visibleInMenu: true },
    { label: 'Cherry', value: 'cherry', visibleInMenu: true },
    { label: 'Grape', value: 'grape', visibleInMenu: true },
    { label: 'Orange', value: 'orange', visibleInMenu: true }
  ]);
  
  const [value, setValue] = useState('');
  const autocompleteRef = useRef<HTMLModusWcAutocompleteElement>(null);
  
  useEffect(() => {
    const element = autocompleteRef.current;
    if (!element) return;
    
    const handleInputChange = (e: CustomEvent) => {
      const input = e.detail.target as HTMLInputElement;
      const searchText = input.value.toLowerCase();
      
      setValue(input.value);
      
      // Update items visibility based on search text
      const updatedItems = items.map(item => ({
        ...item,
        visibleInMenu: item.label.toLowerCase().includes(searchText)
      }));
      
      setItems(updatedItems);
      if (element) {
        element.items = updatedItems;
      }
    };
    
    const handleItemSelect = (e: CustomEvent) => {
      setValue(e.detail.label);
      console.log('Selected item:', e.detail);
    };
    
    element.addEventListener('inputChange', handleInputChange);
    element.addEventListener('itemSelect', handleItemSelect);
    
    return () => {
      element.removeEventListener('inputChange', handleInputChange);
      element.removeEventListener('itemSelect', handleItemSelect);
    };
  }, [items]);
  
  useEffect(() => {
    if (autocompleteRef.current) {
      autocompleteRef.current.items = items;
    }
  }, [items]);
  
  return (
    <ModusWcAutocomplete
      ref={autocompleteRef}
      aria-label="Fruit search"
      label="Select a fruit"
      placeholder="Type to search..."
      bordered={true}
      min-chars={0}
      size="md"
      value={value}
    />
  );
};

export default BasicAutocomplete;
```

**Notes:**
- When updating `items`, always create a new array to ensure proper re-rendering
- The component doesn't filter items automatically; you must update the `visibleInMenu` property
- For accessibility, always include an appropriate `aria-label`

## Prompt 2

**User Question:** How can I implement a multi-select autocomplete with chip removal?

**Agent Answer:**
References:
- **Properties**:
  - `multi-select` (boolean): Enables selection of multiple items
  - All other properties from basic autocomplete apply

- **Events**:
  - `chipRemove`: Emitted when a chip is removed in multi-select mode
  - All other events from basic autocomplete apply

- **Usage Patterns**: Multi-select autocomplete is useful for selecting multiple items from a list, displaying selected items as removable chips.

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcAutocomplete } from '@trimble-oss/moduswebcomponents-react';

interface IAutocompleteItem {
  label: string;
  value: string;
  visibleInMenu: boolean;
  selected?: boolean;
  disabled?: boolean;
  focused?: boolean;
}

interface IAutocompleteNoResults {
  ariaLabel: string;
  label: string;
  subLabel: string;
}

const MultiSelectAutocomplete: React.FC = () => {
  const [items, setItems] = useState<IAutocompleteItem[]>([
    { label: 'JavaScript', value: 'js', visibleInMenu: true },
    { label: 'TypeScript', value: 'ts', visibleInMenu: true },
    { label: 'React', value: 'react', visibleInMenu: true },
    { label: 'Angular', value: 'angular', visibleInMenu: true },
    { label: 'Vue', value: 'vue', visibleInMenu: true },
    { label: 'Node.js', value: 'node', visibleInMenu: true }
  ]);
  
  const [inputValue, setInputValue] = useState('');
  const autocompleteRef = useRef<HTMLModusWcAutocompleteElement>(null);
  
  // No results configuration
  const noResults = {
    ariaLabel: 'No results found',
    label: 'No results found',
    subLabel: 'Try a different search term'
  };
  
  useEffect(() => {
    const element = autocompleteRef.current;
    if (!element) return;
    
    const handleInputChange = (e: CustomEvent) => {
      const input = e.detail.target as HTMLInputElement;
      const searchText = input.value.toLowerCase();
      
      setInputValue(input.value);
      
      // Update items visibility based on search text
      const updatedItems = items.map(item => ({
        ...item,
        visibleInMenu: item.label.toLowerCase().includes(searchText)
      }));
      
      setItems(updatedItems);
      if (element) {
        element.items = updatedItems;
      }
    };
    
    const handleItemSelect = (e: CustomEvent<IAutocompleteItem>) => {
      // Update selected status for the clicked item
      const updatedItems = items.map(item => 
        item.value === e.detail.value 
        ? { ...item, selected: true } 
        : item
      );
      
      setItems(updatedItems);
      if (element) {
        element.items = updatedItems;
        element.value = ''; // Clear input after selection
      }
      
      setInputValue('');
    };
    
    const handleChipRemove = (e: CustomEvent<IAutocompleteItem>) => {
      // Update the selected status for the removed item
      const updatedItems = items.map(item => 
        item.value === e.detail.value 
        ? { ...item, selected: false } 
        : item
      );
      
      setItems(updatedItems);
      if (element) {
        element.items = updatedItems;
      }
    };
    
    element.addEventListener('inputChange', handleInputChange);
    element.addEventListener('itemSelect', handleItemSelect);
    element.addEventListener('chipRemove', handleChipRemove);
    
    return () => {
      element.removeEventListener('inputChange', handleInputChange);
      element.removeEventListener('itemSelect', handleItemSelect);
      element.removeEventListener('chipRemove', handleChipRemove);
    };
  }, [items]);
  
  useEffect(() => {
    if (autocompleteRef.current) {
      autocompleteRef.current.items = items;
    }
  }, []);
  
  return (
    <ModusWcAutocomplete
      ref={autocompleteRef}
      aria-label="Tags selector"
      label="Select tags"
      placeholder="Type to search tags"
      multi-select={true}
      bordered={true}
      min-chars={0}
      size="md"
      value={inputValue}
      noResults={noResults}
    />
  );
};

export default MultiSelectAutocomplete;
```

**Notes:**
- When an item is selected in multi-select mode, it appears as a chip above the input
- Always clear the input value after selection in multi-select mode
- Handle the `chipRemove` event to update the item's selected state
- The component doesn't automatically update the items' visibility or selected state, you must handle this manually

---

# ModusWcAvatar

## Prompt 1
**User Question:** How do I implement a simple avatar component with an image in my React application?

**Agent Answer:**
References:
- **Properties**:
  - `img-src` (string, required): URL of the image to display in the avatar
  - `alt` (string, required): Alternative text for the image for accessibility
  - `size` ('xs' | 'sm' | 'md' | 'lg'): Size of the avatar (default: 'md')
  - `shape` ('circle' | 'square'): Shape of the avatar (default: 'circle')
  - `custom-class` (string, optional): Additional CSS class names to apply

- **Usage Patterns**: Avatars are commonly used to represent people or entities in user interfaces, particularly in user profiles, comment sections, or team listings.

**HTML Example:**
```html
<modus-wc-avatar
  img-src="https://example.com/profile-image.jpg"
  alt="Profile picture of Jane Doe"
  size="md"
  shape="circle"
  aria-label="Avatar">
</modus-wc-avatar>
```

**TypeScript Example:**
```tsx
import React from 'react';
import { ModusWcAvatar } from '@trimble-oss/moduswebcomponents-react';

const ProfileAvatar: React.FC = () => {
  return (
    <ModusWcAvatar
      img-src="https://picsum.photos/200/200?random=1"
      alt="Profile picture of Jane Doe"
      size="md"
      shape="circle"
      aria-label="Avatar"
    />
  );
};

export default ProfileAvatar;
```

**Notes:**
- Always provide an `alt` text for accessibility
- The default size is 'md' if not specified
- The default shape is 'circle' if not specified
- For best results, use square images with equal width and height

## Prompt 2
**User Question:** How can I create a user profile section with different avatar sizes and shapes?

**Agent Answer:**
References:
- **Sizes**:
  - `xs`: Extra small (24px)
  - `sm`: Small (32px)
  - `md`: Medium (40px, default)
  - `lg`: Large (48px)
- **Shapes**:
  - `circle`: Round avatar (default)
  - `square`: Square avatar with optional border radius

- **Usage Patterns**: Different avatar sizes can be used based on the context - smaller for compact layouts like comments or tables, larger for main profile sections.

**TypeScript Example:**
```jsx
import React from 'react';
import { ModusWcAvatar } from '@trimble-oss/moduswebcomponents-react';

const UserProfileWithTeam =  () => {
  // Sample data
  const user = {
    name: 'John Smith',
    role: 'Software Developer',
    imageSrc: 'https://picsum.photos/200/200?random=1'
  };
  
  const teamMembers = [
    { 
      id: '1', 
      name: 'Sarah Johnson', 
      role: 'Designer', 
      imageSrc: 'https://picsum.photos/150/150?random=2' 
    },
    { 
      id: '2', 
      name: 'Mike Brown', 
      role: 'Product Manager', 
      imageSrc: 'https://picsum.photos/150/150?random=3' 
    },
    { 
      id: '3', 
      name: 'Emily Clark', 
      role: 'UX Researcher', 
      imageSrc: 'https://picsum.photos/150/150?random=4' 
    }
  ];
  
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
      {/* User profile with large avatar */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
        <ModusWcAvatar
          img-src={user.imageSrc}
          alt={`Profile image of ${user.name}`}
          size="lg"
          shape="circle"
        />
        <div>
          <h3>{user.name}</h3>
          <p>{user.role}</p>
        </div>
      </div>
      
      {/* Team section */}
      <div>
        <h4>Team Members</h4>
        <div style={{ display: 'flex', gap: '8px' }}>
          {teamMembers.map(member => (
            <div key={member.id} style={{ textAlign: 'center' }}>
              <ModusWcAvatar
                img-src={member.imageSrc}
                alt={`Profile image of ${member.name}`}
                size="md"
                shape="square"
              />
              <div style={{ marginTop: '4px', fontSize: '12px' }}>{member.name}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default UserProfileWithTeam;
```

**Notes:**
- Combine different avatar sizes and shapes based on visual hierarchy
- Square avatars work well for team listings or grid layouts
- Circle avatars are often used for individual profile representations
- The component will maintain the aspect ratio of the provided image
- If the image fails to load, consider implementing a fallback (e.g., initials or a default icon)

---

# ModusWcBadge

## Prompt 1
**User Question:** How do I implement basic badge components with different color variants in my React application?

**Agent Answer:**
References:
- **Properties**:
  - `color` ('primary' | 'secondary' | 'tertiary' | 'high-contrast' | 'success' | 'warning' | 'danger'): Color scheme of the badge (default: 'primary')
  - `variant` ('counter' | 'filled' | 'text'): Visual style of the badge (default: 'filled')
  - `size` ('sm' | 'md' | 'lg'): Size of the badge (default: 'md')
  - `custom-class` (string, optional): Additional CSS class names to apply

- **Usage Patterns**: Badges are used to highlight information such as status, count, or categorization in a compact and visually distinct way.

**TypeScript Example:**
```tsx
import React from 'react';
import { ModusWcBadge } from '@trimble-oss/moduswebcomponents-react';

type BadgeColor = 'primary' | 'secondary' | 'tertiary' | 'high-contrast' | 'success' | 'warning' | 'danger';
type BadgeVariant = 'counter' | 'filled' | 'text';

interface BadgeExampleProps {
  variant: BadgeVariant;
}

const BadgeExample: React.FC<BadgeExampleProps> = ({ variant }) => {
  const colors: BadgeColor[] = ['primary', 'secondary', 'tertiary', 'high-contrast', 'success', 'warning', 'danger'];
  
  return (
    <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
      {colors.map(color => (
        <ModusWcBadge
          key={`${variant}-${color}`}
          color={color}
          variant={variant}
          size="md"
        >
          {color.charAt(0).toUpperCase() + color.slice(1)}
        </ModusWcBadge>
      ))}
    </div>
  );
};

const BadgesShowcase: React.FC = () => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
      <h3>Filled Badges</h3>
      <BadgeExample variant="filled" />
      
      <h3>Text Badges</h3>
      <BadgeExample variant="text" />
      
      <h3>Counter Badges</h3>
      <BadgeExample variant="counter" />
    </div>
  );
};

export default BadgesShowcase;
```

**Notes:**
- Use the `filled` variant for standard badges with a colored background
- Use the `text` variant for a more subtle appearance with just colored text
- Use the `counter` variant for numerical indicators, typically in notifications
- Choose appropriate colors to convey meaning: success (green), warning (yellow), danger (red)

## Prompt 2
**User Question:** How can I create badges with icons and use them in a notification context?

**Agent Answer:**
References:
- **Content**:
  - Badges can contain any valid HTML content including text and icons
  - When using icons, the component provides proper alignment and spacing

- **Usage Patterns**: 
  - Icon + text badges enhance meaning with visual indicators
  - Counter badges can display notification counts
  - Badges are often used in navigation menus, lists, and near interactive elements

**TypeScript Example:**
```tsx
import React from 'react';
import { ModusWcBadge, ModusWcIcon } from '@trimble-oss/moduswebcomponents-react';

interface NotificationItem {
  id: string;
  label: string;
  badgeType: 'counter' | 'status';
  badgeColor: 'primary' | 'secondary' | 'success' | 'warning' | 'danger';
  badgeContent: string;
  iconName?: string;
  count?: number;
}

const NotificationsExample: React.FC = () => {
  const notifications: NotificationItem[] = [
    {
      id: '1',
      label: 'Messages',
      badgeType: 'counter',
      badgeColor: 'danger',
      badgeContent: '',
      count: 5
    },
    {
      id: '2',
      label: 'Project Status',
      badgeType: 'status',
      badgeColor: 'success',
      badgeContent: 'Complete',
      iconName: 'check'
    },
    {
      id: '3',
      label: 'System Updates',
      badgeType: 'status',
      badgeColor: 'warning',
      badgeContent: 'Required',
      iconName: 'exclamation'
    },
    {
      id: '4',
      label: 'Security Alerts',
      badgeType: 'status',
      badgeColor: 'danger',
      badgeContent: 'Critical',
      iconName: 'shield'
    }
  ];
  
  return (
    <div style={{ 
      display: 'flex', 
      flexDirection: 'column', 
      gap: '16px',
      maxWidth: '400px'
    }}>
      {notifications.map(item => (
        <div key={item.id} style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          padding: '12px',
          borderRadius: '4px',
          backgroundColor: '#f5f5f5'
        }}>
          <span>{item.label}</span>
          
          {item.badgeType === 'counter' ? (
            <ModusWcBadge 
              color={item.badgeColor} 
              variant="counter" 
              size="sm"
            >
              {item.count}
            </ModusWcBadge>
          ) : (
            <ModusWcBadge 
              color={item.badgeColor} 
              variant="filled" 
              size="sm"
            >
              {item.iconName && (
                <ModusWcIcon
                  style={{ marginRight: '4px' }}
                  decorative={true}
                  name={item.iconName}
                  size="xs"
                />
              )}
              {item.badgeContent}
            </ModusWcBadge>
          )}
        </div>
      ))}
    </div>
  );
};

export default NotificationsExample;
```

**Notes:**
- When using icons inside badges, add appropriate spacing (margin or padding)
- Counter badges work best with just numbers and minimal padding
- For accessibility, ensure sufficient color contrast between badge text and background
- Consider the badge size appropriate to its context - smaller badges for menu items, larger badges for general UI elements

---

# ModusWcBreadcrumbs

## Prompt 1
**User Question:** How do I implement breadcrumb navigation in my React application using Modus?

**Agent Answer:**
References:
- **Properties**:
  - `items` (IBreadcrumb[], required): Array of breadcrumb items to display
  - `size` ('xs' | 'sm' | 'md' | 'lg'): Size of the breadcrumbs (default: 'md')
  - `custom-class` (string, optional): Additional CSS class names to apply

- **Interfaces**:
  ```typescript
  interface IBreadcrumb {
    label: string;   // Text to display for the breadcrumb
    url?: string;    // Optional URL for the breadcrumb link
  }
  ```

- **Events**:
  - `breadcrumbClick`: Emitted when a breadcrumb is clicked, with the clicked item as the event detail

- **Usage Patterns**: Breadcrumbs are used to help users navigate hierarchical structures by showing the current location and path back to the starting point.

**TypeScript Example:**
```tsx
import React, { useRef, useEffect } from 'react';
import { ModusWcBreadcrumbs } from '@trimble-oss/moduswebcomponents-react';

interface IBreadcrumb {
  label: string;
  url?: string;
}

const BreadcrumbNavigation: React.FC = () => {
  const breadcrumbsRef = useRef<HTMLModusWcBreadcrumbsElement>(null);
  
  // Sample breadcrumbs data
  const breadcrumbItems: IBreadcrumb[] = [
    { label: 'Home', url: '/home' },
    { label: 'Products', url: '/products' },
    { label: 'Category', url: '/products/category' },
    { label: 'Current Item' }
  ];
  
  useEffect(() => {
    const handleBreadcrumbClick = (e: CustomEvent<IBreadcrumb>) => {
      if (e.detail.url) {
        console.log('Navigating to:', e.detail.url);
        // Handle navigation here, e.g., with React Router
        // history.push(e.detail.url);
      }
    };
    
    const breadcrumbsElement = breadcrumbsRef.current;
    if (breadcrumbsElement) {
      breadcrumbsElement.addEventListener('breadcrumbClick', handleBreadcrumbClick as EventListener);
      
      return () => {
        breadcrumbsElement.removeEventListener('breadcrumbClick', handleBreadcrumbClick as EventListener);
      };
    }
  }, []);
  
  return (
    <ModusWcBreadcrumbs
      ref={breadcrumbsRef}
      items={breadcrumbItems}
      size="md"
      aria-label="Page navigation"
    />
  );
};

export default BreadcrumbNavigation;
```

**Notes:**
- The last breadcrumb in the list typically represents the current page and doesn't need a URL
- For accessibility, always include an appropriate `aria-label`
- Use consistent URL patterns for better user experience and SEO



---

# ModusWcButton

## Prompt 1
**User Question:** How do I implement different button variants and styles using the Modus Button component in React?

**Agent Answer:**
References:
- **Properties**:
  - `variant` ('filled' | 'outlined' | 'borderless'): Visual style of the button (default: 'filled')
  - `color` ('primary' | 'secondary' | 'tertiary' | 'warning' | 'danger'): Color scheme (default: 'primary')
  - `size` ('xs' | 'sm' | 'md' | 'lg'): Size of the button (default: 'md')
  - `shape` ('rectangle' | 'square' | 'circle'): Shape of the button (default: 'rectangle')
  - `type` ('button' | 'submit' | 'reset'): HTML button type (default: 'button')
  - `disabled` (boolean): Whether the button is disabled (default: false)
  - `pressed` (boolean): Whether the button appears in a pressed state (default: false)
  - `full-width` (boolean): Whether the button should take up the full width (default: false)
  - `custom-class` (string, optional): Additional CSS class names to apply

- **Events**:
  - `buttonClick`: Emitted when the button is clicked

- **Usage Patterns**: Buttons are used for actions, with different variants and colors indicating hierarchy and purpose.

**TypeScript Example:**
```tsx
import React from 'react';
import { ModusWcButton } from '@trimble-oss/moduswebcomponents-react';

type ButtonVariant = 'filled' | 'outlined' | 'borderless';
type ButtonColor = 'primary' | 'secondary' | 'tertiary' | 'warning' | 'danger';

interface ButtonDemoProps {
  variant: ButtonVariant;
  disabled?: boolean;
}

const ButtonDemo: React.FC<ButtonDemoProps> = ({ variant, disabled = false }) => {
  // Array of button colors to display
  const colors: ButtonColor[] = ['primary', 'secondary', 'tertiary', 'warning', 'danger'];
  
  const handleButtonClick = (color: string) => {
    console.log(`${variant} ${color} button clicked`);
  };
  
  return (
    <div style={{ marginBottom: '24px' }}>
      <h3>{variant.charAt(0).toUpperCase() + variant.slice(1)} Buttons</h3>
      <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
        {colors.map(color => (
          <ModusWcButton
            key={`${variant}-${color}`}
            variant={variant}
            color={color}
            disabled={disabled}
            size="md"
            aria-label={`${color} button`}
            onClick={() => handleButtonClick(color)}
          >
            {color.charAt(0).toUpperCase() + color.slice(1)}
          </ModusWcButton>
        ))}
      </div>
    </div>
  );
};

const ButtonVariantsShowcase: React.FC = () => {
  return (
    <div>
      <ButtonDemo variant="filled" />
      <ButtonDemo variant="outlined" />
      <ButtonDemo variant="borderless" />
      
      <h3>Disabled Buttons</h3>
      <ButtonDemo variant="filled" disabled={true} />
    </div>
  );
};

export default ButtonVariantsShowcase;
```

**Notes:**
- Use `filled` variant for primary actions and main call-to-actions
- Use `outlined` variant for secondary actions
- Use `borderless` variant for tertiary actions or in space-constrained areas
- Match the color to the action's semantic meaning: danger for destructive actions, warning for caution, etc.

## Prompt 2
**User Question:** How can I create buttons with icons and handle button events properly in React?

**Agent Answer:**
References:
- **Icon Integration**:
  - Icons can be added using the `modus-wc-icon` component as a child of the button
  - Icons can be placed before, after, or instead of text

- **Event Handling**:
  - Use `buttonClick` event to handle button clicks
  - Remember to properly clean up event listeners in React
  
**TypeScript Example:**
```tsx
import React, { useRef, useEffect } from 'react';
import { ModusWcButton, ModusWcIcon } from '@trimble-oss/moduswebcomponents-react';

// Example component showing different icon buttons with proper event handling
const IconButtonsExample: React.FC = () => {
  // Example of using refs and event listeners
  const downloadButtonRef = useRef<HTMLModusWcButtonElement>(null);
  
  useEffect(() => {
    const handleButtonClick = (e: Event) => {
      console.log('Download started');
      // Your download logic here
    };
    
    const buttonElement = downloadButtonRef.current;
    if (buttonElement) {
      buttonElement.addEventListener('buttonClick', handleButtonClick);
      
      return () => {
        buttonElement.removeEventListener('buttonClick', handleButtonClick);
      };
    }
  }, []);
  
  // Example of using onClick for simpler cases
  const handleAddClick = () => {
    console.log('Add item clicked');
    // Your add logic here
  };
  
  const handleNextClick = () => {
    console.log('Next clicked');
    // Your navigation logic here
  };
  
  return (
    <div>
      <h3>Icon Buttons</h3>
      
      <div style={{ display: 'flex', gap: '8px', marginBottom: '16px', alignItems: 'center' }}>
        {/* Icon-only button (using shape="circle" for a round button) */}
        <ModusWcButton 
          aria-label="Add item"
          shape="circle"
          onClick={handleAddClick}>
          <ModusWcIcon decorative={true} name="add" />
        </ModusWcButton>
        
        {/* Icon left button with ref */}
        <ModusWcButton 
          ref={downloadButtonRef}
          variant="filled" 
          color="primary">
          <ModusWcIcon decorative={true} name="download" />
          Download
        </ModusWcButton>
        
        {/* Icon right button */}
        <ModusWcButton 
          variant="outlined" 
          color="secondary"
          onClick={handleNextClick}>
          Next
          <ModusWcIcon decorative={true} name="arrow_right" />
        </ModusWcButton>
      </div>
      
      <h3>Icon Buttons with Different Shapes</h3>
      <div style={{ display: 'flex', gap: '8px' }}>
        <ModusWcButton 
          shape="square" 
          aria-label="Settings">
          <ModusWcIcon decorative={true} name="settings" />
        </ModusWcButton>
        
        <ModusWcButton 
          shape="circle" 
          aria-label="Notifications">
          <ModusWcIcon decorative={true} name="notifications" />
        </ModusWcButton>
        
        <ModusWcButton 
          shape="rectangle" 
          variant="outlined" 
          aria-label="Search button">
          <ModusWcIcon decorative={true} name="search" />
          Search
        </ModusWcButton>
      </div>
    </div>
  );
};

// Example component demonstrating form submission with buttons
const FormWithButtons: React.FC = () => {
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Form submitted');
  };
  
  const handleReset = () => {
    console.log('Form reset');
  };
  
  return (
    <form onSubmit={handleSubmit} style={{ marginTop: '24px' }}>
      <h3>Form Buttons</h3>
      <div style={{ marginBottom: '16px' }}>
        <input type="text" placeholder="Enter your name" style={{ padding: '8px', marginRight: '8px' }} />
      </div>
      
      <div style={{ display: 'flex', gap: '8px' }}>
        <ModusWcButton 
          type="submit" 
          variant="filled" 
          color="primary">
          <ModusWcIcon decorative={true} name="save" />
          Submit
        </ModusWcButton>
        
        <ModusWcButton 
          type="reset" 
          variant="outlined" 
          color="secondary"
          onClick={handleReset}>
          Reset
        </ModusWcButton>
      </div>
    </form>
  );
};

const ButtonsWithIconsDemo: React.FC = () => {
  return (
    <div>
      <IconButtonsExample />
      <FormWithButtons />
    </div>
  );
};

export default ButtonsWithIconsDemo;
```

**Notes:**
- Always provide `aria-label` for icon-only buttons for accessibility
- Set the `decorative` property to `true` on icons inside buttons
- For form buttons, use the appropriate `type` attribute: 'submit', 'reset', or 'button'
- Choose the appropriate button shape based on your design:
  - `rectangle` (default) for standard text buttons
  - `square` for icon buttons in toolbars or grids
  - `circle` for floating action buttons or icon buttons that should stand out
- In React, you can handle button clicks either by:
  1. Using a ref and the native `buttonClick` event (useful for complex interactions)
  2. Using the React `onClick` prop (simpler for most cases)

---

# ModusWcCard

## Prompt 1

**User Question:** How can I create different card layouts like horizontal cards or cards with background images?

**Agent Answer:**
References:
- **Properties**:
  - `layout` ('vertical' | 'horizontal'): Direction in which the card content flows (default: 'vertical')
  - `padding` ('normal' | 'compact'): Amount of padding inside the card (default: 'normal')
  - `bordered` (boolean): Whether the card has a border (default: false)
  - `background-figure` (boolean): Whether the figure should appear as a background (default: false)
  - `custom-class` (string, optional): Additional CSS class names to apply

- **Slots**:
  - `header`: Content to display at the top of the card, often used for images
  - `title`: Card title content
  - `subtitle`: Card subtitle content
  - Default slot: Main content of the card
  - `actions`: Action buttons or links at the bottom of the card
  - `footer`: Additional content at the bottom of the card

- **Layout Options**:
  - Use `layout="horizontal"` to create side-by-side content layout
  - Use `background-figure="true"` to make the header image serve as a background

- **Styling Techniques**:
  - Cards can be customized with CSS for shadows, transitions, and other effects
  - Use the `custom-class` property to apply custom styling

**TypeScript Example:**
```tsx
import React from 'react';
import { ModusWcCard, ModusWcButton } from '@trimble-oss/moduswebcomponents-react';

interface CardItem {
  id: string;
  title: string;
  subtitle: string;
  content: string;
  imageUrl: string;
  type: 'horizontal' | 'background';
}

const CardGallery: React.FC = () => {
  const cards: CardItem[] = [
    {
      id: '1',
      title: 'Horizontal Layout',
      subtitle: 'Side-by-side content',
      content: 'Perfect for displaying an image alongside text content.',
      imageUrl: 'https://picsum.photos/200/200?random=5',
      type: 'horizontal',
    },
    {
      id: '2',
      title: 'Background Image',
      subtitle: 'Overlay content',
      content: 'Text displayed over a full background image.',
      imageUrl: 'https://picsum.photos/200/200?random=2',
      type: 'background',
    },
    {
      id: '3',
      title: 'News Article',
      subtitle: 'Latest updates',
      content: 'Breaking news and important announcements.',
      imageUrl: 'https://picsum.photos/200/200?random=3',
      type: 'horizontal',
    }
  ];
  
  const cardContainerStyle: React.CSSProperties = {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
    gap: '16px',
    padding: '16px'
  };
  
  const hoverShadowClass = {
    transition: 'box-shadow 0.3s ease',
    '&:hover': {
      boxShadow: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
    }
  };
  
  const imageStyle: React.CSSProperties = {
    width: '100%',
    height: '100%',
    objectFit: 'cover'
  };
  
  const textOverlayStyle: React.CSSProperties = {
    color: 'white',
    textShadow: '0 1px 3px rgba(0, 0, 0, 0.6)'
  };
  
  const backgroundContentStyle: React.CSSProperties = {
    position: 'relative',
    zIndex: 1,
    padding: '16px',
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-end'
  };
  
  return (
    <div style={cardContainerStyle}>
      {cards.map(card => (
        card.type === 'horizontal' ? (
          <ModusWcCard
            key={card.id}
            aria-label={`${card.title} card`}
            layout="horizontal"
            bordered={true}
            custom-class="hover-shadow">
            <figure slot="header" style={{ width: '150px', height: '100%' }}>
              <img style={imageStyle} src={card.imageUrl} alt={`${card.title} image`} />
            </figure>
            <div>
              <span slot="title">{card.title}</span>
              <span slot="subtitle">{card.subtitle}</span>
              <p>{card.content}</p>
              <div slot="actions">
                <ModusWcButton aria-label="Learn more">Learn More</ModusWcButton>
              </div>
            </div>
          </ModusWcCard>
        ) : (
          <ModusWcCard
            key={card.id}
            aria-label={`${card.title} card`}
            background-figure={true}
            custom-class="hover-shadow">
            <figure slot="header" style={{ height: '200px' }}>
              <img style={imageStyle} src={card.imageUrl} alt={`${card.title} background`} />
            </figure>
            <div style={backgroundContentStyle}>
              <span slot="title" style={textOverlayStyle}>{card.title}</span>
              <span slot="subtitle" style={textOverlayStyle}>{card.subtitle}</span>
              <p style={textOverlayStyle}>{card.content}</p>
              <div slot="actions">
                <ModusWcButton color="secondary" variant="filled">View</ModusWcButton>
              </div>
            </div>
          </ModusWcCard>
        )
      ))}
    </div>
  );
};

export default CardGallery;
```

**Notes:**
- For horizontal cards, the figure slot is positioned on the side, making it ideal for thumbnail images
- When using `background-figure="true"`, the header image becomes a background, allowing content to overlay it
- Consider text contrast when placing content over background images for accessibility
- Use CSS properties like `object-fit: cover` to control how images display in cards
- Add custom hover effects (shadows, transitions) using the `custom-class` property and CSS

---

# ModusWcCheckbox

## Prompt 1
**User Question:** How do I implement a basic checkbox component in my React application using Modus?

**Agent Answer:**
References:
- **Properties**:
  - `value` (boolean): Whether the checkbox is checked (default: false)
  - `label` (string, optional): Text label for the checkbox
  - `indeterminate` (boolean): Whether the checkbox is in an indeterminate state (default: false)
  - `disabled` (boolean): Whether the checkbox is disabled (default: false)
  - `required` (boolean): Whether the checkbox is required (default: false)
  - `size` ('sm' | 'md' | 'lg'): Size of the checkbox (default: 'md')
  - `input-id` (string, optional): ID for the input element
  - `input-tab-index` (number, optional): Tab index for the input element
  - `name` (string, optional): Name attribute for the input element
  - `custom-class` (string, optional): Additional CSS class names to apply

- **Events**:
  - `inputChange`: Emitted when the checkbox value changes
  - `inputFocus`: Emitted when the checkbox receives focus
  - `inputBlur`: Emitted when the checkbox loses focus

- **Usage Patterns**: Checkboxes are used for selecting one or multiple options in a list, or to enable/disable a feature.

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcCheckbox } from '@trimble-oss/moduswebcomponents-react';

const CheckboxExample: React.FC = () => {
  const [isChecked, setIsChecked] = useState(false);
  const checkboxRef = useRef<HTMLModusWcCheckboxElement>(null);
  
  useEffect(() => {
    const checkbox = checkboxRef.current;
    if (checkbox) {
      const handleChange = (e: CustomEvent) => {
        setIsChecked(e.detail.target.checked);
        console.log('Checkbox value changed:', e.detail.target.checked);
      };
      
      checkbox.addEventListener('inputChange', handleChange);
      
      return () => {
        checkbox.removeEventListener('inputChange', handleChange);
      };
    }
  }, []);
  
  return (
    <ModusWcCheckbox
      ref={checkboxRef}
      aria-label="Terms and conditions"
      label="I agree to the terms and conditions"
      value={isChecked}
      required={true}
      size="md"
    />
  );
};

export default CheckboxExample;
```

**Notes:**
- Always use the controlled component pattern in React by managing the checkbox state
- The `value` property in ModusWcCheckbox corresponds to the checked state
- For accessibility, provide either a `label` or an `aria-label`
- When using form validation, include the `required` property as needed

## Prompt 2
**User Question:** How can I create a group of checkboxes and handle their state in React?

**Agent Answer:**
References:
- **Group Management**:
  - Checkboxes in groups need individual state management
  - Indeterminate state is useful for parent checkboxes controlling a group

- **Form Integration**:
  - Checkboxes can be used within forms for multiple selections
  - State can be managed with a single state object for all checkboxes

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcCheckbox } from '@trimble-oss/moduswebcomponents-react';

interface CheckboxOption {
  id: string;
  label: string;
  checked: boolean;
}

const CheckboxGroupExample: React.FC = () => {
  // Sample options for the checkbox group
  const [options, setOptions] = useState<CheckboxOption[]>([
    { id: 'option1', label: 'Option 1', checked: false },
    { id: 'option2', label: 'Option 2', checked: false },
    { id: 'option3', label: 'Option 3', checked: false },
    { id: 'option4', label: 'Option 4', checked: false }
  ]);
  
  // Calculate if the parent checkbox should be checked, unchecked, or indeterminate
  const allChecked = options.every((option) => option.checked);
  const someChecked = options.some((option) => option.checked);
  const isIndeterminate = someChecked && !allChecked;
  
  // Reference for the parent checkbox
  const parentCheckboxRef = useRef<HTMLModusWcCheckboxElement>(null);
  
  // Update the indeterminate state
  useEffect(() => {
    if (parentCheckboxRef.current) {
      parentCheckboxRef.current.indeterminate = isIndeterminate;
    }
  }, [isIndeterminate]);
  
  // Handle parent checkbox change
  const handleParentChange = (e: CustomEvent) => {
    const newCheckedState = e.detail.target.checked;
    const newOptions = options.map(option => ({
      ...option,
      checked: newCheckedState
    }));
    setOptions(newOptions);
  };
  
  // Handle individual checkbox change
  const handleOptionChange = (id: string) => (e: CustomEvent) => {
    const newCheckedState = e.detail.target.checked;
    const newOptions = options.map(option =>
      option.id === id ? { ...option, checked: newCheckedState } : option
    );
    setOptions(newOptions);
  };
  
  // Get the current form values (for submission or processing)
  const getSelectedOptions = () => {
    return options.filter(option => option.checked);
  };
  
  const handleSubmit = () => {
    const selectedOptions = getSelectedOptions();
    console.log('Selected options:', selectedOptions);
    // Process the selected options...
  };
  
  return (
    <div className="checkbox-group-container">
      <h3>Select Items</h3>
      
      {/* Parent checkbox */}
      <ModusWcCheckbox
        ref={parentCheckboxRef}
        aria-label="Select all options"
        label="Select All"
        value={allChecked}
        indeterminate={isIndeterminate}
        size="md"
        onInputChange={handleParentChange}
      />
      
      {/* Child checkboxes */}
      <div style={{ marginLeft: '24px', marginTop: '8px' }}>
        {options.map(option => (
          <div key={option.id} style={{ marginBottom: '8px' }}>
            <ModusWcCheckbox
              aria-label={option.label}
              label={option.label}
              value={option.checked}
              size="md"
              onInputChange={handleOptionChange(option.id)}
            />
          </div>
        ))}
      </div>
      
      {/* Action button */}
      <button 
        onClick={handleSubmit}
        disabled={!someChecked}
        style={{ 
          marginTop: '16px',
          padding: '8px 16px',
          background: someChecked ? '#0063a3' : '#cccccc',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: someChecked ? 'pointer' : 'not-allowed'
        }}>
        Submit Selection
      </button>
    </div>
  );
};

export default CheckboxGroupExample;
```

**Notes:**
- Use the `indeterminate` state for parent checkboxes when some but not all child options are selected
- Maintain a consistent state management approach for all checkboxes in a group
- For better accessibility, use logical grouping with fieldsets and legends for checkbox groups
- Consider providing select all/none functionality for convenience with larger checkbox groups
- When handling form submission, collect checked values by filtering the options array

---

# ModusWcChip

## Prompt 1
**User Question:** How can I implement a simple chip component that can be removed and handle click events in my React application?

**Agent Answer:**
References:
- **Properties**: 
  - `label`: string - The text to display in the chip
  - `showRemove`: boolean - Whether to show the remove button (default: false)
  - `active`: boolean - Active state of chip (default: false)
  - `disabled`: boolean - Whether the chip is disabled (default: false)
  - `hasError`: boolean - Whether the chip has an error (default: false)
  - `size`: "sm" | "md" | "lg" - The size of the chip (default: "md")
  - `variant`: "filled" | "outline" - The style variant of the chip (default: "filled")
  - `customClass`: string - Custom CSS class to apply to the inner div
- **Events**: 
  - `chipClick`: CustomEvent<KeyboardEvent | MouseEvent> - Emitted when the chip is clicked
  - `chipRemove`: CustomEvent<KeyboardEvent | MouseEvent> - Emitted when the remove button is clicked
- **Usage Patterns**: Commonly used in filter interfaces, tag systems, or data selection components

**TypeScript Example:**
```tsx
import React, { useRef, useEffect, useState } from 'react';
import { ModusWcChip } from '@trimble-oss/moduswebcomponents-react';

interface Tag {
  id: string;
  name: string;
}

const ChipExample: React.FC = () => {
  const [tags, setTags] = useState<Tag[]>([
    { id: '1', name: 'React' },
    { id: '2', name: 'TypeScript' },
    { id: '3', name: 'Modus' }
  ]);
  
  const handleChipRemove = (id: string) => {
    setTags(tags.filter(tag => tag.id !== id));
  };
  
  return (
    <div className="chip-container">
      {tags.map(tag => (
        <ChipWithEvents 
          key={tag.id}
          id={tag.id}
          label={tag.name}
          onRemove={handleChipRemove}
        />
      ))}
    </div>
  );
};

interface ChipProps {
  id: string;
  label: string;
  onRemove: (id: string) => void;
}

const ChipWithEvents: React.FC<ChipProps> = ({ id, label, onRemove }) => {
  const chipRef = useRef<HTMLModusWcChipElement>(null);
  
  useEffect(() => {
    const chip = chipRef.current;
    if (chip) {
      const handleRemove = (e: Event) => {
        e.preventDefault();
        onRemove(id);
      };
      
      chip.addEventListener('chipRemove', handleRemove);
      
      return () => {
        chip.removeEventListener('chipRemove', handleRemove);
      };
    }
  }, [id, onRemove]);
  
  return (
    <ModusWcChip
      ref={chipRef}
      label={label}
      showRemove={true}
      variant="filled"
      size="md"
    />
  );
};

export default ChipExample;
```

**Notes:**
- The chip component supports slotted content, enabling custom elements like icons or avatars
- Use the `chipClick` event for selection handling and the `chipRemove` event for removal logic
- For accessibility, ensure chips used in interactive contexts have proper keyboard navigation
- When used as filters or selections, maintain React state to keep track of selected/removed chips

## Prompt 2
**User Question:** How can I create chips with custom content like icons or avatars, and use them in a form as a multi-select component?

**Agent Answer:**
References:
- **Properties**: 
  - All properties from Prompt 1
  - The component supports slotted content for customization
- **Events**: 
  - `chipClick`: CustomEvent<KeyboardEvent | MouseEvent>
  - `chipRemove`: CustomEvent<KeyboardEvent | MouseEvent>
- **Usage Patterns**: 
  - Chip components can include slotted content like icons or avatars
  - Multiple chips can be used together for multi-select functionality
  - Can be used with form submissions for selected options


**TypeScript Example:**
```tsx
import React, { useRef, useEffect, useState } from 'react';
import { ModusWcChip, ModusWcIcon, ModusWcAvatar } from '@trimble-oss/moduswebcomponents-react';

interface User {
  id: string;
  name: string;
  avatar: string;
  selected: boolean;
}

const MultiSelectChips: React.FC = () => {
  const [users, setUsers] = useState<User[]>([
    { id: '1', name: 'John Doe', avatar: 'https://randomuser.me/api/portraits/men/1.jpg', selected: false },
    { id: '2', name: 'Jane Smith', avatar: 'https://randomuser.me/api/portraits/women/2.jpg', selected: true },
    { id: '3', name: 'Mike Johnson', avatar: 'https://randomuser.me/api/portraits/men/3.jpg', selected: true }
  ]);
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const selectedUsers = users.filter(user => user.selected);
    console.log('Selected users:', selectedUsers);
    // Process form submission with selected users
  };
  
  const toggleUser = (userId: string) => {
    setUsers(users.map(user => 
      user.id === userId ? { ...user, selected: !user.selected } : user
    ));
  };
  
  const removeUser = (userId: string) => {
    setUsers(users.map(user => 
      user.id === userId ? { ...user, selected: false } : user
    ));
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <h3>Select Team Members:</h3>
      
      <div className="available-users">
        {users.filter(user => !user.selected).map(user => (
          <button 
            key={user.id} 
            type="button"
            onClick={() => toggleUser(user.id)}
            className="user-option">
            <img src={user.avatar} alt={user.name} width="24" height="24" />
            {user.name}
          </button>
        ))}
      </div>
      
      <div className="selected-chips">
        {users.filter(user => user.selected).map(user => (
          <UserChip 
            key={user.id}
            user={user}
            onRemove={() => removeUser(user.id)}
          />
        ))}
      </div>
      
      <button type="submit">Save Team</button>
    </form>
  );
};

interface UserChipProps {
  user: User;
  onRemove: () => void;
}

const UserChip: React.FC<UserChipProps> = ({ user, onRemove }) => {
  const chipRef = useRef<HTMLModusWcChipElement>(null);
  
  useEffect(() => {
    const chip = chipRef.current;
    if (chip) {
      const handleRemove = () => {
        onRemove();
      };
      
      chip.addEventListener('chipRemove', handleRemove);
      
      return () => {
        chip.removeEventListener('chipRemove', handleRemove);
      };
    }
  }, [onRemove]);
  
  return (
    <ModusWcChip
      ref={chipRef}
      label={user.name}
      showRemove={true}
      variant="outline"
      size="md"
    >
      <ModusWcAvatar
        imgSrc={user.avatar}
        alt={user.name}
        size="xs"
      />
    </ModusWcChip>
  );
};

export default MultiSelectChips;
```

**Notes:**
- When using chips with avatars or icons, they should be placed as children of the ModusWcChip component
- For multi-select functionality, maintain the selection state in the parent React component
- The examples show how to use chips both as options selection and as display of selected items
- For form integration, chips represent selected values that can be submitted with the form
- Custom styling can be applied to the chip container to control layout (e.g., flex container for wrapping)
- For better accessibility, ensure the selected state is correctly communicated (e.g., using `active` prop or ARIA attributes)

---

# ModusWcCollapse

## Prompt 1
**User Question:** How can I implement a basic collapsible component with a title and content in React?

**Agent Answer:**
References:
- **Properties**: 
  - `expanded`: boolean - Controls whether the collapse is expanded or not (default: false)
  - `bordered`: boolean - Indicates if the component should have a border (default: false)
  - `collapseId`: string - A unique identifier for the component
  - `customClass`: string - Custom CSS class to apply to the outer div
  - `options`: ICollapseOptions - Configuration options for rendering the collapse component
    - `title`: string - The title to render in the collapse header
    - `description`: string - The description to render in the collapse header
    - `icon`: string - The Modus icon name to render in the collapse header
    - `iconAriaLabel`: string - The icon's aria-label
    - `size`: "xs" | "sm" | "md" | "lg" - The size of the collapse header
- **Events**: 
  - `expandedChange`: CustomEvent<{ expanded: boolean }> - Emitted when the expanded state changes
- **Usage Patterns**: Used for organizing and toggling the visibility of content sections

**TypeScript Example:**
```tsx
import React, { useRef, useEffect, useState } from 'react';
import { ModusWcCollapse } from '@trimble-oss/moduswebcomponents-react';

const CollapseExample: React.FC = () => {
  const [isExpanded, setIsExpanded] = useState(false);
  const collapseRef = useRef<HTMLModusWcCollapseElement>(null);
  
  useEffect(() => {
    const collapse = collapseRef.current;
    if (collapse) {
      const handleExpandedChange = (e: CustomEvent<{ expanded: boolean }>) => {
        setIsExpanded(e.detail.expanded);
        console.log('Collapse state changed:', e.detail.expanded ? 'expanded' : 'collapsed');
      };
      
      collapse.addEventListener('expandedChange', handleExpandedChange as EventListener);
      
      return () => {
        collapse.removeEventListener('expandedChange', handleExpandedChange as EventListener);
      };
    }
  }, []);
  
  const toggleCollapse = () => {
    setIsExpanded(!isExpanded);
  };
  
  return (
    <div>
      <button onClick={toggleCollapse}>
        {isExpanded ? 'Collapse Section' : 'Expand Section'}
      </button>
      
      <ModusWcCollapse
        ref={collapseRef}
        bordered={true}
        expanded={isExpanded}
        options={{
          title: 'Collapsible Content',
          description: 'Click to toggle visibility',
          icon: 'document',
          iconAriaLabel: 'Documentation',
          size: 'md'
        }}
      >
        <div slot="content">
          <h4>Section Content</h4>
          <p>This content can be expanded or collapsed.</p>
          <p>It's useful for hiding complex information until needed.</p>
        </div>
      </ModusWcCollapse>
    </div>
  );
};

export default CollapseExample;
```

**Notes:**
- You can either use the `options` prop to configure the header or use the `header` slot for custom header content
- The component emits `expandedChange` event when the state changes, which can be used to sync with React state
- You can programmatically control the expanded state using the `expanded` prop
- For accessibility, ensure your implementation maintains proper keyboard navigation and ARIA attributes
- The collapse component works well in accordion-like UI patterns when multiple collapses are used together

## Prompt 2
**User Question:** How can I create a custom collapse component with interactive elements in the header (like buttons) that don't trigger the collapse toggle?

**Agent Answer:**
References:
- **Properties**: 
  - Same properties as in Prompt 1
  - The component supports custom slotted header content
- **Events**: 
  - `expandedChange`: CustomEvent<{ expanded: boolean }> - Emitted when the expanded state changes
- **Usage Patterns**: 
  - Using slotted content for custom interactive headers
  - Implementing proper event handling to prevent collapse toggle when interacting with header elements

```tsx
import React, { useRef, useEffect, useState } from 'react';
import { ModusWcCollapse, ModusWcButton } from '@trimble-oss/moduswebcomponents-react';

interface CustomCollapseProps {
  title: string;
  children: React.ReactNode;
}

const CustomCollapse: React.FC<CustomCollapseProps> = ({ title, children }) => {
  const [isExpanded, setIsExpanded] = useState(false);
  const collapseRef = useRef<HTMLModusWcCollapseElement>(null);
  
  useEffect(() => {
    const collapse = collapseRef.current;
    if (collapse) {
      const handleExpandedChange = (e: CustomEvent<{ expanded: boolean }>) => {
        setIsExpanded(e.detail.expanded);
      };
      
      collapse.addEventListener('expandedChange', handleExpandedChange as EventListener);
      
      return () => {
        collapse.removeEventListener('expandedChange', handleExpandedChange as EventListener);
      };
    }
  }, []);
  
  const handleReset = (e: React.MouseEvent) => {
    e.stopPropagation(); // Prevent the collapse toggle
    console.log('Reset clicked');
    // Reset logic here
  };
  
  const handleSave = (e: React.MouseEvent) => {
    e.stopPropagation(); // Prevent the collapse toggle
    console.log('Save clicked');
    // Save logic here
  };
  
  const headerButtonRef = useRef<HTMLModusWcButtonElement>(null);
  const saveButtonRef = useRef<HTMLModusWcButtonElement>(null);
  
  useEffect(() => {
    const resetButton = headerButtonRef.current;
    const saveButton = saveButtonRef.current;
    
    // Add event listeners for the Modus buttons
    if (resetButton) {
      const handleResetClick = (e: Event) => {
        e.stopPropagation(); // Prevent collapse toggle
        console.log('Reset button clicked');
        // Reset implementation
      };
      
      resetButton.addEventListener('buttonClick', handleResetClick);
      return () => resetButton.removeEventListener('buttonClick', handleResetClick);
    }
    
    if (saveButton) {
      const handleSaveClick = (e: Event) => {
        e.stopPropagation(); // Prevent collapse toggle
        console.log('Save button clicked');
        // Save implementation
      };
      
      saveButton.addEventListener('buttonClick', handleSaveClick);
      return () => saveButton.removeEventListener('buttonClick', handleSaveClick);
    }
  }, []);
  
  return (
    <ModusWcCollapse
      ref={collapseRef}
      bordered={true}
      expanded={isExpanded}
      collapseId="custom-collapse"
    >
      <div slot="header" className="custom-collapse-header">
        <span>{title}</span>
        <div className="button-group" onClick={(e) => e.stopPropagation()}>
          <ModusWcButton 
            ref={headerButtonRef}
            size="sm" 
            variant="tertiary"
          >
            Reset
          </ModusWcButton>
          <ModusWcButton 
            ref={saveButtonRef}
            size="sm" 
            variant="primary"
          >
            Save
          </ModusWcButton>
        </div>
      </div>
      <div slot="content">
        {children}
      </div>
    </ModusWcCollapse>
  );
};

const CollapseWithInteractiveHeader: React.FC = () => {
  return (
    <div className="collapse-container">
      <h3>Configuration Panels</h3>
      
      <CustomCollapse title="User Preferences">
        <div className="form-content">
          <label>Theme:</label>
          <select>
            <option>Light</option>
            <option>Dark</option>
            <option>System</option>
          </select>
          
          <label>Language:</label>
          <select>
            <option>English</option>
            <option>Spanish</option>
            <option>French</option>
          </select>
        </div>
      </CustomCollapse>
      
      <CustomCollapse title="Notification Settings">
        <div className="form-content">
          <label>
            <input type="checkbox" /> Enable email notifications
          </label>
          <label>
            <input type="checkbox" /> Enable push notifications
          </label>
        </div>
      </CustomCollapse>
    </div>
  );
};

export default CollapseWithInteractiveHeader;
```

**Notes:**
- When using interactive elements in the header, use `stopPropagation()` to prevent the collapse toggle event
- Apply CSS with proper z-index to ensure clickable elements receive click events
- Custom headers are implemented using the `header` slot, which overrides the `options` prop
- For optimal accessibility, ensure focus management works correctly with keyboard navigation
- Interactive elements in the header should have appropriate ARIA attributes and keyboard support
- Consider using a wrapper component pattern as shown to encapsulate complex collapse behavior

---

# ModusWcDate

## Prompt 1
**User Question:** How can I implement a date input field with validation in my React application using the Modus Date component?

**Agent Answer:**
References:
- **Properties**: 
  - `value`: string - The value of the control in ISO 8601 format (yyyy-mm-dd)
  - `label`: string - The text to display within the label
  - `min`: string - Minimum date value
  - `max`: string - Maximum date value
  - `required`: boolean - Whether a value is required (default: false)
  - `disabled`: boolean - Whether the form control is disabled (default: false)
  - `readOnly`: boolean - Whether the value is editable (default: false)
  - `bordered`: boolean - Indicates that the input should have a border (default: true)
  - `size`: "sm" | "md" | "lg" - The size of the input (default: "md")
  - `feedback`: IInputFeedbackProp - Feedback object with level ('error' | 'info' | 'success' | 'warning') and message
- **Events**: 
  - `inputChange`: InputEvent - Emitted when the input value changes
  - `inputBlur`: FocusEvent - Emitted when the input loses focus
  - `inputFocus`: FocusEvent - Emitted when the input gains focus
- **Usage Patterns**: Date fields for forms, date range selection, appointment scheduling


**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcDate } from '@trimble-oss/moduswebcomponents-react';

interface DateFormValues {
  startDate: string;
  endDate: string;
}

interface DateValidationErrors {
  startDate?: string;
  endDate?: string;
}

const DateInputExample: React.FC = () => {
  const [formValues, setFormValues] = useState<DateFormValues>({
    startDate: '',
    endDate: ''
  });
  
  const [errors, setErrors] = useState<DateValidationErrors>({});
  const startDateRef = useRef<HTMLModusWcDateElement>(null);
  const endDateRef = useRef<HTMLModusWcDateElement>(null);
  
  // Get today's date in yyyy-mm-dd format
  const today = new Date().toISOString().split('T')[0];
  
  useEffect(() => {
    const startDateElement = startDateRef.current;
    const endDateElement = endDateRef.current;
    
    if (startDateElement) {
      const handleStartDateChange = (e: Event) => {
        const inputEvent = e as CustomEvent;
        const newStartDate = inputEvent.target?.value || '';
        
        setFormValues(prev => ({
          ...prev,
          startDate: newStartDate
        }));
        
        // Validate start date
        if (newStartDate === '' && errors.startDate !== 'Start date is required') {
          setErrors(prev => ({ ...prev, startDate: 'Start date is required' }));
        } else if (newStartDate !== '') {
          setErrors(prev => ({ ...prev, startDate: undefined }));
          
          // Check if start date is after end date
          if (formValues.endDate && newStartDate > formValues.endDate) {
            setErrors(prev => ({ ...prev, endDate: 'End date must be after start date' }));
          } else if (errors.endDate === 'End date must be after start date') {
            setErrors(prev => ({ ...prev, endDate: undefined }));
          }
        }
      };
      
      startDateElement.addEventListener('inputChange', handleStartDateChange);
      
      return () => {
        startDateElement.removeEventListener('inputChange', handleStartDateChange);
      };
    }
    
    if (endDateElement) {
      const handleEndDateChange = (e: Event) => {
        const inputEvent = e as CustomEvent;
        const newEndDate = inputEvent.target?.value || '';
        
        setFormValues(prev => ({
          ...prev,
          endDate: newEndDate
        }));
        
        // Validate end date
        if (newEndDate === '' && errors.endDate !== 'End date is required') {
          setErrors(prev => ({ ...prev, endDate: 'End date is required' }));
        } else if (newEndDate !== '') {
          setErrors(prev => ({ ...prev, endDate: undefined }));
          
          // Check if end date is before start date
          if (formValues.startDate && newEndDate < formValues.startDate) {
            setErrors(prev => ({ ...prev, endDate: 'End date must be after start date' }));
          } else if (errors.endDate === 'End date must be after start date') {
            setErrors(prev => ({ ...prev, endDate: undefined }));
          }
        }
      };
      
      endDateElement.addEventListener('inputChange', handleEndDateChange);
      
      return () => {
        endDateElement.removeEventListener('inputChange', handleEndDateChange);
      };
    }
  }, [formValues.startDate, formValues.endDate, errors.startDate, errors.endDate]);
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    // Validate form before submission
    const newErrors: DateValidationErrors = {};
    
    if (!formValues.startDate) {
      newErrors.startDate = 'Start date is required';
    }
    
    if (!formValues.endDate) {
      newErrors.endDate = 'End date is required';
    } else if (formValues.startDate && formValues.endDate < formValues.startDate) {
      newErrors.endDate = 'End date must be after start date';
    }
    
    setErrors(newErrors);
    
    // If no errors, process form submission
    if (Object.keys(newErrors).length === 0) {
      console.log('Form submitted with values:', formValues);
      // Process form submission
    }
  };
  
  return (
    <form onSubmit={handleSubmit} className="date-range-form">
      <h3>Select Date Range</h3>
      
      <div className="form-group">
        <ModusWcDate
          ref={startDateRef}
          label="Start Date"
          required={true}
          min={today}
          value={formValues.startDate}
          feedback={errors.startDate ? { level: 'error', message: errors.startDate } : undefined}
        />
      </div>
      
      <div className="form-group">
        <ModusWcDate
          ref={endDateRef}
          label="End Date"
          required={true}
          min={formValues.startDate || today}
          value={formValues.endDate}
          feedback={errors.endDate ? { level: 'error', message: errors.endDate } : undefined}
        />
      </div>
      
      <button type="submit">Submit</button>
    </form>
  );
};

export default DateInputExample;
```

**Notes:**
- The Date component uses the ISO 8601 format (`yyyy-mm-dd`) for date values
- Use the `min` and `max` properties to restrict date selection to a valid range
- The component supports form validation with the `feedback` property for displaying error messages
- For proper validation, use event listeners to capture input changes and validate in your React component
- Remember to clean up event listeners in the `useEffect` return function to prevent memory leaks


---

# ModusWcDivider

## Prompt 1
**User Question:** How can I implement horizontal and vertical dividers to separate content sections in my React application?

**Agent Answer:**
References:
- **Properties**: 
  - `orientation`: "horizontal" | "vertical" - The orientation of the divider (default: "vertical")
  - `color`: "primary" | "secondary" | "tertiary" | "high-contrast" | "success" | "warning" | "danger" - The color of the divider line (default: "tertiary")
  - `content`: string - Optional text content to display in the divider (default: "")
  - `position`: "center" | "end" | "start" - The position of the content within the divider (default: "center") 
  - `responsive`: boolean - Whether the divider adjusts to container size (default: true)
  - `customClass`: string - Custom CSS class to apply to the divider element (default: "")
- **Events**: None
- **Usage Patterns**: Dividers are used to visually separate content sections and create visual hierarchy

**TypeScript Example:**
```tsx
import React from 'react';
import { ModusWcDivider } from '@trimble-oss/moduswebcomponents-react';

const DividerExample: React.FC = () => {
  return (
    <div className="divider-examples">
      {/* Horizontal divider example */}
      <section className="example-section">
        <h3>Horizontal Divider</h3>
        <div className="content-section">
          <p>This is the content above the divider. It demonstrates how to separate content horizontally.</p>
          
          <ModusWcDivider 
            orientation="horizontal"
            color="tertiary"
            aria-label="Section divider"
          />
          
          <p>This is the content below the divider. Notice the clean separation between these paragraphs.</p>
        </div>
      </section>
      
      {/* Vertical divider example */}
      <section className="example-section">
        <h3>Vertical Divider</h3>
        <div style={{ display: 'flex', height: '100px' }}>
          <div style={{ flex: 1, padding: '8px' }}>
            <p>Left side content</p>
            <p>This demonstrates content separation using a vertical divider.</p>
          </div>
          
          <ModusWcDivider 
            orientation="vertical"
            color="primary"
            aria-label="Column divider"
          />
          
          <div style={{ flex: 1, padding: '8px' }}>
            <p>Right side content</p>
            <p>This content is visually separated from the left side.</p>
          </div>
        </div>
      </section>
      
      {/* Divider with content example */}
      <section className="example-section">
        <h3>Divider with Content</h3>
        <div className="form-container">
          <div className="signin-section">
            <h4>Sign in with credentials</h4>
            <input type="email" placeholder="Email" />
            <input type="password" placeholder="Password" />
            <button>Sign In</button>
          </div>
          
          <ModusWcDivider 
            orientation="horizontal"
            content="OR"
            color="secondary"
            position="center"
            aria-label="Alternative sign-in options"
          />
          
          <div className="social-signin">
            <h4>Sign in with social media</h4>
            <button>Google</button>
            <button>Facebook</button>
          </div>
        </div>
      </section>
    </div>
  );
};

export default DividerExample;
```

**Notes:**
- For horizontal dividers, the parent container needs sufficient width
- For vertical dividers, the parent container needs sufficient height and should use `display: flex` or similar
- When using dividers with content, ensure the content text is concise
- The divider's color should complement your application's color scheme
- Consider accessibility by including appropriate `aria-label` attributes, especially when using content within dividers

---

# ModusWcIcon

## Prompt 1
**User Question:** How can I use Modus icons in my React application and customize their appearance?

**Agent Answer:**
References:
- **Properties**: 
  - `name`: string - The icon name, should match the CSS class in the icon font
  - `size`: "xs" | "sm" | "md" | "lg" - The icon size (default: "md")
  - `decorative`: boolean - Indicates that the icon is purely decorative (hidden from screen readers when true) (default: true)
  - `customClass`: string - Custom CSS class to apply to the icon element (default: "")
- **Events**: None (use standard DOM events like `click` on the element)
- **Usage Patterns**: Used for visual indicators, action buttons, status indicators, and to enhance UI elements with visual cues

**TypeScript Example:**
```tsx
import React from 'react';
import { ModusWcIcon } from '@trimble-oss/moduswebcomponents-react';

// Note: Make sure Modus Icons is installed in your application
// npm install @trimble-oss/modus-icons

interface IconDemoProps {
  name: string;
  size?: 'xs' | 'sm' | 'md' | 'lg';
  color?: string;
  label?: string;
}

const IconWithLabel: React.FC<IconDemoProps> = ({
  name,
  size = 'md',
  color,
  label
}) => {
  const iconStyle = color ? { color } : undefined;
  
  return (
    <div className="icon-with-label">
      <ModusWcIcon
        name={name}
        size={size}
        decorative={!label}
        aria-label={label}
        style={iconStyle}
      />
      {label && <span className="icon-label">{label}</span>}
    </div>
  );
};

const IconsDemo: React.FC = () => {
  // Common icons used in applications
  const commonIcons = [
    { name: 'alert', label: 'Alert', color: '#d54309' },
    { name: 'check_circle', label: 'Success', color: '#0ca45c' },
    { name: 'info', label: 'Information', color: '#0063a3' },
    { name: 'warning', label: 'Warning', color: '#ffbe00' },
    { name: 'error', label: 'Error', color: '#d54309' },
    { name: 'settings', label: 'Settings' },
    { name: 'search', label: 'Search' },
    { name: 'user', label: 'User Profile' },
    { name: 'notifications', label: 'Notifications' }
  ];
  
  const handleIconClick = (iconName: string) => {
    console.log(`Icon ${iconName} clicked`);
    // Handle icon click action
  };
  
  // Styles for demonstration
  const containerStyle: React.CSSProperties = {
    display: 'flex',
    flexWrap: 'wrap',
    gap: '20px',
    marginBottom: '30px'
  };
  
  const sizeContainerStyle: React.CSSProperties = {
    display: 'flex',
    alignItems: 'center',
    gap: '24px'
  };
  
  const iconCardStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: '16px',
    border: '1px solid #e0e0e0',
    borderRadius: '4px',
    width: '100px',
    cursor: 'pointer'
  };
  
  return (
    <div className="icons-demo">
      <h2>Icon Sizes</h2>
      <div style={sizeContainerStyle}>
        <div>
          <ModusWcIcon name="search" size="xs" aria-label="Extra small icon" />
          <p>Extra Small (xs)</p>
        </div>
        <div>
          <ModusWcIcon name="search" size="sm" aria-label="Small icon" />
          <p>Small (sm)</p>
        </div>
        <div>
          <ModusWcIcon name="search" size="md" aria-label="Medium icon" />
          <p>Medium (md)</p>
        </div>
        <div>
          <ModusWcIcon name="search" size="lg" aria-label="Large icon" />
          <p>Large (lg)</p>
        </div>
      </div>
      
      <h2>Common Icons</h2>
      <div style={containerStyle}>
        {commonIcons.map((icon) => (
          <div 
            key={icon.name}
            style={iconCardStyle}
            onClick={() => handleIconClick(icon.name)}
            role="button"
            tabIndex={0}
          >
            <IconWithLabel
              name={icon.name}
              label={icon.label}
              color={icon.color}
              size="md"
            />
          </div>
        ))}
      </div>
      
      <h2>Interactive Icons</h2>
      <div style={containerStyle}>
        <button className="icon-button">
          <ModusWcIcon name="edit" decorative={true} />
          Edit
        </button>
        
        <button className="icon-button">
          <ModusWcIcon name="delete" decorative={true} />
          Delete
        </button>
        
        <button className="icon-button">
          <ModusWcIcon name="download" decorative={true} />
          Download
        </button>
      </div>
    </div>
  );
};

export default IconsDemo;
```

**Notes:**
- You must install the Modus Icons package separately: `npm install @trimble-oss/modus-icons`
- For accessibility, use the `aria-label` attribute when icons convey meaning or use `decorative={true}` for purely decorative icons
- Icon color is controlled via CSS, not through component props
- Use standard DOM click events on the component for interactive icons
- For icons with text, ensure proper spacing between the icon and text for readability
- The available icon names come from the Modus Icons library

---

# ModusWcInputFeedback

## Prompt 1
**User Question:** How can I display validation feedback messages for form inputs in my React application using the Modus Input Feedback component?

**Agent Answer:**
References:
- **Properties**: 
  - `level`: "error" | "info" | "success" | "warning" - The feedback level that determines the icon and color
  - `message`: string - The feedback message to display
  - `size`: "sm" | "md" | "lg" - The size of the feedback component (default: "md")
  - `icon`: string - Optional custom Modus icon name to override the default icon for the level
  - `customClass`: string - Custom CSS class to apply to the outer div element
- **Events**: None
- **Usage Patterns**: Used to provide feedback for form inputs such as validation errors, helpful information, or success messages

**TypeScript Example:**
```tsx
import React, { useState } from 'react';
import { ModusWcInputFeedback, ModusWcTextInput } from '@trimble-oss/moduswebcomponents-react';

type FeedbackLevel = 'error' | 'info' | 'success' | 'warning';

interface FeedbackState {
  level?: FeedbackLevel;
  message?: string;
}

const FormWithFeedback: React.FC = () => {
  // Form states for different fields
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [emailFeedback, setEmailFeedback] = useState<FeedbackState>({});
  const [passwordFeedback, setPasswordFeedback] = useState<FeedbackState>({
    level: 'info',
    message: 'Password must be at least 8 characters with one uppercase letter and one number'
  });
  
  // Email validation
  const validateEmail = (value: string) => {
    if (!value) {
      setEmailFeedback({
        level: 'error',
        message: 'Email is required'
      });
      return false;
    } else if (!/\S+@\S+\.\S+/.test(value)) {
      setEmailFeedback({
        level: 'error',
        message: 'Please enter a valid email address'
      });
      return false;
    } else {
      setEmailFeedback({
        level: 'success',
        message: 'Email is valid'
      });
      return true;
    }
  };
  
  // Password validation
  const validatePassword = (value: string) => {
    if (!value) {
      setPasswordFeedback({
        level: 'error',
        message: 'Password is required'
      });
      return false;
    } else if (value.length < 8) {
      setPasswordFeedback({
        level: 'error',
        message: 'Password must be at least 8 characters long'
      });
      return false;
    } else if (!/[A-Z]/.test(value) || !/[0-9]/.test(value)) {
      setPasswordFeedback({
        level: 'warning',
        message: 'Password should contain at least one uppercase letter and one number'
      });
      return true; // Warning doesn't invalidate the form
    } else {
      setPasswordFeedback({
        level: 'success',
        message: 'Password meets requirements'
      });
      return true;
    }
  };
  
  const handleEmailChange = (e: CustomEvent) => {
    const newValue = e.detail.target?.value || '';
    setEmail(newValue);
    validateEmail(newValue);
  };
  
  const handlePasswordChange = (e: CustomEvent) => {
    const newValue = e.detail.target?.value || '';
    setPassword(newValue);
    validatePassword(newValue);
  };
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    const isEmailValid = validateEmail(email);
    const isPasswordValid = validatePassword(password);
    
    if (isEmailValid && isPasswordValid) {
      console.log('Form submitted:', { email, password });
      // Process form submission
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <h3>Sign Up</h3>
      
      <div style={{ marginBottom: '20px' }}>
        <ModusWcTextInput
          label="Email"
          type="email"
          value={email}
          required={true}
          onInputChange={handleEmailChange}
          onInputBlur={() => validateEmail(email)}
          feedback={emailFeedback.level ? {
            level: emailFeedback.level,
            message: emailFeedback.message
          } : undefined}
        />
      </div>
      
      <div style={{ marginBottom: '20px' }}>
        <ModusWcTextInput
          label="Password"
          type="password"
          value={password}
          required={true}
          onInputChange={handlePasswordChange}
          onInputBlur={() => validatePassword(password)}
        />
        
        {/* Only render feedback if we have a level */}
        {passwordFeedback.level && (
          <ModusWcInputFeedback
            level={passwordFeedback.level}
            message={passwordFeedback.message}
            size="md"
          />
        )}
      </div>
      
      <button 
        type="submit"
        disabled={
          !email || 
          !password || 
          emailFeedback.level === 'error' || 
          passwordFeedback.level === 'error'
        }
      >
        Sign Up
      </button>
    </form>
  );
};

export default FormWithFeedback;
```

**Notes:**
- Use appropriate feedback levels based on the context:
  - `error`: For invalid inputs that prevent form submission
  - `warning`: For potential issues that don't prevent submission
  - `info`: For helpful instructions or context
  - `success`: For valid inputs or successful actions
- The component automatically selects appropriate icons based on the feedback level
- You can override the default icon using the `icon` property
- For accessibility, ensure error messages are clear and descriptive
- When used with Modus input components, you can pass feedback directly to those components
- Consider showing feedback only after user interaction (e.g., on blur or submit)


---

# ModusWcInputLabel

## Prompt 1
**User Question:** How can I create accessible form labels with required field indicators using the Modus Input Label component in React?

**Agent Answer:**
References:
- **Properties**: 
  - `labelText`: string - The text to display within the label
  - `forId`: string - The `for` attribute of the label, matching the `id` of the associated input
  - `required`: boolean - Whether the label indicates a required field (default: false)
  - `size`: "sm" | "md" | "lg" - The size of the label (default: "md")
  - `subLabelText`: string - Additional text rendered beneath the main label text
  - `customClass`: string - Additional classes for custom styling
- **Events**: None
- **Usage Patterns**: Used to provide accessible labels for form inputs with consistent styling and support for required field indicators

**TypeScript Example:**
```tsx
import React from 'react';
import { ModusWcInputLabel, ModusWcTextInput } from '@trimble-oss/moduswebcomponents-react';

const AccessibleForm: React.FC = () => {
  return (
    <form className="signup-form">
      <div className="form-group">
        <ModusWcInputLabel
          labelText="Username"
          forId="username-input"
          size="md"
        />
        <input 
          id="username-input" 
          type="text" 
          className="form-control"
          aria-describedby="username-help"
        />
        <small id="username-help" className="form-text text-muted">
          Choose a unique username for your account.
        </small>
      </div>
      
      <div className="form-group">
        <ModusWcInputLabel
          labelText="Email Address"
          forId="email-input"
          required={true}
          size="md"
        />
        <input 
          id="email-input" 
          type="email" 
          className="form-control" 
          required
          aria-describedby="email-help"
        />
        <small id="email-help" className="form-text text-muted">
          We'll never share your email with anyone else.
        </small>
      </div>
      
      <div className="form-group">
        <ModusWcInputLabel
          labelText="Password"
          forId="password-input"
          required={true}
          subLabelText="Must contain at least 8 characters, one uppercase letter, and one number"
          size="md"
        />
        <input 
          id="password-input" 
          type="password" 
          className="form-control" 
          required
          pattern="(?=.*\d)(?=.*[A-Z]).{8,}"
          aria-describedby="password-requirements"
        />
        <div id="password-requirements" className="requirements-list">
          <ul>
            <li>Minimum 8 characters</li>
            <li>At least one uppercase letter</li>
            <li>At least one number</li>
          </ul>
        </div>
      </div>
      
      <div className="form-group">
        <ModusWcInputLabel
          labelText="Confirm Password"
          forId="confirm-password"
          required={true}
          size="md"
        />
        <input 
          id="confirm-password" 
          type="password" 
          className="form-control"
          required
        />
      </div>
      
      <button type="submit" className="btn btn-primary">Submit</button>
    </form>
  );
};

// Example with Modus Text Input component
const ModusFormExample: React.FC = () => {
  const [username, setUsername] = React.useState('');
  const [email, setEmail] = React.useState('');
  
  const handleUsernameChange = (e: CustomEvent) => {
    setUsername(e.detail.target?.value || '');
  };
  
  const handleEmailChange = (e: CustomEvent) => {
    setEmail(e.detail.target?.value || '');
  };
  
  return (
    <form className="modus-form">
      <div className="form-group">
        <ModusWcInputLabel
          labelText="Username"
          forId="modus-username"
          size="md"
        />
        <ModusWcTextInput
          id="modus-username"
          value={username}
          onInputChange={handleUsernameChange}
        />
      </div>
      
      <div className="form-group">
        <ModusWcInputLabel
          labelText="Email Address"
          forId="modus-email"
          required={true}
          size="md"
          subLabelText="We'll send a confirmation to this address"
        />
        <ModusWcTextInput
          id="modus-email"
          type="email"
          required={true}
          value={email}
          onInputChange={handleEmailChange}
        />
      </div>
      
      <button type="submit">Submit</button>
    </form>
  );
};

export default AccessibleForm;
```

**Notes:**
- Always use the `forId` property to associate the label with its input element for accessibility
- The `required` property adds a visual indicator (typically an asterisk) to show that the field is mandatory
- Use `subLabelText` for additional instructions or context that doesn't fit in the main label
- When used with Modus input components, ensure IDs match between the label and input
- The component works with standard HTML inputs or with Modus form components
- For complex instructions, consider using `aria-describedby` with additional help text elements
- Different sizes (sm, md, lg) can be used to maintain proper visual hierarchy


---

# ModusWcLoader

## Prompt 1
**User Question:** How can I implement loading indicators with different styles in my React application using the Modus Loader component?

**Agent Answer:**
References:
- **Properties**: 
  - `variant`: "spinner" | "ball" | "bars" | "dots" | "infinity" | "ring" - The visual style of the loader (default: "spinner")
  - `color`: "primary" | "secondary" | "accent" | "neutral" | "info" | "success" | "warning" | "error" - The color of the loader (default: "primary")
  - `size`: "xs" | "sm" | "md" | "lg" - The size of the loader (default: "md")
  - `customClass`: string - Custom CSS class to apply to the loader element (default: "")
- **Events**: None
- **Usage Patterns**: Used to indicate loading states for various UI elements, pages, or processes


**TypeScript Example:**
```tsx
import React, { useState, useEffect } from 'react';
import { ModusWcLoader } from '@trimble-oss/moduswebcomponents-react';

// LoadingState component - shows different loader variants based on loading state
const LoadingState: React.FC = () => {
  const [loadingState, setLoadingState] = useState<'initial' | 'loading' | 'processing' | 'success' | 'error'>('initial');
  const [progress, setProgress] = useState(0);
  
  // Simulate a loading sequence
  useEffect(() => {
    if (loadingState === 'initial') {
      return;
    }
    
    let timer: NodeJS.Timeout;
    
    if (loadingState === 'loading' && progress < 100) {
      timer = setTimeout(() => {
        const nextProgress = progress + 10;
        setProgress(nextProgress);
        
        if (nextProgress >= 100) {
          setLoadingState('processing');
          setProgress(0);
        }
      }, 500);
    } else if (loadingState === 'processing' && progress < 100) {
      timer = setTimeout(() => {
        const nextProgress = progress + 20;
        setProgress(nextProgress);
        
        if (nextProgress >= 100) {
          // 80% chance of success, 20% chance of error
          setLoadingState(Math.random() < 0.8 ? 'success' : 'error');
        }
      }, 300);
    }
    
    return () => {
      if (timer) clearTimeout(timer);
    };
  }, [loadingState, progress]);
  
  const startLoading = () => {
    setLoadingState('loading');
    setProgress(0);
  };
  
  const resetLoading = () => {
    setLoadingState('initial');
    setProgress(0);
  };
  
  // Map loading states to loader variants and colors
  const getLoaderProps = () => {
    switch (loadingState) {
      case 'loading':
        return { variant: 'spinner', color: 'primary', ariaLabel: 'Loading data' };
      case 'processing':
        return { variant: 'bars', color: 'info', ariaLabel: 'Processing data' };
      case 'success':
        return { variant: 'infinity', color: 'success', ariaLabel: 'Processing complete' };
      case 'error':
        return { variant: 'ring', color: 'error', ariaLabel: 'Error occurred' };
      default:
        return { variant: 'spinner', color: 'primary', ariaLabel: 'Loading' };
    }
  };
  
  const { variant, color, ariaLabel } = getLoaderProps() as {
    variant: "spinner" | "ball" | "bars" | "dots" | "infinity" | "ring";
    color: "primary" | "secondary" | "accent" | "neutral" | "info" | "success" | "warning" | "error";
    ariaLabel: string;
  };
  
  return (
    <div className="loading-demo">
      <h2>Loading States</h2>
      
      {loadingState === 'initial' ? (
        <button onClick={startLoading} className="start-button">
          Start Loading
        </button>
      ) : (
        <div className="loading-container">
          <ModusWcLoader
            variant={variant}
            color={color}
            size="md"
            aria-label={ariaLabel}
          />
          
          <div className="loading-status">
            <p>
              {loadingState === 'loading' && 'Loading data...'}
              {loadingState === 'processing' && 'Processing data...'}
              {loadingState === 'success' && 'Processing complete!'}
              {loadingState === 'error' && 'Error processing data.'}
            </p>
            
            {(loadingState === 'loading' || loadingState === 'processing') && (
              <div className="progress-bar">
                <div 
                  className="progress-fill" 
                  style={{ width: `${progress}%` }}
                ></div>
              </div>
            )}
            
            {(loadingState === 'success' || loadingState === 'error') && (
              <button onClick={resetLoading} className="reset-button">
                Reset
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

// Page component using loader for different sections
interface PageLoaderProps {
  isLoading: boolean;
  variant?: "spinner" | "ball" | "bars" | "dots" | "infinity" | "ring";
  size?: "xs" | "sm" | "md" | "lg";
  color?: "primary" | "secondary" | "accent" | "neutral" | "info" | "success" | "warning" | "error";
  children: React.ReactNode;
}

const PageLoader: React.FC<PageLoaderProps> = ({
  isLoading,
  variant = "spinner",
  size = "md",
  color = "primary",
  children
}) => {
  return (
    <div className="page-section">
      {isLoading ? (
        <div className="section-loader">
          <ModusWcLoader
            variant={variant}
            color={color}
            size={size}
            aria-label="Loading section content"
          />
        </div>
      ) : (
        children
      )}
    </div>
  );
};

// Example page with multiple loading sections
const LoaderDemo: React.FC = () => {
  const [loadingStates, setLoadingStates] = useState({
    header: true,
    content: true,
    sidebar: true,
    footer: true
  });
  
  // Simulate staggered loading of different page sections
  useEffect(() => {
    const timers: NodeJS.Timeout[] = [];
    
    timers.push(setTimeout(() => {
      setLoadingStates(prev => ({ ...prev, header: false }));
    }, 1000));
    
    timers.push(setTimeout(() => {
      setLoadingStates(prev => ({ ...prev, sidebar: false }));
    }, 2000));
    
    timers.push(setTimeout(() => {
      setLoadingStates(prev => ({ ...prev, content: false }));
    }, 3000));
    
    timers.push(setTimeout(() => {
      setLoadingStates(prev => ({ ...prev, footer: false }));
    }, 3500));
    
    return () => {
      timers.forEach(timer => clearTimeout(timer));
    };
  }, []);
  
  return (
    <div className="page-container">
      <style>{`
        .page-container {
          display: grid;
          grid-template-areas:
            "header header"
            "sidebar content"
            "footer footer";
          grid-template-rows: auto 1fr auto;
          grid-template-columns: 250px 1fr;
          min-height: 500px;
          gap: 16px;
        }
        
        .page-section {
          background-color: #f8f9fa;
          padding: 16px;
          border-radius: 4px;
          min-height: 100px;
          position: relative;
        }
        
        .section-header { grid-area: header; }
        .section-sidebar { grid-area: sidebar; }
        .section-content { grid-area: content; }
        .section-footer { grid-area: footer; }
        
        .section-loader {
          display: flex;
          justify-content: center;
          align-items: center;
          width: 100%;
          height: 100%;
          min-height: inherit;
        }
      `}</style>
      
      <PageLoader 
        isLoading={loadingStates.header} 
        variant="spinner" 
        color="primary"
        size="md"
      >
        <div className="section-header">
          <h1>Page Header</h1>
        </div>
      </PageLoader>
      
      <PageLoader 
        isLoading={loadingStates.sidebar} 
        variant="dots" 
        color="secondary"
        size="sm"
      >
        <div className="section-sidebar">
          <h2>Sidebar Navigation</h2>
          <ul>
            <li>Home</li>
            <li>Products</li>
            <li>About</li>
            <li>Contact</li>
          </ul>
        </div>
      </PageLoader>
      
      <PageLoader 
        isLoading={loadingStates.content} 
        variant="bars" 
        color="info"
        size="lg"
      >
        <div className="section-content">
          <h2>Main Content</h2>
          <p>This is the main content area of the page.</p>
          <p>Content is loaded after the header and sidebar.</p>
        </div>
      </PageLoader>
      
      <PageLoader 
        isLoading={loadingStates.footer} 
        variant="infinity" 
        color="neutral"
        size="sm"
      >
        <div className="section-footer">
          <p>Page Footer © 2023</p>
        </div>
      </PageLoader>
    </div>
  );
};

export default LoaderDemo;
```

**Notes:**
- Always include an `aria-label` attribute for accessibility, as loaders are often used for important UI state changes
- Choose the appropriate loader variant based on the context and loading duration
- Use consistent loader types and colors throughout your application for a cohesive design
- For long-running operations, consider showing progress indicators alongside loaders
- Loaders should be placed in a way that doesn't disrupt the user experience or cause layout shifts
- For full-page loading, center the loader in the viewport and consider a semi-transparent overlay

---

# ModusWcMenu 

## Prompt 1
**User Question:** How do I create a simple vertical navigation menu with selection handling in React using the Modus Menu components?

**Agent Answer:**
References:
- **Properties (Menu)**:
  - `bordered`: boolean - Indicates if the menu should have a border
  - `customClass`: string - Custom CSS class to apply to the ul element
  - `orientation`: 'horizontal' | 'vertical' - The orientation of the menu (default: 'vertical')
  - `size`: 'sm' | 'md' | 'lg' - The size of the menu (default: 'md')

- **Properties (MenuItem)**:
  - `bordered`: boolean - Indicates if the menu item should have a border
  - `customClass`: string - Custom CSS class to apply to the li element
  - `disabled`: boolean - The disabled state of the menu item
  - `focused`: boolean - The focused state of the menu item
  - `label`: string - The text rendered in the menu item
  - `selected`: boolean - The selected state of the menu item
  - `size`: 'sm' | 'md' | 'lg' - The size of the menu item
  - `startIcon`: string - The Modus icon name to render at the start of the menu item
  - `subLabel`: string - The text rendered beneath the label
  - `value`: string - The unique identifying value of the menu item

- **Events (MenuItem)**:
  - `itemSelect`: CustomEvent<{ value: string }> - Event emitted when a menu item is selected

- **Usage Patterns**:
  - Menu component serves as a container for MenuItem components
  - Both vertical and horizontal orientation supported
  - Can handle item selection with the itemSelect event
  - Supports customization with icons, sub-labels and different sizes

**TypeScript Example:**
```tsx
import React, { useRef, useEffect, useState } from 'react';
import { ModusWcMenu, ModusWcMenuItem } from '@trimble-oss/moduswebcomponents-react';

interface MenuItem {
  label: string;
  value: string;
  icon?: string;
  subLabel?: string;
  disabled?: boolean;
}

const NavigationMenu: React.FC = () => {
  const [selectedItem, setSelectedItem] = useState<string>('home');
  
  // Menu items data
  const menuItems: MenuItem[] = [
    { label: 'Home', value: 'home', icon: 'home' },
    { label: 'Dashboard', value: 'dashboard', icon: 'dashboard' },
    { label: 'Analytics', value: 'analytics', icon: 'bar_chart', subLabel: 'View detailed statistics' },
    { label: 'Settings', value: 'settings', icon: 'settings', disabled: true },
  ];
  
  // Setup refs for event handling
  const menuItemRefs = useRef<(HTMLModusWcMenuItemElement | null)[]>([]);
  
  useEffect(() => {
    // Attach event listeners to menu items
    menuItemRefs.current.forEach((item, index) => {
      if (item) {
        const handleSelect = (e: CustomEvent<{ value: string }>) => {
          setSelectedItem(e.detail.value);
          console.log('Selected item:', e.detail.value);
        };
        
        item.addEventListener('itemSelect', handleSelect as EventListener);
        
        return () => {
          item.removeEventListener('itemSelect', handleSelect as EventListener);
        };
      }
    });
  }, []);
  
  return (
    <ModusWcMenu aria-label="Main Navigation" orientation="vertical" size="md">
      {menuItems.map((item, index) => (
        <ModusWcMenuItem
          key={item.value}
          ref={el => menuItemRefs.current[index] = el}
          label={item.label}
          value={item.value}
          startIcon={item.icon}
          subLabel={item.subLabel}
          disabled={item.disabled}
          selected={selectedItem === item.value}
        />
      ))}
    </ModusWcMenu>
  );
};

export default NavigationMenu;
```

**Notes:**
- Always provide a unique `value` for each MenuItem to properly track selection state
- Use the `itemSelect` event to handle user interactions
- You need to maintain the selected state manually in your React component
- Menu items can be customized with icons, sub-labels, and different sizes
- Use `aria-label` on the menu for better accessibility

## Prompt 2
**User Question:** How can I create a custom dropdown menu with the Modus Menu components that integrates with a button trigger?

**Agent Answer:**
References:
- **Properties (Menu)**:
  - `bordered`: boolean - Adds border to the menu
  - `customClass`: string - Custom CSS class for styling
  - `orientation`: 'horizontal' | 'vertical' - Menu layout direction
  - `size`: 'sm' | 'md' | 'lg' - Size variant of the menu

- **Properties (MenuItem)**:
  - `label`: string - Text content of the menu item
  - `value`: string - Unique identifier for the item
  - `startIcon`: string - Icon name from Modus icon library
  - `disabled`: boolean - Disables interaction with the menu item
  - `selected`: boolean - Visually indicates selected state
  - `subLabel`: string - Supplementary text below the main label

- **Events (MenuItem)**:
  - `itemSelect`: CustomEvent<{ value: string }> - Fires when an item is selected

- **Usage Patterns**:
  - Combining with buttons to create dropdown menus
  - Using with portals or popovers for proper positioning
  - Managing visibility state and click outside handling
  - Creating nested or cascading menu structures

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcButton, ModusWcMenu, ModusWcMenuItem, ModusWcIcon } from '@trimble-oss/moduswebcomponents-react';

interface DropdownMenuItem {
  label: string;
  value: string;
  icon: string;
  disabled?: boolean;
}

const DropdownMenu: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const buttonRef = useRef<HTMLModusWcButtonElement>(null);
  const menuItems = useRef<(HTMLModusWcMenuItemElement | null)[]>([]);
  
  // Menu items data
  const items: DropdownMenuItem[] = [
    { label: 'Edit', value: 'edit', icon: 'edit' },
    { label: 'Duplicate', value: 'duplicate', icon: 'content_copy' },
    { label: 'Delete', value: 'delete', icon: 'delete' },
    { label: 'Share', value: 'share', icon: 'share', disabled: true }
  ];
  
  // Toggle dropdown visibility
  const toggleDropdown = () => {
    setIsOpen(!isOpen);
  };
  
  // Handle item selection
  useEffect(() => {
    const handleItemSelect = (e: CustomEvent<{ value: string }>) => {
      console.log('Selected action:', e.detail.value);
      
      // Perform action based on selection
      switch(e.detail.value) {
        case 'edit':
          console.log('Edit item');
          break;
        case 'duplicate':
          console.log('Duplicate item');
          break;
        case 'delete':
          console.log('Delete item');
          break;
        default:
          break;
      }
      
      // Close the dropdown after selection
      setIsOpen(false);
    };
    
    // Add event listeners to menu items
    menuItems.current.forEach(item => {
      if (item) {
        item.addEventListener('itemSelect', handleItemSelect as EventListener);
      }
    });
    
    // Cleanup event listeners
    return () => {
      menuItems.current.forEach(item => {
        if (item) {
          item.removeEventListener('itemSelect', handleItemSelect as EventListener);
        }
      });
    };
  }, []);
  
  // Handle click outside to close dropdown
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        dropdownRef.current && 
        !dropdownRef.current.contains(event.target as Node) && 
        buttonRef.current && 
        !buttonRef.current.contains(event.target as Node)
      ) {
        setIsOpen(false);
      }
    };
    
    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);
  
  // Position the dropdown below the button
  useEffect(() => {
    if (isOpen && buttonRef.current && dropdownRef.current) {
      const buttonRect = buttonRef.current.getBoundingClientRect();
      dropdownRef.current.style.top = `${buttonRect.bottom}px`;
      dropdownRef.current.style.left = `${buttonRect.left}px`;
    }
  }, [isOpen]);
  
  return (
    <div style={{ position: 'relative' }}>
      <ModusWcButton 
        ref={buttonRef}
        onClick={toggleDropdown}
        aria-haspopup="true"
        aria-expanded={isOpen ? 'true' : 'false'}>
        Actions
        <ModusWcIcon name={isOpen ? "chevron_up" : "chevron_down"}></ModusWcIcon>
      </ModusWcButton>
      
      {isOpen && (
        <div 
          ref={dropdownRef} 
          style={{
            position: 'absolute',
            zIndex: 1000,
            boxShadow: '0 4px 8px rgba(0,0,0,0.1)',
            background: 'white',
            borderRadius: '4px',
            marginTop: '4px'
          }}>
          <ModusWcMenu bordered size="md">
            {items.map((item, index) => (
              <ModusWcMenuItem
                key={item.value}
                ref={el => menuItems.current[index] = el}
                label={item.label}
                value={item.value}
                startIcon={item.icon}
                disabled={item.disabled}
              />
            ))}
          </ModusWcMenu>
        </div>
      )}
    </div>
  );
};

export default DropdownMenu;
```

**Notes:**
- The dropdown implementation requires manual positioning and visibility management
- Remember to handle keyboard navigation and accessibility for the dropdown menu
- Use `aria-haspopup` and `aria-expanded` attributes for accessibility
- Add click-outside detection to close the menu when clicking elsewhere
- Consider using a portal (React.createPortal) for more complex positioning requirements
- For nested/cascading menus, you'll need to implement additional hover detection

---

# ModusWcMenuItem

## Prompt 1
**User Question:** How do I create a menu item with an icon and sublabel, and handle its selection event in React?

**Agent Answer:**
References:
- **Properties**:
  - `bordered`: boolean - Indicates if the menu item should have a border
  - `customClass`: string - Custom CSS class for styling
  - `disabled`: boolean - The disabled state of the menu item
  - `focused`: boolean - The focused state of the menu item
  - `label`: string - The text rendered in the menu item
  - `selected`: boolean - The selected state of the menu item
  - `size`: 'sm' | 'md' | 'lg' - The size of the menu item
  - `startIcon`: string - The Modus icon name to render at the start of the menu item
  - `subLabel`: string - The text rendered beneath the label
  - `value`: string - The unique identifying value of the menu item

- **Events**:
  - `itemSelect`: CustomEvent<{ value: string }> - Event emitted when a menu item is selected

- **Usage Patterns**:
  - Menu items should be used within a ModusWcMenu component
  - Add icons to make menu items more visually distinctive
  - Use subLabels to provide additional context
  - Handle item selection via event listeners

**TypeScript Example:**
```tsx
import React, { useRef, useEffect } from 'react';
import { ModusWcMenu, ModusWcMenuItem } from '@trimble-oss/moduswebcomponents-react';

const ProfileMenuItem: React.FC = () => {
  const menuItemRef = useRef<HTMLModusWcMenuItemElement>(null);
  
  useEffect(() => {
    const menuItem = menuItemRef.current;
    
    if (menuItem) {
      const handleSelect = (e: CustomEvent<{ value: string }>) => {
        console.log('Selected item:', e.detail.value);
        // Navigate to profile page or open modal
        if (e.detail.value === 'profile') {
          // Example: navigate or perform action
          console.log('Navigating to profile page');
        }
      };
      
      menuItem.addEventListener('itemSelect', handleSelect as EventListener);
      
      return () => {
        menuItem.removeEventListener('itemSelect', handleSelect as EventListener);
      };
    }
  }, []);
  
  return (
    <ModusWcMenu aria-label="Settings Menu">
      <ModusWcMenuItem
        ref={menuItemRef}
        label="User Profile"
        subLabel="Update your personal information"
        value="profile"
        startIcon="person"
      />
    </ModusWcMenu>
  );
};

export default ProfileMenuItem;
```

**Notes:**
- The `value` property is important for identifying which item was selected
- Use the `startIcon` property to display an icon from the Modus icon library
- The `subLabel` property adds a secondary line of text below the primary label
- Remember to properly clean up event listeners in your React components


---

# ModusWcModal

## Prompt 1
**User Question:** How do I create a basic modal dialog with header, content, and footer in React using the Modus Modal component?

**Agent Answer:**
References:
- **Properties**:
  - `backdrop`: 'default' | 'static' - Backdrop behavior (static doesn't close on outside click)
  - `customClass`: string - Custom CSS class to apply
  - `fullscreen`: boolean - Whether the modal should be displayed full-screen
  - `modalId`: string - Required ID for the inner dialog element
  - `position`: 'bottom' | 'center' | 'top' - Vertical position of the modal
  - `showClose`: boolean - Whether to show the close icon button (default: true)
  - `showFullscreenToggle`: boolean - Whether to show fullscreen toggle button (default: false)

- **Events**:
  - The component uses native HTML dialog element events
  - No custom events specific to this component

- **Usage Patterns**:
  - Modal content is organized using slots: "header", "content", and "footer"
  - Uses the native dialog element's showModal() and close() methods
  - Can be customized with different positions and backdrop behaviors

**TypeScript Example:**
```tsx
import React, { useRef } from 'react';
import { ModusWcModal, ModusWcButton } from '@trimble-oss/moduswebcomponents-react';

const BasicModal: React.FC = () => {
  // Generate a unique ID for the modal
  const modalId = 'modal-' + Math.random().toString(36).substring(2, 9);
  const dialogRef = useRef<HTMLDialogElement | null>(null);
  
  const openModal = () => {
    // Access the native dialog element through DOM and call showModal()
    const modal = document.getElementById(modalId) as HTMLDialogElement;
    if (modal) {
      modal.showModal();
    }
  };
  
  const closeModal = () => {
    // Access the native dialog element through DOM and call close()
    const modal = document.getElementById(modalId) as HTMLDialogElement;
    if (modal) {
      modal.close();
    }
  };
  
  const handleConfirm = () => {
    // Perform confirm action here
    console.log('Confirmed!');
    closeModal();
  };
  
  return (
    <>
      <ModusWcButton onClick={openModal}>Open Modal</ModusWcButton>
      
      <ModusWcModal
        aria-label="Example Modal"
        modalId={modalId}
        backdrop="default"
        position="center"
        showClose={true}>
        <div slot="header">Modal Title</div>
        <div slot="content">
          <p>This is the modal content. You can put any React content here.</p>
          <p>Multiple paragraphs or complex content is supported.</p>
        </div>
        <div slot="footer" style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
          <ModusWcButton color="secondary" onClick={closeModal}>
            Cancel
          </ModusWcButton>
          <ModusWcButton color="primary" onClick={handleConfirm}>
            Confirm
          </ModusWcButton>
        </div>
      </ModusWcModal>
    </>
  );
};

export default BasicModal;
```

**Notes:**
- The `modalId` property is required for accessing the dialog element via DOM
- Use slots ("header", "content", "footer") to organize modal content
- Modal behavior relies on the native HTML dialog element methods: `showModal()` and `close()`
- The component doesn't manage its own state; you need to control when to open/close it
- Use `backdrop="static"` to prevent closing when clicking outside the modal
- For accessibility, always provide an aria-label attribute

## Prompt 2
**User Question:** How can I create a reusable confirmation modal component in React that can be triggered from different parts of my application?

**Agent Answer:**
References:
- **Properties**:
  - `modalId`: string - Required identifier for the modal dialog
  - `backdrop`: 'default' | 'static' - Controls if clicking backdrop closes modal
  - `position`: 'bottom' | 'center' | 'top' - Vertical positioning
  - `customClass`: string - For custom styling
  - `fullscreen`: boolean - For full-screen modal display
  - `showClose`: boolean - Controls visibility of close button
  - `showFullscreenToggle`: boolean - Controls visibility of fullscreen toggle

- **Events**:
  - Uses native dialog element events (no custom events)

- **Usage Patterns**:
  - Creating reusable modal components with React Context
  - Implementing modal service patterns for application-wide access
  - Managing modal stacks for multiple concurrent modals

**TypeScript Example:**
```tsx
import React, { createContext, useContext, useState, ReactNode } from 'react';
import { ModusWcModal, ModusWcButton } from '@trimble-oss/moduswebcomponents-react';

// Types for our confirmation dialog
interface ConfirmationDialogProps {
  title: string;
  message: string;
  confirmLabel?: string;
  cancelLabel?: string;
  onConfirm: () => void;
  onCancel?: () => void;
}

// Context for our modal service
interface ModalContextType {
  showConfirmation: (props: ConfirmationDialogProps) => void;
}

const ModalContext = createContext<ModalContextType | undefined>(undefined);

// Provider component that will wrap our app
export const ModalProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const modalId = 'confirmation-modal';
  const [dialogProps, setDialogProps] = useState<ConfirmationDialogProps | null>(null);
  
  // Method to show the confirmation dialog
  const showConfirmation = (props: ConfirmationDialogProps) => {
    setDialogProps(props);
    
    // Use setTimeout to ensure DOM is updated before showing modal
    setTimeout(() => {
      const modal = document.getElementById(modalId) as HTMLDialogElement;
      if (modal) {
        modal.showModal();
      }
    }, 0);
  };
  
  // Method to close the modal
  const closeModal = () => {
    const modal = document.getElementById(modalId) as HTMLDialogElement;
    if (modal) {
      modal.close();
    }
  };
  
  // Handle confirm action
  const handleConfirm = () => {
    if (dialogProps?.onConfirm) {
      dialogProps.onConfirm();
    }
    closeModal();
  };
  
  // Handle cancel action
  const handleCancel = () => {
    if (dialogProps?.onCancel) {
      dialogProps.onCancel();
    }
    closeModal();
  };
  
  return (
    <ModalContext.Provider value={{ showConfirmation }}>
      {children}
      
      {/* The actual modal component */}
      {dialogProps && (
        <ModusWcModal
          aria-label={dialogProps.title}
          modalId={modalId}
          backdrop="static"
          position="center"
          showClose={false}>
          <div slot="header">{dialogProps.title}</div>
          <div slot="content">
            <p>{dialogProps.message}</p>
          </div>
          <div slot="footer" style={{ display: 'flex', justifyContent: 'flex-end', gap: '8px' }}>
            <ModusWcButton color="secondary" onClick={handleCancel}>
              {dialogProps.cancelLabel || 'Cancel'}
            </ModusWcButton>
            <ModusWcButton color="primary" onClick={handleConfirm}>
              {dialogProps.confirmLabel || 'Confirm'}
            </ModusWcButton>
          </div>
        </ModusWcModal>
      )}
    </ModalContext.Provider>
  );
};

// Custom hook to use the modal service
export const useModal = (): ModalContextType => {
  const context = useContext(ModalContext);
  if (!context) {
    throw new Error('useModal must be used within a ModalProvider');
  }
  return context;
};

// Example usage in a component:
const DeleteButton: React.FC<{ itemId: string }> = ({ itemId }) => {
  const { showConfirmation } = useModal();
  
  const handleDelete = () => {
    console.log(`Deleting item ${itemId}`);
    // API call to delete the item
  };
  
  const confirmDelete = () => {
    showConfirmation({
      title: 'Delete Item',
      message: 'Are you sure you want to delete this item? This action cannot be undone.',
      confirmLabel: 'Delete',
      onConfirm: handleDelete,
      // Optional cancel handler
      onCancel: () => console.log('Deletion cancelled')
    });
  };
  
  return (
    <ModusWcButton color="danger" onClick={confirmDelete}>
      Delete Item
    </ModusWcButton>
  );
};
```

**Notes:**
- This pattern creates a reusable modal service using React Context
- The ModalProvider should be placed near the root of your component tree
- Using `backdrop="static"` prevents accidental dismissal of important confirmations
- The context API allows any component to trigger the modal without prop drilling
- You can extend this pattern to support different types of modals (alert, form, etc.)
- For complex forms in modals, consider state management solutions like Formik or React Hook Form
- Always implement keyboard navigation (Escape to close, Enter to confirm) for accessibility

---

# ModusWcNavbar

## Prompt 1
**User Question:** How do I implement a basic Modus Navbar in my React application with user profile and customized menu options?

**Agent Answer:**
References:

**⚡ Important Rule:** Always use `modus-classic-light` and `modus-classic-dark` as defaults unless the user specifically requests compact themes. Classic themes provide the best UX for most applications.


- **Properties**:
  - `userCard`: INavbarUserCard - User information (name, email, avatar)
  - `visibility`: INavbarVisibility - Controls visibility of navbar elements
  - `textOverrides`: INavbarTextOverrides - Custom text for navbar elements
  - `condensed`: boolean - Applies condensed layout and styling
  - `mainMenuOpen`, `userMenuOpen`, etc. - Control the open state of different menus
  - `customClass`: string - Custom CSS class for styling

- **Events**:
  - `trimbleLogoClick`: CustomEvent - When logo is clicked
  - `mainMenuOpenChange`: CustomEvent<boolean> - When main menu state changes
  - `userMenuOpenChange`: CustomEvent<boolean> - When user menu state changes
  - `searchChange`: CustomEvent<{ value: string }> - When search input changes
  - `signOutClick`: CustomEvent - When sign out is clicked
  - Various other events for different navbar elements

- **Usage Patterns**:
  - Configuring user profile information
  - Controlling visibility of individual navbar elements
  - Handling menu state changes
  - Customizing menu content via slots

**TypeScript Example:**
```tsx
import React, { useRef, useEffect, useState } from 'react';
import { 
  ModusWcNavbar, 
  ModusWcThemeSwitcher 
} from '@trimble-oss/moduswebcomponents-react';

// Interface definitions for better TypeScript support
interface INavbarUserCard {
  avatarAlt?: string;
  avatarSrc?: string;
  email: string;
  name: string;
  myTrimbleButton?: string;
  signOutButton?: string;
}

interface INavbarVisibility {
  ai?: boolean;
  apps?: boolean;
  help?: boolean;
  mainMenu?: boolean;
  notifications?: boolean;
  search?: boolean;
  searchInput?: boolean;
  user?: boolean;
}

const MyComponent: React.FC = () => {
  // Component references for event handling
  const navbarRef = useRef<HTMLModusWcNavbarElement>(null);
  
  // State management
  const [searchValue, setSearchValue] = useState<string>('');
  const [currentTheme, setCurrentTheme] = useState<'modus-classic-light' | 'modus-classic-dark'>('modus-classic-light');
  
  // User information
  const userCard: INavbarUserCard = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    avatarSrc: 'https://modus.trimble.com/img/trimble-logo.svg',
    avatarAlt: 'John Doe'
  };
  
  // Visibility configuration - Updated to include theme switcher
  const visibility: INavbarVisibility = {
    mainMenu: true,
    notifications: true,
    search: true,
    apps: true,
    help: true,
    user: true
  };
  
  // Text overrides for localization or customization
  const textOverrides = {
    help: 'Support',
    notifications: 'Alerts',
    apps: 'Theme'
  };
  
  // Theme handling function
  const toggleTheme = () => {
    const newTheme = currentTheme === 'modus-classic-light' 
      ? 'modus-classic-dark' 
      : 'modus-classic-light';
    
    setCurrentTheme(newTheme);
    
    // Apply theme to HTML element following Modus guidelines
    document.documentElement.setAttribute('data-theme', newTheme);
    document.documentElement.setAttribute('data-mode', newTheme.includes('dark') ? 'dark' : 'light');
    document.documentElement.className = newTheme.includes('dark') ? 'dark' : 'light';
    
    console.log(`Theme switched to: ${newTheme}`);
  };

  // Event handlers
  useEffect(() => {
    const navbar = navbarRef.current;
    
    // Initialize theme on component mount
    document.documentElement.setAttribute('data-theme', currentTheme);
    document.documentElement.setAttribute('data-mode', 'light');
    document.documentElement.className = 'light';
    
    if (navbar) {
      // Handle search input changes
      const handleSearchChange = (e: CustomEvent<{ value: string }>) => {
        setSearchValue(e.detail.value);
        console.log('Search value:', e.detail.value);
      };
      
      // Handle sign out clicks
      const handleSignOut = () => {
        console.log('User clicked sign out');
        // Implement sign out logic
      };
      
      // Add event listeners
      navbar.addEventListener('searchChange', handleSearchChange as EventListener);
      navbar.addEventListener('signOutClick', handleSignOut);
      
      // Clean up event listeners
      return () => {
        navbar.removeEventListener('searchChange', handleSearchChange as EventListener);
        navbar.removeEventListener('signOutClick', handleSignOut);
      };
    }
  }, [currentTheme]);

  return (
    <ModusWcNavbar
      ref={navbarRef}
      userCard={userCard}
      visibility={visibility}
      textOverrides={textOverrides}
    >
      <div slot="main-menu" style={{padding: '1rem'}}>
        <h3>Main Menu</h3>
        <ul>
          <li>Dashboard</li>
          <li>Projects</li>
          <li>Reports</li>
          <li>Settings</li>
        </ul>
      </div>
      
      {/* Theme Switcher in Apps slot */}
      <div slot="apps" style={{padding: '1rem'}}>
        <h4>🎨 Theme Settings</h4>
        <p>Current: {currentTheme.includes('dark') ? '🌙 Dark' : '☀️ Light'} Theme</p>
        <ModusWcThemeSwitcher 
          aria-label="Toggle theme between light and dark"
          onClick={toggleTheme}
        />
        <p style={{fontSize: '12px', marginTop: '8px'}}>
          Switch between Classic Light and Dark themes
        </p>
      </div>
      
      {/* Notifications menu content */}
      <div slot="notifications">
        <div style={{padding: '0.5rem 1rem'}}>
          <h4 style={{margin: '0.5rem 0'}}>🔔 New message</h4>
          <p style={{margin: '0.5rem 0'}}>You have a new message from Admin</p>
        </div>
        <div style={{padding: '0.5rem 1rem', borderTop: '1px solid #eee'}}>
          <h4 style={{margin: '0.5rem 0'}}>🔧 System update</h4>
          <p style={{margin: '0.5rem 0'}}>System maintenance scheduled for tomorrow</p>
        </div>
      </div>
    </ModusWcNavbar>
  );
};

export default MyComponent;
```

**Notes:**
- The `userCard` property is required to display user information in the menu
- Use the `visibility` property to control which elements appear in the navbar
- Customize menu content using the available slots: "main-menu", "notifications", "apps"
- Remember to add event listeners for interactive elements and clean them up properly
- For React applications, you may need to manipulate the DOM directly to access the navbar's methods

## Prompt 2
**User Question:** How can I create a responsive Modus Navbar with a condensed mobile view and custom search functionality?

**Agent Answer:**
References:
- **Properties**:
  - `condensed`: boolean - Enables the condensed mobile view
  - `condensedMenuOpen`: boolean - Controls the open state of condensed menu
  - `searchInputOpen`: boolean - Controls visibility of search input
  - `searchDebounceMs`: number - Debounce time for search input (default: 300ms)
  - `visibility`: INavbarVisibility - Control which elements are visible

- **Events**:
  - `searchChange`: CustomEvent<{ value: string }> - Triggered when search input changes
  - `searchClick`: CustomEvent - When search button is clicked
  - `searchInputOpenChange`: CustomEvent<boolean> - When search input visibility changes
  - `condensedMenuOpenChange`: CustomEvent<boolean> - When condensed menu state changes

- **Usage Patterns**:
  - Implementing responsive behavior based on screen size
  - Custom search functionality with debounce
  - Managing condensed menu for mobile views

**TypeScript Example:**
```tsx
import React, { useRef, useEffect, useState } from 'react';
import { ModusWcNavbar } from '@trimble-oss/moduswebcomponents-react';

interface SearchResult {
  id: string;
  title: string;
  url: string;
}

const ResponsiveNavbar: React.FC = () => {
  // State for responsive behavior
  const [isCondensed, setIsCondensed] = useState<boolean>(window.innerWidth < 768);
  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);
  const [isSearching, setIsSearching] = useState<boolean>(false);
  
  // Ref for event handling
  const navbarRef = useRef<HTMLModusWcNavbarElement>(null);
  
  // User information
  const userCard = {
    name: 'Jane Smith',
    email: 'jane.smith@example.com',
    avatarSrc: 'https://i.pravatar.cc/150?img=23',
    avatarAlt: 'Jane Smith'
  };
  
  // Handle window resize for responsive behavior
  useEffect(() => {
    const handleResize = () => {
      setIsCondensed(window.innerWidth < 768);
    };
    
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);
  
  // Handle navbar events
  useEffect(() => {
    const navbar = navbarRef.current;
    if (navbar) {
      // Mock search functionality
      const handleSearch = async (e: CustomEvent<{ value: string }>) => {
        const searchTerm = e.detail.value;
        if (searchTerm.length > 2) {
          setIsSearching(true);
          
          try {
            // Simulate API call with timeout
            setTimeout(() => {
              // Mock search results
              const results: SearchResult[] = [
                { id: '1', title: `Result for "${searchTerm}" - Item 1`, url: '#1' },
                { id: '2', title: `Result for "${searchTerm}" - Item 2`, url: '#2' },
                { id: '3', title: `Result for "${searchTerm}" - Item 3`, url: '#3' }
              ];
              setSearchResults(results);
              setIsSearching(false);
            }, 500);
          } catch (error) {
            console.error('Search error:', error);
            setIsSearching(false);
          }
        } else {
          setSearchResults([]);
        }
      };
      
      // Listen for search changes
      navbar.addEventListener('searchChange', handleSearch as EventListener);
      
      // Clean up event listeners
      return () => {
        navbar.removeEventListener('searchChange', handleSearch as EventListener);
      };
    }
  }, []);
  
  // Render search results beneath the navbar
  const renderSearchResults = () => {
    if (searchResults.length === 0) {
      return null;
    }
    
    return (
      <div style={{
        position: 'absolute',
        top: '60px',
        right: isCondensed ? '0' : '200px',
        width: isCondensed ? '100%' : '400px',
        background: 'white',
        boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
        zIndex: 100
      }}>
        {isSearching ? (
          <div style={{ padding: '1rem', textAlign: 'center' }}>Searching...</div>
        ) : (
          <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
            {searchResults.map(result => (
              <li key={result.id} style={{ padding: '0.75rem 1rem', borderBottom: '1px solid #eee' }}>
                <a href={result.url} style={{ textDecoration: 'none', color: '#0063a3' }}>
                  {result.title}
                </a>
              </li>
            ))}
          </ul>
        )}
      </div>
    );
  };
  
  return (
    <>
      <ModusWcNavbar
        ref={navbarRef}
        condensed={isCondensed}
        userCard={userCard}
        searchDebounceMs={400}
        visibility={{
          mainMenu: true,
          search: true,
          searchInput: true,
          notifications: true,
          user: true,
          help: true
        }}>
        {/* Main menu content for both condensed and regular views */}
        <div slot="main-menu" style={{
          backgroundColor: '#0063a3',
          color: 'white',
          padding: '1rem',
          minHeight: isCondensed ? '300px' : '250px'
        }}>
          <h3>Navigation</h3>
          <ul style={{ listStyleType: 'none', padding: 0 }}>
            <li style={{ padding: '0.5rem 0' }}>Home</li>
            <li style={{ padding: '0.5rem 0' }}>Dashboard</li>
            <li style={{ padding: '0.5rem 0' }}>Projects</li>
            <li style={{ padding: '0.5rem 0' }}>Reports</li>
            <li style={{ padding: '0.5rem 0' }}>Settings</li>
          </ul>
        </div>
        
        {/* Notifications panel */}
        <div slot="notifications">
          <div style={{ padding: '1rem', textAlign: 'center' }}>
            <p>You have no new notifications</p>
          </div>
        </div>
      </ModusWcNavbar>
      
      {/* Search results panel */}
      {renderSearchResults()}
    </>
  );
};

export default ResponsiveNavbar;
```

**Notes:**
- Set the `condensed` property based on screen width for responsive behavior
- Use `searchDebounceMs` to control the frequency of search event triggers
- Create a custom search results UI positioned below the navbar
- For mobile views, the navbar automatically adapts its layout when in condensed mode
- Remember to handle the open/close state of menus differently in condensed vs. regular mode
- In condensed mode, menus appear as fullscreen overlays rather than dropdown menus
- Always ensure your responsive design works well at all breakpoints

---

# ModusWcNumberInput

## Prompt 1
**User Question:** How do I create a basic number input field with validation constraints in React using the Modus Number Input component?

**Agent Answer:**
References:
- **Properties**:
  - `value`: string - The current value of the input
  - `min`: number - The minimum allowed value
  - `max`: number - The maximum allowed value
  - `step`: number - Increment/decrement step value
  - `type`: 'number' | 'range' - Input type
  - `inputMode`: 'numeric' | 'decimal' | 'none' - Hints for virtual keyboard (default: 'numeric')
  - `required`: boolean - Whether the input is required
  - `disabled`: boolean - Whether the input is disabled
  - `readOnly`: boolean - Whether the value is editable
  - `size`: 'sm' | 'md' | 'lg' - Size of the input (default: 'md')
  - `label`: string - Text label for the input
  - `placeholder`: string - Placeholder text
  - `currencySymbol`: string - Currency symbol to display
  - `feedback`: IInputFeedbackProp - Validation feedback object
  - `bordered`: boolean - Whether to show a border (default: true)

- **Events**:
  - `inputChange`: CustomEvent<InputEvent> - Fired when the input value changes
  - `inputBlur`: CustomEvent<FocusEvent> - Fired when the input loses focus
  - `inputFocus`: CustomEvent<FocusEvent> - Fired when the input gains focus

- **Usage Patterns**:
  - Creating controlled number inputs with validation
  - Implementing numeric form fields with constraints
  - Creating currency inputs with formatting

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcNumberInput } from '@trimble-oss/moduswebcomponents-react';

// Interface for feedback object
interface InputFeedback {
  level: 'error' | 'info' | 'success' | 'warning';
  message: string;
}

const AgeInputForm: React.FC = () => {
  // State for the input value
  const [age, setAge] = useState<string>('');
  const [feedback, setFeedback] = useState<InputFeedback | undefined>(undefined);
  
  // Reference to the input element for event handling
  const inputRef = useRef<HTMLModusWcNumberInputElement>(null);
  
  // Validate the age value
  const validateAge = (value: string) => {
    const numValue = Number(value);
    
    if (value === '') {
      return {
        level: 'error' as const,
        message: 'Age is required'
      };
    } else if (isNaN(numValue)) {
      return {
        level: 'error' as const,
        message: 'Please enter a valid number'
      };
    } else if (numValue < 18) {
      return {
        level: 'error' as const,
        message: 'Age must be at least 18'
      };
    } else if (numValue > 120) {
      return {
        level: 'error' as const,
        message: 'Age cannot exceed 120'
      };
    }
    
    return undefined;
  };
  
  // Set up event listeners
  useEffect(() => {
    const input = inputRef.current;
    
    if (input) {
      // Handle value changes
      const handleChange = (e: CustomEvent<InputEvent>) => {
        const target = e.detail.target as HTMLInputElement;
        const newValue = target.value;
        
        setAge(newValue);
        setFeedback(validateAge(newValue));
      };
      
      // Handle blur event
      const handleBlur = (e: CustomEvent<FocusEvent>) => {
        setFeedback(validateAge(age));
      };
      
      // Add event listeners
      input.addEventListener('inputChange', handleChange as EventListener);
      input.addEventListener('inputBlur', handleBlur as EventListener);
      
      // Clean up
      return () => {
        input.removeEventListener('inputChange', handleChange as EventListener);
        input.removeEventListener('inputBlur', handleBlur as EventListener);
      };
    }
  }, [age]);
  
  // Handle form submission
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    const validationResult = validateAge(age);
    setFeedback(validationResult);
    
    if (!validationResult) {
      console.log('Form submitted with age:', age);
      // Process form submission
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <ModusWcNumberInput
        ref={inputRef}
        label="Age"
        min={18}
        max={120}
        step={1}
        value={age}
        required
        feedback={feedback}
        placeholder="Enter your age"
      />
      
      <div style={{ marginTop: '20px' }}>
        <button type="submit">Submit</button>
      </div>
    </form>
  );
};

export default AgeInputForm;
```

**Notes:**
- Always handle both validation and value state in React applications
- For HTML-only implementations, you can still use the feedback property to display validation messages
- Use min/max/step to constrain the input to appropriate ranges
- For the best user experience, perform validation on blur rather than on every change
- The component emits custom events, so make sure to add appropriate type casting when handling them in TypeScript
- The value property is a string, not a number, so you need to convert it when doing numeric operations


---

# ModusWcPagination

## Prompt 1
**User Question:** How do I implement basic pagination for a data table in React using the Modus Pagination component?

**Agent Answer:**
References:
- **Properties**:
  - `page`: number - The current page number (default: 1)
  - `count`: number - Total number of pages (default: 1)
  - `size`: 'sm' | 'md' | 'lg' - Size of pagination buttons (default: 'md')
  - `prevButtonText`: string - Text for previous page button (defaults to icon if not set)
  - `nextButtonText`: string - Text for next page button (defaults to icon if not set)
  - `customClass`: string - Custom CSS class to apply
  - `ariaLabelValues`: IAriaLabelValues - Custom accessibility labels for buttons

- **Events**:
  - `pageChange`: CustomEvent<IPageChange> - Event emitted when page changes, with payload:
    - `newPage`: number - The newly selected page number
    - `prevPage`: number - The previously selected page number

- **Usage Patterns**:
  - Implementing pagination for data tables and lists
  - Handling page changes and fetching data
  - Customizing accessibility labels for screen readers

**TypeScript Example:**
```tsx
import React, { useState, useEffect, useRef } from 'react';
import { ModusWcPagination } from '@trimble-oss/moduswebcomponents-react';

// Define interfaces for our data and pagination event
interface User {
  id: number;
  name: string;
  email: string;
}

interface PageChangeEvent {
  newPage: number;
  prevPage: number;
}

const PaginatedTable: React.FC = () => {
  // State for current page and data
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [totalPages, setTotalPages] = useState<number>(1);
  
  // Reference to pagination component for event handling
  const paginationRef = useRef<HTMLModusWcPaginationElement>(null);
  
  // Items per page
  const itemsPerPage = 5;
  
  // Fetch data based on the current page
  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      
      try {
        // In a real app, you would call an API with pagination parameters
        // Example: const response = await fetch(`/api/users?page=${currentPage}&limit=${itemsPerPage}`);
        
        // For this example, we'll simulate an API call with timeout
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // Mock data - in a real app, this would come from your API
        const mockData: User[] = Array.from({ length: itemsPerPage }, (_, i) => {
          const id = (currentPage - 1) * itemsPerPage + i + 1;
          return {
            id,
            name: `User ${id}`,
            email: `user${id}@example.com`
          };
        });
        
        setUsers(mockData);
        setTotalPages(10); // In a real app, this would come from API metadata
        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };
    
    fetchData();
  }, [currentPage]);
  
  // Handle page change events
  useEffect(() => {
    const pagination = paginationRef.current;
    
    if (pagination) {
      const handlePageChange = (e: CustomEvent<PageChangeEvent>) => {
        setCurrentPage(e.detail.newPage);
      };
      
      pagination.addEventListener('pageChange', handlePageChange as EventListener);
      
      return () => {
        pagination.removeEventListener('pageChange', handlePageChange as EventListener);
      };
    }
  }, []);
  
  return (
    <div className="table-container">
      <h2>Users List</h2>
      
      {loading ? (
        <div>Loading data...</div>
      ) : (
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ backgroundColor: '#f2f2f2' }}>
              <th style={{ padding: '8px', textAlign: 'left', borderBottom: '1px solid #ddd' }}>ID</th>
              <th style={{ padding: '8px', textAlign: 'left', borderBottom: '1px solid #ddd' }}>Name</th>
              <th style={{ padding: '8px', textAlign: 'left', borderBottom: '1px solid #ddd' }}>Email</th>
            </tr>
          </thead>
          <tbody>
            {users.map(user => (
              <tr key={user.id}>
                <td style={{ padding: '8px', borderBottom: '1px solid #ddd' }}>{user.id}</td>
                <td style={{ padding: '8px', borderBottom: '1px solid #ddd' }}>{user.name}</td>
                <td style={{ padding: '8px', borderBottom: '1px solid #ddd' }}>{user.email}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
      
      <div style={{ marginTop: '20px', display: 'flex', justifyContent: 'center' }}>
        <ModusWcPagination
          ref={paginationRef}
          page={currentPage}
          count={totalPages}
          size="md"
        />
      </div>
    </div>
  );
};

export default PaginatedTable;
```

**Notes:**
- The component displays at most 5 page buttons relative to the current page
- It automatically adds first/last navigation buttons for easier navigation
- Always listen for the `pageChange` event to update your data when the page changes
- Ensure that the `page` and `count` properties are properly synchronized with your data
- For accessibility, consider using custom aria labels via the `ariaLabelValues` property
- The pagination component doesn't handle data fetching or display - you need to implement that logic


---

# ModusWcProgress

## Prompt 1
**User Question:** How do I implement a basic progress bar in React using the Modus Progress component to show file upload progress?

**Agent Answer:**
References:
- **Properties**:
  - `value`: number - The current value of the progress (default: 0)
  - `max`: number - The maximum value of the progress (default: 100)
  - `indeterminate`: boolean - Whether to show an indeterminate progress state (default: false)
  - `variant`: 'default' | 'radial' - The style variant of the progress component (default: 'default')
  - `label`: string - Optional text to render within the progress bar
  - `customClass`: string - Custom CSS class for styling

- **Events**:
  - No custom events emitted by this component

- **Usage Patterns**:
  - Showing determinate progress for tasks with known completion points
  - Displaying indeterminate progress for operations with unknown duration
  - Using radial progress for circular display
  - Customizing appearance through CSS

**TypeScript Example:**
```tsx
import React, { useState, useEffect } from 'react';
import { ModusWcProgress } from '@trimble-oss/moduswebcomponents-react';

const FileUploader: React.FC = () => {
  // State for tracking upload
  const [uploadProgress, setUploadProgress] = useState<number>(0);
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [status, setStatus] = useState<string>('');
  const [isUploading, setIsUploading] = useState<boolean>(false);
  const [timerId, setTimerId] = useState<number | null>(null);
  
  // Handle file selection
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files;
    if (files && files.length > 0) {
      setSelectedFile(files[0]);
      setStatus('');
      setUploadProgress(0);
    }
  };
  
  // Clean up timer when component unmounts
  useEffect(() => {
    return () => {
      if (timerId !== null) {
        window.clearInterval(timerId);
      }
    };
  }, [timerId]);
  
  // Start upload process (simulation)
  const handleUpload = () => {
    if (!selectedFile) return;
    
    setIsUploading(true);
    setUploadProgress(0);
    setStatus('Uploading...');
    
    // Simulate progress with a timer
    const timer = window.setInterval(() => {
      setUploadProgress(prev => {
        if (prev >= 100) {
          window.clearInterval(timer);
          setIsUploading(false);
          setStatus('Upload complete!');
          return 100;
        }
        return prev + 5;
      });
    }, 300);
    
    setTimerId(timer as unknown as number);
  };
  
  // Cancel the upload simulation
  const handleCancel = () => {
    if (timerId !== null) {
      window.clearInterval(timerId);
      setTimerId(null);
      setIsUploading(false);
      setStatus('Upload cancelled');
    }
  };
  
  return (
    <div className="uploader-container">
      <h2>File Upload</h2>
      
      <div className="file-selection">
        <input
          type="file"
          onChange={handleFileChange}
          id="file-input"
          style={{ display: 'none' }}
        />
        <label htmlFor="file-input" className="file-select-button">
          Select File
        </label>
        <span className="file-name">
          {selectedFile ? selectedFile.name : 'No file selected'}
        </span>
      </div>
      
      <div className="progress-container">
        <ModusWcProgress
          value={uploadProgress}
          max={100}
          aria-label="File upload progress"
          label={`${uploadProgress}%`}
        />
      </div>
      
      <div className="status-text">{status}</div>
      
      <div className="control-buttons">
        <button
          onClick={handleUpload}
          disabled={!selectedFile || isUploading}
          className="upload-button"
        >
          Upload
        </button>
        {isUploading && (
          <button onClick={handleCancel} className="cancel-button">
            Cancel
          </button>
        )}
      </div>
      
      <style>{`
        .uploader-container {
          max-width: 500px;
          margin: 0 auto;
          padding: 20px;
          border: 1px solid #e0e0e0;
          border-radius: 8px;
          box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        .file-selection {
          display: flex;
          align-items: center;
          margin-bottom: 20px;
        }
        
        .file-select-button {
          background-color: #0063a3;
          color: white;
          padding: 8px 16px;
          border-radius: 4px;
          cursor: pointer;
          display: inline-block;
        }
        
        .file-name {
          margin-left: 12px;
          font-size: 14px;
          color: #666;
        }
        
        .progress-container {
          margin-bottom: 16px;
        }
        
        .status-text {
          margin-bottom: 16px;
          font-size: 14px;
          color: #666;
          min-height: 20px;
        }
        
        .control-buttons {
          display: flex;
          gap: 12px;
        }
        
        .upload-button {
          background-color: #0063a3;
          color: white;
          border: none;
          border-radius: 4px;
          padding: 8px 16px;
          cursor: pointer;
        }
        
        .upload-button:disabled {
          background-color: #ccc;
          cursor: not-allowed;
        }
        
        .cancel-button {
          background-color: white;
          color: #0063a3;
          border: 1px solid #0063a3;
          border-radius: 4px;
          padding: 8px 16px;
          cursor: pointer;
        }
      `}</style>
    </div>
  );
};

export default FileUploader;
```

**Notes:**
- Use the `value` and `max` properties to show determinate progress for operations where progress can be measured
- Set the `label` property to show a text description or percentage inside the progress bar
- The component doesn't emit events, so you need to update the value property from your application logic
- Make sure to handle error states and provide a way to cancel operations when appropriate
- Use custom CSS classes to style the progress bar's color, height, or other visual properties
- For upload scenarios, track progress using XHR's upload progress events and update the progress value accordingly


---

# ModusWcRadio

## Prompt 1
**User Question:** How do I implement a controlled radio button group in React using the Modus Radio component?

**Agent Answer:**
References:
- **Properties**:
  - **value** (boolean): The checked state of the radio button
  - **name** (string): Name of the form control, used for grouping radios
  - **label** (string): The text to display with the radio
  - **disabled** (boolean): Disables the radio when true
  - **required** (boolean): Indicates if the field is required
  - **size** ("xs" | "sm" | "md" | "lg"): Controls the size of the radio
  - **inputId** (string): ID for the radio input element

- **Events**:
  - **inputChange**: `CustomEvent<InputEvent>` - Fired when radio selection changes
  - **inputBlur**: `CustomEvent<FocusEvent>` - Fired when radio loses focus 
  - **inputFocus**: `CustomEvent<FocusEvent>` - Fired when radio gains focus

- **Usage Patterns**:
  - Group radios with the same `name` property
  - Manage selection state in parent component
  - Only one radio in a group should have `value={true}`
  
**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcRadio } from '@trimble-oss/moduswebcomponents-react';

interface RadioOption {
  id: string;
  label: string;
  value: string;
}

const RadioGroupExample: React.FC = () => {
  const [selectedValue, setSelectedValue] = useState('vanilla');
  const options: RadioOption[] = [
    { id: 'vanilla-opt', label: 'Vanilla', value: 'vanilla' },
    { id: 'chocolate-opt', label: 'Chocolate', value: 'chocolate' },
    { id: 'strawberry-opt', label: 'Strawberry', value: 'strawberry' }
  ];

  const handleSelectionChange = (selectedOption: string) => {
    setSelectedValue(selectedOption);
  };

  const renderRadioButtons = () => {
    return options.map((option) => {
      const radioRef = useRef<HTMLModusWcRadioElement>(null);
      
      useEffect(() => {
        const element = radioRef.current;
        if (element) {
          const handleChange = () => {
            handleSelectionChange(option.value);
          };
          
          element.addEventListener('inputChange', handleChange);
          
          return () => {
            element.removeEventListener('inputChange', handleChange);
          };
        }
      }, [option.value]);
      
      return (
        <ModusWcRadio
          key={option.id}
          ref={radioRef}
          inputId={option.id}
          name="flavor-choice"
          label={option.label}
          value={selectedValue === option.value}
        />
      );
    });
  };

  return (
    <div>
      <h3>Select your favorite flavor:</h3>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
        {renderRadioButtons()}
      </div>
      <p>Selected flavor: {selectedValue}</p>
    </div>
  );
};

export default RadioGroupExample;
```

**Notes:**
- Radio buttons should be grouped using the same `name` property
- Unlike standard HTML radio inputs, ModusWcRadio uses a boolean `value` prop to indicate selection state
- You must manually track which option is selected in your state management
- For accessibility, provide unique `inputId` values and ensure labels are properly associated

## Prompt 2
**User Question:** How can I implement form validation with radio button groups using the Modus Radio component?

**Agent Answer:**
References:
- **Properties**:
  - **required** (boolean): Indicates if selection is required 
  - **disabled** (boolean): Disables the radio when true
  - **customClass** (string): Custom CSS class for styling
  - **inputTabIndex** (number): Controls tab navigation order

- **Events**:
  - **inputBlur**: `CustomEvent<FocusEvent>` - Useful for validation on field exit
  - **inputChange**: `CustomEvent<InputEvent>` - Used to track selection changes

- **Usage Patterns**:
  - Validate radio group selection on form submission
  - Display validation messages when appropriate
  - Group radio buttons with fieldset and legend for proper accessibility

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect, FormEvent } from 'react';
import { 
  ModusWcRadio, 
  ModusWcInputFeedback, 
  ModusWcButton 
} from '@trimble-oss/moduswebcomponents-react';

interface SubscriptionOption {
  id: string;
  label: string;
  value: string;
}

const ValidatedRadioForm: React.FC = () => {
  const [selectedPlan, setSelectedPlan] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [submitted, setSubmitted] = useState(false);
  const feedbackRef = useRef<HTMLModusWcInputFeedbackElement>(null);
  
  const subscriptionOptions: SubscriptionOption[] = [
    { id: 'plan-basic', label: 'Basic ($10/month)', value: 'basic' },
    { id: 'plan-premium', label: 'Premium ($20/month)', value: 'premium' },
    { id: 'plan-professional', label: 'Professional ($30/month)', value: 'professional' }
  ];
  
  // Validate whenever selection or submission state changes
  useEffect(() => {
    if (submitted) {
      validateSelection();
    }
  }, [selectedPlan, submitted]);
  
  const validateSelection = () => {
    if (!selectedPlan) {
      setError('Please select a subscription plan');
      if (feedbackRef.current) {
        feedbackRef.current.hidden = false;
      }
      return false;
    }
    
    setError(null);
    if (feedbackRef.current) {
      feedbackRef.current.hidden = true;
    }
    return true;
  };
  
  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
    
    if (validateSelection()) {
      // Form is valid, proceed with submission
      console.log(`Selected plan: ${selectedPlan}`);
      alert(`Form submitted with plan: ${selectedPlan}`);
    }
  };
  
  const createRadioHandler = (value: string) => {
    return () => {
      setSelectedPlan(value);
    };
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <fieldset style={{ border: '1px solid #ccc', padding: '16px', marginBottom: '16px' }}>
        <legend>Choose a subscription plan (Required)</legend>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
          {subscriptionOptions.map((option) => {
            const radioRef = useRef<HTMLModusWcRadioElement>(null);
            
            useEffect(() => {
              const element = radioRef.current;
              if (element) {
                const handleChange = () => {
                  createRadioHandler(option.value)();
                };
                
                element.addEventListener('inputChange', handleChange);
                
                return () => {
                  element.removeEventListener('inputChange', handleChange);
                };
              }
            }, [option.value]);
            
            return (
              <ModusWcRadio
                key={option.id}
                ref={radioRef}
                inputId={option.id}
                name="subscription-plan"
                label={option.label}
                required={true}
                value={selectedPlan === option.value}
              />
            );
          })}
        </div>
      </fieldset>
      
      <ModusWcInputFeedback
        ref={feedbackRef}
        message={error || ''}
        state="error"
        hidden={!error}
      />
      
      <ModusWcButton type="submit" color="primary" style={{ marginTop: '16px' }}>
        Submit
      </ModusWcButton>
    </form>
  );
};

export default ValidatedRadioForm;
```

**Notes:**
- Radio button groups should be wrapped in a `<fieldset>` with a `<legend>` for accessibility
- The `required` property should be set on each radio in the group
- Form validation should check if any radio is selected (has `value={true}`)
- Use ModusWcInputFeedback to display validation error messages
- Remember to handle both initial form submission and real-time validation as selections change
- For proper accessibility, ensure error messages are properly associated with the input group

---

# ModusWcRating

## Prompt 1
**User Question:** How do I implement a star rating component with half-star ratings in React?

**Agent Answer:**
References:
- **Properties**:
  - **value** (number): Current rating value
  - **variant** ("star" | "heart" | "smiley" | "thumb"): Visual style of rating items
  - **allowHalf** (boolean): Enables half-step rating selection
  - **count** (number): Number of rating items to display
  - **size** ("sm" | "md" | "lg"): Controls the size of rating items
  - **disabled** (boolean): Disables interaction when true
  - **getAriaLabelText** ((ratingValue: number) => string): Function to generate accessible labels

- **Events**:
  - **ratingChange**: `CustomEvent<IRatingChange>` - Emitted when rating value changes

- **Usage Patterns**:
  - Controlled component with external state management
  - Can be customized with CSS variables
  - Provides accessibility with custom ARIA labels

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcRating } from '@trimble-oss/moduswebcomponents-react';

interface RatingProps {
  initialValue?: number;
  onChange?: (value: number) => void;
  disabled?: boolean;
  variant?: 'star' | 'heart' | 'smiley' | 'thumb';
  count?: number;
  size?: 'sm' | 'md' | 'lg';
  allowHalf?: boolean;
}

const StarRating: React.FC<RatingProps> = ({ 
  initialValue = 0, 
  onChange,
  disabled = false,
  variant = 'star',
  count = 5,
  size = 'md',
  allowHalf = false
}) => {
  const [rating, setRating] = useState<number>(initialValue || 0);
  const ratingRef = useRef<HTMLModusWcRatingElement | null>(null);
    // Function to handle rating changes
  const handleRatingChange = (e: Event) => {
    // Cast to CustomEvent to access detail property
    const customEvent = e as CustomEvent;
    console.log('Rating changed:', customEvent.detail);
    
    if (customEvent.detail && customEvent.detail.newRating !== undefined) {
      const newValue = customEvent.detail.newRating;
      console.log('New rating value:', newValue);
      setRating(newValue);
      
      if (onChange) {
        onChange(newValue);
      }
    }
  };
  
  // Setup event listener for rating changes
  useEffect(() => {
    const element = ratingRef.current;
    if (element) {
      // Remove any existing event listeners to prevent duplicates
      element.removeEventListener('ratingChange', handleRatingChange);
      
      // Add the new event listener
      element.addEventListener('ratingChange', handleRatingChange);
      
      console.log('Event listener attached to rating component');
      
      // Cleanup function
      return () => {
        element.removeEventListener('ratingChange', handleRatingChange);
        console.log('Event listener removed from rating component');
      };
    }
  }, [ratingRef.current]); // Only re-run when the ref changes
  
  // Custom ARIA label generator for accessibility
  const getAriaLabelText = (value: number): string => {
    if (value === 0) return 'No stars';
    if (value === 0.5) return 'Half star';
    if (value === 1) return '1 star';
    if (value % 1 === 0) return `${value} stars`;
    
    const whole = Math.floor(value);
    return `${whole} and a half stars`;
  };
  return (
    <div className="star-rating-container" style={{ padding: '20px', maxWidth: '400px' }}>
      <ModusWcRating
        ref={ratingRef}
        value={rating}
        variant={variant}
        count={count}
        size={size}
        disabled={disabled}
        aria-label="Rating scale component"
        // Use camelCase for React props that map to kebab-case HTML attributes
        allowHalf={allowHalf}
        // Pass the ARIA label function as a property
        getAriaLabelText={getAriaLabelText}
      />
      <div className="rating-display" style={{ marginTop: '10px', fontSize: '16px' }}>
        Current rating: <strong>{rating !== undefined && rating !== null ? rating.toFixed(1) : '0.0'}</strong>
      </div>
    </div>
  );
};

export default StarRating;
```

**Notes:**
- Use the `allowHalf` property to enable half-star ratings
- Half ratings are only supported with "star" and "heart" variants
- The `getAriaLabelText` function should provide descriptive labels for each rating value
- The component emits a `ratingChange` event when the user selects a new rating
- Avoid the use of `event.detail.value` use event `event.detail` instead


---

# ModusWcSelect

## Prompt 1
**User Question:** How do I implement a controlled select dropdown with validation in React using the Modus Select component?

**Agent Answer:**
References:
- **Properties**:
  - **options** (ISelectOption[]): Array of objects with `label` and `value` properties
  - **value** (string): The currently selected value
  - **label** (string): Text label for the select
  - **feedback** (IInputFeedbackProp): Object with `level` ('error', 'info', 'success', 'warning') and `message`
  - **required** (boolean): Indicates if the field is required
  - **disabled** (boolean): Disables the select when true
  - **size** ("sm" | "md" | "lg"): Controls the size of the select
  - **bordered** (boolean): Applies border styling to the select

- **Events**:
  - **inputChange**: `CustomEvent<InputEvent>` - Triggered when selection changes
  - **inputBlur**: `CustomEvent<FocusEvent>` - Triggered when the select loses focus
  - **inputFocus**: `CustomEvent<FocusEvent>` - Triggered when the select gains focus

- **Usage Patterns**:
  - Controlled component pattern with external state management
  - Form validation with feedback display
  - Dynamic options population

**HTML Example:**
```html
<modus-wc-select
  label="Choose a country"
  required
  options='[
    {"label": "United States", "value": "us"},
    {"label": "Canada", "value": "ca"},
    {"label": "Mexico", "value": "mx"}
  ]'
  feedback='{"level": "error", "message": "Please select a country"}'
  value="">
</modus-wc-select>
```

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcSelect } from '@trimble-oss/moduswebcomponents-react';

interface ISelectOption {
  label: string;
  value: string;
  disabled?: boolean;
}

interface CountrySelectorProps {
  onCountrySelect?: (country: string) => void;
}

const CountrySelector: React.FC<CountrySelectorProps> = ({ onCountrySelect }) => {
  // State for selected value and validation
  const [selectedCountry, setSelectedCountry] = useState<string>('');
  const [isTouched, setIsTouched] = useState(false);
  const [feedback, setFeedback] = useState<{ level: 'error' | 'info' | 'success' | 'warning', message: string } | undefined>(undefined);
  
  // Reference to the select element
  const selectRef = useRef<HTMLModusWcSelectElement>(null);
  
  // Country options
  const countryOptions: ISelectOption[] = [
    { label: 'Select a country', value: '', disabled: true },
    { label: 'United States', value: 'us' },
    { label: 'Canada', value: 'ca' },
    { label: 'Mexico', value: 'mx' },
    { label: 'United Kingdom', value: 'uk' },
    { label: 'France', value: 'fr' },
    { label: 'Germany', value: 'de' }
  ];
  
  // Validate selection and update feedback
  const validateSelection = () => {
    if (isTouched && !selectedCountry) {
      setFeedback({ level: 'error', message: 'Please select a country' });
      return false;
    }
    
    setFeedback(undefined);
    return true;
  };
  
  // Validate on selection changes
  useEffect(() => {
    if (isTouched) {
      validateSelection();
    }
    
    // Notify parent component if needed
    if (selectedCountry && onCountrySelect) {
      onCountrySelect(selectedCountry);
    }
  }, [selectedCountry, isTouched, onCountrySelect]);
  
  // Setup event listeners
  useEffect(() => {
    const select = selectRef.current;
    if (!select) return;
    
    // Handle selection change
    const handleChange = (e: CustomEvent) => {
      setSelectedCountry(e.detail.value);
    };
    
    // Handle blur for validation
    const handleBlur = () => {
      setIsTouched(true);
      validateSelection();
    };
    
    select.addEventListener('inputChange', handleChange as EventListener);
    select.addEventListener('inputBlur', handleBlur as EventListener);
    
    return () => {
      select.removeEventListener('inputChange', handleChange as EventListener);
      select.removeEventListener('inputBlur', handleBlur as EventListener);
    };
  }, []);
  
  return (
    <div className="country-selector">
      <ModusWcSelect
        ref={selectRef}
        label="Country"
        options={countryOptions}
        value={selectedCountry}
        required={true}
        feedback={feedback}
        size="md"
        bordered={true}
      />
    </div>
  );
};

// Usage example
const FormExample: React.FC = () => {
  const handleCountrySelect = (country: string) => {
    console.log(`Selected country: ${country}`);
  };
  
  return (
    <form>
      <CountrySelector onCountrySelect={handleCountrySelect} />
      {/* Other form fields */}
    </form>
  );
};

export default FormExample;
```

**Notes:**
- The `options` property requires an array of objects with `label` and `value` properties
- Each option can also have an optional `disabled` property to prevent selection
- Use the `feedback` property to display validation messages below the select
- Listen for the `inputChange` event to respond to user selections
- Combine with `inputBlur` event for validation on field exit
- For accessibility, ensure proper labels and ARIA attributes

## Prompt 2
**User Question:** How can I implement a dynamic, searchable multiselect dropdown using the Modus Select component?

**Agent Answer:**
References:
- **Properties**:
  - **options** (ISelectOption[]): Array of option objects with `label`, `value`, and optional `disabled` properties
  - **customClass** (string): Custom CSS class for styling
  - **inputId** (string): ID for the select element
  
- **Events**:
  - **inputChange**: `CustomEvent<InputEvent>` - Triggered when selection changes
  
- **Usage Patterns**:
  - While ModusWcSelect doesn't natively support multiselect, we can build it with multiple components
  - Combine with ModusWcChip to display selected items
  - Implement search functionality with filtered options

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcSelect, ModusWcChip, ModusWcTextInput } from '@trimble-oss/moduswebcomponents-react';

interface ISelectOption {
  label: string;
  value: string;
  disabled?: boolean;
}

interface MultiSelectProps {
  label: string;
  allOptions: ISelectOption[];
  placeholder?: string;
  onChange?: (selectedValues: string[]) => void;
}

const SearchableMultiSelect: React.FC<MultiSelectProps> = ({
  label,
  allOptions,
  placeholder = 'Search and select...',
  onChange
}) => {
  // State for selections and search filter
  const [selectedValues, setSelectedValues] = useState<string[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredOptions, setFilteredOptions] = useState<ISelectOption[]>(allOptions);
  const [currentValue, setCurrentValue] = useState<string>('');
  
  // References
  const selectRef = useRef<HTMLModusWcSelectElement>(null);
  const searchInputRef = useRef<HTMLModusWcTextInputElement>(null);
  
  // Get selected items as full objects
  const selectedItems = selectedValues.map(value => 
    allOptions.find(option => option.value === value)!
  );
  
  // Filter available options based on search and already selected
  useEffect(() => {
    const searchFilter = searchTerm.toLowerCase();
    const filtered = allOptions
      .filter(option => 
        // Don't show already selected options
        !selectedValues.includes(option.value) && 
        // Filter by search term
        option.label.toLowerCase().includes(searchFilter)
      );
    setFilteredOptions(filtered);
  }, [searchTerm, selectedValues, allOptions]);
  
  // Notify parent of changes to selection
  useEffect(() => {
    if (onChange) {
      onChange(selectedValues);
    }
  }, [selectedValues, onChange]);
  
  // Handle search input changes
  const handleSearchChange = (e: CustomEvent) => {
    setSearchTerm(e.detail.value);
  };
  
  // Handle select dropdown changes
  useEffect(() => {
    const select = selectRef.current;
    if (!select) return;
    
    const handleSelectionChange = (e: CustomEvent) => {
      const value = e.detail.value;
      if (!value) return;
      
      // Add to selected values if not already included
      if (!selectedValues.includes(value)) {
        setSelectedValues(prev => [...prev, value]);
      }
      
      // Reset the select and search
      setCurrentValue('');
      setSearchTerm('');
      
      // Focus back on search input for convenient multiple selections
      if (searchInputRef.current) {
        searchInputRef.current.focus();
      }
    };
    
    select.addEventListener('inputChange', handleSelectionChange as EventListener);
    
    return () => {
      select.removeEventListener('inputChange', handleSelectionChange as EventListener);
    };
  }, [selectedValues]);
  
  // Handle chip removal
  const handleChipRemove = (valueToRemove: string) => {
    setSelectedValues(selectedValues.filter(value => value !== valueToRemove));
  };
  
  // Setup event listeners for chips
  const setupChipRemovalListener = (value: string) => {
    return (e: CustomEvent) => {
      handleChipRemove(value);
    };
  };
  
  return (
    <div className="searchable-multiselect">
      <label>{label}</label>
      
      {/* Search input */}
      <div className="search-container">
        <ModusWcTextInput
          ref={searchInputRef}
          value={searchTerm}
          placeholder={placeholder}
          onInputChange={handleSearchChange as any}
          style={{ marginBottom: '8px', width: '100%' }}
        />
      </div>
      
      {/* Options dropdown */}
      <ModusWcSelect
        ref={selectRef}
        options={filteredOptions}
        value={currentValue}
        disabled={filteredOptions.length === 0}
        bordered
        style={{ marginBottom: '12px', width: '100%' }}
      />
      
      {/* Selected items display as chips */}
      <div className="selected-items" style={{ 
        display: 'flex', 
        flexWrap: 'wrap',
        gap: '8px',
        marginTop: '12px' 
      }}>
        {selectedItems.map((item) => {
          // Create a ref for each chip
          const chipRef = useRef<HTMLModusWcChipElement>(null);
          
          useEffect(() => {
            const chipElement = chipRef.current;
            if (chipElement) {
              const removeHandler = setupChipRemovalListener(item.value);
              chipElement.addEventListener('chipClose', removeHandler as EventListener);
              
              return () => {
                chipElement.removeEventListener('chipClose', removeHandler as EventListener);
              };
            }
          }, [item.value]);
          
          return (
            <ModusWcChip
              key={item.value}
              ref={chipRef}
              label={item.label}
              removable
              size="sm"
              color="secondary"
            />
          );
        })}
        
        {selectedValues.length === 0 && (
          <div className="no-selections" style={{ color: '#666', fontStyle: 'italic' }}>
            No items selected
          </div>
        )}
      </div>
    </div>
  );
};

// Usage example
const LanguageSelector: React.FC = () => {
  const languageOptions: ISelectOption[] = [
    { label: 'JavaScript', value: 'js' },
    { label: 'TypeScript', value: 'ts' },
    { label: 'Python', value: 'py' },
    { label: 'Java', value: 'java' },
    { label: 'C#', value: 'cs' },
    { label: 'Ruby', value: 'rb' },
    { label: 'Go', value: 'go' },
    { label: 'Rust', value: 'rs' },
    { label: 'PHP', value: 'php' },
    { label: 'Swift', value: 'swift' },
  ];
  
  const handleSelectionChange = (selected: string[]) => {
    console.log('Selected languages:', selected);
  };
  
  return (
    <div style={{ width: '400px' }}>
      <h3>Programming Skills</h3>
      <SearchableMultiSelect
        label="Select languages you're proficient in"
        allOptions={languageOptions}
        placeholder="Search for a language..."
        onChange={handleSelectionChange}
      />
    </div>
  );
};

export default LanguageSelector;
```

**Notes:**
- This implementation creates a multi-select by combining ModusWcSelect with ModusWcChip components
- For searchability, we use ModusWcTextInput to filter the available options
- The component maintains two states: the filtered options and the selected values
- Selected values are displayed as removable chips that the user can delete
- The search input filters the options dropdown in real-time
- When an option is selected, it's removed from the available options to prevent duplicate selections
- This approach creates a fully accessible custom multi-select interface
- You can customize the appearance using the customClass property and CSS variables

---

# ModusWcSideNavigation

## Prompt 1
**User Question:** How do I implement a responsive side navigation menu with the Modus Side Navigation component in React?

**Agent Answer:**
References:
- **Properties**:
  - **expanded** (boolean): Controls whether the side navigation is expanded or collapsed
  - **maxWidth** (string): Sets the maximum width of the expanded navigation panel
  - **collapseOnClickOutside** (boolean): Controls if navigation collapses when clicking elsewhere
  - **customClass** (string): Custom CSS class for additional styling

- **Events**:
  - No custom events; typically used with ModusWcNavbar's "mainMenuOpenChange" event
  - Combined with ModusWcMenu and ModusWcMenuItem for navigation options

- **Usage Patterns**:
  - Side navigation works as a companion to ModusWcNavbar
  - Contains ModusWcMenu with ModusWcMenuItem components for navigation options
  - Typically toggled by the hamburger menu in the navbar


**TypeScript Example:**
```tsx
import React, { useState, useEffect, useRef } from 'react';
import { 
  ModusWcSideNavigation,
  ModusWcNavbar,
  ModusWcMenu,
  ModusWcMenuItem 
} from '@trimble-oss/moduswebcomponents-react';

interface MenuItem {
  id: string;
  label: string;
  icon: string;
  path: string;
}

const AppLayout: React.FC = () => {
  // State for side navigation
  const [isExpanded, setIsExpanded] = useState(false);
  const [activeItemId, setActiveItemId] = useState('dashboard');
  
  // Ref for the navbar component
  const navbarRef = useRef<HTMLModusWcNavbarElement>(null);
  
  // Menu items data
  const menuItems: MenuItem[] = [
    { id: 'dashboard', label: 'Dashboard', icon: 'home', path: '/' },
    { id: 'projects', label: 'Projects', icon: 'folder', path: '/projects' },
    { id: 'team', label: 'Team', icon: 'group', path: '/team' },
    { id: 'reports', label: 'Reports', icon: 'chart-bar', path: '/reports' },
    { id: 'settings', label: 'Settings', icon: 'gears', path: '/settings' }
  ];
  
  // Handle navbar menu button click
  useEffect(() => {
    const navbar = navbarRef.current;
    
    if (navbar) {
      const handleMainMenuToggle = () => {
        setIsExpanded(prevState => !prevState);
      };
      
      navbar.addEventListener('mainMenuOpenChange', handleMainMenuToggle);
      
      return () => {
        navbar.removeEventListener('mainMenuOpenChange', handleMainMenuToggle);
      };
    }
  }, []);
  
  // Handle menu item selection
  const handleMenuItemSelect = (itemId: string) => {
    setActiveItemId(itemId);
    
    // On mobile, collapse the navigation after selection
    if (window.innerWidth < 768) {
      setIsExpanded(false);
    }
    
    // In a real app, you would use routing here
    console.log(`Navigating to: ${itemId}`);
  };
  
  return (
    <div className="app-layout" style={{ display: 'flex', flexDirection: 'column', height: '100vh' }}>
      <ModusWcNavbar
        ref={navbarRef}
        appTitle="Modus App"
        logo="/assets/logo.svg"
        visibility={{ mainMenu: true, user: true, notifications: true }}
        style={{ zIndex: 2 }}
      />
      
      <div style={{ display: 'flex', flex: 1, overflow: 'hidden' }}>
        <ModusWcSideNavigation
          expanded={isExpanded}
          collapseOnClickOutside={true}
          maxWidth="250px"
          style={{ height: '100%' }}
        >
          <ModusWcMenu size="lg">
            {menuItems.map((item) => (
              <ModusWcMenuItem
                key={item.id}
                label={item.label}
                startIcon={item.icon}
                selected={activeItemId === item.id}
                onClick={() => handleMenuItemSelect(item.id)}
              />
            ))}
          </ModusWcMenu>
        </ModusWcSideNavigation>
        
        <div className="content-area" style={{ 
          flex: 1,
          padding: '1rem',
          overflow: 'auto'
        }}>
          <h1>Main Content Area</h1>
          <p>Current page: {activeItemId}</p>
          {/* Page content would go here */}
        </div>
      </div>
    </div>
  );
};

export default AppLayout;
```

**Notes:**
- Side Navigation is typically used alongside ModusWcNavbar and toggled by the hamburger menu
- Use ModusWcMenu and ModusWcMenuItem components inside the side navigation for navigation options
- For responsive design, consider collapsing the navigation automatically on mobile devices
- The `collapseOnClickOutside` property improves UX on mobile by automatically closing the menu
- You can control the width of the expanded panel with the `maxWidth` property
- When using with routing, update the active menu item based on the current route


---

# ModusWcSkeleton

## Prompt 1
**User Question:** How do I implement loading states for a profile card component using the Modus Skeleton component?

**Agent Answer:**
References:
- **Properties**:
  - **width** (string): Width of the skeleton element (default: '100%')
  - **height** (string): Height of the skeleton element (default: '1.5rem')
  - **shape** ("circle" | "rectangle"): Shape of the skeleton (default: 'rectangle')
  - **customClass** (string): Custom CSS class for styling

- **Events**:
  - No custom events provided by this component

- **Usage Patterns**:
  - Use to represent loading states for content
  - Combine multiple skeletons to create complex loading placeholders
  - Mimic the actual layout and proportions of the expected content
  
**TypeScript Example:**
```tsx
import React, { useState, useEffect } from 'react';
import { ModusWcSkeleton, ModusWcAvatar, ModusWcCard } from '@trimble-oss/moduswebcomponents-react';

interface ProfileData {
  id: string;
  name: string;
  title: string;
  bio: string;
  avatarUrl: string;
}

interface ProfileCardProps {
  userId: string;
  onProfileLoad?: (profile: ProfileData) => void;
}

const ProfileCard: React.FC<ProfileCardProps> = ({ userId, onProfileLoad }) => {
  const [profile, setProfile] = useState<ProfileData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Reset states when userId changes
    setLoading(true);
    setError(null);
    
    // Simulated API call to fetch profile data
    const fetchProfile = async () => {
      try {
        // In real app, replace with actual API call
        await new Promise(resolve => setTimeout(resolve, 1500));
          // Mock data
        const profileData: ProfileData = {
          id: userId,
          name: 'Sarah Johnson',
          title: 'Senior Product Manager',
          bio: 'Product strategy expert with 8+ years of experience in SaaS and construction technology.',
          avatarUrl: `https://picsum.photos/200/200?random=${userId}`
        };
        
        setProfile(profileData);
        if (onProfileLoad) {
          onProfileLoad(profileData);
        }
      } catch (err) {
        setError('Failed to load profile data');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, [userId, onProfileLoad]);

  return (
    <ModusWcCard style={{ width: '100%', maxWidth: '500px' }}>
      {loading ? (
        // Skeleton loading state
        <div style={{ padding: '1.5rem', display: 'flex', gap: '1rem' }}>
          {/* Avatar skeleton */}
          <ModusWcSkeleton 
            shape="circle" 
            width="4rem" 
            height="4rem"
          />
          
          <div style={{ 
            display: 'flex', 
            flexDirection: 'column', 
            gap: '0.75rem',
            flex: 1
          }}>
            {/* Name skeleton */}
            <ModusWcSkeleton 
              width="60%" 
              height="1.5rem"
            />
            
            {/* Title skeleton */}
            <ModusWcSkeleton 
              width="40%" 
              height="1rem"
            />
            
            {/* Bio skeleton - multiple lines */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
              <ModusWcSkeleton height="0.875rem" />
              <ModusWcSkeleton height="0.875rem" />
              <ModusWcSkeleton width="75%" height="0.875rem" />
            </div>
          </div>
        </div>
      ) : error ? (
        // Error state
        <div style={{ padding: '1.5rem', color: 'var(--modus-wc-color-danger)' }}>
          {error}
        </div>
      ) : (        // Content state - actual profile data
        <div style={{ padding: '1.5rem', display: 'flex', gap: '1rem' }}>          
        <ModusWcAvatar
            size="lg"
            img-src={profile?.avatarUrl}
            alt={`${profile?.name}'s avatar`}
            shape="circle"
          />
          <div>
            <h3 style={{ margin: '0 0 0.25rem 0' }}>{profile?.name}</h3>
            <p style={{ 
              margin: '0 0 0.75rem 0', 
              color: 'var(--modus-wc-color-text-secondary)' 
            }}>
              {profile?.title}
            </p>
            <p style={{ margin: '0', lineHeight: '1.5' }}>
              {profile?.bio}
            </p>
          </div>
        </div>
      )}
    </ModusWcCard>
  );
};

// Example usage
const App: React.FC = () => {
  const [selectedUser, setSelectedUser] = useState<string>("user123");
  
  const userIds = ["user123", "user456", "user789"];
  
  return (
    <div style={{ padding: '2rem' }}>
      <h2>User Profile</h2>
      
      <div style={{ marginBottom: '1rem' }}>
        <label style={{ marginRight: '0.5rem' }}>Select User: </label>
        <select 
          value={selectedUser} 
          onChange={(e) => setSelectedUser(e.target.value)}
          style={{ padding: '0.5rem' }}
        >
          <option value="user123">Sarah Johnson</option>
          <option value="user456">Michael Smith</option>
          <option value="user789">Jessica Williams</option>
        </select>
      </div>
      
      <ProfileCard 
        userId={selectedUser} 
        onProfileLoad={(profile) => console.log('Profile loaded:', profile)}
      />
    </div>
  );
};

export default App;
```

**Notes:**
- Use skeletons that match the shape and approximate size of the actual content
- For text content, use multiple rectangle skeletons to mimic text lines
- For images or avatars, use the `shape="circle"` property
- Consider the overall layout and spacing to create a realistic loading placeholder
- Skeletons improve perceived performance by showing content structure before data loads
- You can customize the animation with CSS variables via the `customClass` property
- For accessibility, consider adding an aria-busy="true" attribute to the container during loading


---

# ModusWcSlider

## Prompt 1
**User Question:** How do I implement a controlled slider component with min, max, and step values in React using the Modus Slider component?

**Agent Answer:**
References:
- **Properties**:
  - **value** (number): Current value of the slider
  - **min** (number): Minimum value allowed
  - **max** (number): Maximum value allowed
  - **step** (number): Increment step size
  - **disabled** (boolean): Disables the slider when true
  - **label** (string): Text label for the slider
  - **size** ("sm" | "md" | "lg"): Controls the size of the slider
  - **required** (boolean): Indicates if the field is required

- **Events**:
  - **inputChange**: `CustomEvent<InputEvent>` - Emitted when slider value changes
  - **inputBlur**: `CustomEvent<FocusEvent>` - Emitted when slider loses focus
  - **inputFocus**: `CustomEvent<FocusEvent>` - Emitted when slider gains focus

- **Usage Patterns**:
  - Controlled component pattern with state management
  - Range selection with customizable min/max boundaries
  - Variable precision with step property
  
**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcSlider } from '@trimble-oss/moduswebcomponents-react';

interface VolumeControlProps {
  initialValue?: number;
  onChange?: (value: number) => void;
}

const VolumeControl: React.FC<VolumeControlProps> = ({
  initialValue = 50,
  onChange
}) => {
  const [volume, setVolume] = useState(initialValue);
  const sliderRef = useRef<HTMLModusWcSliderElement>(null);
  
  // Set up event listener for slider changes
  useEffect(() => {
    const slider = sliderRef.current;
    
    if (slider) {      const handleChange = (e: Event) => {
        // Get the value from the input element target
        const input = e.target as HTMLInputElement;
        const newValue = Number(input.value);
        
        console.log('Slider value changed:', newValue);
        setVolume(newValue);
        
        // Notify parent component if callback provided
        if (onChange) {
          onChange(newValue);
        }
      };
      
      slider.addEventListener('inputChange', handleChange as EventListener);
      
      return () => {
        slider.removeEventListener('inputChange', handleChange as EventListener);
      };
    }
  }, [onChange]);
  
  return (
    <div className="volume-control">
      <div className="slider-container" style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
        <ModusWcSlider
          ref={sliderRef}
          label="Volume"
          min={0}
          max={100}
          step={1}
          value={volume}
          size="md"
        />
        <span className="volume-display" style={{ 
          minWidth: '40px',
          fontWeight: 'bold',
          textAlign: 'right'
        }}>
          {volume}%
        </span>
      </div>
      
      <div className="volume-presets" style={{ marginTop: '16px' }}>
        <button 
          onClick={() => setVolume(0)} 
          style={{ padding: '4px 8px', marginRight: '8px' }}
        >
          Mute
        </button>
        <button 
          onClick={() => setVolume(25)} 
          style={{ padding: '4px 8px', marginRight: '8px' }}
        >
          25%
        </button>
        <button 
          onClick={() => setVolume(50)} 
          style={{ padding: '4px 8px', marginRight: '8px' }}
        >
          50%
        </button>
        <button 
          onClick={() => setVolume(75)} 
          style={{ padding: '4px 8px', marginRight: '8px' }}
        >
          75%
        </button>
        <button 
          onClick={() => setVolume(100)} 
          style={{ padding: '4px 8px' }}
        >
          Max
        </button>
      </div>
    </div>
  );
};

export default VolumeControl;
```

**Notes:**
- The `value` property must be a number (not a string) in React
- Use the `min` and `max` properties to define the valid range of values
- The `step` property controls the granularity of the slider values
- Listen for the `inputChange` event to track value changes
- To update the slider programmatically, modify the controlled value state variable
- For accessibility, always provide a meaningful label
- Consider showing the current value numerically alongside the slider for better usability


---

# ModusWcStepper

## Prompt 1
**User Question:** How do I implement a horizontal multi-step process indicator with different status colors for each step?

**Agent Answer:**
References:
- **Properties**: 
  - `steps`: Array of IStepperItem[] objects that define the steps to display
  - `orientation`: The direction of the stepper ("horizontal" | "vertical")
  - `customClass`: Optional CSS class for additional styling
- **Step Item Properties**:
  - `label`: Text label for the step
  - `color`: Color theme ('primary', 'secondary', 'accent', 'info', 'success', 'warning', 'error', 'neutral')
  - `content`: Optional custom content to display in the step indicator (can be text or emoji)
  - `customClass`: Optional custom CSS class for individual step styling
- **Usage Patterns**: Commonly used for multi-step forms, onboarding processes, checkout flows

**TypeScript Example:**
```tsx
import React, { useState } from 'react';
import { ModusWcStepper } from '@trimble-oss/moduswebcomponents-react';

interface StepperItem {
  color?: 'primary' | 'secondary' | 'accent' | 'info' | 'success' | 'warning' | 'error' | 'neutral';
  content?: string;
  customClass?: string;
  label?: string;
}

const CheckoutProcess: React.FC = () => {
  const [currentStep, setCurrentStep] = useState<number>(1);
  
  // Update steps based on current progress
  const getSteps = (): StepperItem[] => {
    return [
      { 
        label: 'Cart', 
        color: currentStep > 0 ? 'success' : 'primary',
      },
      { 
        label: 'Shipping', 
        color: currentStep > 1 ? 'success' : currentStep === 1 ? 'primary' : 'neutral',
      },
      { 
        label: 'Payment', 
        color: currentStep > 2 ? 'success' : currentStep === 2 ? 'primary' : 'neutral',
      },
      { 
        label: 'Confirmation', 
        color: currentStep === 3 ? 'primary' : 'neutral',
      },
    ];
  };

  // For demonstration purposes - advance to next step
  const handleNextStep = () => {
    if (currentStep < 3) {
      setCurrentStep(currentStep + 1);
    }
  };
  
  return (
    <div>
      <ModusWcStepper 
        orientation="horizontal"
        steps={getSteps()}
      />
      
      {/* Content for current step would go here */}
      <div style={{ marginTop: '20px' }}>
        <p>Current step: {currentStep + 1}</p>
        <button onClick={handleNextStep} disabled={currentStep === 3}>
          Next Step
        </button>
      </div>
    </div>
  );
};

export default CheckoutProcess;
```

**Notes:**
- Stepper is a visual-only component and doesn't handle state or navigation logic
- Use state management in your React application to track the current step
- Color properties can be used to indicate completion status ('success' for completed steps)
- For complex content, you can use the `content` property to insert custom indicators or emoji icons


---

# ModusWcSwitch

## Prompt 1
**User Question:** How do I implement a toggle switch for a dark/light theme with proper event handling in React?

**Agent Answer:**
References:
- **Properties**: 
  - `value`: Boolean representing the switch state (true/false)
  - `label`: Text label to display next to the switch
  - `disabled`: Boolean to disable the switch
  - `size`: Size of the switch ("sm" | "md" | "lg")
  - `customClass`: Custom CSS class for additional styling
  - `indeterminate`: Boolean for indeterminate state
  - `required`: Boolean to mark as required in forms
  - `name`: Form input name
  - `inputId`: ID for the input element
  - `inputTabIndex`: Tabindex for the input
- **Events**: 
  - `inputChange`: Emitted when the switch value changes
  - `inputBlur`: Emitted when the switch loses focus
  - `inputFocus`: Emitted when the switch gains focus
- **Usage Patterns**: Commonly used for toggle settings, enabled/disabled states, and theme switching

**TypeScript Example:**
```tsx
import React, { useRef, useEffect, useState } from 'react';
import { ModusWcSwitch } from '@trimble-oss/moduswebcomponents-react';

const ThemeToggle: React.FC = () => {
  // Initialize state based on user preference
  const [isDarkMode, setIsDarkMode] = useState(() => {
    return window.matchMedia('(prefers-color-scheme: dark)').matches;
  });
  
  const switchRef = useRef<HTMLModusWcSwitchElement>(null);
  
  // Apply theme whenever it changes
  useEffect(() => {
    document.body.classList.toggle('dark-theme', isDarkMode);
    
    // Optional: Store preference
    localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
  }, [isDarkMode]);
  
  useEffect(() => {
    const element = switchRef.current;
    if (element) {
      const handleChange = (e: CustomEvent) => {
        setIsDarkMode(e.detail.target.value);
      };
      
      element.addEventListener('inputChange', handleChange as EventListener);
      
      return () => {
        element.removeEventListener('inputChange', handleChange as EventListener);
      };
    }
  }, []);
  
  return (
    <div className="theme-toggle-container">
      <ModusWcSwitch 
        ref={switchRef}
        label="Dark Mode"
        value={isDarkMode}
        size="md"
      />
    </div>
  );
};

export default ThemeToggle;
```

**Notes:**
- When using with React, always implement proper event handling with `useRef` and `useEffect`
- Remember to clean up event listeners in the useEffect return function to prevent memory leaks
- The `value` property is the controlled state of the switch (true = on, false = off)
- Access the new value in the event handler via `e.detail.target.value`
- Consider adding appropriate ARIA attributes for accessibility if not using the label property


---

# ModusWcTable

## Prompt 1
**User Question:** How do I create a sortable data table with pagination in React?

**Agent Answer:**
References:
- **Properties**: 
  - `columns`: Array of column definitions (ITableColumn[]) - **required**
  - `data`: Array of data objects (Record<string, unknown>[]) - **required**
  - `sortable`: Enable sorting functionality (boolean, default: true)
  - `paginated`: Enable pagination (boolean, default: false)
  - `currentPage`: Current page number (number, default: 1)
  - `pageSizeOptions`: Available page sizes (number[], default: [5, 10, 15])
  - `showPageSizeSelector`: Show page size dropdown (boolean, default: true) 
  - `density`: Table density ("comfortable" | "compact" | "relaxed", default: "comfortable")
  - `hover`: Enable row hover effect (boolean, default: true)
  - `zebra`: Enable zebra striping (boolean, default: false)
- **Events**: 
  - `sortChange`: Emitted when sorting changes
  - `paginationChange`: Emitted when page or page size changes
  - `rowClick`: Emitted when a row is clicked
- **Usage Patterns**: Data tables for displaying structured information with sorting, filtering, and pagination

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcTable } from '@trimble-oss/moduswebcomponents-react';

interface User {
  id: string;
  name: string;
  email: string;
  role: string;
}

interface ColumnSort {
  id: string;
  desc: boolean;
}

interface PaginationState {
  currentPage: number;
  pageSize: number;
  totalItems: number;
}

// Hardcoded demo data
const createDemoData = (count = 20): User[] => {
  const data: User[] = [];
  for (let i = 1; i <= count; i++) {
    data.push({
      id: i.toString(),
      name: `User ${i}`,
      email: `user${i}@example.com`,
      role: i % 3 === 0 ? 'Admin' : 'User',
    });
  }
  return data;
};

// Create a larger set of users for our demo
const DEMO_USERS = createDemoData(50);

const UserTable: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [pagination, setPagination] = useState<PaginationState>({
    currentPage: 1,
    pageSize: 10,
    totalItems: DEMO_USERS.length
  });
  
  const tableRef = useRef<HTMLModusWcTableElement>(null);
  
  // Column definitions
  const columns = [
    {
      id: 'id',
      header: 'ID',
      accessor: 'id',
      width: '80px',
      sortable: true
    },
    {
      id: 'name',
      header: 'Full Name',
      accessor: 'name',
      sortable: true
    },
    {
      id: 'email',
      header: 'Email Address',
      accessor: 'email',
      sortable: true
    },
    {
      id: 'role',
      header: 'Role',
      accessor: 'role',
      sortable: false,
      cellRenderer: (value: unknown) => {
        const span = document.createElement('span');
        span.textContent = value as string;
        
        // Apply styling based on role
        if (value === 'Admin') {
          span.style.fontWeight = 'bold';
          span.style.color = '#0063a3';
        }
        
        return span;
      }
    }
  ];
  
  // Fetch users on component mount
  useEffect(() => {
    fetchUsers();
  }, []);
  
  // Set up event listeners
  useEffect(() => {
    const element = tableRef.current;
    if (element) {
      const handleSortChange = (e: CustomEvent<ColumnSort[]>) => {
        const sortConfig = e.detail[0];
        if (sortConfig) {
          fetchUsers(sortConfig.id, sortConfig.desc ? 'desc' : 'asc');
        }
      };
      
      const handlePaginationChange = (e: CustomEvent) => {
        const { currentPage, pageSize } = e.detail;
        setPagination(prev => ({ ...prev, currentPage, pageSize }));
        fetchUsers(undefined, undefined, currentPage, pageSize);
      };
      
      element.addEventListener('sortChange', handleSortChange as EventListener);
      element.addEventListener('paginationChange', handlePaginationChange as EventListener);
      
      return () => {
        element.removeEventListener('sortChange', handleSortChange as EventListener);
        element.removeEventListener('paginationChange', handlePaginationChange as EventListener);
      };
    }
  }, []);
  
  // Mock data handling - simulates API functionality
  const fetchUsers = (
    sortBy: string = 'id',
    sortOrder: string = 'asc',
    page: number = pagination.currentPage,
    pageSize: number = pagination.pageSize
  ) => {
    setLoading(true);
    
    // Simulate API delay
    setTimeout(() => {
      try {
        // Sort the data
        const sortedData = [...DEMO_USERS].sort((a, b) => {
          const aValue = a[sortBy as keyof User];
          const bValue = b[sortBy as keyof User];
          
          if (sortOrder === 'asc') {
            return aValue > bValue ? 1 : aValue < bValue ? -1 : 0;
          } else {
            return aValue < bValue ? 1 : aValue > bValue ? -1 : 0;
          }
        });
        
        // Calculate pagination
        const startIndex = (page - 1) * pageSize;
        const paginatedData = sortedData.slice(startIndex, startIndex + pageSize);
        
        setUsers(paginatedData);
        setPagination({
          currentPage: page,
          pageSize: pageSize,
          totalItems: DEMO_USERS.length
        });
      } catch (error) {
        console.error('Error processing users:', error);
      } finally {
        setLoading(false);
      }
    }, 300); // Simulate network delay
  };
  
  return (
    <div className="user-table-container">
      <h2>User Management</h2>
      
      {loading ? (
        <div className="loading-indicator">Loading...</div>
      ) : (
        <ModusWcTable
          ref={tableRef}
          columns={columns}
          data={users}
          sortable={true}
          paginated={true}
          currentPage={pagination.currentPage}
          pageSizeOptions={[5, 10, 20, 50]}
          showPageSizeSelector={true}
          density="comfortable"
          hover={true}
          totalItems={pagination.totalItems}
        />
      )}
    </div>
  );
};

export default UserTable;
```

**Notes:**
- The `columns` array defines the structure of the table with each column having an `id`, `header`, and `accessor` property
- Use the `sortable` property to enable column sorting (both at table and column level)
- For custom cell rendering, use the `cellRenderer` function
- For server-side sorting and pagination, handle the events and make API calls with the appropriate parameters
- The pagination UI is automatically generated when `paginated` is true


---

# ModusWcTabs

## Prompt 1
**User Question:** How do I create a tabbed interface with content panels in React?

**Agent Answer:**
References:
- **Properties**: 
  - `tabs`: Array of tab objects to display (ITab[])
  - `activeTabIndex`: Index of the currently active tab (number, default: 0)
  - `tabStyle`: Visual style of tabs ("bordered" | "boxed" | "lifted" | "none", default: "bordered")
  - `size`: Size of the tabs ("sm" | "md" | "lg", default: "md")
  - `customClass`: Custom CSS class
- **Tab Object Properties**: 
  - `label`: Text content of the tab
  - `icon`: Icon name for tab
  - `iconPosition`: Where the icon appears ("left" | "right")
  - `disabled`: Whether tab is disabled
  - `customClass`: Custom CSS class for the tab
- **Events**: 
  - `tabChange`: Emitted when active tab changes, includes previous and new tab indices
- **Usage Patterns**: Content organization, workflow steps, settings panels

**TypeScript Example:**
```tsx
import React, { useRef, useEffect, useState } from 'react';
import { ModusWcTabs } from '@trimble-oss/moduswebcomponents-react';

interface ITab {
  label?: string;
  icon?: string;
  iconPosition?: 'left' | 'right';
  disabled?: boolean;
  customClass?: string;
}

const SettingsTabs: React.FC = () => {
  const [activeTab, setActiveTab] = useState<number>(0);
  const tabsRef = useRef<HTMLModusWcTabsElement>(null);
  
  // Define tabs
  const tabs: ITab[] = [
    { label: 'Account', icon: 'person', iconPosition: 'left' },
    { label: 'Notifications', icon: 'bell', iconPosition: 'left' },
    { label: 'Privacy', icon: 'shield', iconPosition: 'left' }
  ];
  
  // Set up event listeners
  useEffect(() => {
    const element = tabsRef.current;
    
    if (element) {
      const handleTabChange = (e: CustomEvent<{ previousTab: number; newTab: number }>) => {
        setActiveTab(e.detail.newTab);
        
        // You might want to perform additional actions when tab changes
        console.log(`Tab changed from ${e.detail.previousTab} to ${e.detail.newTab}`);
      };
      
      element.addEventListener('tabChange', handleTabChange as EventListener);
      
      return () => {
        element.removeEventListener('tabChange', handleTabChange as EventListener);
      };
    }
  }, []);
  
  return (
    <div className="settings-container">
      <h2>User Settings</h2>
      
      <ModusWcTabs
        ref={tabsRef}
        tabs={tabs}
        activeTabIndex={activeTab}
        tabStyle="boxed"
        size="md"
      >
        {/* Account Settings Tab Content */}
        <div slot="tab-0">
          <h3>Account Settings</h3>
          <form onSubmit={(e) => e.preventDefault()}>
            <div className="form-group">
              <label htmlFor="username">Username</label>
              <input id="username" type="text" defaultValue="currentuser" />
            </div>
            
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input id="email" type="email" defaultValue="user@example.com" />
            </div>
            
            <button type="submit">Save Account Settings</button>
          </form>
        </div>
        
        {/* Notifications Tab Content */}
        <div slot="tab-1">
          <h3>Notification Preferences</h3>
          <div className="settings-group">
            {/* Using other Modus components within the tab panel */}
            <div className="setting-item">
              <label className="setting-label">Email Notifications</label>
              <input type="checkbox" defaultChecked={true} />
            </div>
            
            <div className="setting-item">
              <label className="setting-label">Push Notifications</label>
              <input type="checkbox" defaultChecked={false} />
            </div>
          </div>
        </div>
        
        {/* Privacy Tab Content */}
        <div slot="tab-2">
          <h3>Privacy Settings</h3>
          <div className="settings-group">
            <p>Manage your privacy settings and data sharing preferences.</p>
            
            <div className="setting-item">
              <label className="setting-label">Share Usage Data</label>
              <input type="checkbox" defaultChecked={true} />
            </div>
            
            <div className="setting-item">
              <label className="setting-label">Allow Third-Party Cookies</label>
              <input type="checkbox" defaultChecked={false} />
            </div>
          </div>
        </div>
      </ModusWcTabs>
    </div>
  );
};

export default SettingsTabs;
```

**Notes:**
- Use slot names with format `tab-{index}` to associate content with tabs (`tab-0`, `tab-1`, etc.)
- The active tab's content is displayed while others are hidden automatically
- For dynamic tab content, use state management in combination with the `activeTabIndex` prop
- Tab styles options include "bordered" (default), "boxed", "lifted", and "none"
- Icons can be placed on either side of tab label or used alone


---

# ModusWcTextInput

## Prompt 1
**User Question:** How do I create a form with validation using text inputs in React?

**Agent Answer:**
References:
- **Properties**: 
  - `value`: Input value (controlled component) (string)
  - `label`: Text label for the input (string)
  - `type`: Input type ("text", "email", "password", etc.)
  - `required`: Whether input is required (boolean)
  - `pattern`: Regex pattern for validation (string)
  - `minLength`/`maxLength`: Text length constraints (number)
  - `placeholder`: Placeholder text (string)
  - `feedback`: Validation feedback object `{level: 'error'|'info'|'success'|'warning', message: string}`
  - `size`: Input size ("sm", "md", "lg")
  - `disabled`: Disable the input (boolean)
  - `readOnly`: Make input read-only (boolean)
  - `bordered`: Show border around input (boolean)
- **Events**: 
  - `inputChange`: Emitted when value changes
  - `inputBlur`: Emitted when input loses focus
  - `inputFocus`: Emitted when input gains focus
- **Usage Patterns**: Forms, search inputs, login/registration forms, data entry

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcTextInput } from '@trimble-oss/moduswebcomponents-react';

interface IFeedback {
  level: 'error' | 'info' | 'success' | 'warning';
  message: string;
}

interface FormData {
  name: string;
  email: string;
  password: string;
}

const RegistrationForm: React.FC = () => {
  // Form state
  const [formData, setFormData] = useState<FormData>({
    name: '',
    email: '',
    password: ''
  });
  
  // Feedback state
  const [nameFeedback, setNameFeedback] = useState<IFeedback | undefined>();
  const [emailFeedback, setEmailFeedback] = useState<IFeedback | undefined>();
  const [passwordFeedback, setPasswordFeedback] = useState<IFeedback | undefined>();
  
  // Input refs
  const nameInputRef = useRef<HTMLModusWcTextInputElement>(null);
  const emailInputRef = useRef<HTMLModusWcTextInputElement>(null);
  const passwordInputRef = useRef<HTMLModusWcTextInputElement>(null);
  
  // Set up event handlers
  useEffect(() => {
    const setupInputListeners = (
      ref: React.RefObject<HTMLModusWcTextInputElement>,
      fieldName: keyof FormData,
      validate: () => void
    ) => {
      const element = ref.current;
      if (element) {
        const handleChange = (e: CustomEvent) => {
          setFormData(prev => ({
            ...prev,
            [fieldName]: e.detail.target.value
          }));
        };
        
        const handleBlur = () => {
          validate();
        };
        
        element.addEventListener('inputChange', handleChange as EventListener);
        element.addEventListener('inputBlur', handleBlur as EventListener);
        
        return () => {
          element.removeEventListener('inputChange', handleChange as EventListener);
          element.removeEventListener('inputBlur', handleBlur as EventListener);
        };
      }
      return undefined;
    };
    
    const cleanupFuncs = [
      setupInputListeners(nameInputRef, 'name', validateName),
      setupInputListeners(emailInputRef, 'email', validateEmail),
      setupInputListeners(passwordInputRef, 'password', validatePassword)
    ];
    
    return () => {
      cleanupFuncs.forEach(cleanup => cleanup && cleanup());
    };
  }, [formData]);
  
  // Validation functions
  const validateName = (): boolean => {
    if (!formData.name) {
      setNameFeedback({
        level: 'error',
        message: 'Name is required'
      });
      return false;
    } else if (!/^[a-zA-Z ]+$/.test(formData.name)) {
      setNameFeedback({
        level: 'error',
        message: 'Name should contain only letters and spaces'
      });
      return false;
    } else {
      setNameFeedback(undefined);
      return true;
    }
  };
  
  const validateEmail = (): boolean => {
    if (!formData.email) {
      setEmailFeedback({
        level: 'error',
        message: 'Email is required'
      });
      return false;
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      setEmailFeedback({
        level: 'error',
        message: 'Please enter a valid email address'
      });
      return false;
    } else {
      setEmailFeedback(undefined);
      return true;
    }
  };
  
  const validatePassword = (): boolean => {
    if (!formData.password) {
      setPasswordFeedback({
        level: 'error',
        message: 'Password is required'
      });
      return false;
    } else if (formData.password.length < 8) {
      setPasswordFeedback({
        level: 'error',
        message: 'Password must be at least 8 characters'
      });
      return false;
    } else {
      setPasswordFeedback({
        level: 'success',
        message: 'Password strength: Good'
      });
      return true;
    }
  };
  
  // Form submission handler
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    const nameValid = validateName();
    const emailValid = validateEmail();
    const passwordValid = validatePassword();
    
    if (nameValid && emailValid && passwordValid) {
      // Submit the form data
      console.log('Form submitted with:', formData);
      
      // In a real application, you would make an API call here
      submitRegistration(formData);
    }
  };
  
  // Mock API call
  const submitRegistration = async (data: FormData) => {
    try {
      // Replace with actual API endpoint
      await fetch('/api/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      
      // Handle successful registration
      console.log('Registration successful!');
    } catch (error) {
      console.error('Registration failed:', error);
    }
  };
  
  return (
    <form onSubmit={handleSubmit} className="registration-form">
      <h2>Create an Account</h2>
      
      <div className="form-field">
        <ModusWcTextInput
          ref={nameInputRef}
          label="Full Name"
          required={true}
          pattern="^[a-zA-Z ]+$"
          placeholder="Enter your full name"
          value={formData.name}
          feedback={nameFeedback}
        />
      </div>
      
      <div className="form-field">
        <ModusWcTextInput
          ref={emailInputRef}
          label="Email Address"
          type="email"
          required={true}
          placeholder="Enter your email"
          value={formData.email}
          feedback={emailFeedback}
        />
      </div>
      
      <div className="form-field">
        <ModusWcTextInput
          ref={passwordInputRef}
          label="Password"
          type="password"
          minLength={8}
          required={true}
          placeholder="Create a password"
          value={formData.password}
          feedback={passwordFeedback}
        />
      </div>
      
      <div className="form-actions">
        <button type="submit" className="submit-button">
          Register
        </button>
      </div>
    </form>
  );
};

export default RegistrationForm;
```

**Notes:**
- Always use the appropriate input type ("email", "password", etc.) for better user experience and built-in validation
- The `feedback` property accepts an object with `level` and `message` to show validation state
- Validation can be performed both on blur and on input change, depending on the UX requirements
- In React applications, maintain a state for form data and feedback messages
- Use refs to access the web component's DOM methods and event listeners
- Don't forget to clean up event listeners in your React components to avoid memory leaks
- The input follows the controlled component pattern in React, where value is managed in state


---

# ModusWcTextarea

## Prompt 1
**User Question:** How do I create a multiline text input field with validation for a feedback form using the ModusWcTextarea component?

**Agent Answer:**
References:
- **Properties**:
  - `bordered` (boolean): Determines if the textarea has a border
  - `disabled` (boolean): Disables the textarea input
  - `feedback` (object): Provides validation feedback with properties:
    - `level` ('error' | 'info' | 'success' | 'warning'): The feedback type
    - `message` (string): The feedback message text
  - `label` (string): Label text for the textarea
  - `max-length` (number): Maximum character length allowed
  - `placeholder` (string): Placeholder text displayed when no value exists
  - `readonly` (boolean): Makes the textarea read-only
  - `required` (boolean): Marks the textarea as required
  - `rows` (number): Number of visible text lines
  - `size` ('sm' | 'md' | 'lg'): Size of the textarea
  - `value` (string): The current value of the textarea

- **Events**:
  - `inputChange`: Fired when the textarea value changes
  - `inputBlur`: Fired when the textarea loses focus
  - `inputFocus`: Fired when the textarea gains focus

- **Usage Patterns**:
  - Controlled component pattern with state management
  - Form input validation with feedback messaging
  - Form submission handling

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcTextarea } from '@trimble-oss/moduswebcomponents-react';

interface FeedbackFormProps {
  // No props needed for now
}

const FeedbackForm: React.FC<FeedbackFormProps> = () => {
  const [feedback, setFeedback] = useState('');
  const [validationState, setValidationState] = useState<{
    level: 'error' | 'success' | 'info' | 'warning' | null,
    message?: string
  }>({ level: null });
  
  const textareaRef = useRef<HTMLModusWcTextareaElement>(null);
  
  const handleChange = (e: CustomEvent) => {
    const newValue = e.detail.target.value;
    setFeedback(newValue);
    
    // Validation logic
    if (newValue.trim().length < 10) {
      setValidationState({
        level: 'error',
        message: 'Please provide at least 10 characters of feedback'
      });
    } else {
      setValidationState({
        level: 'success',
        message: 'Thank you for your detailed feedback'
      });
    }
  };
  
  const handleLogFeedback = () => {
    console.log('Current feedback:', feedback);
  };
  
  useEffect(() => {
    const element = textareaRef.current;
    if (element) {
      element.addEventListener('inputChange', handleChange as EventListener);
      
      return () => {
        element.removeEventListener('inputChange', handleChange as EventListener);
      };
    }
  }, []);
  
  return (
    <div>
      <ModusWcTextarea
        ref={textareaRef}
        aria-label="Feedback comments"
        bordered
        {...(validationState.level !== null && { 
          feedback: {
            level: validationState.level,
            message: validationState.message
          }
        })}
        label="Your Feedback"
        max-length={500}
        placeholder="Please provide your detailed feedback here..."
        required
        rows={5}
        size="md"
        value={feedback}
      />
      <button 
        type="button" 
        onClick={handleLogFeedback} 
        disabled={validationState.level === 'error'}
      >
        Log Feedback
      </button>
    </div>
  );
};

export default FeedbackForm;
```

**Notes:**
- Always handle form validation with both client-side and server-side checks
- Remember to provide meaningful error messages to guide users
- Use `max-length` to prevent overly long submissions
- The controlled component pattern ensures your application state stays in sync with the textarea
- Setting appropriate `rows` helps users understand the expected length of input


---

# ModusWcThemeSwitcher

## Prompt 1
**User Question:** How do I implement a theme switcher to toggle between light and dark modes in my application?

**Agent Answer:**
References:
- **Properties**: 
  - `custom-class` (string): Custom CSS class to apply to the theme switcher element
- **Events**: 
  - `themeChange`: Fires when the theme is changed, emitting a CustomEvent with IThemeConfig data
- **Usage Patterns**: 
  - Must be used with a `modus-wc-theme-provider` parent component
  - Automatically handles theme toggling between light and dark modes
  - Persists theme preferences in local storage

**TypeScript Example:**
```tsx
import React, { useEffect, useRef } from 'react';
import { 
  ModusWcThemeProvider, 
  ModusWcThemeSwitcher 
} from '@trimble-oss/moduswebcomponents-react';

// Import the CSS
import '@trimble-oss/moduswebcomponents/modus-wc-styles.css';

interface IThemeConfig {
  theme: string;
  mode: 'light' | 'dark';
}

const App: React.FC = () => {
  const themeSwitcherRef = useRef<HTMLModusWcThemeSwitcherElement>(null);
  
  useEffect(() => {
    const themeSwitcher = themeSwitcherRef.current;
    if (themeSwitcher) {
      const handleThemeChange = (e: CustomEvent<IThemeConfig>) => {
        const newTheme = e.detail;
        console.log('Theme changed to:', newTheme);
        
        // You can perform additional theme-related actions here
        updateThemeDependentUI(newTheme);
      };
      
      themeSwitcher.addEventListener('themeChange', handleThemeChange as EventListener);
      
      return () => {
        themeSwitcher.removeEventListener('themeChange', handleThemeChange as EventListener);
      };
    }
  }, []);
  
  const updateThemeDependentUI = (themeConfig: IThemeConfig) => {
    // Example: Update chart colors or other theme-dependent UI elements
    const isDarkMode = themeConfig.mode === 'dark';
    // Apply theme-specific adjustments to components
  };
  
  return (
    <ModusWcThemeProvider 
      initialTheme={{ theme: 'modus-modern-light' }}
    >
      <div className="app-container">
        <header className="app-header">
          <h1>My React Application</h1>
          <ModusWcThemeSwitcher
            ref={themeSwitcherRef}
            aria-label="Toggle light/dark theme"
          />
        </header>
        
        <main className="content">
          <h2>Welcome to my React app</h2>
          <p>This app automatically handles theme switching.</p>
        </main>
      </div>
    </ModusWcThemeProvider>
  );
};

export default App;
```

**Notes:**
- The theme switcher must always be used within a `modus-wc-theme-provider` component
- The theme provider accepts an `initialTheme` object to set the default theme
- Available theme options are:
  - `modus-modern-light` (default)
  - `modus-modern-dark` 
  - `modus-classic-light`
  - `modus-classic-dark`
- Theme preferences are automatically saved in local storage under the `modus-theme-config` key
- The theme switcher automatically detects and respects the user's system preference for dark/light mode
- For accessibility, always include an aria-label on the theme switcher component

---

# ModusWcTimeInput

## Prompt 1
**User Question:** How can I implement a simple time picker input with validation in a React application using the Modus Time Input component?

**Agent Answer:**
References:
- **Properties**: 
  - `value`: string - The value of the time input (format: 'HH:mm' or 'HH:mm:ss')
  - `label`: string - Text label for the input
  - `min`: string - Minimum time value (format: 'HH:mm' or 'HH:mm:ss')
  - `max`: string - Maximum time value (format: 'HH:mm' or 'HH:mm:ss')
  - `required`: boolean - Whether a value is required
  - `disabled`: boolean - Whether the control is disabled
  - `showSeconds`: boolean - Display seconds in the time format
  - `feedback`: IInputFeedbackProp - Validation feedback object
  - `size`: "sm" | "md" | "lg" - The size of the input

- **Events**: 
  - `inputChange`: CustomEvent<Event> - Fired when the input value changes
  - `inputBlur`: CustomEvent<FocusEvent> - Fired when the input loses focus
  - `inputFocus`: CustomEvent<FocusEvent> - Fired when the input gains focus

- **Usage Patterns**: 
  - Creating controlled time inputs with validation
  - Implementing time range restrictions (min/max)
  - Handling time selection in forms

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { ModusWcTimeInput } from '@trimble-oss/moduswebcomponents-react';

interface AppointmentFormProps {
  onSubmit: (time: string) => void;
}

const AppointmentForm: React.FC<AppointmentFormProps> = ({ onSubmit }) => {
  const [time, setTime] = useState('');
  const [isValid, setIsValid] = useState(true);
  const [errorMessage, setErrorMessage] = useState('');
  const timeInputRef = useRef<HTMLModusWcTimeInputElement>(null);
  
  useEffect(() => {
    const timeInput = timeInputRef.current;
    
    if (!timeInput) return;
    
    const handleTimeChange = (e: CustomEvent<Event>) => {
      const target = e.target as HTMLModusWcTimeInputElement;
      const newTime = target.value;
      setTime(newTime);
      
      // Validate business hours (9 AM - 5 PM)
      if (newTime) {
        const [hours] = newTime.split(':').map(Number);
        
        if (hours < 9 || hours >= 17) {
          setIsValid(false);
          setErrorMessage('Please select a time between 9:00 AM and 5:00 PM');
        } else {
          setIsValid(true);
          setErrorMessage('');
        }
      }
    };
    
    timeInput.addEventListener('inputChange', handleTimeChange);
    
    return () => {
      timeInput.removeEventListener('inputChange', handleTimeChange);
    };
  }, []);
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (time && isValid) {
      onSubmit(time);
    }
  };
  
  return (
    <form onSubmit={handleSubmit}>
      <ModusWcTimeInput
        ref={timeInputRef}
        label="Appointment Time"
        min="09:00"
        max="17:00"
        required={true}
        value={time}
        feedback={!isValid ? { level: 'error', message: errorMessage } : undefined}
      />
      
      <button 
        type="submit" 
        disabled={!time || !isValid}
        style={{ marginTop: '1rem' }}
      >
        Schedule Appointment
      </button>
    </form>
  );
};

export default AppointmentForm;
```

**Notes:**
- Always implement the controlled component pattern with React, keeping the time value in state
- The time input uses 24-hour format by default ('HH:mm' or 'HH:mm:ss')
- Use the `feedback` property to provide validation messages to the user
- Setting `min` and `max` properties helps restrict the time selection range
- Remember to clean up event listeners in the useEffect hook to prevent memory leaks
- For accessible forms, include a descriptive label for the time input


---

# ModusWcToast

## Prompt 1
**User Question:** How can I implement a simple toast notification system using the Modus Toast component in my React application?

**Agent Answer:**
References:
- **Properties**: 
  - `customClass`: string - Additional classes for custom styling
  - `delay`: number - Time in milliseconds before toast is automatically dismissed
  - `position`: "top-start" | "top-center" | "top-end" | "middle-start" | "middle-center" | "middle-end" | "bottom-start" | "bottom-center" | "bottom-end" - The position of the toast

- **Usage Patterns**: 
  - Toast container for notifications
  - Positioning feedback messages on the page
  - Displaying temporary alerts with auto-dismissal

**TypeScript Example:**
```tsx
import React, { useState, useRef, useEffect } from 'react';
import { 
  ModusWcToast, 
  ModusWcAlert 
} from '@trimble-oss/moduswebcomponents-react';

interface ToastMessage {
  id: string;
  title: string;
  message: string;
  variant: 'success' | 'danger' | 'warning' | 'info';
  duration?: number;
}

const ToastNotificationSystem: React.FC = () => {
  const [toasts, setToasts] = useState<ToastMessage[]>([]);
  const toastContainerRef = useRef<HTMLDivElement>(null);

  const addToast = (toast: Omit<ToastMessage, 'id'>) => {
    const id = Math.random().toString(36).substring(2, 9);
    setToasts(prev => [...prev, { ...toast, id }]);
    
    // Auto-remove toast after specified duration
    if (toast.duration) {
      setTimeout(() => {
        removeToast(id);
      }, toast.duration);
    }
  };

  const removeToast = (id: string) => {
    setToasts(prev => prev.filter(toast => toast.id !== id));
  };

  // Example usage
  useEffect(() => {
    // Add a welcome toast when component mounts
    addToast({
      title: 'Welcome',
      message: 'Application loaded successfully',
      variant: 'success',
      duration: 5000
    });
  }, []);

  // Demonstrate different toast notifications
  const handleAddSuccessToast = () => {
    addToast({
      title: 'Success!',
      message: 'Operation completed successfully',
      variant: 'success',
      duration: 5000
    });
  };

  const handleAddErrorToast = () => {
    addToast({
      title: 'Error',
      message: 'Something went wrong. Please try again.',
      variant: 'danger',
      duration: 8000
    });
  };

  return (
    <div>
      <div className="actions">
        <button onClick={handleAddSuccessToast}>Show Success Toast</button>
        <button onClick={handleAddErrorToast}>Show Error Toast</button>
      </div>

      {/* Toast container with fixed positioning */}
      <div ref={toastContainerRef} style={{ height: '100vh', position: 'relative' }}>
        {toasts.map((toast) => (
          <ModusWcToast
            key={toast.id}
            position="top-end"
            delay={toast.duration}
            customClass="custom-toast"
          >
            <ModusWcAlert
              variant={toast.variant}
              alertTitle={toast.title}
              dismissible={true}
              onDismiss={() => removeToast(toast.id)}
            >
              {toast.message}
            </ModusWcAlert>
          </ModusWcToast>
        ))}
      </div>
    </div>
  );
};

export default ToastNotificationSystem;
```

**Notes:**
- The ModusWcToast component is a container that positions content in a specific location on the screen
- Use ModusWcAlert inside ModusWcToast to create toast notifications with appropriate styling
- The toast component doesn't have built-in dismiss functionality; implement this in your slotted content
- For auto-dismissal, use the `delay` property to automatically remove the toast after a specified time
- When managing multiple toasts, assign unique keys and maintain toast state in your React component
- Position the toast container with a relative or fixed position and sufficient height for proper rendering
- For accessibility, ensure your toast alerts have appropriate ARIA labels and roles


---

# ModusWcToolbar

## Prompt 1
**User Question:** How do I create a toolbar with different sections in a Modus application using React?

**Agent Answer:**
References:
- **Properties**: 
  - `customClass` (string, optional): Custom CSS class to apply to the toolbar for additional styling.
- **Slots**:
  - `start`: Content to be placed at the start of the toolbar
  - `center`: Content to be placed in the center of the toolbar
  - `end`: Content to be placed at the end of the toolbar
- **Usage Patterns**: 
  - Page-level navigation controls
  - Action buttons organization
  - Search and filter controls placement

**TypeScript Example:**
```tsx
import React from 'react';
import { ModusWcToolbar } from '@trimble-oss/moduswebcomponents-react';

interface AppToolbarProps {
  title: string;
  onSearch: (query: string) => void;
  onSettingsClick: () => void;
}

const AppToolbar: React.FC<AppToolbarProps> = ({ title, onSearch, onSettingsClick }) => {
  return (
    <ModusWcToolbar customClass="app-main-toolbar">
      <div slot="start">
        <button onClick={() => window.history.back()}>Back</button>
        <button onClick={() => window.history.forward()}>Forward</button>
      </div>
      
      <div slot="center">
        <h3>{title}</h3>
      </div>
      
      <div slot="end">
        <input 
          type="search" 
          placeholder="Search..."
          onChange={(e) => onSearch(e.target.value)}
        />
        <button onClick={onSettingsClick}>Settings</button>
      </div>
    </ModusWcToolbar>
  );
};

export default AppToolbar;
```

**Notes:**
- The toolbar provides a flexible layout system using slots to organize content areas
- Use CSS for fine-tuning spacing between elements within each slot
- Often used in conjunction with ModusWcNavbar for complete application navigation
- For responsive designs, consider content priority and hiding less important elements on smaller screens


---

# ModusWcTooltip

## Prompt 1
**User Question:** How do I add tooltips to UI elements in my React application using Modus components?

**Agent Answer:**
References:
- **Properties**: 
  - `content` (string): The text content displayed in the tooltip
  - `position` ("auto" | "top" | "right" | "bottom" | "left"): Tooltip position relative to the target element, default is "auto"
  - `disabled` (boolean): When true, prevents the tooltip from being displayed
  - `forceOpen` (boolean): Forces the tooltip to remain open when true
  - `customClass` (string): Custom CSS class for additional styling
  - `tooltipId` (string): ID for the tooltip element, useful for accessibility with aria-describedby
- **Usage Patterns**: 
  - Providing additional context for UI elements
  - Displaying help text for form fields
  - Explaining icons or buttons with minimal visual space

**TypeScript Example:**
```tsx
import React, { useState } from 'react';
import { ModusWcTooltip, ModusWcButton } from '@trimble-oss/moduswebcomponents-react';

interface TooltipDemoProps {
  showHelpTooltips: boolean;
}

const TooltipDemo: React.FC<TooltipDemoProps> = ({ showHelpTooltips }) => {
  const [isHovered, setIsHovered] = useState(false);
  
  return (
    <div className="tooltip-examples">
      {/* Basic tooltip */}
      <ModusWcTooltip content="Click to submit the form" position="top">
        <ModusWcButton color="primary">Submit</ModusWcButton>
      </ModusWcTooltip>
      
      {/* Tooltip with accessibility enhancement */}
      <div className="form-field">
        <ModusWcTooltip 
          content="Enter a valid email address" 
          position="right" 
          tooltipId="email-help-tooltip"
        >
          <label htmlFor="email-input">
            Email
            <span className="help-icon">?</span>
          </label>
        </ModusWcTooltip>
        <input 
          type="email" 
          id="email-input" 
          aria-describedby="email-help-tooltip" 
        />
      </div>
      
      {/* Conditionally disabled tooltip */}
      <ModusWcTooltip 
        content="This feature requires administrator access" 
        disabled={!showHelpTooltips}
      >
        <ModusWcButton color="secondary" disabled={true}>
          Admin Settings
        </ModusWcButton>
      </ModusWcTooltip>
      
      {/* Programmatically controlled tooltip */}
      <ModusWcTooltip 
        content="Click anywhere to close" 
        forceOpen={isHovered}
        position="bottom"
      >
        <ModusWcButton
          color="tertiary"
          onClick={() => setIsHovered(!isHovered)}
        >
          {isHovered ? 'Close Tooltip' : 'Show Tooltip'}
        </ModusWcButton>
      </ModusWcTooltip>
    </div>
  );
};

export default TooltipDemo;
```

**Notes:**
- Tooltips appear when users hover over or focus on the wrapped element
- For accessibility, use tooltipId with aria-describedby to associate the tooltip with form elements
- Tooltips should be concise and provide additional context, not essential information
- The forceOpen property is useful for tutorial flows or demonstrating functionality
- Avoid using tooltips for critical information that users need to complete a task


---

# ModusWcTypography

## Prompt 1
**User Question:** How do I use the Typography component in my Modus application to ensure consistent text styling across my UI?

**Agent Answer:**
References:
- **Properties**: 
  - `variant` ("body" | "h1" | "h2" | "h3" | "h4" | "h5" | "h6" | "p"): Specifies the HTML element to render
  - `size` ("xs" | "sm" | "md" | "lg"): Controls text size, default is "md"
  - `weight` ("light" | "normal" | "semibold" | "bold"): Controls text weight, default is "normal"
  - `customClass` (string): Optional CSS class for additional styling
- **Usage Patterns**: 
  - Page headings and section titles
  - Body text and paragraphs
  - Featured text with custom styling

**TypeScript Example:**
```tsx
import React from 'react';
import { ModusWcTypography } from '@trimble-oss/modus-web-components-react';

interface ContentSectionProps {
  title: string;
  subtitle?: string;
  body: string;
  lastUpdated?: Date;
}

const ContentSection: React.FC<ContentSectionProps> = ({ 
  title, 
  subtitle, 
  body,
  lastUpdated 
}) => {
  // Format the date if provided
  const formattedDate = lastUpdated 
    ? new Intl.DateTimeFormat('en-US', { 
        dateStyle: 'medium', 
        timeStyle: 'short' 
      }).format(lastUpdated)
    : null;
  
  return (
    <section className="content-section">
      <ModusWcTypography variant="h2" weight="bold" size="lg">
        {title}
      </ModusWcTypography>
      
      {subtitle && (
        <ModusWcTypography variant="h3" weight="semibold" size="md">
          {subtitle}
        </ModusWcTypography>
      )}
      
      <ModusWcTypography variant="p" size="md">
        {body}
      </ModusWcTypography>
      
      {formattedDate && (
        <ModusWcTypography 
          variant="body" 
          size="xs" 
          weight="light"
          customClass="timestamp-text"
        >
          Last updated: {formattedDate}
        </ModusWcTypography>
      )}
    </section>
  );
};

export default ContentSection;
```

**Notes:**
- Use the Typography component consistently throughout your application for a unified text appearance
- Heading variants (h1-h6) automatically apply semantic HTML markup for proper document structure
- Maintain a hierarchy with headings for better accessibility and SEO
- Size and weight can be adjusted independently of the variant to achieve the desired visual styling
- For custom text styles that extend beyond the component's properties, use the customClass property


---

