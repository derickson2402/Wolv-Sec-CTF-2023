# WolvSec CTF 2023

Elijah and I are doing the WolvSec CTF this year!
These are our writups for the challenges we did.

## baby-pwn

For this challenge we pretty quickly realized that we had to do a buffer overflow attack to change the variable ```a```.
It was pretty simple and we got the program to print locally, but we forgot that the other part of the hint was ```nc baby-pwn.wolvctf.io 1337```.
We thought maybe the compiled file had the flag in it so we were running gdb in an Ubuntu container to try and find it haha.
Turned out you just run the nc command and do the overflow, it takes < 1 second.
But we got it at least!
