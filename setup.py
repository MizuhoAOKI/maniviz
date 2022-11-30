import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="maniviz",
    version="0.0.1",
    install_requires=[
        "rich",
        "logging",
        "numpy",
        "matplotlib"
    ],
    entry_points={
        'console_scripts': [
        ],
    },
    author="MizuhoAOKI",
    author_email="mizuhoaoki1998@gmail.com",
    description="Manipulator visualizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)