# tests/test_calculator.py
import pytest
from calculator import add,subtract


# 正常情况测试
def test_add_normal():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


# 边界情况测试
def test_add_edge_cases():
    assert add(999999, 1) == 1000000
    assert add(-999999, -1) == -1000000
    assert add(1.5, 2.5) == 4.0


# 异常情况测试（类型错误）
def test_add_type_error():
    with pytest.raises(TypeError):
        add("string", 1)
    with pytest.raises(TypeError):
        add(None, 2)
    with pytest.raises(TypeError):
        add([], {})


def test_subtract_normal():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-1, -1) == 0


def test_subtract_edge_cases():
    assert subtract(1.5, 0.5) == 1.0
    assert subtract(1000, -1) == 1001


def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract("a", 1)
    with pytest.raises(TypeError):
        subtract(None, [])
