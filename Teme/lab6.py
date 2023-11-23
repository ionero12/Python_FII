import os
import sys

def read_files_in_directory(directory, extension):
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        # Check if the provided path is a directory
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"Not a directory: {directory}")

        print("EX 1")
        # Iterate through files in the directory
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            # Check if the file has the specified extension
            if filename.endswith(extension):
                try:
                    # Read and print the contents of the file
                    with open(file_path, 'r') as file:
                        contents = file.read()
                        print(f"Contents of {filename}:\n{contents}\n{'-'*30} \n")

                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("EX 1 Usage: python script.py <directory_path> <file_extension> \n")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]

        # Call the function with the provided arguments
        read_files_in_directory(directory_path, file_extension)

# python Teme/lab6.py Teme/lab6 txt



def rename_files_with_prefix(directory):
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        # Check if the provided path is a directory
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"Not a directory: {directory}")

        # Get a list of files in the directory
        files = os.listdir(directory)

        print("EX 2")
        # Iterate through files and rename them with sequential number prefixes
        for i, filename in enumerate(files, start=1):
            old_path = os.path.join(directory, filename)
            new_filename = f"file{i}.{filename.split('.')[-1]}"  # Use the original file extension
            new_path = os.path.join(directory, new_filename)

            try:
                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed {filename} to {new_filename}")
            except Exception as e:
                print(f"Error renaming file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")
    print("\n")


if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("EX 2 Usage: python script.py <directory_path> \n")
    else:
        directory_path = sys.argv[1]

        # Call the function with the provided directory path
        rename_files_with_prefix(directory_path)

# python Teme/lab6.py Teme/lab6



def calculate_total_size(directory):
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        # Check if the provided path is a directory
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"Not a directory: {directory}")

        total_size = 0

        # Iterate through files in the directory and its subdirectories
        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)

                try:
                    # Get the size of the file and add it to the total
                    file_size = os.path.getsize(file_path)
                    total_size += file_size

                except Exception as e:
                    print(f"Error accessing file {file_path}: {e}")

        print("EX 3")
        print(f"Total size of all files in {directory}: {total_size} bytes \n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("EX 3 Usage: python script.py <directory_path> \n")
    else:
        directory_path = sys.argv[1]

        # Call the function with the provided directory path
        calculate_total_size(directory_path)

# python Teme/lab6.py Teme/lab6



def count_files_by_extension(directory):
    try:
        # Check if the directory exists
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        # Check if the provided path is a directory
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"Not a directory: {directory}")

        # Get a list of all files in the directory
        files = os.listdir(directory)

        # Check if the directory is empty
        if not files:
            raise ValueError(f"The directory is empty: {directory}")

        # Create a dictionary to store counts of each file extension
        extension_counts = {}

        # Iterate through files and count each extension
        for filename in files:
            _, file_extension = os.path.splitext(filename)

            # Increment the count for the file extension
            extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1

        # Print the counts for each extension
        print("EX 4")
        print("File counts by extension: ")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} files")
        print("\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("EX 4 Usage: python script.py <directory_path> \n")
    else:
        directory_path = sys.argv[1]

        # Call the function with the provided directory path
        count_files_by_extension(directory_path)

# python Teme/lab6.py Teme/lab6
