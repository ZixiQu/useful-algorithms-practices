import os
from datetime import datetime



note = """
few things about os:
    os.getcwd(): get current work dir
    os.chdir(path): go to <path> 
    os.listdir(): print (in a list) all elements in current word dir
    os.mkdir("name"): make a dir under current work dir with name <name>
    os.makedirs("top_level\\sub_level"): make a dir recursively; 
                create a folder <top_level> under current work dir
                create a sub-folder in <top_level> called <sub_level>
    os.rmdir("top_level\\sub_level"): remove <sub_level>
    os.removedirs("top_level\\sub_level"): recursively remove everything along this path.
    os.rename(old, new): rename the file <old> with new name <new>

    os.stat("path + filename"): print various information about <filename>
        few notes about stat: stat().st_mtime = modification time
                              stat().size = size in byte.
    os.walk(path): **recursively** traverse all elements in <path> in the way of triple.
        the triple will be (dirpath, dirnames, filenames) where 
        dirpath: the current path 
        dirnames: a list of all folders in dirpath
        filename: a list of all file in dirpath.
    os.path.exists(path): return True iff path exists in this computer

"""



def print_items(d: str, indentation: str) -> None:
    """
    Print the list of files and directories in directory <d>, recursively,
    prefixing each with the given indentation.
    """
    print(indentation + d + ':')
    for filename in os.listdir(d):
        print(indentation + filename)
        subitem = os.path.join(d, filename)
        if os.path.isdir(subitem):
            print_items(subitem, indentation + '    ')


def get_modification_time(filename: str) -> str:
    """ return the modification time of <filename>. 
    None if <filename> is not found"""
    try:
        return datetime.fromtimestamp(filename)
    except Exception as e:
        # print("maybe the file cannot found. Error", e, sep="\n")
        return None


def _demo_of_oswalk(path=os.getcwd()):
    """ a demonstration of pretty os.walk()"""
    for dirpath, dirnames, filenames in os.walk(path):
        print("current path: " + dirpath)
        print("folders: " + str(dirnames))
        print("files: " + str(filenames))
        print()


if __name__ == '__main__':
    # Put in a path like
    # "C:\\Users\\Administrator\\Desktop\\ut_csc_Assignment" (Windows) or
    # '/Users/dianeh/Documents/courses/csc148/assignments' (OSX)
    # to print the contents of that folder.
    # print_items('C:\\Users\\Administrator\\Desktop\\ut_csc_Assignment', '')

    # print(os.chdir("C:\\Users\\Administrator\\Desktop\\useful-algorithms-practices"))
    # print(os.listdir())
    # _demo_of_oswalk()
    # print(os.path.exists("\\Administrator\\Desktop\\useful-algorithms-practices"))
    print(note)
    
