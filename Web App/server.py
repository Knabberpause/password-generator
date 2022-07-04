from flask import Flask, render_template
from flask import *
import random
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

 
@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/pwd')
def pwd():
    length=random.randint(6,16)
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890():;,.-_=!@'

    pwd1=""
    pwd2=""
    pwd3=""
    pwd4=""
    pwd5=""
    for character in range(0,length):
            passwordchar = random.choice(characters)
            pwd1 += passwordchar

    for character in range(0,length):
            passwordchar = random.choice(characters)
            pwd2 += passwordchar

    for character in range(0,length):
            passwordchar = random.choice(characters)
            pwd3 += passwordchar

    for character in range(0,length):
            passwordchar = random.choice(characters)
            pwd4 += passwordchar

    for character in range(0,length):
            passwordchar = random.choice(characters)
            pwd5 += passwordchar
    
    return render_template('pwd.html', pwd1=pwd1,pwd2=pwd2, pwd3=pwd3, pwd4=pwd4, pwd5=pwd5)
 
    

if __name__=='__main__':
    app.run(debug=True)
