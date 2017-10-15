from Square import *
import os
import time
import serial
import re

ser = serial.Serial('/dev/cu.usbmodem14511', 9600)

class Player:
    def __init__(self, playerNum, currentSquare, win):
        self.playerNum = playerNum
        self.currentSquare = currentSquare
        self.win = win

    def moveTo(self, square, numOfSquares, squares):

        if square.chuteNum != -1:
            for sqr in squares:
                if(sqr.squareNum == square.chuteNum):
                    os.system("say -v " + 'Ava' + " Player " + str(self.playerNum) + " You rolled a" + str(square.squareNum - self.currentSquare.squareNum))
                    haveReached = False
                    while not haveReached:
                        for num in range(numOfSquares):
                            arduino = str(ser.readline().decode('UTF-8'))
                            sqrA = re.search(r'\d+', arduino).group()
                            val = arduino[arduino.find(":")+1:].split()[0]
                            if square.squareNum == int(sqrA):
                                if int(val) == 1:
                                    haveReached = True
                    os.system("say -v " + 'Ava' + " You landed on a chute!")
                    os.system("say -v " + 'Ava' + " Move to space" + str(sqr.squareNum))
                    self.currentSquare = sqr
            while self.currentSquare.active != 1:
                    for num in range(numOfSquares):
                        arduino = str(ser.readline().decode('UTF-8'))
                        sqrA = re.search(r'\d+', arduino).group()
                        val = val = arduino[arduino.find(":")+1:].split()[0]
                        print(self.currentSquare.squareNum)
                        print(square.chuteNum)
                        print(val)
                        if int(sqrA) == square.chuteNum:
                            self.currentSquare.active = int(val)
        elif square.ladderNum != -1:
            for sqr in squares:
                if(sqr.squareNum == square.ladderNum):
                    os.system("say -v " + 'Ava' + " Player " + str(self.playerNum) + " You rolled a" + str(square.squareNum - self.currentSquare.squareNum))
                    haveReached = False
                    while not haveReached:
                        for num in range(numOfSquares):
                            arduino = str(ser.readline().decode('UTF-8'))
                            sqrA = re.search(r'\d+', arduino).group()
                            val = arduino[arduino.find(":")+1:].split()[0]
                            if square.squareNum == int(sqrA):
                                if int(val) == 1:
                                    haveReached = True
                    os.system("say -v " + 'Ava' + " You landed on a ladder!")
                    os.system("say -v " + 'Ava' + " Move to space" + str(sqr.squareNum))
                    self.currentSquare = sqr
            while self.currentSquare.active != 1:
                    for num in range(numOfSquares):
                        arduino = str(ser.readline().decode('UTF-8'))
                        sqrA = re.search(r'\d+', arduino).group()
                        val = val = arduino[arduino.find(":")+1:].split()[0]
                        print(self.currentSquare.squareNum)
                        print(square.ladderNum)
                        print(val)
                        if int(sqrA) == square.ladderNum:
                            print("---------")
                            self.currentSquare.active = int(val)
        else:
            os.system("say -v " + 'Ava' + " Player " + str(self.playerNum) + " You rolled a" + str(square.squareNum - self.currentSquare.squareNum))
            while square.active != 1:
                for num in range(numOfSquares):
                    arduino = str(ser.readline().decode('UTF-8'))
                    #print(arduino)
                    sqrA = re.search(r'\d+', arduino).group()
                    val = arduino[arduino.find(":")+1:].split()[0]
                    if square.squareNum == int(sqrA):
                        square.active = int(val)

            self.currentSquare = square

        print(self.currentSquare.squareNum)
        if self.currentSquare.squareNum == numOfSquares:
            os.system("say -v " + 'Ava' + " Congrats player " + str(self.playerNum) + ", you win!")
            self.win = True
