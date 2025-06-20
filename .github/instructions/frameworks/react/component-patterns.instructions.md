-----
applyTo: "*.tsx, *.jsx"
-----

# Modus React Component Patterns

> **LEAD LEVEL GUIDANCE**: This document provides React-specific patterns for implementing Modus components effectively.

## Component Implementation Patterns

### ModusWcButton

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

### ModusWcCheckbox

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

### ModusWcNavbar

```tsx
import React, { useRef, useEffect, useState } from 'react';
import { ModusWcNavbar } from '@trimble-oss/moduswebcomponents-react';

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

const AppNavbar: React.FC = () => {
  // Navbar reference for event handling
  const navbarRef = useRef<HTMLModusWcNavbarElement>(null);
  const [searchValue, setSearchValue] = useState<string>('');
  
  // User information
  const userCard: INavbarUserCard = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    avatarSrc: 'path/to/avatar.jpg',
    avatarAlt: 'John Doe'
  };
  
  // Visibility configuration
  const visibility: INavbarVisibility = {
    mainMenu: true,
    notifications: true,
    search: true,
    apps: false,
    help: true,
    user: true
  };
  
  // Text overrides for localization or customization
  const textOverrides = {
    help: 'Support',
    notifications: 'Alerts'
  };
  
  // Event handlers
  useEffect(() => {
    const navbar = navbarRef.current;
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
  }, []);
  
  return (
    <ModusWcNavbar
      ref={navbarRef}
      userCard={userCard}
      visibility={visibility}
      textOverrides={textOverrides}>
      
      {/* Custom main menu content */}
      <div slot="main-menu" style={{backgroundColor: '#0063a3', color: 'white', padding: '1rem'}}>
        <h3>Main Menu</h3>
        <ul>
          <li>Dashboard</li>
          <li>Projects</li>
          <li>Reports</li>
          <li>Settings</li>
        </ul>
      </div>
      
      {/* Notifications menu content */}
      <div slot="notifications">
        <div style={{padding: '0.5rem 1rem'}}>
          <h4 style={{margin: '0.5rem 0'}}>New message</h4>
          <p style={{margin: '0.5rem 0'}}>You have a new message from Admin</p>
        </div>
        <div style={{padding: '0.5rem 1rem', borderTop: '1px solid #eee'}}>
          <h4 style={{margin: '0.5rem 0'}}>System update</h4>
          <p style={{margin: '0.5rem 0'}}>System maintenance scheduled for tomorrow</p>
        </div>
      </div>
      
      {/* Apps menu content */}
      <div slot="apps">
        <div style={{padding: '1rem'}}>
          <p>No application shortcuts configured.</p>
        </div>
      </div>
    </ModusWcNavbar>
  );
};

export default AppNavbar;
```

### ModusWcTabs

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
