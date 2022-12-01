import setuptools
import maniviz

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="maniviz",
    version=maniviz.__version__,
    install_requires=[
        "typing>=3.7.4.3",
        "rich>=12.6.0",
        "numpy>=1.19.5",
        "matplotlib>=3.4.0"
    ],
    entry_points={
        'console_scripts': [
        ],
    },
    author="MizuhoAOKI",
    author_email="mizuhoaoki1998@gmail.com",
    description="maniviz: A simple visualizer of a manipulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MizuhoAOKI/maniviz",
    download_url="https://github.com/MizuhoAOKI/maniviz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
        "Framework :: Matplotlib",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
