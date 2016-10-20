# python_app
How To Package And Distribute Python Applications

https://www.digitalocean.com/community/tutorials/how-to-package-and-distribute-python-applications

#### Installation

- Working directory: `~/MyApplication/FlaskApp$`
- For develop, we just need two commands like bellow:
```
python setup.py develop
```

- To reverse this, please:
```
python setup.py develop -u
```

#### NOTE:

- Use setuptools alternative for distutils
```
#from distutils.core import setup
from setuptools import setup
```
- Upgrade setuptools

```
pip install --upgrade setuptools pip
```

- Finally, this is my env in my test case:
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

  + Remove load config: app/__init__.py
  + Return fixed value in module_one/controllers.py
