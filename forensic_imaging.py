
import hashlib
import os
from datetime import datetime

# Function to create a forensic image (bit-by-bit copy)
def create_forensic_image(source_file, image_file):
    try:
        with open(source_file, 'rb') as src, open(image_file, 'wb') as img:
            while (chunk := src.read(4096)):
                img.write(chunk)
        print(f"Forensic image created: {image_file}")
    except Exception as e:
        print(f"Error creating forensic image: {e}")

# Function to calculate file hash for integrity verification
def calculate_hash(file_path, algorithm='sha256'):
    hash_func = hashlib.new(algorithm)
    try:
        with open(file_path, 'rb') as f:
            while (chunk := f.read(4096)):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        print(f"Error calculating hash: {e}")
        return None

# Function to simulate deleted file recovery
def recover_deleted_files(source_file, output_file):
    try:
        create_forensic_image(source_file, output_file)
        print(f"Simulated recovery: {output_file}")
    except Exception as e:
        print(f"Error recovering file: {e}")

# Function to handle anti-forensic measures (mock detection)
def detect_anti_forensic(file_path):
    if not os.path.exists(file_path):
        print("File does not exist. Possible overwriting or secure deletion detected.")
        return False
    print("File exists. No overwriting detected.")
    return True

# Function to log actions for chain of custody
def log_action(action, details):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chain_of_custody.log", "a") as log:
        log.write(f"[{timestamp}] {action}: {details}\n")
    print(f"Logged action: {action}")

# Main function
def main():
    source_file = "source.txt"
    forensic_image = "forensic_image.img"
    recovered_file = "recovered_file.txt"

    # Create a sample source file
    with open(source_file, "w") as f:
        f.write("This is a test file for forensic imaging.")

    # Step 1: Create forensic image
    log_action("Create Forensic Image", f"Source: {source_file}, Image: {forensic_image}")
    create_forensic_image(source_file, forensic_image)

    # Step 2: Verify integrity of forensic image
    original_hash = calculate_hash(source_file)
    image_hash = calculate_hash(forensic_image)
    print(f"Original File Hash: {original_hash}")
    print(f"Forensic Image Hash: {image_hash}")
    if original_hash == image_hash:
        print("Integrity verified. Hashes match.")
    else:
        print("Integrity verification failed. Hashes do not match.")

    # Step 3: Simulate file recovery
    log_action("Recover Deleted File", f"Source: {forensic_image}, Recovered: {recovered_file}")
    recover_deleted_files(forensic_image, recovered_file)

    # Step 4: Detect anti-forensic measures
    log_action("Anti-Forensic Detection", f"Check file existence for: {source_file}")
    detect_anti_forensic(source_file)

if __name__ == "__main__":
    main()
