import os
import shutil
import hashlib

def calculate_hash(file_path):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def backup_new_patches(main_ssd_path, backup_ssd_path):
    """Backup new .nmsv synth patches from the main SSD to the backup SSD."""
    backup_patches = []
    new_patches = []

    # Get the list of patches already backed up
    for root, dirs, files in os.walk(backup_ssd_path):
        for file in files:
            if file.endswith(".nmsv"):
                backup_patches.append(file)

    # Check for new patches in the main SSD
    for root, dirs, files in os.walk(main_ssd_path):
        for file in files:
            if file.endswith(".nmsv") and file not in backup_patches:
                new_patches.append(os.path.join(root, file))

    # Backup new patches to the backup SSD
    for patch_path in new_patches:
        patch = os.path.basename(patch_path)
        backup_path = os.path.join(backup_ssd_path, patch)
        shutil.copy2(patch_path, backup_path)
        print(f"Backed up {patch} to {backup_path}")

if __name__ == "__main__":
    # Specify the paths to the main SSD and backup SSD
    main_ssd_path = ".././may 2023 patches"
    backup_ssd_path = ".././Patch Python Output"

    # Backup new patches
    backup_new_patches(main_ssd_path, backup_ssd_path)
