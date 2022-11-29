import os
import pprint

def _total_size(source):
        total_size = os.path.getsize(source)
        for item in os.listdir(source):
            itempath = os.path.join(source, item)
            if os.path.isfile(itempath):
                total_size += os.path.getsize(itempath)
            elif os.path.isdir(itempath):
                try:
                    total_size += _total_size(itempath)
                except:
                    print(f"{itempath} permission denied")
        return total_size

def main():
    basepath = 'C:/'
    information = {}
    for each in os.listdir(basepath):
        print(each)
        each = f"{basepath}/{each}" 
        # print(each, os.path.isdir(each))
        if os.path.isdir(each):
            try:
                information[each] = _total_size(each) / 1024**3
                # print(f"{each}: {_total_size(each) / 1024**3} GB")
            except:
                print(f"{each} permission denied 2")
        else:
            pass
            # print(f"{each} is a file")
    print(f"current folder: {basepath}")
    for path, size in sorted(information.items(), key=lambda x:x[1], reverse=True):
        print(f"{path.split('/')[-1]}: {size} GB")

if __name__ == "__main__":
    # main()
    print(os.getcwd())