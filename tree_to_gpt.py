import os
from openai import OpenAI

# Load the OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY")
)

# Define the input file and output file
input_file = "REPO_STRUCTURE.md"
output_file = "MERMAID_DIAGRAM.md"

# Read the repository structure from the input file
with open(input_file, 'r') as file:
    repo_structure = file.read()

# Define the prompt to send to the ChatGPT API
prompt = f"""
The following is the directory structure of a Git repository:

{repo_structure}

Please convert this directory structure into a Mermaid diagram using the 'graph TD' syntax. 
- Group files logically based on their folder structure.
- Use nested nodes where appropriate.
- Apply cool styles such as different colors for folders and files, use subgraph for groups, and add meaningful labels.
- Make sure the Mermaid syntax is correct and ready to be used in a Markdown file.
- Example:
This input:

# Repository Structure
```markdown
graph-git-repo
├── .gitignore
├── README.md
├── REPO_STRUCTURE.md
├── base.sh
└── tree_to_gpt.py
```
should generate this output:
```mermaid
graph TB
    %% Repository Structure
    subgraph graph_git_repo
        root[graph-git-repo]
        root --> gitignore[.gitignore]
        root --> README[README.md]
        root --> REPO_STRUCTURE[REPO_STRUCTURE.md]
        root --> base[base.sh]
        root --> tree_to_gpt[tree_to_gpt.py]
    end
    style graph_git_repo fill:#e0f7fa,stroke:#333,stroke-width:2px;
```

Output only the Mermaid diagram, starting from the opening backticks with 'mermaid' specification up until including the closing backticks after the mermaid graph!
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
            ],
        }
    ],
)

# Extract the generated text from the response
gpt_output = response.choices[0].message.content.strip()
print(gpt_output)

# Write the response to the output file, wrapping it in code block formatting for Markdown
with open(output_file, 'w') as file:
  file.write("# Mermaid Diagram\n\n")
  # file.write("```mermaid\n")
  file.write(gpt_output)
  # file.write("\n```")

print(f"Mermaid diagram written to {output_file}")
