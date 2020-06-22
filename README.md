# packaging demo

After downloading / cloning , CD into the myapp folder 

```python setup.py install --user --force```

 * the --user makes it a local install
 * the --force means you can re install the same version without uninstalling first
 

 this installs a package cammed demopkg and a module called examplecode
To Use this, 
```
>>> from examplecode import examplepac1
>>> mit = examplepac1.mitch()
>>> mit.speak()
hello world
>>> 

```
A script was included in bin, the above code was placed in rundemo.py. setuptools takes script files and places them in
 * /usr/local/bin/
 
or 
 * ~/.local/bin

 as we use  --user, the script was placed in the later (in your home folder)


to uninstall, use the pip command

```pip uninstall demopkg```