# "gendiff" CLI Application

[![Actions Status](https://github.com/himetik/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/himetik/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/408d27b88775611bdfc5/maintainability)](https://codeclimate.com/github/himetik/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/408d27b88775611bdfc5/test_coverage)](https://codeclimate.com/github/himetik/python-project-50/test_coverage)

> "gendiff" can make a difference!

<br/>

GenDiff is a command-line application that compares two files and generates the difference between them. 
The application supports files in JSON and YAML formats and provides three output formats for displaying the differences: stylish, plain, and json.

#### Features

 - File Comparison: Compares two files and identifies the differences between them.
 - Supported Formats: Works with files in JSON and YAML (YML) formats.
 - Output Formats: Displays the differences in three different formats:
   - Stylish: A nested format that shows the differences in a hierarchical structure.
   - Plain: A plain text format that shows the differences in a straightforward, linear way.
   - JSON: A JSON format that outputs the differences as a JSON object.
 
<br/>

## Installation

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

# Use "gendiff" to Compare Two JSON/YAML Files

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

# Tools and Technologies Used

- **Git**: ![Git](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/svgs/brands/git.svg)  
  A distributed version control system for managing source code changes.

- **Bash**: ![Bash](https://cdn-icons-png.flaticon.com/512/862/862188.png)  
  A Unix shell and command language used for scripting and automation.

- **Python**: ![Python](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/svgs/brands/python.svg)  
  A high-level programming language known for its simplicity and readability.

- **VSCode**: ![VSCode](https://cdn.iconscout.com/icon/free/png-256/visual-studio-code-3629045-3029780.png)  
  A source-code editor with support for debugging, syntax highlighting, and more.

- **Poetry**: ![Poetry](https://avatars.githubusercontent.com/u/37447213?s=200&v=4)  
  A dependency management and packaging tool for Python projects.

- **pytest**: ![pytest](https://avatars.githubusercontent.com/u/1844188?s=200&v=4)  
  A framework for writing simple and scalable test cases in Python.
  