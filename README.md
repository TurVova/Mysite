# Instructions for installing and running the project

### Preparing to launch the project
To download and install Python, click on the link below.
[![Python](https://www.python.org/static/img/python-logo.png)](https://www.python.org/)
### For the Linux operating system ![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSG2Ae7OVqAojXjtotc7wJ5FMZPLvMg_botLD86URCZ48U3YTnCYA)
##### Install pip
```sh
$ sudo apt-get install python3-pip
```
##### Install the virtual environment
```sh
$ pip3 install virtualenv
```
##### Create and activate virtual environments
```sh
$ cd (path to the project folder)
$ virtualenv (the name of the virtual environment)
$ source (the name of the virtual environment)/bin/activate
```
##### Installing additional packages
 - Installing additional packages from the requirements file
```sh
$ pip install -r req.txt
```
 - Installing additional packages one at a time
```sh
$ pip install (package name)
```
 - Checking installed packages
```sh
$ pip freeze
```
More information on [pip freeze](https://pip.pypa.io/en/stable/reference/pip_freeze).
