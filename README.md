# Demo_Project

This repository contains a Python-based Tic-Tac-Toe game and a Todo List application.

## Software Requirements

- Python3
- Pip (Python Package Installer)

## Setup for Windows

- Download and install Python3 from [Python Official Site](https://www.python.org/downloads/).
- Verify the installation by opening a command prompt and running the following commands:

```bash
python --version
pip --version
```
You should see the installed Python and Pip versions respectively.

## Setup for Mac

- Open a terminal window and install Python3 using Homebrew:

```bash
brew install python3
```
- Verify the installation by running the following commands:

```bash
python3 --version
pip3 --version
```
You should see the installed Python and Pip versions respectively.

## Starting Locally

After installation, navigate to the Python directory of this repository and you can run either of the programs by typing `python filename.py`, replacing "filename" with the name of the file you'd like to run (either `tic-tac-toe` or `todo`):

```bash
python tic-tac-toe.py
```
or

```bash
python todo.py
```
## Environments

There are no specific environments required for this project as Python is platform-agnostic. There is also no need for any databases as the apps run ephemerally and don't store state across sessions.

## Deployment Steps

There are no specific deployment steps necessary as the applications are local command-line-based apps in Python. Be sure that your machine meets the Software Requirements as outlined above. Please refer to the "Starting Locally" section for commands needed to run the applications.

Please note there is a .gitignore file included. This file is designed to specify intentionally untracked files to ignore when git is considering changes to the codebase. This can be particularly useful when considering what to deploy or share in production code and what to keep in local or test code. This file does not impact running the applications in this repository.