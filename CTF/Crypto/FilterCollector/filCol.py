#!/usr/bin/python3
from Crypto.Util.number import getPrime
import random
import math
import cmath

Welcome = "Instagram filters are fun, aren't they?"
print(Welcome);

flag = int(open('flag.txt','rb').read().hex(),16);
k = 7
p = int(input("Input your favorite mod: "));
assert(p * p < flag);

# Divides tot randomly into n parts
def get_partition(tot,n):
	# tot == flag in hex
	partitions = [tot];
	# Radomly appends 28 elements to partitions 0, tot
	# then sort them
	for i in range(28):
		partitions.append(random.randint(0,tot));
	partitions.sort()

	for i in range(28,0,-1):
	# setting pos i = subtracting pos i to pos prev pos
		partitions[i] -= partitions[i - 1];
	return partitions

def gen_poly(partitions,n):
	poly = [];
	cnt = 0
	for i in range(200):
		if(i % 7 == 0):
			# essentially copying partitions to poly
			poly.append(partitions[cnt]);
			cnt += 1;
		else:
			# Other than 28 value which is from partition
			# the others are random 0, usrInput - 1
			poly.append(random.randint(0,p - 1));
	assert(cnt == len(partitions));
	return poly

def hash(poly,x):
	res = 0;
	# poly has 200 elements
	# 28 of which are from partitions 
	# apparently other than the values 
	# from partitions the rest are 0s
	for i,c in enumerate(poly):
		print(f'{i}, {c}')
		# x and p is usrInput
		# i seems to be the index
		res += c * pow(x,i,p) % p;
		# This means res is only += 28 times 
		# since the values that is not from 
		# partitions are 0s
	return res % p;

partitions = get_partition(flag, 29);
poly = gen_poly(partitions,200);
for i in range(7):
	x = int(input("Input the a number: "));
	y = hash(poly,x);
	print("The hash of the number under your mod filter is " + str(y));