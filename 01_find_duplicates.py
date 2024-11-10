import hashlib
import os

# Define base path using $HOME
base_path = os.path.join(os.path.expanduser("~"), "Documents", "lg", "multimedia")
print(f"Base path is: {base_path}")


# Function to generate a unique hash for each file
def hash_file(filepath):
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        # Read file in chunks
        for block in iter(lambda: f.read(4096), b""):
            hasher.update(block)
    return hasher.hexdigest()


# Function to get the file size
def get_file_size(filepath):
    return os.path.getsize(filepath)


# Dictionary to store files by their hash
files_by_hash = {}

# Variables for statistics
total_files = 0
duplicate_files = 0
unique_files = 0
total_duplicate_size = 0  # In bytes
total_unique_size = 0  # In bytes

# Recursive traversal of the base folder
for root, dirs, files in os.walk(base_path):
    for file in files:
        # Filter for images and videos only
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.mp4', '.mov', '.avi', '.dng', '.raw')):
            filepath = os.path.join(root, file)
            total_files += 1  # Count total files
            print(end=".")  # Debug print
            file_hash = hash_file(filepath)

            # If the hash already exists in the dictionary
            if file_hash in files_by_hash:
                # Append the new file path to the duplicates list
                files_by_hash[file_hash].append(filepath)
                duplicate_files += 1
                total_duplicate_size += get_file_size(filepath)  # Add file size to duplicates total
            else:
                # If it's not a duplicate, create a new list with the first path
                files_by_hash[file_hash] = [filepath]
                unique_files += 1
                total_unique_size += get_file_size(filepath)  # Add file size to unique total

print(end="\n")

# Check if duplicates were found
if any(len(paths) > 1 for paths in files_by_hash.values()):
    # Save duplicates to a file
    with open("duplicates.txt", "w") as f:
        for file_hash, filepaths in files_by_hash.items():
            if len(filepaths) > 1:  # Only save duplicates
                f.write(f"{file_hash}:\n")
                for filepath in filepaths:
                    f.write(f"{filepath}\n")
                f.write("\n")
    print("The file 'duplicates.txt' has been generated with the map of duplicate files.")
else:
    print("No duplicate files were found.")

# Print out statistics
print("\nStatistics:")
print(f"Total files processed: {total_files}")
print(f"Unique files: {unique_files}")
print(f"Duplicate files found: {duplicate_files}")

# Calculate percentages
if total_files > 0:
    duplicate_percentage = (duplicate_files / total_files) * 100
    unique_percentage = (unique_files / total_files) * 100
    print(f"Percentage of unique files: {unique_percentage:.2f}%")
    print(f"Percentage of duplicate files: {duplicate_percentage:.2f}%")


# Convert size to MB for easier readability
def bytes_to_mb(byte_size):
    return byte_size / (1024 * 1024)


# Show the space that could be freed by deleting duplicates
print(f"Total space occupied by unique files: {bytes_to_mb(total_unique_size):.2f} MB")
print(f"Total space occupied by duplicates (could be freed): {bytes_to_mb(total_duplicate_size):.2f} MB")
