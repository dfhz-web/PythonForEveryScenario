import argparse

# Create ArgumentParser object
parser = argparse.ArgumentParser(description='A simple script with command-line arguments.')

# Add command-line arguments
parser.add_argument('input_file', help='Path to the input file')
parser.add_argument('--output', '-o', help='Path to the output file (optional)')

# Parse the command-line arguments
args = parser.parse_args()

# Access the values of the arguments
input_file_path = args.input_file
output_file_path = args.output

# Perform actions based on the provided arguments
print(f"Input file: {input_file_path}")
print(f"Output file: {output_file_path}")
