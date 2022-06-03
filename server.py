#!/usr/bin/python3

#-*- coding:UTF-8 -*-

import socket, time, subprocess, random

def reset():
    # Dovrebbe  riavviarsi ma...
    exit()

def parser(stringclient):
    global guessWord, guess, word

    first_word=stringclient.split("#")[0]
    print(first_word)
    stringWithGuessedLetters=""

    if first_word=="LETTER":
        check=False
        i=0
        first_word, letter=stringclient.split("#")
        for l in guessWord:
            print(l)
            if l==letter:
                check=True
                if word[i]=="-":
                    word[i]=l
            i+=1
            print(word)
        x=0
        for e in word:
            stringWithGuessedLetters+=str(word[x])
            x+=1
        if check==True:
            stringclient="+OK_LETTER#"+stringWithGuessedLetters
        else:
            guess-=1
            stringclient="-ERR#"+stringWithGuessedLetters+"#"+str(guess)
    if first_word=="WORD":
        first_word, word1=stringclient.split("#")
        if word1==guessWord:
            stringclient="+OK_WORD#"+guessWord
            c.send(stringclient.encode())
            print("Messagge from server: "+stringclient)
            c.close
            print("Connection interrupted")
            exit()
        else:
            guess-=1
            stringclient="-ERR#"+stringWithGuessedLetters+"#"+str(guess)
    if first_word=="DISCONNECTED":
        reset()

    return stringclient

host="127.0.0.1"
port=12555
subprocess.Popen("fuser -k "+str(port)+"/tcp", shell=True)
print("Service door free")
time.sleep(3)
print("Server started")

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

f=open("data.txt", "r")
n=random.randint(0, 570)
guessWord=f.readlines()[n]
guessWord=guessWord.rstrip("\n")
f.close()
guess=6
x=0
word=[]
i=0
print(guessWord)
while i<len(guessWord):
    word.append("-")
    i+=1

while True:
	c, addr=s.accept()
	print("Connection established with "+str(addr))
	inputmessage=c.recv(1024).decode()
	print("Messagge from client: "+inputmessage)
	outputmessage=parser(inputmessage)
	c.send(outputmessage.encode())
	print("Messagge from server: "+outputmessage)
	c.close
	print("Connection interrupted with "+str(addr))
