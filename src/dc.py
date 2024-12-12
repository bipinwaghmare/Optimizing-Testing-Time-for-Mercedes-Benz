import os
import shutil
import zipfile

# Define paths
kaggle_json_path = "kaggle.json"  # Ensure this file is in the same directory as this script
kaggle_dir = os.path.expanduser("~/.kaggle")
download_path = "./data"

# Ensure the Kaggle directory exists
os.makedirs(kaggle_dir, exist_ok=True)

# Move `kaggle.json` to the Kaggle directory
if os.path.exists(kaggle_json_path):
    shutil.copy(kaggle_json_path, os.path.join(kaggle_dir, "kaggle.json"))
else:
    raise FileNotFoundError(f"{kaggle_json_path} not found. Place it in the script's directory.")

# Set permissions for `kaggle.json` (optional on Windows)
kaggle_json_file = os.path.join(kaggle_dir, "kaggle.json")
if os.name != "nt":  # Skip chmod on Windows
    os.chmod(kaggle_json_file, 0o600)

# Download the dataset
os.makedirs(download_path, exist_ok=True)
os.system(f"kaggle competitions download -c mercedes-benz-greener-manufacturing -p {download_path}")

# Extract the dataset
for file in os.listdir(download_path):
    if file.endswith(".zip"):
        with zipfile.ZipFile(os.path.join(download_path, file), "r") as zip_ref:
            zip_ref.extractall(download_path)
        print(f"Extracted: {file}")
