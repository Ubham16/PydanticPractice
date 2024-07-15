from setuptools import setup, find_packages

setup(
    name='PydanticPractice',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pydantic',  # Add any other dependencies your project requires
    ],
    entry_points={
        'console_scripts': [
            # If you have any scripts to run, specify them here
            # 'your-script-name = your_module:main_function',
        ],
    },
)
