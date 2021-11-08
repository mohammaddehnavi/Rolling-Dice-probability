# Rolling-Dice-probability
Python3 GUI app for calculate Rolling Dice probability

## Clone project

```bash
git clone https://github.com/mohammaddehnavi/Rolling-Dice-probability.git
```
## Install virtual env 

```bash
pip3 install virtualenv
python3 -m venv rolling-dice-probability
cd rolling-dice-probability
source bin/activate
```

## Install requirements

```bash
## Upgrade your pip
pip install --upgrade pip

## install packages
pip install -r requirements.txt
```

## RUN

```bash
python main.py
```

## Change GUI

If you want to change the GUI file please use QT Designer and open `dice.ui` and edit it and then create
your python file with `pyuic5 -x dice.ui -o yourMain.py`


## Create executable file 

I use `auto-py-to-exe` to compile this project to a single executable file. [Link!](https://pypi.org/project/auto-py-to-exe/)

```bash
## install auto-py-to-exe
pip install auto-py-to-exe

## Run auto-py-to-exe for compile and build 
auto-py-to-exe
```
