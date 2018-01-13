#!/usr/bin/python3

import numpy as np
import pickle

with open('score_data.pickle','rb') as fp:
    score = pickle.load(fp)

for (subj,data) in score.items():
    print("%s: mean: %f, std: %f, var: %f" % (subj, np.mean(data),np.std(data),np.var(data)))
    print("%s: above 90 %d" % (subj,np.sum( data >= 90 )))
    print("%s: below 50 %d" % (subj,np.sum( data <= 50 )))

scores = np.concatenate( [i for _,i in score.items()] )
print("Total mean: %f, variance: %f, standard deviation: %f" % (np.mean(scores),np.var(scores),np.std(scores)))


    
