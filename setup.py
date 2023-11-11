from setuptools import setup

setup(name='curriculum', version='1.0.0',packages=['curriculum'],
entry_points= {
    'console.scripts': ['curriculum = curriculum.__main__:main']
})