import sys

"""
sys is useful when you are handling command from cmd. 

sys.args[0] is the file name, the rest are:
    say you have command in cmd: 

        >python Sys.py something newcommand

    then args will be ["Sys.py", "something", "newcommand"]
    or

        >python Sys.py -m goodnote

    sys.argv will be ['Sys.py', '-m', 'goodnote']
    so you have a way to use this module without open it but directly run from cmd/terminal
"""

if __name__ == "__main__":
    print(sys.argv)