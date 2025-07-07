import os

def write_file(working_directory, file_path, content):
    # absolute paths
    abs_working = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    # check if the file is in working directory:
    if os.path.commonpath([abs_working, abs_file_path]) != abs_working:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        os.makedirs(os.path.dirname(abs_file_path), mode=0o777, exist_ok=True)

        with open(abs_file_path, "w") as f:
            f.write(content)
        
    except Exception as e:
        return f'Error: {e}'
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'