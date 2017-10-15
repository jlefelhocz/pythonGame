import pygame
import serial
import random
import time
import os
import re
from Player import *
from Square import *

ser = serial.Serial('/dev/cu.usbmodem14511', 9600)

pygame.display.set_mode((200,100))
pygame.display.flip()

start = Square(0, -1, -1, 0)
players = []
squares = [start]

def setUpPlayers(numOfPlayers):
    #create numOfPlayers players
    for p in range(0, numOfPlayers):
        players.append(Player(p, start, False))

def setUpSquares(numOfSquares):
    #create numOfSquares squares
    for num in range(1, numOfSquares + 1):
        squares.append(Square(num, -1, -1, 0))


def rollDice():
    return random.randint(1, 6)

def startGame():
    numChutes = random.randint(int(len(squares)/10), int(len(squares)/7))
    numLadders = random.randint(int(len(squares)/10), int(len(squares)/7))
    chutes = []
    ladders = []

    newChutes = random.sample(range(3, len(squares) - 2), numChutes)
    for newRandom in newChutes:
        chutes.append(newRandom)
    for chute in chutes:
        squares[chute].chuteNum = random.randint(1, chute - 1)
        print(squares[chute].chuteNum)

    newLadders = random.sample(range(1, len(squares) - 3), numLadders)
    for newRandom in newLadders:
        ladders.append(newRandom)
    for ladder in ladders:
        squares[ladder].ladderNum = random.randint(ladder + 1, len(squares) - 2)
        print(squares[ladder].ladderNum)

    print("Filler")

running = True

os.system("say -v "+'Ava'+" Hello and welcome to the Game!")
os.system("say -v "+'Ava'+" How many players do you have?")
time.sleep(0.2)
myNum = int(input("How many players do you have?"))
setUpPlayers(myNum)
os.system("say -v "+'Ava'+" How many squares are there?")
time.sleep(0.2)
myNumS = int(input("How many squares do you have?"))

setUpSquares(myNumS)

startGame()
print(len(squares))


while running:
    for p in players:
        print("Player " + str(p.playerNum))
        possibleMoves = []
        for i in range(p.currentSquare.squareNum + 1, p.currentSquare.squareNum + 7):
            possibleMoves.append(i)
            #print(i)
        for person in players:
            if person != p:
                for x in range(1, 7):
                    if p.currentSquare.squareNum + x == person.currentSquare.squareNum:
                        if possibleMoves.count(p.currentSquare.squareNum + x) > 0:
                            possibleMoves.remove(p.currentSquare.squareNum + x)
                            #print(possibleMoves)
        newSpot = random.choice(possibleMoves)

        if newSpot > myNumS:
            newSpot = myNumS

        print(newSpot)
        newSquare = squares[newSpot]
        p.moveTo(newSquare, myNumS, squares)



        if(p.win == True):
            running = False
            break

        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False



