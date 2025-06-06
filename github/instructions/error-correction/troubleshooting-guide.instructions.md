# Modus Troubleshooting Guide

> **DEVELOPER LEVEL GUIDANCE**: This document provides practical solutions for common issues encountered when implementing Modus components.

## Diagnostic Approach

When troubleshooting issues with Modus components:

1. **Identify the Component**: Determine which component is causing the issue.
2. **Verify Implementation**: Check that the component is being used correctly by reviewing the component details.
3. **Inspect Console Errors**: Check browser console for specific error messages.
4. **Validate Events**: Verify that event handlers are properly attached and cleaned up.
5. **Test in Isolation**: Test the component in isolation to eliminate interference from other components.

## Common Issues and Solutions

### Component Not Found

**Symptoms:**
- Error message: "Cannot find component ModusSomething"
- Component not rendering

**Solutions:**
1. Verify the component exists using `get_list_of_all_modus_components`
2. Check import statement (`import { ModusComponent } from '@trimble-oss/modus-react-components'`)
3. Ensure the package is properly installed in package.json

### Events Not Firing

**Symptoms:**
- Component renders but doesn't respond to interactions
- No errors in console

**Solutions:**
1. Verify event name using `get_component_details` (e.g., 'buttonClick' not 'onClick')
2. Check that event listeners are added using DOM methods not React props
3. Ensure useRef is properly assigned to the component
4. Verify event listener cleanup in useEffect return function

### Styling and Layout Issues

**Symptoms:**
- Components not centered
- Inconsistent widths
- Overflow issues

**Solutions:**
1. Use CSS flexbox or grid for layout containment
2. Apply width: 100% to container elements
3. Use appropriate margin and padding settings
4. Check for any conflicting CSS rules

### Nested Components Issues

**Symptoms:**
- Child components not rendering
- Parent-child relationship not working as expected

**Solutions:**
1. Verify correct component pairing (e.g., ModusDatePicker must wrap ModusDateInput)
2. Check component nesting order
3. Ensure all required props are passed to both parent and child components

### ModusTabs Not Working

**Symptoms:**
- Tabs don't switch
- Content doesn't update

**Solutions:**
1. Follow the exact implementation pattern from the component patterns guide
2. Make sure tabs are being set on the native element using querySelector
3. Ensure the tabChange event listener is properly attached
4. Verify tab data structure matches the expected format

### ModusSideNavigation Issues

**Symptoms:**
- Side navigation doesn't expand/collapse
- Content area doesn't adjust

**Solutions:**
1. Verify that side navigation is in the layout component, not individual pages
2. Ensure mode="push" and targetContent is set to the correct selector
3. Set proper height calculation: height: calc(100vh - 56px)
4. Check that navigation context is properly implemented and connected

## Installation Issues

**Symptoms:**
- Package installation fails
- Dependency conflicts

**Solutions:**
1. Use the `--legacy-peer-deps` flag when installing
2. Verify React version compatibility
3. Check for duplicate React installations in node_modules
4. Clear npm cache and reinstall

## Browser Compatibility Issues

**Symptoms:**
- Components work in some browsers but not others
- Visual inconsistencies across browsers

**Solutions:**
1. Check browser console for specific errors
2. Verify that polyfills are included if targeting older browsers
3. Test with Browser MCP in multiple browsers
4. Review Modus documentation for browser compatibility notes

## Performance Issues

**Symptoms:**
- Slow rendering
- UI freezes during interactions

**Solutions:**
1. Minimize unnecessary re-renders with proper dependency arrays in useEffect
2. Use React.memo for expensive components
3. Implement virtualization for large lists
4. Profile with React DevTools to identify bottlenecks
