import re

def replace_inline_math(text):
    # Define the regular expression pattern to match text between single $ signs

    # We want to match text between single $ signs, but we want to ignore text between double $ signs
    pattern = r'(?<!\$)\$([^$]+)\$(?!\$)'

    # Define the replacement pattern with \\( and \\)
    # We need to escape the backslashes in the replacement pattern
    replacement = r'\\\\(\1\\\\)'
    
    # Use re.sub() to replace all instances of the pattern with the replacement
    return re.sub(pattern, replacement, text)


def process_file(input_file, output_file):
    # Read content from input file
    with open(input_file, 'r') as f:
        content = f.read()
    
    # Perform replacement
    modified_content = replace_inline_math(content)
    # Write modified content to output file
    with open(output_file, 'w') as f:
        f.write(modified_content)

# Example usage
input_file = 'morpho-manual.md'  # Path to the input LaTeX file
output_file = 'morpho-manual-mathjax.md'  # Path to the output LaTeX file
process_file(input_file, output_file)
