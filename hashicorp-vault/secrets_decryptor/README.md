# Secret Decryptor

This Python script decrypts base64-encoded secrets stored in a YAML file and converts them into separate JSON files. Each JSON file is named based on a specific key (e.g., `SecretName`) within each section of the YAML file.

## Features

- Decrypts base64-encoded strings.
- Supports multiple sections within a single YAML file.
- Generates separate JSON files for each section based on a specified key.

## Requirements

- Python 3.x
- PyYAML library

## Installation

1. **Clone the repository** or download the script.

2. **Install the required dependencies** using pip:

   ```bash
   pip install pyyaml

## Usage

### Command-Line Arguments

- **`yaml_file`**: The path to the YAML file containing the secrets.

### Example Command

```bash
python decrypt_secrets.py secrets.yaml