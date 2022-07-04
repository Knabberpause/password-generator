import random
import time

   
print("Hello. Welcome to the password generator. Please follow on screen instructions to get a randomly generated password")
length = input('How long should it be?')
pwds = 1
length = int(length)
if length >1000000:
    print('No one needs something that secure except the North Korean Government! Try a digit smaller')
else:
    pwds = pwds
    print("Generating Password...")

    print("Generating Password. Please wait")

    chars = ['A', 'B', 'D', 'C', 'E', 'F', 'G', 'H', 'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','!',"@","(",")"]
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890():;,.-_=!@'
    done = 1

    while done == 1:
        for pwd in range(pwds):
            print(pwd)
            password = ""
            for character in range(0,length):
                passwordchar = random.choice(characters)
                password += passwordchar
                done = done+1

    print(password)




        

        




    