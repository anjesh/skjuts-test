import sys, os

path = os.getcwd() + '/tests'
sys.path.append(path)

from auth import login

login()
