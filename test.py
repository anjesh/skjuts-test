import sys, os

path = os.getcwd() + '/tests'
sys.path.append(path)

from auth import login, register, verifyCode
from trips import createTrip
from groups import group
from users import updateUser

# temporary implementation; will be focused on workflows
# createTrip()
group()
updateUser()
