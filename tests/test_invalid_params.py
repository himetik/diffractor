from pathlib import Path

from gendiff.gendiff import generate_diff
import pytest

FIXT_PATH = Path('tests/fixtures/input')

flat1_json = FIXT_PATH / 'flat1.json'
flat2_json = FIXT_PATH / 'flat2.json'
file1_bat = FIXT_PATH / 'nested1.bat'
file2_bat = FIXT_PATH / 'nested2.bat'


def test_generate_diff_unssupported_formatter_type():
    """Test generate_diff function with unssupported formatter type."""
    formatter_type = 'some_type'
    expected = (
        'formatter_type parameter can only take the following values: '
        f'plain, json, stylish. Current value is {formatter_type}'
    )
    with pytest.raises(ValueError) as excinfo:
        generate_diff(flat1_json, flat2_json, formatter_type)
    assert str(excinfo.value) == expected


def test_generate_diff_unssupported_file_type():
    """Test generate_diff function with unsupported file type."""
    expected = (
        'Error parsing files: Unsupported file type: ".bat". '
        'Supported file types: .json, .yml, .yaml'
    )
    diff = generate_diff(file1_bat, file1_bat)
    assert diff == expected


@pytest.mark.parametrize(
    'file1, file2, expected_error',
    [
        (file1_bat, file2_bat, 'Error parsing files: Unsupported file type: ".bat". Supported file types: .json, .yml, .yaml'),
        # Можно добавить другие примеры
    ]
)
def test_generate_diff_unsupported_file_types(file1, file2, expected_error):
    """Test generate_diff function with unsupported file types."""
    diff = generate_diff(file1, file2, 'json')
    assert diff == expected_error
