import bcrypt

# Declaring our password
password = b'testing123'

# Adding the salt to password
salt = bcrypt.gensalt()
# Hashing the password
hashed = bcrypt.hashpw(password, salt)

# printing the salt
print("Salt :")
print(salt)

# printing the hashed
print("Hashed")
print(hashed)

# def insertIntoDb():
#   postgres.runUpdate(
# "INSERT INTO USERS
# VALUES($user,$hashed)"
# )

if bcrypt.checkpw(password, hashed):
    print("It matches!")
else:
    print("Didn't match")