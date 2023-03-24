from setuptools import setup

setup(
    name='getip',
    version='1.0.0',
    py_modules=['getip'],
    install_requires=[
        'Click',
        'Requests'
    ],
    entry_points={
        'console_scripts': [
            'getip = getip:main',
        ],
    },
)
