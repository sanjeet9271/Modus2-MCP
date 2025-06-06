# Modus React Component Patterns

> **LEAD LEVEL GUIDANCE**: This document provides React-specific patterns for implementing Modus components effectively.

## Component Implementation Patterns

### ModusButton

```jsx
import { ModusButton } from '@trimble-oss/modus-react-components';
import { useRef, useEffect } from 'react';

const Button = () => {
  const buttonRef = useRef(null);
  
  useEffect(() => {
    if (buttonRef.current) {
      buttonRef.current.addEventListener('buttonClick', handleClick);
      return () => {
        buttonRef.current?.removeEventListener('buttonClick', handleClick);
      };
    }
  }, []);
  
  const handleClick = () => {
    console.log('Button clicked');
  };
  
  return (
    <ModusButton 
      ref={buttonRef} 
      color="primary" 
      type="button"
    >
      Click Me
    </ModusButton>
  );
};
```

### ModusNavbar

```jsx
import { ModusNavbar } from '@trimble-oss/modus-react-components';
import { useRef, useEffect, useContext } from 'react';
import { NavigationContext } from '../../context/NavigationContext';

const Navbar = () => {
  const navbarRef = useRef(null);
  const { toggleSidenav } = useContext(NavigationContext);
  
  useEffect(() => {
    if (navbarRef.current) {
      navbarRef.current.addEventListener('mainMenuClick', toggleSidenav);
      return () => {
        navbarRef.current?.removeEventListener('mainMenuClick', toggleSidenav);
      };
    }
  }, [toggleSidenav]);
  
  return (
    <ModusNavbar
      ref={navbarRef}
      appName="My Application"
      showMainMenu={true}
      logoUrl="https://modus.trimble.com/img/trimble-logo.svg"
    />
  );
};
```

### ModusSideNavigation

```jsx
import { ModusSideNavigation } from '@trimble-oss/modus-react-components';
import { useRef, useEffect, useContext } from 'react';
import { NavigationContext } from '../../context/NavigationContext';

const Sidebar = () => {
  const sidenavRef = useRef(null);
  const { isExpanded, navItems } = useContext(NavigationContext);
  
  useEffect(() => {
    if (sidenavRef.current) {
      // Initialize sidenav properties
      if (sidenavRef.current.initialized) {
        sidenavRef.current.items = navItems;
      }
    }
  }, [navItems]);
  
  return (
    <ModusSideNavigation
      ref={sidenavRef}
      expanded={isExpanded}
      mode="push"
      targetContent="#main-content"
      style={{ height: 'calc(100vh - 56px)' }}
    />
  );
};
```

### ModusTabs

```jsx
import { ModusTabs } from '@trimble-oss/modus-react-components';
import { useRef, useEffect, useState } from 'react';

const Tabs = () => {
  const tabsRef = useRef(null);
  const [activeTab, setActiveTab] = useState(0);
  const tabData = [
    { id: 0, label: 'Tab 1', icon: 'sun' },
    { id: 1, label: 'Tab 2' },
    { id: 2, label: 'Tab 3', icon: 'moon' },
  ];

  useEffect(() => {
    const modusTabs = tabsRef.current?.querySelector('modus-tabs');
    if (modusTabs) {
      modusTabs.tabs = tabData.map(tab => ({
        id: tab.id,
        label: tab.label,
        leftIcon: tab.icon,
      }));
      
      modusTabs.addEventListener('tabChange', (e) => {
        setActiveTab(e.detail);
      });
      
      return () => {
        modusTabs.removeEventListener('tabChange', (e) => {
          setActiveTab(e.detail);
        });
      }
    }
  }, []);

  return (
    <div ref={tabsRef} style={{ width: '100%' }}>
      <ModusTabs></ModusTabs>
      <div style={{ padding: '16px' }}>
        Content for tab {activeTab}
      </div>
    </div>
  );
};
```

### ModusAccordion with Items

```jsx
import { ModusAccordion, ModusAccordionItem } from '@trimble-oss/modus-react-components';
import { useRef, useEffect } from 'react';

const Accordion = () => {
  const accordionRef = useRef(null);
  
  useEffect(() => {
    if (accordionRef.current) {
      accordionRef.current.addEventListener('accordionItemSelect', (e) => {
        console.log('Item selected:', e.detail);
      });
      
      return () => {
        accordionRef.current?.removeEventListener('accordionItemSelect', (e) => {
          console.log('Item selected:', e.detail);
        });
      };
    }
  }, []);
  
  return (
    <ModusAccordion ref={accordionRef}>
      <ModusAccordionItem header="Section 1">
        Content for section 1
      </ModusAccordionItem>
      <ModusAccordionItem header="Section 2">
        Content for section 2
      </ModusAccordionItem>
      <ModusAccordionItem header="Section 3">
        Content for section 3
      </ModusAccordionItem>
    </ModusAccordion>
  );
};
```

### ModusDatePicker with ModusDateInput

```jsx
import { ModusDatePicker, ModusDateInput } from '@trimble-oss/modus-react-components';
import { useRef, useEffect, useState } from 'react';

const DateSelector = () => {
  const dateInputRef = useRef(null);
  const [selectedDate, setSelectedDate] = useState('');
  
  useEffect(() => {
    if (dateInputRef.current) {
      dateInputRef.current.addEventListener('dateSelect', (e) => {
        setSelectedDate(e.detail);
      });
      
      return () => {
        dateInputRef.current?.removeEventListener('dateSelect', (e) => {
          setSelectedDate(e.detail);
        });
      };
    }
  }, []);
  
  return (
    <ModusDatePicker>
      <ModusDateInput
        ref={dateInputRef}
        showCalendarIcon={true}
        placeholder="Select a date"
      />
    </ModusDatePicker>
  );
};
```

### Layout with Navbar and SideNavigation

```jsx
import { ModusNavbar, ModusSideNavigation } from '@trimble-oss/modus-react-components';
import { useRef, useEffect, useContext } from 'react';
import { NavigationContext } from '../../context/NavigationContext';

const Layout = ({ children }) => {
  const navbarRef = useRef(null);
  const sidenavRef = useRef(null);
  const { isExpanded, toggleSidenav } = useContext(NavigationContext);
  
  useEffect(() => {
    if (navbarRef.current) {
      navbarRef.current.addEventListener('mainMenuClick', toggleSidenav);
      return () => {
        navbarRef.current?.removeEventListener('mainMenuClick', toggleSidenav);
      };
    }
  }, [toggleSidenav]);

  return (
    <div className="app-container">
      <ModusNavbar
        ref={navbarRef}
        appName="My Application"
        showMainMenu={true}
        logoUrl="https://modus.trimble.com/img/trimble-logo.svg"
      />
      <div className="content-container">
        <ModusSideNavigation
          ref={sidenavRef}
          expanded={isExpanded}
          mode="push"
          targetContent="#main-content"
          style={{ height: 'calc(100vh - 56px)' }}
        />
        <main id="main-content">
          {children}
        </main>
      </div>
    </div>
  );
};
```
