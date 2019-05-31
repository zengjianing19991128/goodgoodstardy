import pytest


@pytest.mark.parametrize("num", [1, 2, 3, 4])
def test_csh(num):
    print("test_csh:", num)
    assert num != 2
