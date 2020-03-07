#!/usr/bin/python3

__doc__ = '''
A script to manage other utility scripts.
Contains information about what scripts exist 
and how to use them.
'''

import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', 
                    help='increase amount of text printed for some commands',
                    action='store_true')
parser.add_argument('--tags', 
                    help='list all of the tags for all of the scripts',
                    action='store_true')
parser.add_argument('--scripts', 
                    help='list all of the scripts',
                    action='store_true')
parser.add_argument('--attributes',
                    help='show the dict entry for the selected scripts',
                    action='store_true')
parser.add_argument('--info',
                    help='information about this script',
                    action='store_true')

info_string = '''
This script is for documenting and organizing utility scripts.
Otherwise I have a problem with forgetting how to use my scripts,
or that I ever wrote them.

Information on the scripts is kept in a .json file which is 
read when this script is invoked. The .json file is not the definitive
source on the script. If you find a script that looks useful, look at it 
to make sure it actually does what this scripts says it does. 

If you want to find a script for a particular task,
you can search by tags. The tags are areas where a script may be useful.
To show all tags:

$ myscripts --tags

To see which tags apply to which scripts:

$ myscripts --tags --verbose

some typical tags are things like:
lustre - useful for lustre in some way, either development or admin
git - does something with git
pipeable - can be used in a pipeline, meaning it reads and writes

If you want to find a script that uses a particular interpreter
you can find all the interpreters used and which scripts use them:
$ myscripts --interpreters
$ myscripts --interpreters --verbose
'''

scripts_json_path = '/g/g0/defazio1/bin/scripts.json'

def load_scripts(path):
    '''Load a .json file at path.
    The result should be a dict containing a dict for each
    script. The dict for each script has the script name a the key
    and its '''
    with open(path, 'r') as f:
        return json.load(f)

def indirect_get(external_dict, script_name, key):
    '''get the value for external_dict[script_name][key].
    if either script_name or key does not exist, returns None.'''
    internal_dict = external_dict.get(script_name, {})
    return internal_dict.get(key, None)


# TODO clean this up
def reverse_by_field(scripts, key):
    '''create a dict that is {tag_value : set of scripts}'''
    all_values = {}
    for s in scripts:
        # find the value, if it exists
        v = indirect_get(scripts, s, key)
        # if value is None, do nothing
        if v is None:
            continue

        # if value is not a set or list

        elif not isinstance(v, (list, set)):
            if v in all_values:
                all_values[v] =  all_values[v] | {s}
            else: 
                all_values[v] =  {s}
        else:
            for x in v:
                if x in all_values:
                    all_values[x] =  all_values[x] | {s}
                else: 
                    all_values[x] =  {s}
    return all_values


def show_field(scripts, field, verbose):
    values = reverse_by_field(scripts, field)
    sorted_values = sorted([  (k, sorted(list(v)) )  for k,v in values.items() ])
    for val,scripts in sorted_values:
        if verbose:
            print('{}:\t'.format(val), end='')
            print(' '.join(scripts))
        else:
            print(val)

#def show_script(scritps, name, verbose, )

def pare_script():
    '''attempt to parse a script'''





if __name__ == '__main__':
    args = parser.parse_args()
        
    # no need to load data otherwise
    scripts = {}
    if args.tags or args.scripts:
        scripts = load_scripts(scripts_path)
    
    if args.tags:
        show_field(scripts, 'tags', args.verbose)
        

    

    # print(scripts)

    # print(indirect_get(scripts, 'add-hooks', 'tags'))



    # tags = reverse_by_field(scripts, 'tags')
    # interpretors = reverse_by_field(scripts, 'interpreter')
    # descriptions = reverse_by_field(scripts, 'description')
    # print(tags)
    # print(interpretors)
    # print(descriptions)






# scripts = {}
# scripts['add-hooks'] = {"interpreter": "bash",
#     "description": "Activate the Lustre git-hooks that are used when making a commit that will be submmitted to lustre.",
#     "tags": ["lustre", "git"],
#     "args": None}

# remove_hooks = {"interpreter": "bash",
#     "description": "Deactivate the Lustre git-hooks that are used when making a commit that will be submmitted to lustre. These hooks don't make sense when doing normal, local commits",
#     "tags": ["lustre", "git"],
#     "args": None}

# scripts['remove-hooks'] = remove_hooks





# class Script:

#     def __init__(self, name, interpreter, description,
#                  interpreter_path=None,
#                  tags='', args=''):
#         self.name = name
#         self.interpreter = self.interpreter
#         self.description = description
#         self.interpreter_path = interpreter_path
#         self.tags = tags
#         self.args = args





#with open('scripts.json', 'w') as f:
 #   for s in scripts:
#    json.dump(scripts, f, indent=4)


# with open('scripts.json', 'r') as f:
# #     #for s in scripts:
#     x = json.load(f)
#     print(x)
# #     print(type(x[0]))
    

#def load_scripts()



#scripts = load_scripts()


#scripts have:


# name
# interpreter
# arguments 
# examples
# description
# uses (what they are used for e.g. lustre, git  can have several
