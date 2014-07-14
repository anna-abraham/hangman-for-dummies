#!/usr/bin/env python3
import os, time, states

def clear():
  os.system(['clear','cls'][os.name == 'nt'])

def main():
  clear()

  game = states.Hangman()
  word_status = []

  for letter in game.word:
    word_status.append("_")

  win = False

  while not win:
    game.print_status()
    print(word_status)

    inp = input()

    clear()


main()
