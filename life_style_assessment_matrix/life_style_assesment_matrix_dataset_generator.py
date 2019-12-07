#!/usr/bin/env python 

import csv
import random
data_set=[]

def main():
    for i in range(100000):
        data_set.append(generate_data())
    with open('life_style_matrix_dataset.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_set)

def generate_data():
    new_data=[]
    psychometric_test_score=random.randint(1, 10)
    social_media_score=social_media_score_generator()
    browsing_history=browser_history_score_generator()
    app_history=browser_history_score_generator()
    matrix_score=2*psychometric_test_score + \
                1*social_media_score + \
                1*browsing_history + \
                1*app_history
    new_data.append(psychometric_test_score)
    new_data.append(social_media_score)
    new_data.append(browsing_history)
    new_data.append(app_history)
    new_data.append(round(matrix_score,2))
    return new_data

def social_media_score_generator():
    facebook_score=random.randint(0, 4)
    linkdln_score=random.randint(0, 3)
    twitter_score=random.randint(0, 3)
    total_score=facebook_score+linkdln_score+twitter_score
    return total_score

def browser_history_score_generator():
    type_of_site=random.randint(0, 3)
    time_spent=random.randint(0, 3)
    frequency_of_visit=random.randint(0, 4)
    total_score=type_of_site+time_spent+frequency_of_visit
    return total_score

if __name__== "__main__":
      main()


