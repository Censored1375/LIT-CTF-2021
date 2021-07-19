#!/usr/bin/python3
import random

'''
google unshuffle list python
'''

f = open("shuffle.txt", "r").read()
ls = list(f[:-1])

#print(''.join(l))

def unshuffle_list(shuffled_ls, seed):
  n = len(shuffled_ls)
  # Perm is [1, 2, ..., n]
  perm = [i for i in range(1, n + 1)]
  # Apply sigma to perm
  shuffled_perm = shuffle_under_seed(perm, seed)
  # Zip and unshuffle
  zipped_ls = list(zip(shuffled_ls, shuffled_perm))
  zipped_ls.sort(key=lambda x: x[1])
  return [a for (a, b) in zipped_ls]
def shuffle_under_seed(ls, seed):
  # Shuffle the list ls using the seed `seed`
  random.seed(seed)
  random.shuffle(ls)
  return ls

for i in range(1000):
    scr = ''.join(unshuffle_list(ls,i))
    if 'flag' in scr:
        print(scr)

# A shorter implementation
'''
import random
string = "zftr}__g5y_ee0y1{graua00n1l"
for i in range(1000):
    random.seed(i)
    l = [i for i in range(27)]
    random.shuffle(l)
    nl = [0]*27
    for i in range(len(l)):
        nl[l[i]] = string[i]
    print("".join(nl))
'''