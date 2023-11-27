import os
import sys


def calculate_total_size(directory: str) -> None:
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"Not a directory: {directory}")

        total_size = 0

        for root, dirs, files in os.walk(directory):
            for filename in files:
                file_path = os.path.join(root, filename)

                try:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size

                except Exception as e:
                    print(f"Error accessing file {file_path}: {e}")

        print("EX 3")
        print(f"Total size of all files in {directory}: {total_size} bytes \n")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("EX 3 Usage: python script.py <directory_path> \n")
    else:
        directory_path = sys.argv[1]

        calculate_total_size(directory_path)

# python Teme/lab6/lab6_ex3.py Teme/lab6/lab6_files
