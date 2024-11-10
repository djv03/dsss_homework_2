
#### 5. `setup.py`:

from setuptools import setup, find_packages

setup(
    name="math_quiz",            # The name of the package
    version="0.1.0",             # Version of your package
    packages=find_packages(),    # Automatically find the math_quiz package
    install_requires=[           # External dependencies (if any)
        # 'dependency_name',
    ],
    entry_points={               # Define the command line interface
        'console_scripts': [
            'math_quiz=math_quiz.math_quiz:main',  # Command to run your app
        ],
    },
    tests_require=['pytest'],    # Testing dependencies
    test_suite='tests',          # Test directory
    include_package_data=True,   # Include non-Python files (if any)
    zip_safe=False,
)
