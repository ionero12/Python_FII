import os
import sys


def rename_files_with_prefix(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"Not a directory: {directory}")

        files = os.listdir(directory)

        print("EX 2")
        for i, filename in enumerate(files, start=1):
            old_path = os.path.join(directory, filename)
            new_filename = f"file{i}.{filename.split('.')[-1]}"
            new_path = os.path.join(directory, new_filename)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed {filename} to {new_filename}")
            except Exception as e:
                print(f"Error renaming file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")
    print("\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("EX 2 Usage: python script.py <directory_path> \n")
    else:
        directory_path = sys.argv[1]

        rename_files_with_prefix(directory_path)

# python Teme/lab6/lab6_ex2.py Teme/lab6/lab6_files
