import os

def create(name, type, content=''):
    '''
    This module lets you create a folder or a file of a certain type.

    Arguments:
    name - name of a folder you want to create.
    type - file extension. If set to "folder", then the module is going to create a folder.
    content - optional - only if type != folder. Lets you write content for the file.
    '''

    if type == 'folder'.lower():
        os.mkdir(name)

    else:
        file = open(f'name\.type', 'a')
        file.write(content)
        file.close()

create('albinos', 'folder')