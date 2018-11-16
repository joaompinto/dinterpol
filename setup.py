from setuptools import setup, find_packages
setup(
    name="dinterpol",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dinterpol = dinterpol.__main__:main'
        ]
    }
)
