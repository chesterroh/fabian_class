#!/usr/bin/python3

import numpy as np
import pickle

num_students = 10000000
np.random.seed(4)

def cleanse_data( score ):
    mask = ( score > 0 ) * ( score < 200 )
    print(np.sum(mask))
    return score * mask

score = {}
score['subj1'] = np.random.normal(120,58,num_students)
score['subj2'] = np.random.normal(130,62,num_students)
score['subj3'] = np.random.normal(140,64,num_students)
score['subj4'] = np.random.normal(130,19,num_students)
score['subj5'] = np.random.normal(90,45,num_students)

# cleanse the data
for (subj,data) in score.items():
    score[subj] = cleanse_data(data)

for (subj,data)  in score.items():
    print("%s: mean: %f, std: %f" % (subj, np.mean(data),np.std(data)))

with open("score_data.pickle",'wb') as fp:
    pickle.dump(score,fp)


