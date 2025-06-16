from functions.get_file_content import get_file_content
import unittest

def test_get_calculator_dir_info():
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
test_get_calculator_dir_info()
