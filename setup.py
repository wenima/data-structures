from setuptools import setup

setup(
    name="Priority Queue",
    description="In a priority queue, an element with a high priority will be served before an element with a lower priority. If both have equal priority, the first element that entered the list will be added",
    version=1.1,
    author="Marc Fieser and Mark Kessler-Wenicker",
    author_email="",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["binheap, priorityq"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={}
)
