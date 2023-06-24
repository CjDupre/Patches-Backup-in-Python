Title: Synth Patch Backup Utility
Objective: The objective of this program is to automate the process of checking for new .nmsv synth patches on a main SSD, and back up the new patches to a chosen folder on a backup SSD while ignoring duplicates or already backed up ones.
Functional Requirements:
The program should scan the main SSD folder for .nmsv files.
It should compare the files in the main SSD folder with the files in the backup SSD folder to identify new patches.
New patches should be copied from the main SSD folder to the backup SSD folder.
The program should ignore duplicates or patches that have already been backed up.
The program should log the backup process, displaying the names and paths of the new patches that are successfully backed up.
Non-functional Requirements:
The program should be implemented in Python.
The program should be efficient in processing large numbers of patches.
The program should handle file copying and hash calculations in a robust and reliable manner.
The user interface should be simple and user-friendly.
The program should provide informative error messages in case of any failures or exceptions.
Inputs:
Path to the main SSD folder containing the .nmsv patches.
Path to the backup SSD folder where the new patches will be backed up.
Outputs:
Log messages indicating the backup process, including the names and paths of the new patches that are successfully backed up.
Informative error messages in case of any failures or exceptions.
Algorithm:
Initialize empty lists to store the names of patches in the main SSD and backup SSD folders.
Traverse the backup SSD folder and populate the backup patches list with the names of the existing patches.
Traverse the main SSD folder and populate the main patches list with the names of the patches.
Compare the main patches list with the backup patches list to identify new patches.
For each new patch, copy the file from the main SSD folder to the backup SSD folder.
Log the backup process by displaying the names and paths of the new patches that are successfully backed up.
Error Handling:
If the main SSD folder or backup SSD folder does not exist or is inaccessible, display an error message indicating the issue.
If there are any file-related errors during the backup process, such as permission issues or disk full errors, display an appropriate error message.
Constraints:
The program should handle large numbers of patches efficiently.
The program should handle patch files of varying sizes.
The program should handle long file paths and names.
The program should handle special characters in file names.
