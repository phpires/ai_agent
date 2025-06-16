import os

MAX_CHAR_SIZE = 10000
def get_file_content(working_directory, file_path):
    
    abs_working_dir = os.path.abspath(working_directory)
    #print(f"abs_working_dir: {abs_working_dir}")
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    #print(f"abs_file_path: {abs_file_path}")

    if not abs_file_path.startswith(abs_working_dir):
        print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile(abs_file_path):
        print(f'Error: File not found or is not a regular file: "{file_path}"')
    try:
        with open(abs_file_path, "r") as f:
            file_content_total = f.read()
            print(f"Total chars: {len(file_content_total)}")
            if len(file_content_total) > MAX_CHAR_SIZE:
                file_content_total = file_content_total[:MAX_CHAR_SIZE]
                file_content_total += f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content_total
    except Exception as e:
        print(f'Error: {e}')
