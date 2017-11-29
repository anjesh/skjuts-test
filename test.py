import sys, os

path = os.getcwd() + '/tests'
sys.path.append(path)

from auth import login
from trips import createTrip


# temporary implementation; will be focused on workflows
createTrip()
