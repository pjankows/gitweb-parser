import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name="gitweb-parser",
        version="0.1.0",
        author="Piotr Jankowski",
        author_email="pjankows@gmail.com",
        description="Gitweb pasrser to list directories and get file contents",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/pjankows/gitweb-parser",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=2.7"
)
