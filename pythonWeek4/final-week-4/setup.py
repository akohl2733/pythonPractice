from setuptools import setup, find_packages

setup(
    name="taskmanager",
    version="0.1",
    packages = find_packages(),
    entry_points = {
        'console_scripts' : [
            'taskmanager=taskmanager.__main__:main'
        ]
    },
    description="A simple CLI task manager",
    author="Andrew",
    python_requires='>=3.6',
)