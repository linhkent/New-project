import mlab
from models.user import User

mlab.connect()
u = User(username = "hieu", password = "hieu")
u.save()