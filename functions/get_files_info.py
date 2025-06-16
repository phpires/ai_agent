import os

def get_files_info(working_directory, directory=None):
    print(f"Working on dir: {directory}")
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        working_dirs = os.listdir(working_dir_abs_path)

        if directory == "." or not directory:
            dir_abs_path = working_dir_abs_path
        else:
            dir_abs_path = working_dir_abs_path + "/" + directory
        
        if (directory not in working_dirs) and (directory != "."):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(dir_abs_path):
            return f'Error: "{directory}" is not a directory'

        result_str = ""

        for file_name in os.listdir(dir_abs_path):
            file_path = dir_abs_path + "/" + file_name
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            result_str += f'- {file_name}: file_size={file_size} bytes, is_dir={is_dir}\n'
        return result_str
    except Exception as e:
        return f"Error: {e}"
    
