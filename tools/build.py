import os
import json
import zipfile

def build_extension():
    try: # check files exists
        with open('manifest.json', 'r') as f:
            manifest = json.load(f)
            version = manifest['version']
    except FileNotFoundError:
        print("Error: manifest.json not found in root directory.")
        return

    zip_filename = f"epoch-focus-v{version}.zip"
    
    # package files
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk('.'):
            for file in files:
                file_path = os.path.join(root, file)
                # ignore list
                if any(x in file_path for x in [
                    '.git', '.github', 'tools', '__pycache__', '.DS_Store', 
                    'LICENSE', 'README.md', '.gitignore'
                ]):
                    continue
                
                if file.endswith('.zip'):
                    continue
                    
                # zip using relative path
                zf.write(file_path, arcname=os.path.relpath(file_path, '.'))
                
    print(f"build complete: {zip_filename}")

if __name__ == "__main__":
    build_extension()