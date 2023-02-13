# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 20:00:20 2023

@author: Léopold Varlet
"""

# connect 4

import numpy as np
import operator as op
from enum import Enum

class Token(Enum):
    Yellow = 1
    Red = 2


def noOp(a, b):
    return a


class Grid:
    numberOfColumn = 7
    numberOfRow = 6

    def __init__(self):
        self.grid = np.zeros((Grid.numberOfColumn, Grid.numberOfRow), dtype=Token)

    @staticmethod
    def isValidColumnIndex(columnIndex: int):
        return 0 <= columnIndex < Grid.numberOfColumn

    @staticmethod
    def isValidRowIndex(rowIndex: int):
        return 0 <= rowIndex < Grid.numberOfRow

    def isValidCoordinate(self, columnIndex: int, rowIndex: int):
        return self.isValidColumnIndex(columnIndex) and self.isValidRowIndex(rowIndex)

    def testColumnIndexValidity(self, columnIndex: int):
        if not self.isValidColumnIndex(columnIndex):
            raise Exception("Not a valid column index")

    def getFirstFreeIndexOfColumn(self, columnIndex: int):
        self.testColumnIndexValidity(columnIndex)
        for index in range(Grid.numberOfRow):
            if self.grid[columnIndex][index] == 0:
                return index
        return Grid.numberOfRow

    def columnIsFull(self, columnIndex: int):
        self.testColumnIndexValidity(columnIndex)
        return self.getFirstFreeIndexOfColumn(columnIndex) == Grid.numberOfRow

    def isFull(self):
        for columnIndex in range(Grid.numberOfColumn):
            if not self.columnIsFull(columnIndex):
                return False
        return True

    def addTokenToColumn(self, token: Token, columnIndex: int):
        self.testColumnIndexValidity(columnIndex)
        if self.columnIsFull(columnIndex):
            raise Exception("Column is full")
        self.grid[columnIndex][self.getFirstFreeIndexOfColumn(columnIndex)] = token
        print(self.grid)

    def directionWin(self, token: Token, columnIndex: int, columnOp, rowIndex: int, rowOp):
        for index in range(4):
            if not (self.isValidCoordinate(columnOp(columnIndex, index), rowOp(rowIndex, index)) and
                    self.grid[columnOp(columnIndex, index)][rowOp(rowIndex, index)] == token):
                return False
        return True

    def fourTokenAligned(self, token: Token, columnIndex: int, rowIndex: int):
        win = False
        if self.grid[columnIndex][rowIndex] == token:
            win = win or self.directionWin(token, columnIndex, op.add, rowIndex, op.sub)
            win = win or self.directionWin(token, columnIndex, op.add, rowIndex, noOp)
            win = win or self.directionWin(token, columnIndex, op.add, rowIndex, op.add)
            win = win or self.directionWin(token, columnIndex, noOp, rowIndex, op.add)
        return win

    def isWinner(self, token: Token):
        for columnIndex in range(Grid.numberOfColumn):
            for rowIndex in range(Grid.numberOfRow):
                if self.fourTokenAligned(token, columnIndex, rowIndex):
                    return True
        return False
