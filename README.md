# 🌅 Command-Line File Comparison Tool

[![Actions Status](https://github.com/himetik/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/himetik/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/408d27b88775611bdfc5/maintainability)](https://codeclimate.com/github/himetik/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/408d27b88775611bdfc5/test_coverage)](https://codeclimate.com/github/himetik/python-project-50/test_coverage)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-himetik-%2321A366)](https://www.linkedin.com/in/george-igolkin-120247231/)

> 'gendiff' can make a difference!

<br/>

*'gendiff' is a command-line application that compares two files and generates the difference between them. 
The application supports files in JSON and YAML formats and provides three output formats for displaying the differences: stylish, plain, and json.*

<br/>

### ⚙️ Features

 - File Comparison: Compares two files and identifies the differences between them.

 - Supported Formats: Works with files in JSON and YAML (YML) formats.

 - Output Formats: Displays the differences in three different formats:
   - Stylish: A nested format that shows the differences in a hierarchical structure.
   - Plain: A plain text format that shows the differences in a straightforward, linear way.
   - JSON: A JSON format that outputs the differences as a JSON object.
 
<br/>

### 🔌 Installation

> It is recommended to use a virtual environment

1. **Well, this is how you can start the virtual environment**
(let's call it, for example, bubble) **if you have Python3 installed.**

```bash
python3 -m venv bubble
source bubble/bin/activate
```

2. **Clone the repository and then go into it:**

```bash
git clone git@github.com:himetik/python-project-50.git
cd python-project-50
```

3. **Install the app with just one command:**

```bash
make run
```

<br/>

### 🕹️ Use 'gendiff' to Compare Two JSON/YAML Files

- **Stylish Format (default)**: 
  Displays the differences in a human-readable format.

```bash
gendiff -f stylish first.yaml second.yml
```

- **Plain Format**: 
  Shows the differences in a plain text format.

```bash
gendiff -f plain first.json second.json
```

- **JSON Format**: 
  Outputs the differences in JSON.

```bash
gebdiff -f json first.json first.yaml
```

<br/>

### 🛠️ Tools and Technologies Used

The project utilizes a variety of tools and technologies to enhance development and maintain code quality:

<img src="images/git.png" width="25" height="25" alt="Git"> **Git** is a distributed version control system used for managing source code changes and collaboration. 

<img src="images/bash.png" width="25" height="25" alt="Bash"> **Bash** serves as a Unix shell and command language, essential for scripting and automation tasks in development environments.

<img src="images/python3.png" width="25" height="25" alt="Python"> **Python** is employed as a high-level programming language, valued for its simplicity and readability, making it a preferred choice for various programming tasks.

<img src="images/code.png" width="25" height="25" alt="VSCode"> **VSCode** is the source-code editor of choice, offering robust support for debugging, syntax highlighting, and many other features that streamline coding and development.

🔩 **Poetry** is used as a dependency management and packaging tool specifically designed for Python projects, facilitating easy management of project dependencies and packaging.

🧪 **pytest** is the testing framework adopted for writing simple and scalable test cases in Python, ensuring code reliability and correctness through comprehensive testing.

<br/>

### 🛰️ Project Version and Dependencies

<small>**Project version**: `0.1.0`</small><br>

The project requires the following dependencies:

<small>**Python**: `^3.10`</small><br>
<small>**PyYAML**: `^6.0`</small><br>

For development and testing, the following packages are used:

<small>**pytest**: `^7.2.0`</small><br>
<small>**ipython**: `^8.8.0`</small><br>
<small>**pytest-cov**: `^4.0.0`</small><br>
<small>**flake8**: `^6.0.0`</small><br>
<small>**isort**: `^5.11.4`</small><br>

<br/>
