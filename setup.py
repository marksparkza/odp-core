import pathlib
import re

from setuptools import setup

HERE = pathlib.Path(__file__).parent.resolve()
VERSION = eval(re.search(
    '^VERSION = (.*)$',
    (HERE / 'odp' / 'version.py').read_text(encoding='utf-8'),
    re.MULTILINE,
)[1])

setup(version=VERSION)
