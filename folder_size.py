"""
folder_size.py: list each folder size of the specified (OS)path sorted by size
"""

import os
import pprint

DEBUG = 0

def _total_size(source):
    """ this function was found somewhere online. 
    By the time I realized I should reference the source, I couldn't 
    found the web page. Thank you, whoever wrote this.
    """
        total_size = os.path.getsize(source)
        for item in os.listdir(source):
            itempath = os.path.join(source, item)
            if os.path.isfile(itempath):
                total_size += os.path.getsize(itempath)
            elif os.path.isdir(itempath):
                try:
                    total_size += _total_size(itempath)
                except:
                    if DEBUG: print(f"{itempath} permission denied")
        return total_size

def main():
    basepath = 'C:/'  # change this to target path!
    information = {}
    folder_total_size = 0
    file_total_size = 0
    for each in os.listdir(basepath):
        # print(each)
        each = f"{basepath}/{each}" 
        # print(each, os.path.isdir(each))
        if os.path.isdir(each):
            try:
                folder_size = _total_size(each) / 1024**3
                information[each] = folder_size
                folder_total_size += folder_size
                # print(f"{each}: {_total_size(each) / 1024**3} GB")
            except:
                if DEBUG: print(f"{each} permission denied 2")
        else:
            file_total_size += os.path.getsize(each)
    print(f"current folder: {basepath}")
    print("="*30)
    for path, size in sorted(information.items(), key=lambda x:x[1], reverse=True):
        print(f"{path.split('/')[-1]}: {size} GB")
    print("==============SUMMARY=============")
    print(f"folder_total_size: {folder_total_size} GB")
    print(f"file_total_size: {file_total_size / 1024**3} GB")

if __name__ == "__main__":
    main()
    # print(os.getcwd())