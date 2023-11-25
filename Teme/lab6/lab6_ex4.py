import os
import sys


def count_files_by_extension(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"Not a directory: {directory}")

        files = os.listdir(directory)

        if not files:
            raise ValueError(f"The directory is empty: {directory}")

        extension_counts = {}

        for filename in files:
            _, file_extension = os.path.splitext(filename)

            extension_counts[file_extension] = extension_counts.get(file_extension, 0) + 1

        print("EX 4")
        print("File counts by extension: ")
        for extension, count in extension_counts.items():
            print(f"{extension}: {count} files")
        print("\n")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("EX 4 Usage: python script.py <directory_path> \n")
    else:
        directory_path = sys.argv[1]

        count_files_by_extension(directory_path)

# python Teme/lab6/lab6_ex4.py Teme/lab6/lab6_files
