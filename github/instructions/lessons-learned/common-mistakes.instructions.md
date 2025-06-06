# Modus Project Quick Reference Guide

A concise reference for GitHub Copilot to avoid common mistakes with Modus components.

## Modus Component Usage

1. **ALWAYS verify component availability**: Use the `get_list_of_all_modus_components` tool to confirm that the component exists before using it.
2. **Get proper properties**: Always use the `get_component_details` tool to understand the properties, events and usage examples.
3. **Follow provided examples**: Use the pattern shown in the example code provided by the tool.
4. **Prefer native Modus components**: Use Modus components instead of creating custom ones when available.
5. **Using ModusPagination**: Use a useRef with proper event listeners for ModusPagination instead of props like `onPageChange`.

## Image URLs

1. **Use provided URLs**: Always use the exact image URLs provided by the user.
2. **Fallback strategy**: If specific URLs are not provided, use placeholder services like:
   - Trimble assets: `https://modus.trimble.com/img/` or `https://modus-bootstrap.trimble.com/img/`
   - Default placeholders: `https://picsum.photos/[width]/[height]?random=[id]`
3. **Logo variants**: For Navbar:
   - Blue variant: `https://modus-bootstrap.trimble.com/img/trimble-logo-rev.svg` (white version)
   - Default variant: `https://modus.trimble.com/img/trimble-logo.svg` (dark version)

## Event Handling

1. **ALWAYS use native DOM events** (not onClick/onChange). Check with `get_component_details` tool.
2. **Core pattern**: useRef + addEventListener in useEffect with proper cleanup.
3. For Navbar hamburger menu, use 'mainMenuClick' event (not 'menuButtonClick').

## SideNavigation Implementation

1. **Location**: Always implement in Layout component for persistence across pages
2. **State Management**: Use context (NavigationContext) to manage expanded state
3. **Mode**: Use "push" mode with proper targetContent selector
4. **Height**: Account for navbar height with calc(100vh - 56px)
5. **Content Area**: Must have overflow handling and proper transitions

## Common Mistakes

1. Using React event handlers instead of native DOM events
2. Missing event listener cleanup in useEffect returns
3. Double event binding (form onSubmit + button onClick)
4. Creating custom properties already provided by Modus
5. Setting wrong button types (use "button" not "submit" with event listeners)
6. Implementing SideNavigation in individual pages instead of Layout
7. Using wrong event name for hamburger menu toggle
8. **CRITICAL: ALWAYS use ModusButton instead of HTML button elements** for any buttons in the interface
9. Not providing component implementation reviews after completing each section
10. **Don't Hallucinate and write `ModusAccordion.Item` instead of `ModusAccordionItem`**
11. **Check the Implemenatation of `ModusTabs` below in best practices follow this Implemenatation only**
12. **ModusDateInput needs ModusDatePicker**: ModusDateInput must be wrapped inside a ModusDatePicker component for the calendar functionality to work correctly, especially when using showCalendarIcon=true.
13. **Always set up global Open Sans font**: Create a global.css file with font-family settings for all elements and import it in main.jsx to ensure consistent typography across the application. Without this, components may use default system fonts instead of the required Open Sans font.

## Best Practice Examples
```tsx
// Button with native event
const btnRef = useRef<any>(null);
useEffect(() => {
  if (btnRef.current) {
    btnRef.current.addEventListener('buttonClick', handler);
    return () => btnRef.current?.removeEventListener('buttonClick', handler);
  }
}, []);
```

```jsx
// ModusTabs with proper property naming and event handling
const MyComponent: React.FC = () => {
  const tabsRef = useRef<any>(null);
  const [activeTab, setActiveTab] = useState(0);
  const tabData = [
    { id: 0, label: 'Tab 1', icon: 'sun' },
    { id: 1, label: 'Tab 2' },
    { id: 2, label: 'Tab 3', icon: 'moon' },
    { id: 3, label: 'Tab 4' },
    { id: 4, label: 'Tab 5', icon: 'sun' },
  ];

  useEffect(() => {
    const modusTabs = tabsRef.current?.querySelector('modus-tabs');
    if (modusTabs) {
      modusTabs.tabs = tabData.map(tab => ({
        id: tab.id,
        label: tab.label,
        leftIcon: tab.icon,
      }));
      modusTabs.addEventListener('tabChange', (e: any) => {
        setActiveTab(e.detail);
      });
    }
  }, []);

  return (
    <div id="tabs-container2" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '16px', padding: '16px', overflow: 'auto' }} ref={tabsRef}>
      <ModusTabs></ModusTabs>
      <div id="tab-content3" style={{ width: '80%', textAlign: 'center' }}>
        <h1 id="tab-heading3">Tab Index: {activeTab}</h1>
      </div>
    </div>
  );
};

```

## Implementation Reviews and Component Priority

1. **Regular implementation reviews**: After completing each major component or section, provide a brief review summarizing:
   - Components used and why they were chosen
   - Any challenges encountered and how they were solved
   - Any optimizations or improvements made

2. **Component prioritization hierarchy**:
   - **First choice**: Always use native Modus components when available
   - **Second choice**: Compose using multiple Modus components
   - **Last resort**: Only use HTML elements when no suitable Modus component exists

3. **Component substitution guide**:
   - `<button>` → `ModusButton`
   - `<input>` → `ModusTextInput`, `ModusNumberInput`, etc.
   - `<select>` → `ModusSelect`
   - `<textarea>` → `ModusTextareaInput`
   - `<div class="card">` → `ModusCard`
   - HTML tabs → `ModusAccordion` or custom tabs with Modus styling

4. **Component testing**: Always use Browser MCP to test that components render properly and maintain proper alignment and width.

5. **Modus Icons Usage**:
   - **ALWAYS verify icon names**: Use the `f1e_get_modus_icons_by_char` tool to confirm that the icon name exists before using it.
   - **Common mistakes to avoid**: 
     - Using `user` instead of `person` for user/profile icons
     - Using `contact` instead of `contacts` for contacts icon
     - Using icons without verifying they exist in the Modus icon library

6. **Navbar Variant Logos**:
   - Blue variant needs white logo: `https://modus-bootstrap.trimble.com/img/trimble-logo-rev.svg`
   - Default variant needs dark logo: `https://modus.trimble.com/img/trimble-logo.svg`

7. **ModusCard Padding**:
   - **Always add internal padding container**: ModusCard doesn't include built-in padding, so always wrap content in a div with padding
   - **Recommended approach**: `<div style={{ padding: '24px' }}>` inside ModusCard for consistent spacing
   - **Avoid CSS conflicts**: Don't rely on CSS classes for padding that might conflict with component structure

8. **Import Verification**:
   - **ALWAYS verify imports during code reviews and implementation**: Missing, incorrect, or improper imports can lead to runtime errors
   - **Required checks**:
     - Verify all Modus component imports (e.g., `import { ModusButton } from '@trimble-oss/modus-react-components'`)
     - Check for correct import paths, especially in larger projects with aliased paths
     - Remove unused imports to reduce bundle size
     - Ensure proper importing of CSS files (global styles vs. component-specific styles)
     - Confirm imports of required utility functions and hooks
