import random
from guess import TebakAngka

tebak = TebakAngka()

tebak.jawaban = random.randint(1,10)

tebak.tebakan = int(input('tebak angka 1 s.d 10'))

if tebak.cek():
    print("tebakan kamu benar!")
else:
    print("tebakan kamu salah!")