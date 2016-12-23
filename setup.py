from setuptools import setup

setup(
    name="simple_graph",
    description="this module demonstrates the graph data structure",
    version=1.1,
    author="Marc Fieser and Marc Kessler-Wenicker",
    author_email="",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["simple_graph"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={}
)
