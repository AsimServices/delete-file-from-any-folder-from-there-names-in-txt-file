import os

def delete_images(folder_path, titles_file):
    # Read the full filenames from the text file
    with open(titles_file, "r") as file:
        filenames_to_delete = {line.strip() for line in file}

    deleted_count = 0  # Counter for deleted files

    # List files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the current filename is in the list of filenames to delete
        if filename in filenames_to_delete:
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f"Deleted: {file_path}")
            deleted_count += 1  # Increment the counter for each deleted file
        else:
            print(f"Skipped: {filename}")

    print(f"\nTotal images deleted: {deleted_count}")

# Specify the path to your images folder and the titles file
images_folder = r"D:\adobe stock work\2\processing_remaining_from_new cleaned"
titles_file = r"C:\Users\saifia computers\Downloads\responses (1)_filenames.txt"

# Call the function with both paths
delete_images(images_folder, titles_file)
