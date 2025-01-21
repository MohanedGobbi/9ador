import subprocess
import os


def execute_executable(file_path):
    """
    Executes an executable file given its path.

    :param file_path: Path to the executable file.
    """
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist.")
            return

        # Execute the file
        print(f"Executing '{file_path}'...")
        result = subprocess.run(file_path, shell=True, check=True)

        # Print the return code (0 usually means success)
        print(f"Execution completed with return code: {result.returncode}")

    except subprocess.CalledProcessError as e:
        print(f"Error: The executable failed with return code {e.returncode}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Path to the executable file (update this to your file's path)
    executable_path = "C:/path/to/your/program.exe"  # Windows example
    # executable_path = "/path/to/your/script.sh"    # Linux/macOS example

    # Execute the executable
    execute_executable(executable_path)