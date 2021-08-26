from database import Database
from admin import Admin

a = Admin("Itamar", "mein3Mutt3r", 3)
a.save()

print(Database.find(lambda x:x["username"]=="Itamar"))