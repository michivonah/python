# Basics in Python

## String functions

## Core concepts
Check if execution is in main program
````python
if __name__ == '__main__':
````

## Load modules
````python
import <MODULE_NAME>
````

````python
from <MODULE_NAME> import <FUNCTION>
````

## Install requirements
Create a file called `requirements.txt` in the root of the directory and add the required python modules
````text
# requirements.txt
python-dotenv
discord-webhook==1.3.0
````

Optionally you can ad == to specify the required version of the module

Install the modules with the following command:
````bash
pip install --no-cache-dir -r requirements.txt
````
