# coding: utf-8

# input()の文字化け防止
"""
import codecs
import sys
sys.stdout = codecs.getwriter("shift_jis")(sys.stdout) # 出力
sys.stdin = codecs.getreader("shift_jis")(sys.stdin) # 入力
"""

def hangman(word):
    wrong = 0
    stages = [
        "",
        "________        ",
        "|               ",
        "|       |       ",
        "|       O       ",
        "|      /|\      ",
        "|      / \      ",
        "|               " 
    ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ……")

    while wrong < len(stages) - 1:
        print("\n")
        msg = str("give me a word you expected!")
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は　{}".format(word))

#問題の選定
import random
anslist =["metal", "venom", "snake", "cat", "dog", "imitation", "medic"]
x = random.randint(0, len(anslist)-1)
mond = str(anslist[x])

hangman(mond)
