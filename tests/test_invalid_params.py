import pytest

from pathlib import Path

from gendiff.gendiff import generate_diff

FIXT_PATH = Path('tests/fixtures/input')

flat1_json = FIXT_PATH / 'flat1.json'
flat2_json = FIXT_PATH / 'flat2.json'
file1_bat = FIXT_PATH / 'nested1.bat'
file2_bat = FIXT_PATH / 'nested2.bat'


def test_generate_diff_unsupported_file_type():
    """Test generate_diff function with unsupported file type."""
    with pytest.raises(ValueError) as excinfo:
        generate_diff(file1_bat, file2_bat)
    
    assert str(excinfo.value) == 'Unsupported file type: ".bat". Supported file types: .json, .yml, .yaml'

@pytest.mark.parametrize(
    'file1, file2, expected_error',
    [
        (file1_bat, file2_bat, 'Unsupported file type: ".bat". Supported file types: .json, .yml, .yaml'),
    ]
)
def test_generate_diff_unsupported_file_types(file1, file2, expected_error):
    """Test generate_diff function with unsupported file types."""
    with pytest.raises(ValueError) as excinfo:
        generate_diff(file1, file2, 'json')
    
    assert str(excinfo.value) == expected_error
