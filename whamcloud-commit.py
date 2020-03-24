__doc__ = '''
Set up for an interactive rebase on the current branch.
Before commiting to whamcloud:

'''

import os
import subprocess
from pathlib import Path
import sys


def lustre_tree_path(env_var='LUSTRE_TREE'):
    '''Uses the environment variable env_var.
    Verifies that env_var exists and is a directory.'''

    # check env_var in environment
    if 'env_var' not in os.environ:
        sys.exit('Error: cannot find env_var in environment.')

    # make sure 'env_var' is set
    if os.environ['env_var'] == '':
        sys.exit('Error: env_var is declared by not set')

    # get absolute path of env_var    
    lustre_tree = Path(lustre_tree).resolve()

    # check if env_var exists
    if not lustre_tree.exists():
        sys.exit('Error: env_var is not a valid path.')    

    # verify that env_var is a directory
    if not lustre_tree.is_dir():
        sys.exit('Error: env_var is not a directory.')

    return lustre_tree


        
# make sure that the current working directory
# is in the lustre tree and there and uses the same .git
# dir 
#cwd = Path.cwd().resolve()

#if (lustre_tree != cwd) and (lustre_tree not in cwd.parents):
#    sys.exit('Error: current working directory must be in'
#             ' lustre tree to make whamcloud commit.')

cmd = ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
subprocess.run(stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    
# check what branch this is


# verify that this is the lustre source tree using the environment

#lustre_root = Path(os.environ)

def hello():
    print(__name__)

hello()
