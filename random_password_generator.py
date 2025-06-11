import random
import string


password_length = 8

AllValues= string.ascii_letters + string.digits + string.punctuation



# USING NORMAL LOOP

# Password = ""
# for i in range(password_length):
#     Password += random.choice(AllValues)



# USING LIST COMPREHENSION

Password = "".join([random.choice(AllValues) for i in range(password_length)])


print("Your random Password is : ",Password)






