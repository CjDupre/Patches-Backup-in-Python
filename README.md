## Synth Patch Backup Utility

The Synth Patch Backup Utility is a Python program that automates the process of checking for new `.nmsv` synth patches on a main SSD and backs them up to a chosen folder on a backup SSD while ignoring duplicates or already backed up patches.

### Functional Requirements

- Scan the main SSD folder for `.nmsv` files.
- Compare the files in the main SSD folder with the files in the backup SSD folder to identify new patches.
- Copy new patches from the main SSD folder to the backup SSD folder.
- Ignore duplicates or patches that have already been backed up.
- Log the backup process, displaying the names and paths of the new patches that are successfully backed up.

### Non-functional Requirements

- Implemented in Python.
- Efficient processing of a large number of patches.
- Robust and reliable handling of file copying and hash calculations.
- Simple and user-friendly user interface.
- Informative error messages in case of failures or exceptions.

### Inputs

- Path to the main SSD folder containing the `.nmsv` patches.
- Path to the backup SSD folder where the new patches will be backed up.

### Outputs

- Log messages indicating the backup process, including the names and paths of the new patches that are successfully backed up.
- Informative error messages in case of failures or exceptions.

### Algorithm

1. Initialize empty lists to store the names of patches in the main SSD and backup SSD folders.
2. Traverse the backup SSD folder and populate the backup patches list with the names of the existing patches.
3. Traverse the main SSD folder and its subdirectories.
4. For each file ending with `.nmsv` encountered:
   - Check if it exists in the backup patches list.
   - If it does not exist, add its path to the new patches list.
5. For each new patch:
   - Copy the file from the main SSD folder to the backup SSD folder.
   - Log the backup process by displaying the names and paths of the new patches that are successfully backed up.

### Error Handling

- Display an error message if the main SSD folder or backup SSD folder does not exist or is inaccessible.
- Provide appropriate error messages for any file-related errors encountered during the backup process, such as permission issues or disk full errors.

### Constraints

- Efficient handling of large numbers of patches.
- Support for patches of varying sizes.
- Support for long file paths and names.
- Support for special characters in file names.

### Testing

- Perform unit testing to ensure the correct functioning of individual components.
- Conduct integration testing to verify the interaction between different modules.
- Test the program with different scenarios, including various combinations of existing and new patches, empty folders, and invalid paths.
- Evaluate the program's performance with a large number of patches.
- Validate the correctness of the backup process by verifying that new patches are successfully backed up while duplicates or already backed up patches are ignored.
