#!/usr/bin/python3
p,r = 0,0
for l in open("../inputs/2015/02.txt").readlines():
    a,b,c,*_ = sorted(map(int, l.split('x')))
    p += 3*a*b + 2*a*c + 2*b*c
    r += 2*a + 2*b + a*b*c
    
print(p, r)