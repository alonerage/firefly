﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
  define me = Character("Я")
  define ma = Character(_("Маша"), color="#db1717")
  define ba = Character(_("Бабушка"), color="#db1717")
  define sis = Character(_("Сестра"), color="#008080")

##glass-smash

# The game starts here.


label start:
  call tram_start
  call summer
  call tram_after_summer
