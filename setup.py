import jiracall
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='jiracall',
    version=jiracall.__version__,
    packages=['jiracall'],
    url='https://github.com/CoolCoderCarl/JAPI',
    license='GNU General Public License v3.0',
    author='Kir',
    author_email='123qwekir2wl@gmail.com',
    description=long_description,
    python_requires='>=3.7',
    install_requires=[
    'configparser==4.0.2',
    'jira==2.0.0'
    ]
)
