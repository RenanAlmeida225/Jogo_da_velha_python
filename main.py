import os
from time import sleep

velha = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

def screen():
    os.system('cls')
    for i in range(len(velha)):
        print(f'|{velha[i][0]}|{velha[i][1]}|{velha[i][2]}|')


while True:
    screen()
    break