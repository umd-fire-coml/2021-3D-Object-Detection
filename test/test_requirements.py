import pytest as pt
import pykitti as pk

def test_reqs():
    assert(pk.__version__ == "0.3.1")
