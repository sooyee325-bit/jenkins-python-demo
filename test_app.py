# test_app.py
import pytest
from app import add, divide   # 🔑 import from app.py

def test_add():
    assert add(2, 3) == 5

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
