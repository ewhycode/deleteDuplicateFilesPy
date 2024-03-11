import os
import hashlib

def get_file_hash(file_path):
    """Calculate the hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def find_duplicate_files(directory):
    """Find duplicate files in a directory."""
    file_hash_dict = {}
    duplicate_files = []

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_hash = get_file_hash(file_path)
            if file_hash in file_hash_dict:
                duplicate_files.append((file_path, file_hash))
            else:
                file_hash_dict[file_hash] = file_path

    return duplicate_files

def delete_duplicate_files(duplicate_files):
    """Delete duplicate files."""
    for file_path, _ in duplicate_files:
        os.remove(file_path)
        print(f"Deleted duplicate file: {file_path}")

if __name__ == "__main__":
    directory = input("Enter the directory path to search for duplicates: ")
    if os.path.isdir(directory):
        duplicates = find_duplicate_files(directory)
        if duplicates:
            print("Duplicate files found:")
            for file_path, _ in duplicates:
                print(file_path)
            delete_files = input("Do you want to delete the duplicate files? (yes/no): ").lower()
            if delete_files == "yes":
                delete_duplicate_files(duplicates)
                print("Duplicate files deleted successfully.")
            else:
                print("Duplicate files not deleted.")
        else:
            print("No duplicate files found.")
    else:
        print("Invalid directory path.")
