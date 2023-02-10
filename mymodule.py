import requests


def get_ip():
    """Get my current external IP."""
    return requests.get("https://icanhazip.com").text.strip()


def get_ip_long_docstring():
    """Get my current external IP, long docstring version"

    This is a long docstring.

    Yes, a really long docstring
    """
    return requests.get("https://github.com/annarailton/test-python-tools").text.strip()