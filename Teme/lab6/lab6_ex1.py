import os
import sys


def read_files_in_directory(directory: str, extension: str) -> None:
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        if not os.path.isdir(directory):
            raise NotADirectoryError(f"Not a directory: {directory}")

        print("EX 1")
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            if filename.endswith(extension):
                try:
                    with open(file_path, 'r') as file:
                        contents = file.read()
                        print(f"Contents of {filename}:\n{contents}\n{'-' * 30} \n")

                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("EX 1 Usage: python script.py <directory_path> <file_extension> \n")
    else:
        directory_path = sys.argv[1]
        file_extension = sys.argv[2]

        read_files_in_directory(directory_path, file_extension)

# python Teme/lab6_ex1.py Teme/lab6/lab6_files txt
