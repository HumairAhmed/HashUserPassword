import bcrypt
import sys
import getpass

#Program:        hash_user_password.py
#Description:    Hashes a username and password input by user and stores the result in a file
#Version:        1.0
#Date:           01/13/2015
#Website:        http://www.HumairAhmed.com
#Lead Developer: Humair Ahmed 


pw_file = "pw.config"

hashed_username = bcrypt.hashpw(getpass.getpass("Enter username: "), bcrypt.gensalt())
hashed_password = bcrypt.hashpw(getpass.getpass("Enter password: "), bcrypt.gensalt())

f = open(pw_file, "w")
f.write(hashed_username + "\n")
f.write(hashed_password)
f.close()