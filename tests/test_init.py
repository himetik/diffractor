import pytest
from gendiff import generate_diff  # Assuming 'gendiff' is the package and 'generate_diff' is exposed

def test_generate_diff_import():
    """Test that generate_diff is imported correctly from the package."""
    assert generate_diff is not None  # Check that the function is imported and not None
