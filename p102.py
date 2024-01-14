import os
import shutil

# Create variables for source and destination paths
from_dir = "path/to/Downloads"
to_dir = "path/to/Document_Files"

# Get the list of files in the source path
list_of_files = os.listdir(from_dir)

# Print the list of files
print("Files in the source path:")
print(list_of_files)

# Traverse through the list of files
for file_name in list_of_files:
    # Get the name and extension of each file
    name, extension = os.path.splitext(file_name)

    # Check if the extension is blank, if true, continue to the next file
    if not extension:
        continue

    # Check if the extension is in the list of allowed extensions
    if extension.lower() in ['.txt', '.doc', '.docx', '.pdf']:
        # Create directory paths
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name

        # Check if the destination path exists
        if os.path.exists(path2):
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)
        else:
            # Create the destination directory path
            os.makedirs(path2)
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)

print("File movement completed.")