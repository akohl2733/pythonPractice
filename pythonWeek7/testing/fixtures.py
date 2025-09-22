import pytest

@pytest.fixture
def sample_numbers():
    return [1, 2, 3, 4]

def test_sum(sample_numbers):
    assert sum(sample_numbers) == 10