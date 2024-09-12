import os
import random
import string

def generate_random_text(size):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Generate random text of 1500 bytes
text1 = generate_random_text(1500)
text2 = generate_random_text(15000)

# Define file paths
file1_path = os.path.join(script_dir, 'arquivo1500.txt')
file2_path = os.path.join(script_dir, 'arquivo15000.txt')

# Write the text to two different files
write_to_file(file1_path, text1)
write_to_file(file2_path, text2)

# Verify the file sizes
print(f"arquivo1500.txt size: {os.path.getsize(file1_path)} bytes")
print(f"arquivo15000.txt size: {os.path.getsize(file2_path)} bytes")