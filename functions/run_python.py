import os
import subprocess

def run_python_file(working_directory, file_path):
    # absolute paths
    abs_working = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    # check if the file is in working directory:
    if os.path.commonpath([abs_working, abs_file_path]) != abs_working:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    # check is file_path exists
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    # check if file is a python file
    if not abs_file_path.endswith(".py"): 
        return f'Error: "{file_path}" is not a Python file.'
    
    lines = []
    try:
        process = subprocess.run(["uv", "run", file_path], cwd=abs_working, timeout=30, capture_output=True)
        stdout = process.stdout.decode()
        stderr = process.stderr.decode()
        if stdout != '':
            lines.append("STDOUT: " + stdout)
        if stderr != '':
            lines.append("STDERR: " + stderr)
        if stdout == '' and stderr == '':
            lines.append("No output produced.")
        if process.returncode != 0:
            lines.append(f"Process exited with code {process.returncode}")
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    return "\n".join(lines).strip()