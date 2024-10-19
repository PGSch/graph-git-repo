#!/bin/bash

# Define the output file and the directory name
OUTPUT_FILE="REPO_STRUCTURE.md"
REPO_NAME=$(basename "$PWD")

# Read excluded patterns from the input argument or use default ones
EXCLUDE_PATTERNS=${1:-'.git|.DS_Store|.idea|.github|*.sample|logs|objects|refs|pack|exclude|*.txt|*.csv|*.pkl|*.ipynb|__pycache__|venv|.venv'}
DEPTH=${2:-'2'}

# Generate the header with the repository name
echo "# Repository Structure" > $OUTPUT_FILE
echo "\`\`\`markdown" >> "$OUTPUT_FILE"
echo "$REPO_NAME" >> "$OUTPUT_FILE"

# Generate the tree structure, excluding the specified patterns
#tree -a -L "$DEPTH" -n -I "$EXCLUDE_PATTERNS" | tail -n +2 | head -n -1 >> "$OUTPUT_FILE"
tree -a -L "$DEPTH" -n -I "$EXCLUDE_PATTERNS" | sed '1d;$d;$d' | awk 'NR==1{printf "%s", $0; next}{printf "\n%s", $0}' >> "$OUTPUT_FILE"

# Display a message indicating the script has finished
echo "\`\`\`" >> "$OUTPUT_FILE"
echo "Repository structure written to $OUTPUT_FILE"