from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="Datapack Manager",
    version = "0.0.0",
    description = 'A set of tools to manage your world\'s datapacks',
    author = 'Leirof',
    author_email = 'vince.lrf@gmail.com',
    url = 'https://github.com/Gunivers/Datapack-Manager',
    readme = "README.md",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['DatapackManager'],
    install_requires=requirements,
    python_requires='>=3.10.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers'
    ]
)