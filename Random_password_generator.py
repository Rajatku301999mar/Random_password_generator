import random
import string

def random_password_generator(n):
    random_source= string.ascii_letters + string.digits + string.punctuation
    password= random.choice(string.ascii_lowercase)
    password+= random.choice(string.ascii_uppercase)
    password+= random.choice(string.digits)
    password+= random.choice(string.punctuation)

    for i in range(n-4):
        password+= random.choice(random_source)

    password_list=list(password)
    random.SystemRandom().shuffle(password_list)
    password=''.join(password_list)
    return password
n=int(input("Length of password ?? (Length must be greater or equal to 4) "))
print(random_password_generator(n))