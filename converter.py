import json
import re
from collections import defaultdict

def split_json_by_prefix(input_file):
    """
    Split JSON file into separate files based on question ID prefixes
    and remove 'refs' field from each object
    
    Args:
        input_file (str): Path to the input JSON file
    """
    try:
        # Read the original JSON file
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Group questions by their prefix (e.g., T1A, T1B, T0C, etc.)
        grouped_data = defaultdict(list)
        
        for item in data:
            # Extract prefix from ID (e.g., "T1A01" -> "T1A")
            question_id = item.get('id', '')
            
            # Use regex to extract the prefix (letters and numbers before the final digits)
            match = re.match(r'^([A-Z]\d+[A-Z])', question_id)
            if match:
                prefix = match.group(1)
                
                # Remove 'refs' field from the item
                new_item = {key: value for key, value in item.items() if key != 'refs'}
                grouped_data[prefix].append(new_item)
            else:
                print(f"Warning: Could not extract prefix from ID '{question_id}'")
        
        # Create separate JSON files for each prefix
        files_created = 0
        for prefix, questions in grouped_data.items():
            output_filename = f"{prefix.lower()}.json"
            
            with open(output_filename, 'w', encoding='utf-8') as f:
                json.dump(questions, f, indent=2, ensure_ascii=False)
            
            files_created += 1
            print(f"Created {output_filename} with {len(questions)} questions")
        
        print(f"\nSuccessfully created {files_created} files from {input_file}")
        print(f"Total questions processed: {sum(len(questions) for questions in grouped_data.values())}")
        
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in input file. {e}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your actual input file path
    input_filename = "/Users/xiuminmartin/Documents/GitHub/RadioWeaves/technician.json"  # Your original file
    
    split_json_by_prefix(input_filename)
    
    # Optional: Display a sample of one of the created files
    try:
        with open("t1a.json", 'r', encoding='utf-8') as f:
            sample_data = json.load(f)
            print(f"\nSample from t1a.json (first item):")
            print(json.dumps(sample_data[0], indent=2))
    except:
        pass