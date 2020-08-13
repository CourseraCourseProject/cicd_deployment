import sys
# sys.path.append('../') # use this if running from the tests folder
sys.path.append('./')  # use this if running from the main folder
from src.app import index

def test_index() :
    assert index() == "Hello World"
