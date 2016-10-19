from distutils.core import setup
#from setuptools import setup, find_packages

setup(
    name='FlaskApp',
    version='0.1.0',
    packages=['app', 'app.module_one'],
    package_data={
       'app': ['templates/module_one/*']
    },
    url='https://github.com/daikk115/python_app/tree/master/FlaskApp',
    license='',
    author='daidv',
    author_email='daikk115@gmail.com',
    description=''
)