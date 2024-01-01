from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


with open("requirements_dev.txt") as f:
    requirements_dev = f.read().splitlines()


setup(
    name="monedero",
    version="0.2",
    author="Sebi",
    author_email="the@sebastardo.com",
    install_requires=requirements,
    extras_require={'dev': requirements_dev},
    packages=['monedero'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'monedero = monedero.__main__:main' 
        ]
    },
)