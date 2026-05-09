import os
import shutil

def organize_images(source_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created directory: {dest_dir}")

    # Count for tracking moved files
    moved_count = 0

    # List all files in the source directory
    try:
        files = os.listdir(source_dir)
        
        for file_name in files:
            # Check if the file ends with .jpg (case-insensitive)
            if file_name.lower().endswith('.jpg'):
                source_path = os.path.join(source_dir, file_name)
                dest_path = os.path.join(dest_dir, file_name)
                
                # Move the file
                shutil.move(source_path, dest_path)
                print(f"Moved: {file_name}")
                moved_count += 1

        print(f"\nTask Complete! Total .jpg files moved: {moved_count}")

    except FileNotFoundError:
        print("The source directory was not found. Please check the path.")

if __name__ == "__main__":
    # You can replace these with your actual folder paths
    # Use r'' for Windows paths to handle backslashes correctly
    src = "Downloads" 
    dst = "Images/JPG_Collection"
    
    organize_images(src, dst)