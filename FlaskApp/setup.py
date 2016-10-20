from setuptools import setup, find_packages

setup(
    name='FlaskApp',
    version='0.1.0',
    packages=find_packages(),
    # entry_points = {
    #     'console_scripts': [
    #     'flaskapp = app.__main__:main',                  
    #     ],              
    # },
    scripts=['bin/flaskapp'],
    url='https://github.com/daikk115/python_app/tree/master/FlaskApp',
    license='',
    author='daidv',
    author_email='daikk115@gmail.com',
    description=''
)