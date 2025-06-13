# Modus Implementation Steps

> **⚠️ MANDATORY PROCESS ⚠️**: You MUST follow these steps in exact sequence with no exceptions. For each step, document your actions and findings before proceeding to the next step. **5th step is most important**

## REQUIRED SEQUENTIAL PROCESS

1. **Read and Document Understanding of Instructions**
   - Review and acknowledge understanding of all the instructions including the custom instructions given regarding modus implementation.
   - Document "Instructions Read" confirmation before proceeding
   - Note any specific requirements or constraints mentioned

2. **Review Past Implementation Mistakes**
   - Ensure you've read [Common Mistakes](./instructions/lessons-learned/common-mistakes.instructions.md) thoroughly
   - Document relevant past issues and their solutions in short form
   - Acknowledge completion of review before proceeding

3. **Installation and setup of Modus**:
   - Use `getting_started_installation_and_guidelines` tools to fetch instruction regarding installation
   - Check if the project's `package.json` has modus components installed if not then only install it
   - Check if the `Open Sans` font and   `defineCustomElements()` are properly set up from `index.html` and `main.jsx` or `main.tsx` respectively.

3. **Get Complete List of Available Modus Components**
   - Use `get_list_of_all_modus_components` tool
   - Document all available components

4. **Create Detailed Implementation Plan**
   - Map requirements to verified Modus components
   - Create a detailed plan page by page stating which components will be used
   - Use `get_component_details` tool to fetch the details of component and for each component
     - Available properties
     - Events and event names
     - Required parent/child relationships
     - Usage examples
   - For components with icons:
     - Use `get_modus_icons_by_char` to verify icon names. use empty string as argument to get all valid modus icon names.
     - Document verified icon names for use

   - Implement following documented patterns [Component Patterns](./instructions/frameworks/react/component-patterns.instructions.md)

5. **Integration Testing**
   - Test components together look for typescipt except trivial ones like `any` and `not used`.
   - Verify interactions between components
   - Document any integration issues

6. **Final Review and Documentation**
   - Review against initial requirements
   - Document any deviations or limitations
   - Create implementation notes for team reference
    

**Implementation with DOM Events**
   - Follow the proper event handling pattern with refs and useEffect
   - Implement proper event cleanup in useEffect return function
   ```jsx
   const elementRef = useRef(null);
   
   useEffect(() => {
     if (elementRef.current) {
       elementRef.current.addEventListener('eventName', handleEvent);
       return () => {
         elementRef.current?.removeEventListener('eventName', handleEvent);
       };
     }
   }, [dependencies]);
   ```

