import pytest
from pathlib import Path
from reverse import reverse

# Функция для получения пути к файлу в папке test_data
def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

# Функция для чтения содержимого файла
def read_file(filename):
    return get_test_data_path(filename).read_text(encoding="utf-8").strip()

def test_reverse():
    input_text = read_file("input.txt")
    expected_result = read_file("expected.txt")
    
    actual_result = reverse(input_text)

    assert actual_result == expected_result
