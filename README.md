# "gendiff" CLI Application

[![Actions Status](https://github.com/himetik/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/himetik/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/408d27b88775611bdfc5/maintainability)](https://codeclimate.com/github/himetik/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/408d27b88775611bdfc5/test_coverage)](https://codeclimate.com/github/himetik/python-project-50/test_coverage)

> "gendiff" make a difference!

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

```sh
python3 -m venv bubble
source bubble/bin/activate
```

2. **Clone the repository and then go into it:**

```sh
git clone git@github.com:himetik/python-project-50.git
cd python-project-50
```

3. **Install the app with just one command:**

```sh
make run
```

<br/>