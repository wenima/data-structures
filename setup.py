from setuptools import setup

setup(
    name="Codefellows Seattle Advanced Python 401 Course - Data Structure Assignments",
    description="this module holds all the data structures we built as part of data structure assignments",
    version=0.9,
    author="Marc Fieser, Ford Fowler, Ted Callahan, Marc Kessler-Wenicker",
    author_email="",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["bst"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={}
)
