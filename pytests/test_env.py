import MY_MODULE
import inspect
from importlib.metadata import version


def test_sum_as_string():
    val = MY_MODULE.sum_as_string(5, 20)
    assert val == "25"


if __name__ == "__main__":
    print(inspect.getsourcefile(MY_MODULE))
    print(MY_MODULE.sum_as_string.__doc__)
    print(version("MY_MODULE"))
