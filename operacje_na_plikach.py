import os

def create(name, type, content=''):
    '''
    This module lets you create a folder or a file of a certain type.

    Arguments:
    name - name of a folder you want to create.
    type - file extension. If set to "folder", then the module is going to create a folder.
    content (optional) -  only if type != folder. Lets you write content for the file.

    Output:
    integer - 2 if a file was created, 1 if a folder was created, 0 if module was unable to create such file/folder.
    '''

    if type == 'folder'.lower():
        try:
            os.mkdir(name)
            return 1
        except:
            print("Such folder already exists")
            return 0

    else:
        try:
            fullname = name + '.' + type
            file = open(fullname, 'x')
            file.write(content)
            file.close()
            return 2
        except:
            print("Such file already exists.")
            return 0
