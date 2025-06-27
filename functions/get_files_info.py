import os

def get_files_info(working_directory, directory=None):
    if directory == None:
        directory = working_directory
    abs_working = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(working_directory, directory))
    if os.path.commonpath([abs_working, abs_directory]) != abs_working:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'
    
    represent = ""

    try:         
        for file in os.listdir(abs_directory):
            file_path = os.path.join(abs_directory, file)
            represent += f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"
    except Exception as e:
        return f"Error: {e}"
    
    return represent
