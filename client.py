#!/usr/bin/python3

#-*- coding:UTF-8 -*-

import socket, os, time

def parser(stringclient):
    global guess

    s=socket.socket()
    host="127.0.0.1"
    port=12555
    s.connect((host, port))
    s.send(stringclient.encode())
    reply=s.recv(1024).decode()
    print(reply)
    s.close()

    first_word=reply.split("#")[0]
    if first_word=="+OK_LETTER":
        first_word, worldind=reply.split("#")
        print(worldind)
    if first_word=="+OK_WORD":
        first_word, worldind=reply.split("#")
        print("You won: "+worldind)
        time.sleep(2)
        exit()
    if first_word=="-ERR":
        first_word, worldind, guess=reply.split("#")
    print("Guess remaining: "+guess)

guess="6"

while True:
    print("Guess: "+guess)
    print("0) Exit")
    print("1) Guess letter")
    print("2) Guess world")
    choose=input("Command: ")
    time.sleep(2)
    os.system("clear")
    if guess==0:
        print("You loose")
        time.sleep(4)
        exit()
    if choose=="1":
        letter=input("Insert the letter: ")
        letter="LETTER#"+letter
        parser(letter)
    if choose=="2":
        world=input("Insert the world: ")
        world="world#"+world
        parser(world)
    if choose=="0":
        parser("DISCONNECTED")
        exit()
