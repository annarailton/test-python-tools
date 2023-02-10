from mymodule import get_ip, get_ip_long_docstring

def test_get_ip_type():
    """The IP is expected to be a string."""
    ip = get_ip()
    assert isinstance(ip, str)


def test_get_ip_dots():
    """The IP(v4) is expected to have 4 dots."""
    ip = get_ip()
    assert ip.count('.') == 3


def test_get_ip_type2():
    """The IP is expected to be a string."""
    ip = get_ip_long_docstring()
    assert isinstance(ip, str)


def test_get_ip_dots2():
    """The IP(v4) is expected to have 4 dots."""
    ip = get_ip_long_docstring()
    assert ip.count('.') == 3
