import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="patterns-yaminipendyala",
    version="0.0.1",
    author="Yamini Pendyala",
    author_email="pendyalay4488@gmail.com",
    description="Design the workflow of each pattern in the Symbols and Numbers, Alphabets, design There is a typical structure to print any pattern, i.e., the number of rows and columns. We need to use two loops to print any pattern, i.e., use nested loops. The outer loop tells us the number of rows, and the inner loop tells us the column needed to print the pattern.Accept the number of rows from a user using the input() function to decide the size of a pattern.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yaminipendyala/patterns",
    project_urls={
        "Bug Tracker": "https://github.com/yaminipendyala/patterns/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)