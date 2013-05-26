This is a prototype of a tool that will take
unix commands and integrate them automatically
into a python command line tool.


All you have to do to get it to work is to place
your own commands in the config.ini

The commands and options are generated based on the values
in the config file.

To start Adapt as a web service:
	python serve.py

To exit the web service:
	Ctrl-C 

To run it check out the repo and type:

python cli.py --help

adapt git:(master) python cli.py --help
Usage: adapt [options]

A commandline tool mapper

Options:

--version   show program's version number and exit
-h, --help  show this help message and exit
--list      
--mybigcmd  
--ip        


➜  adapt git:(master) python cli.py --ip  
10.0.20.11


Picture:

https://raw.github.com/noahgift/Adapt/master/doc/adapt1.png

