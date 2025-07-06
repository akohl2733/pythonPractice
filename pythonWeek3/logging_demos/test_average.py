import pytest
from average import compute_average

def test_valid_input(caplog):
    with caplog.at_level("INFO"):
        result = compute_average([10, 20, 30])
        assert result == 20
        assert "Received numbers: [10, 20, 30]" in caplog.text
        assert "Total is 60" in caplog.text
        assert "Average is 20.0" in caplog.text

def test_list_empty(caplog):
    with caplog.at_level("WARNING"):
        result = compute_average([])
        assert result is None
        assert "Empty list provided - cannot compute average" in caplog.text

def test_non_number(caplog):
    with caplog.at_level("ERROR"):
        result = compute_average(["Andrew"])
        assert result is None
        assert "Values are not all numerical." in caplog.text