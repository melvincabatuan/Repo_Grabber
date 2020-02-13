'''
This script clones Github repos in a repo_list.txt: e.g. 

https://github.com/PinguJM/LBYCPD2-Projects
https://github.com/virambrose/CodingTime
https://github.com/anamagcamit/program-checker
...

Requirements:

pip install gcg

and/or in anaconda:

conda install -c anaconda git

Author:        mkc-cobalt
Date Created : Feb 13, 2020
Date Modified: ...

'''

import os
from git.repo.base import Repo
from datetime import datetime


# create path name
path = "submitted_" + datetime.now().strftime("%Y%m%d_%H%M%S")

# create dataset dir
if not os.path.exists(path):
    os.makedirs(path)

# go to dir
os.chdir(path)

# acquire repositories
with open("../repo_list.txt",'r') as repo_list: 
    for count, repo in enumerate(repo_list):    	
    	pair_id = "LBYCPD2_Pair" + str(count)
    	print("Downloading ", pair_id)
    	Repo.clone_from(repo.strip(), pair_id, branch='master')
    	
print("---- COMPLETED ----")
