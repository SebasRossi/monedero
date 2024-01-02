from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


with open("requirements_dev.txt") as f:
    requirements_dev = f.read().splitlines()


setup(
    name="monedero",
    version="0.2",
    author="Sebi",
    author_email="the@sebastardo.com",
    packages=['monedero'],
    #packages=['monedero', 'monedero.functions'],
    #packages=find_packages(),
    license='MIT',
    entry_points={
        'console_scripts': [
            'monedero = monedero.__main__:main' 
        ]
    },
    install_requires=requirements,
    extras_require={'dev': requirements_dev},
)