import pytest


@pytest.mark.usefixtures("setup")  # browser invocation is defined as fixture, for reducibility
class BaseClass:
    pass
