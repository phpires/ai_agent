from functions.run_python import run_python_file
import unittest

def test_get_calculator_dir_info():
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))
test_get_calculator_dir_info()
