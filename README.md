# WolvSec CTF 2023

Elijah and I are doing the WolvSec CTF this year!
These are our writups for the challenges we did.

## baby-pwn

For this challenge we pretty quickly realized that we had to do a buffer overflow attack to change the variable ```a```.
It was pretty simple and we got the program to print locally, but we forgot that the other part of the hint was ```nc baby-pwn.wolvctf.io 1337```.
We thought maybe the compiled file had the flag in it so we were running gdb in an Ubuntu container to try and find it haha.
Turned out you just run the nc command and do the overflow, it takes < 1 second.
But we got it at least!

## theyseemerolling

This one was really cool.
We figured the python file was what encrypted the flag, so we started out by reverse engineering the encryption process.
We figured that since we would have several blocks to check, we could essentially brute force the key one byte at a time just by checking if the key would decrypt every byte into some sort of ASCII character.

This may have worked but this ended up being such a pain in python since we aren't very fluent.
But then we realized that since only 4 bytes of the actual message are added to each 8 byte block, with the first 4 just being the block number, then we can actually just guess the key first try since all the flags start with a 4 character string ```wctf```.
This was way easier lol.
