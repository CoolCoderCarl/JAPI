from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='jiracall',
    version='0.0.1',
    packages=['jiracall'],
    url='https://github.com/CoolCoderCarl/JAPI',
    license='MIT Licensse',
    author='Kir',
    author_email='123qwekir2wl@gmail.com',
    description=long_description,
    python_requires='>=3.7'
)
