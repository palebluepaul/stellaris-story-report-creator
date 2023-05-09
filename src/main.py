import os
import sys
import json

def main(mode, input_file):
    # Read the input file
    with open(input_file, 'r') as f:
        request = f.read()

    # For now, we're just echoing the input to the output
    # Later, we'll replace this with a call to the agent
    output = request

    # Write the output to a file in the output directory
    output_file = os.path.join('output', f'{os.path.splitext(os.path.basename(input_file))[0]}_output.txt')
    with open(output_file, 'w') as f:
        f.write(output)

    print(f'Successfully wrote output to {output_file}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python main.py <mode> <input_file>')
        sys.exit(1)

    mode = sys.argv[1]
    input_file = sys.argv[2]

    main(mode, input_file)
