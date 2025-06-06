import os
import json

class ComponentRegistry:
    """Registry for Modus 2.0 Web Components, handling component details and examples"""
    
    def __init__(self):
        # Paths for knowledge base files
        self.base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.components_path = os.path.join(self.base_path, "Knowledge Base", "modus2_components.json")
        self.combined_kb_path = os.path.join(self.base_path, "Knowledge Base", "Modus 2", "combined_modus2.md")
        self.react_kb_path = os.path.join(self.base_path, "Knowledge Base", "modus2_react_KB.md")
        self.icons_path = os.path.join(self.base_path, "Knowledge Base", "modus_icons.json")
    
    def get_all_components(self):
        """Get list of all available components from Modus 2.0"""
        try:
            # In Modus 2.0, all components are in a single JSON file
            # Component names are the top-level keys in the JSON
            with open(self.components_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Extract component names (all top-level keys)
                components = list(data.keys())
            
            return components
        except Exception as e:
            print(f"Error getting component list: {e}")
            return []
    
    def get_component_properties_and_events(self, component_name):
        """Get properties, events and description for a specific component"""
        try:
            with open(self.components_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # In Modus 2.0, component data is directly accessible with the component name as the key
            if component_name in data:
                component_data = data[component_name]
                return {
                    "properties": component_data.get("properties", []),
                    "events": component_data.get("events", []),
                    "methods": component_data.get("methods", []),
                    "description": component_data.get("description", "")
                }
            
            return {"properties": [], "events": [], "methods": [], "description": ""}
        
        except Exception as e:
            print(f"Error getting component properties: {e}")
            return {"properties": [], "events": [], "methods": [], "description": ""}
            
    def _extract_kb_examples(self, content, component_name, framework=None):
        """Extract examples for a specific component from the knowledge base
        
        Args:
            content: The content to extract from
            component_name: The component name to find examples for
            framework: The framework to use (not used in Modus 2.0 currently)
            
        Returns:
            list: List of examples for the component
        """
        examples = []
        try:
            # Use the content passed directly rather than reading from a file again
            print(f"Extracting {component_name} examples from the knowledge base")
            examples = self._extract_examples_from_markdown_content(content, component_name)
            
            return examples       
        except Exception as e:
            print(f"Error extracting examples: {e}")
            return []
            
    def _extract_examples_from_content(self, kb_path, component_name, framework=None):
        """Helper method to extract examples from a specific KB file"""
        try:
            with open(kb_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return self._extract_examples_from_markdown_content(content, component_name)
        except Exception as e:
            print(f"Error extracting examples from {kb_path}: {e}")
            return []
    
    def _extract_examples_from_markdown_content(self, content, component_name, framework=None):
        """Extract examples directly from markdown content"""
        try:            
            examples = []
            # Find the component section
            print(f"Searching for {component_name} examples in React KB")
            print(f"Looking for component: {component_name} in markdown content")
            
            # For Modus 2.0, component headers are directly with the component name
            component_marker = f"# {component_name}"
            start_index = content.find(component_marker)
            
            if start_index == -1:
                print(f"Component {component_name} not found in knowledge base")
                return []
            
            print(f"Found component marker: '{component_marker}' at position {start_index}")
            
            # Find the next component section or end of file
            next_component_index = content.find("\n# ", start_index + 1)
            if next_component_index == -1:
                # If this is the last component in the file
                component_section = content[start_index:]
            else:
                component_section = content[start_index:next_component_index]
            
            # Extract TypeScript/JSX code blocks
            code_blocks = []
            current_index = 0
            block_count = 0
            
            while True:
                # Look for code block markers
                code_start_markers = ["```tsx", "```jsx", "```typescript", "```javascript", "```"]
                best_start = -1
                marker_len = 0
                marker_type = ""
                
                for marker in code_start_markers:
                    pos = component_section.find(marker, current_index)
                    if pos != -1 and (best_start == -1 or pos < best_start):
                        best_start = pos
                        marker_len = len(marker)
                        marker_type = marker
                
                if best_start == -1:
                    break
                
                # Find the closing marker
                code_end = component_section.find("```", best_start + marker_len)
                if code_end == -1:
                    break
                
                # Extract the code
                code = component_section[best_start + marker_len:code_end].strip()
                block_count += 1
                
                # Find which prompt this code belongs to (look for "## Prompt" before this block)
                prompt_positions = []
                for i in range(1, 10):  # Look for Prompt 1-9
                    prompt_marker = f"## Prompt {i}"
                    pos = component_section.find(prompt_marker)
                    if pos != -1 and pos < best_start:
                        prompt_positions.append((i, pos))
                
                # Sort by position to find the closest prompt
                prompt_positions.sort(key=lambda x: x[1], reverse=True)
                prompt_index = prompt_positions[0][0] if prompt_positions else 1
                
                # Find the user question for this code block
                question = ""
                question_marker = "**User Question:**"
                question_start = component_section.rfind(question_marker, 0, best_start)
                if question_start != -1:
                    question_end = component_section.find("**Agent Answer:**", question_start)
                    if question_end != -1:
                        question = component_section[question_start + len(question_marker):question_end].strip()
                
                # Add to code blocks
                code_blocks.append({
                    "prompt_number": prompt_index,
                    "question": question,
                    "code": code
                })
                
                # Move to next position
                current_index = code_end + 3
            
            # Method 2: Find prompts and extract code from each if we haven't found any yet
            if not code_blocks:
                # Extract examples from the component section by splitting on "## Prompt"
                prompts = component_section.split("## Prompt")
                print(f"Found {len(prompts)-1} prompts for {component_name}")
                
                # Skip the first split which contains the component header
                for i, prompt in enumerate(prompts[1:], 1):
                    example = {
                        "prompt_number": i,
                        "question": "",
                        "code": ""
                    }
                    
                    # Extract the user question
                    question_parts = prompt.split("**User Question:**")
                    if len(question_parts) > 1:
                        answer_parts = question_parts[1].split("**Agent Answer:**")
                        if len(answer_parts) > 0:
                            example["question"] = answer_parts[0].strip()
                    
                    # Find code blocks
                    code_markers = ["```tsx", "```jsx", "```typescript", "```javascript", "```"]
                    for marker in code_markers:
                        code_start = prompt.find(marker)
                        if code_start != -1:
                            code_end = prompt.find("```", code_start + len(marker))
                            if code_end != -1:
                                code = prompt[code_start + len(marker):code_end].strip()
                                example["code"] = code
                                break
                    
                    # Only add examples that have some code
                    if example["code"]:
                        code_blocks.append(example)
            
            return code_blocks
        except Exception as e:
            print(f"Error extracting examples from markdown content: {e}")
            return []
    
    def get_installation_guidelines(self):
        """Get installation and usage guidelines"""
        try:
            guidelines_path = os.path.join(self.base_path, "Knowledge Base", "Modus 2", "Modus2_guidelines.md")
            with open(guidelines_path, 'r', encoding='utf-8') as f:
                guidelines = f.read()
            return guidelines
        except Exception as e:
            print(f"Error loading guidelines: {e}")
            return "Guidelines not available."
    
    def get_all_icon_names(self):
        """Get a list of all available Modus icon names"""
        try:
            with open(self.icons_path, 'r', encoding='utf-8') as f:
                icons_data = json.load(f)
            return icons_data.get("icons", [])
        except Exception as e:
            print(f"Error loading icon names: {e}")
            return []
    
    def get_icon_names_by_char(self, char_prefix):
        """Get a list of icon names starting with a specific character
        
        Args:
            char_prefix (str): The character prefix to filter icons by
            
        Returns:
            list: List of icon names starting with the specified character
        """
        try:
            if not char_prefix:
                return []
                
            all_icons = self.get_all_icon_names()
            
            # Convert to lowercase for case-insensitive matching
            prefix = char_prefix.lower()
            
            # Filter icons starting with the specified character
            matching_icons = [icon for icon in all_icons if icon.lower().startswith(prefix)]
            
            return matching_icons
        except Exception as e:
            print(f"Error getting icons by character prefix: {e}")
            return []
