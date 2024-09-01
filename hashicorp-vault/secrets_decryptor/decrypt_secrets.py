import yaml
import json
import base64
import re
import argparse

def decrypt_base64(encoded_string):
    # Add padding if necessary
    missing_padding = len(encoded_string) % 4
    if missing_padding:
        encoded_string += '=' * (4 - missing_padding)
    # Decode the base64 encoded string
    return base64.b64decode(encoded_string).decode('utf-8')

def is_base64(s):
    # Check if a string is base64 encoded (ignoring newlines and padding)
    if isinstance(s, str) and re.match(r'^[A-Za-z0-9+/]*={0,2}$', s):
        return True
    return False

def process_secrets(yaml_content):
    # Split the content into individual documents (sections)
    yaml_sections = yaml.safe_load_all(yaml_content)

    for section in yaml_sections:
        # Assuming the key for naming the file is something like 'SecretName'
        secret_name_key = 'SecretName'
        if secret_name_key in section:
            secret_name = section.pop(secret_name_key)  # Remove SecretName from the section
            json_file = f"{secret_name}.json"

            # Decrypt only base64 encoded secrets
            decrypted_data = {}
            for key, value in section.items():
                if is_base64(value.strip()):  # Check if the value is base64
                    decrypted_data[key] = decrypt_base64(value)
                else:
                    decrypted_data[key] = value  # Leave the value unchanged

            # Convert to JSON and save to a file
            with open(json_file, 'w') as file:
                json.dump(decrypted_data, file, indent=4)

            print(f"Decrypted secrets saved to {json_file}")

def main():
    parser = argparse.ArgumentParser(description="Decrypt base64 secrets from a YAML file and convert them to JSON.")
    parser.add_argument('yaml_file', help="The path to the YAML file containing the secrets.")

    args = parser.parse_args()

    # Read the entire content of the YAML file
    with open(args.yaml_file, 'r') as file:
        yaml_content = file.read()

    # Process the YAML content
    process_secrets(yaml_content)

if __name__ == "__main__":
    main()
