import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    add_error = False
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    args = ["python3", f"{abs_file_path}"]
    try:
        completed_process = subprocess.run(args=args, timeout=30, capture_output=True, text=True, cwd=abs_working_dir,)
        #print(f"completed_process: {completed_process}")
        if completed_process.stdout == "":
            return "No output produced"
        if completed_process.returncode != 0:
            add_error = True
        if (add_error):
            output=f"""STDOUT: {completed_process.stdout}
STDERR: {completed_process.stderr}
Process exited with code {completed_process.returncode}"""
        else:
            output=f"""STDOUT: {completed_process.stdout}
STDERR: {completed_process.stderr}"""
        return output
        
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file found on the given file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path for a python file, relative to the working directory. It will be executed if the file ends with '.py' meaning it is a python script.",
            ),
        },
    ),
)