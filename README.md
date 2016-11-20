[![Code Climate](https://codeclimate.com/github/daikk115/package_python_app/badges/gpa.svg)](https://codeclimate.com/github/daikk115/package_python_app)

# python_app
How To Package And Distribute Python Applications

https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications

#### Installation

- Working directory: `~/MyApplication/FlaskApp$`
- For develop, we just need two commands like bellow:

```
python setup.py develop    # create .egg.link to FlaskApp
python setup.py develop -u #To reverse
```
- For normal user:

```
python setup.py install
```

#### Using:

- Just run bellow command in terminal:
```
flaskapp
```

#### Package application to .deb file

```
apt-get install python-stdeb fakeroot python-all
python setup.py --command-packages=stdeb.command bdist_deb
```
- fakeroot: run a command in an environment faking root privileges for file manipulation
- python-steb: produces Debian source packages from Python packages
#### NOTE:

- Use setuptools substitute for distutils
```
#from distutils.core import setup
from setuptools import setup
```
- Upgrade setuptools

```
pip install --upgrade setuptools pip
```
- Config requirement packages: [Normally, we have two ways to say for users which dependencies packages they need for our app](https://packaging.python.org/requirements/).

	+ Config install_requires in setup.py : require when we setup via deb file
	+ Config requirements.txt : not require when we setup, just recommend users run `pip install -r requirements.txt`

In this super small example project, I just use install_requires.
-  <strong>This is my env in my test case</strong>:
```
daidv@Winner:~/MyApplication/FlaskApp$ python
Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import setuptools
>>> setuptools.__version__
'28.6.0'
>>> import flask
>>> flask.__version__
'0.11.1'
>>> 
```

- To do: I must to remove load config and render from template in this branch
because I'm facing some bug like ".egg is not directory, we can read file template in it"
>> In future, I will come back to bump it.

  + Remove load config: app/__init__.py
  + Return fixed value in module_one/controllers.py


#### References

- [two way that we need to add a script into /usr/local/bin](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html)
- [Use stdeb to make Debian packages for a Python package](http://shallowsky.com/blog/programming/python-debian-packages-w-stdeb.html)
- [Python to Debian source package conversion utility](https://pypi.python.org/pypi/stdeb/0.8.5)
