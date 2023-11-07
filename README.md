## Ricxappframe requires python 3.8 and above to work, to install it on Ubuntu 18.4 using virtual environment, follow steps below:

```
    1. sudo apt-get install python3.8 python3.8-dev python3.8-distutils python3.8-venv
    2. python3.8 -m venv venv3.8/
    3. source venv3.8/bin/activate
    Reference: https://askubuntu.com/questions/1197683/how-do-i-install-python-3-8-in-lubuntu-18-04
```

## To install from requirements.txt use: pip install -r requirements.txt
```
If ricxappframe installation failed using the above command, then follow below steps to install it:
    1. sudo apt-get install libssl-dev
    2. sudo apt-get install libffi-dev
    3. pip install wheel
    4. pip install ricxappframe --no-cache-dir

Ubuntu 18.4 was used in the development of this xapp because the O-RAN Alliance RIC: Dawn Release used which required Ubuntu 18.4
```
