import re
import sys
import os

sys.path.append(os.getcwd())

from getip import *


def test_get_current_ip_is_str():
    assert isinstance(get_current_ip(), str)


def test_get_current_ip_is_ip():
    regex = r'(\d{1,3}\.){3}\d{1,3}'
    assert re.match(regex, get_current_ip())


def test_get_ip_data_is_dict():
    ip = get_current_ip()
    assert isinstance(get_ip_data(ip), dict)


def test_get_ip_data_len():
    ip = get_current_ip()
    assert len(get_ip_data(ip)) >= 3


def test_get_help_texts_is_dict():
    assert isinstance(get_help_texts(), dict)
