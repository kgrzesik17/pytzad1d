import os

def create(name, type, content=''):
    '''
    This module lets you create a folder or a file of a certain type.

    Arguments:
    name - name of a folder you want to create.
    type - file extension. If set to "folder", then the module is going to create a folder.
    content (optional) -  only if type != folder. Lets you write content for the file.

    Output:
    bool - 1 if a file was created, 0 if a folder was created.
    
    '''

    if type == 'folder'.lower():
        os.mkdir(name)
        return 0

    else:
        fullname = name + '.' + type
        file = open(fullname, 'x')
        file.write(content)
        file.close()
        return 1