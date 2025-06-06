import os
import json

def test_extract_examples(component_name):
    """Test function to extract examples for a specific component from the KB file"""
    try:
        # Path setup
        base_path = os.path.dirname(os.path.dirname(__file__))
        kb_path = os.path.join(base_path, "Knowledge Base", "modus2_react_KB.md")
        
        # Read the KB content
        print(f"Reading knowledge base from: {kb_path}")
        with open(kb_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract examples
        print(f"\nExtracting examples for: {component_name}")
        examples = extract_examples_from_markdown(content, component_name)
        
        # Print results
        print(f"\nFound {len(examples)} examples for {component_name}")        
        for i, example in enumerate(examples, 1):
            print(f"\n--- Example {i} ---")
            print(f"Question: {example['question'][:60]}..." if example['question'] else "No question found")
            print(f"Code length: {len(example['code'])} characters")
            print(f"First few lines of code: {example['code'].split(chr(10))[0]}")
            print("----------------")
        
        return examples
    except Exception as e:
        print(f"Error in test_extract_examples: {str(e)}")
        return []

def extract_examples_from_markdown(content, component_name):
    """Extract examples directly from markdown content"""
    try:            
        examples = []
        # Find the component section
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
            print("This appears to be the last component in the file")
        else:
            component_section = content[start_index:next_component_index]
            print(f"Found next component at position {next_component_index}")
        
        print(f"Component section length: {len(component_section)} characters")
        
        # Extract TypeScript/JSX code blocks
        print("\nLooking for code blocks...")
        
        # Method 1: Find all code blocks directly
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
                print(f"No more code blocks found after position {current_index}")
                break
            
            # Find the closing marker
            code_end = component_section.find("```", best_start + marker_len)
            if code_end == -1:
                print(f"Warning: Found opening code marker at {best_start} but no closing marker")
                break
            
            # Extract the code
            code = component_section[best_start + marker_len:code_end].strip()
            block_count += 1
            
            print(f"Found code block #{block_count} of type {marker_type} at position {best_start}, code length: {len(code)}")
            
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
                    print(f"Found question: {question[:40]}...")
            
            # Add to code blocks
            code_blocks.append({
                "prompt_number": prompt_index,
                "question": question,
                "code": code
            })
            
            # Move to next position
            current_index = code_end + 3
        
        # Method 2: Find prompts and extract code from each
        if not code_blocks:
            print("\nTrying alternative extraction method...")
            # Extract examples from the component section by splitting on "## Prompt"
            prompts = component_section.split("## Prompt")
            print(f"Found {len(prompts)-1} prompts by splitting on '## Prompt'")
            
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
                        print(f"Extracted question for prompt {i}: {example['question'][:40]}...")
                
                # Find code blocks
                code_markers = ["```tsx", "```jsx", "```typescript", "```javascript", "```"]
                for marker in code_markers:
                    code_start = prompt.find(marker)
                    if code_start != -1:
                        code_end = prompt.find("```", code_start + len(marker))
                        if code_end != -1:
                            code = prompt[code_start + len(marker):code_end].strip()
                            example["code"] = code
                            print(f"Found code in prompt {i} with marker {marker}, code length: {len(code)}")
                            break
                
                # Only add examples that have some code
                if example["code"]:
                    code_blocks.append(example)
        
        # Print results summary
        print(f"\nExtraction complete, found {len(code_blocks)} valid code examples")
        
        return code_blocks
    except Exception as e:
        print(f"Error extracting examples: {e}")
        import traceback
        print(traceback.format_exc())
        return []

if __name__ == "__main__":
    # Test with a component that has examples in the KB
    components_to_test = ["ModusWcAccordion", "ModusWcCard", "ModusWcButton"]
    
    for component_name in components_to_test:
        print("\n" + "="*50)
        print(f"TESTING: {component_name}")
        print("="*50)
        examples = test_extract_examples(component_name)
        
    print("\nDebug testing complete.")
