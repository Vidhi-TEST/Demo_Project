# Demo_Project 

This project is a demonstration of a simple Tic Tac Toe and TO DO list applications coded in Python. The project also includes the handling of common development files like .gitignore.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project requires Python and pip installed. It is suggested to also have virtualenv installed.

#### macOS:

On macOS machines, Python is already installed. pip can be installed with the following command:

```
$ sudo easy_install pip
```

To install virtualenv:

```
$ sudo pip install virtualenv
```

#### Windows:

Download Python and pip from the Python's [official website](https://www.python.org/downloads/), and install in your machine.

To install virtualenv in windows:

```
$ pip install virtualenv
```

### Set Up Project

#### Clone the repository:

```
$ git clone https://github.com/[username]/demo_project.git
$ cd demo_project
```

#### Creating Virtual Environment

Create a virtual environment in which to install Python pip packages. With virtualenv installed, the following commands creates a new virtual environment and activates it.

```
$ virtualenv venv            # create virtualenv named venv
$ source venv/bin/activate   # activate the venv
```

On Windows:

```
$ venv\Scripts\activate
```

If packages were added to requirements.txt, they can be installed with:

```
$ pip install -r requirements.txt
```

It is generally a good idea to keep all project's dependencies in a virtualenv for easier management.

### Running the Applications

After setting up the project, you can run the Tic Tac Toe and To Do list applications with following commands:

```
$ python python/tic-tac-toe.py   # for Tic Tac Toe game.

$ python python/todo.py   # for Todo List.
```

### Deployment

The `.gitignore` file suggests the deployment pipeline involves tools like Grunt, Bower, eslint and stylelint. The project uses Node Package Manager (npm) for handling dependencies.

For Continuous Integration/Deployment setup, usually, additional scripts are added inside `package.json` file similar to below:

```json
"scripts": {
    "test": "jest",
    "build": "npm run clean && webpack --mode production",
    "start": "webpack-dev-server --open --hot",
    "deploy": "npm run test && npm run build && serverless deploy"
  },
```

The steps and tools you need for deployment largely depends on your deployment strategy.

## Authors

- **Your Name** - *Initial work* - [username](https://github.com/username)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.