#!/usr/bin/python

# variance sample

score = [ 45, 60, 78, 80, 90, 100, 77, 80 ]

sum = 0
var_sum = 0
item_num = len(score)

for i in score:
    sum += i

mean = sum / item_num

for j in score:
    var_sum += (mean-j)**2

variance = var_sum / item_num
std = variance**(1/2)

print("mean: %f, variance: %f, standard deviation: %f" % (mean,variance,std))
