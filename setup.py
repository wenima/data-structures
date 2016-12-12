from setuptools import setup

setup(
    name="linked_list",
    description="Week 2 Day 1 Assignment - Linked List",
    version=0.0,
    author="Ted Callahan and Mark Kessler-Wenicker",
    author_email="",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["linkedlist"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={
        'console_scripts': [
            "linked_list = linked_list:main"
        ]
    }
)
