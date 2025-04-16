# Modules
# there are 2 types of modules


# ->1 built in modules
# example = math, random,os ,sys


import math 
print(math.sqrt(25))  # output:5.0


# user defined modules
# Any python file (.py) you create can be used as a module

import mymodule
print(mymodule.add(5,3)) #Output:8


#3. External modules (Third-party modules)
#  install via pip -> pip install module_name

import requests
response = requests.get("https://www.example.com")
print(response.status_code) #Output: 200

#Python provides several ways to import modules:


    #Basic import
import math 
print(math.pi) #Output : 3.1415926...

    #import with Alias(as)
import numpy as np
print(np.array([1,2,3]))

    #Import specific functions or variables
from math import sqrt, pi
print(sqrt(16)) # Output: 4.0
print(pi)       #Output:3.141592653589793


    #Import Everything (from module import*)
from math import * #wild  card
print(sin(0))   #Output : 0.0


# Case 1: 'import math' (Lazy-loading)
import math  # Only loads the module object
# No extra memory used until `math.sqrt()` is called.

# Case 2: 'from math import *' (Eager-loading)
from math import *  # Loads ALL names (pi, sin, cos, sqrt, ...)
# Memory usage increases even if you never use `pi` or `sin`

