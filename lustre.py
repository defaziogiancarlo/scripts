__doc__ = '''
Utility fucntions for lustre.
Meant to be used for basic administrative
and workflow tasks for lustre development.

For the fucntions to work the following
environment variables should be set:

LUSTRE_TREE - path to where lustre is installed
'''

import os
import pathlib
import shutil
import subprocess
import sys

# TODO maybe check permissions
def get_lustre_path(env_var='LUSTRE_TREE'):
    '''Uses the environment variable env_var.
    Verifies that env_var exists and is a directory.
    Exits on failure. Returns a pathlib.Path object\
    with absolute path to env_var on success.'''

    # check env_var in environment
    if env_var not in os.environ:
        sys.exit('Error: cannot find {} in environment.'.format(env_var))

    # make sure 'env_var' is set
    if os.environ[env_var] == '':
        sys.exit('Error: {} is declared by not set'.format(env_var))

    # get absolute path of env_var    
    lustre_tree = pathlib.Path(os.environ[env_var]).resolve()

    # check if env_var exists
    if not lustre_tree.exists():
        sys.exit('Error: {} is not a valid path.'.format(env_var))    

    # verify that env_var is a directory
    if not lustre_tree.is_dir():
        sys.exit('Error: {} is not a directory.'.format(env_var))

    return lustre_tree


# TODO ensure that path is a directory
def get_current_branch(path):
    '''Get the name of the current git branch for a given 
    directory path. Return None on failure.'''
    cmd = ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
    cp = subprocess.run(cmd, cwd=path,
                        stdout=subprocess.PIPE)
    # raise exception on bad return code
    cp.check_returncode()

    # stdout is bytes with trailing newline
    return cp.stdout.decode('utf-8').strip()


def add_lustre_hook(filename, suffix='.deactivated'):
    '''add file from the LUSTRE/contrib/git-hooks directory
    to the LUSTRE/.git/hooks directory.
    The .git/hooks directory has scripts that will be run
    depending on their names. But putting a suffix on the files,
    they will not run.'''
    lustre_path = get_lustre_path()
    git_path = lustre_path / '.git/hooks' / filename

    # check if such a file already exists in the git hooks
    if git_path.exists():
        sys.exit('lustre git hook \'{}\' is already active'
                 .format(str(git_path)))

    # check if a deactivated vesion exists
    # if it does, rename it to the active version
    git_path_d = lustre_path / '.git/hooks' / (filename + suffix)
    if git_path_d.exists():
        git_path_d.rename(git_path)
        return

    # look in LUSTRE/config/git-hooks
    contrib_path = lustre_path / 'contrib/git-hooks' / filename
    if not contrib_path.exists():
        sys.exit('cannot find \'{}\''.format(str(contrib_path)))
    else:
        shutil.copy2(contrib_path, git_path)
        
    
def remove_lustre_hook(filename, suffix='.deactivated'):
    '''look for filename in LUSTRE/.git/hooks, if found replace it with
    (filename + suffix)'''
    lustre_path = get_lustre_path()
    git_path = lustre_path / '.git/hooks' / filename
    git_path_d = lustre_path / '.git/hooks' / (filename + suffix)    
    
    # check if such a file already exists in the git hooks
    if git_path.exists():
        git_path.rename(git_path_d)

    
def rebase_on_master():
    '''update the master branch from remote then
    rebases current branch on it.'''
    lustre_path = get_lustre_path()
    cmd = ['git', 'pull', '--rebase=true', 'origin', 'master']
    cp = subprocess.run(cmd, cwd=lustre_path)
    cp.check_returncode()

    

def push_to_whamcloud():
    '''push current branch to whamcloud'''

    lustre_path = get_lustre_path()
    cmd = ['git', 'push',
           'ssh://{USER}@review.whamcloud.com:29418/fs/lustre-release'
           .format(USER='defazio1'),
           'HEAD:refs/for/master']
    cp = subprocess.run(cmd, cwd=lustre_path)
    cp.check_returncode()

    
    
    
    
