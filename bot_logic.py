import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_rnd_smile():
    smile = ''
    body = [[ '(' , ')' ],[ '[' , ']' ],[ '{' , '}' ]]
    eyes = [ '^' , '*' , '-' , 'u' , "'"]
    mouth = [ '_' , 'o' , 'w']
    body_rnd = random.randint(0,len(body)-1)
    eyes_rnd = random.randint(0,len(eyes)-1)
    mouth_rnd = random.randint(0,len(mouth)-1)
    smile += body[body_rnd][0]
    smile += eyes[eyes_rnd]
    smile += mouth[mouth_rnd]
    smile += eyes[eyes_rnd]
    smile += body[body_rnd][1]

    return smile
