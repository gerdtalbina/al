#!/usr/bin/python3

from sys import stdin
lines = [line.strip() for line in stdin]
lines.sort(reverse=True)
for line in lines:
	print(line)
