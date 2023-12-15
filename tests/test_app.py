from app import adding
from app import calculating
from app import multiplying

def test_calculating():
    result = calculating(2, 2)
    assert result == 16

def test_calculating2():
    result = calculating(7, 3)
    assert result == -10

def test_calculating3():
    result = calculating(1, 4)
    assert result == 4
  
def test_multiplying():
    result = multiplying(2, 5)
    assert result == 10

def test_adding():
    result = adding(6, 3)
    assert result == 9