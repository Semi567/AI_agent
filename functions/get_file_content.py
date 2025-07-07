import os

def get_file_content(working_directory, file_path):
    # absolute paths
    abs_working = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    # check if the file is in  working directory:
    if os.path.commonpath([abs_working, abs_file_path]) != abs_working:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    # check if file_path is a file:
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    file_content_string = ''
    MAX_CHARS = 10000

    try:
        with open(abs_file_path, 'r') as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f'Error: {e}'
    
    return file_content_string