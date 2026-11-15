"""
Package Installation
Right now, we are able to access the package resources from a script just above the package folder. To be able to use the package anywhere in the file system, you need to install it using the PIP utility.

First of all, save the following script in the parent folder, at the level of package folder.
"""
#setup.py
from setuptools import setup
setup(name='mypackage',
version='0.1',
description='Package setup script',
url='#',
author='anonymous',
author_email='test@gmail.com',
license='MIT',
packages=['mypackage'],
zip_safe=False)
"""
Run the PIP utility from command prompt, while remaining in the parent folder.

C:\Users\user\packagedemo>pip3 install .
Processing c:\users\user\packagedemo
 Preparing metadata (setup.py) ... done
Installing collected packages: mypackage
 Running setup.py install for mypackage ... done
Successfully installed mypackage-0.1
You should now be able to import the contents of the package in any environment.

C:\Users>python
Python 3.11.2 (tags/v3.11.2:878ead1, Feb 7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import mypackage
>>> mypackage.circle(5)
78.53981633974483

"""