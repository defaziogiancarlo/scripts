#!/usr/bin/python3

__doc__ = '''Read a lustre param file'''

import glob

# TODO brace expansion doesn't work with python globm it's a bash thing 
file_roots = '{/sys/{fs,kernel/debug}/{lnet,lustre},/proc/{fs,sys}/{lnet,lustre}}'


def find_files(path):
    '''Try to find a file, or glob of files, that matches
    the path appe'''

    full_path = file_roots + '/' + path
    print(full_path)

    # get all the files that match
    return glob.glob(full_path)

def read_param_file(path):
    with open(path, 'r') as f:
        data = f.read()
        print(data)
