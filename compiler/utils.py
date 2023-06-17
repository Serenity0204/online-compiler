import subprocess
import tempfile
import os
import shutil


def run_cpp_code(code):
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Create a temporary file for the C++ code
    code_file = os.path.join(temp_dir, "code.cpp")
    with open(code_file, "w") as file:
        file.write(code)

    # Create a temporary file for the executable
    exe_file = os.path.join(temp_dir, "code.exe")

    try:
        # Compile the C++ code using g++
        compile_result = subprocess.run(
            ["g++", code_file, "-o", exe_file], stderr=subprocess.DEVNULL
        )

        if compile_result.returncode == 0:
            # Execution if compilation succeeds
            # Execute the compiled C++ code
            result = subprocess.run(exe_file, capture_output=True, text=True)

            # Return the output and error (if any)
            return result.stdout, result.stderr
        else:
            # Execution if compilation fails
            return None, "Compilation error"

    finally:
        # Remove the temporary directory and its contents
        shutil.rmtree(temp_dir)
