# Generate [mermaid](https://github.com/mermaid-js/mermaid) Repo Structure Action

[![GitHub Release](https://img.shields.io/github/v/release/PGSch/graph-git-repo?logo=github)](https://github.com/PGSch/graph-git-repo/releases)
[![GitHub License](https://img.shields.io/github/license/PGSch/graph-git-repo)](https://github.com/PGSch/graph-git-repo/blob/main/LICENSE)
[![Sponsor](https://img.shields.io/badge/sponsor-♥-f06292)](https://github.com/sponsors/PGSch)
[![Twitter Follow](https://img.shields.io/twitter/follow/pgschdev?style=social)](https://twitter.com/intent/follow?screen_name=pgschdev)

## Overview

**Generate Repo Structure Action** is a GitHub Action designed to automatically generate a visual representation of your repository's structure using the `tree` command. This action allows users to exclude specific files or directories using customizable patterns, and outputs a structured Markdown file (`REPO_STRUCTURE.md`) with the current repository's layout.

## Features

- **Customizable Exclusions**: Specify patterns to exclude files or directories from the generated structure.
- **Automatic Markdown Output**: Generates a `REPO_STRUCTURE.md` file with the current repository structure.
- **Easy Integration**: Simply add this action to your workflow to keep your repository structure up-to-date.

## How It Works

1. **Define the Workflow**: Include this action in your GitHub workflow.
2. **Customize Exclusions**: Specify which files or directories to exclude through the `exclude_patterns` input.
3. **Generate Structure**: The action runs a script that creates a `REPO_STRUCTURE.md` file, which is committed back to your repository.

## Usage

To use this action in your repository, include it in your GitHub workflow YAML file. Below is an example configuration:

### Example Workflow

```yaml
name: Generate Repo Structure

on:
  push:
    branches:
      - main
  workflow_dispatch:
    inputs:
      exclude_patterns:
        description: 'Patterns to exclude (e.g., ".git|*.log|node_modules")'
        required: false
        default: '.git|.DS_Store|.idea|*.log|*.tmp|__pycache__'

jobs:
  generate-structure:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Generate Repo Structure
        uses: your-username/generate-repo-structure-action@v1.0.0
        with:
          exclude_patterns: '${{ github.event.inputs.exclude_patterns }}'
      
      - name: Download Repo Structure
        uses: actions/download-artifact@v3
        with:
          name: repo-structure
          path: .
```

### Inputs

| Input Name         | Required | Description                                                                                              |
|--------------------|----------|----------------------------------------------------------------------------------------------------------|
| `exclude_patterns` | `false`  | Patterns to exclude from the tree structure (e.g., ".git|*.log|node_modules"). Default is provided.       |

### Outputs

The action generates a `REPO_STRUCTURE.md` file that contains a Markdown-based representation of the repository's structure, excluding specified files and directories.

### Required Permissions

This action requires the following permissions to function properly:

- **Contents**: `write` (to commit the generated structure back to the repository)

## Advanced Configuration

### Customizing Exclusions

You can specify patterns to exclude directly in your workflow file:

```yaml
with:
  exclude_patterns: '.git|node_modules|*.log|*.env'
```

### Triggering the Action

The action will be triggered based on your workflow settings, either automatically on a push or manually through the GitHub UI.

## Contributing

We welcome contributions to improve **Generate Repo Structure Action**! Please open an issue or submit a pull request for any features or bug fixes you’d like to see.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
