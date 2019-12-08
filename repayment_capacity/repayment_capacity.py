#!/usr/bin/env python 

import csv
import random
data_set=[]

def main():
    for i in range(100000):
        data_set.append(generate_data())
    with open('repayment_capacity_dataset.csv', 'w',  newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_set)

def generate_data():
    new_data=[]

    tax_filing_score=random.randint(1, 10)
    monthly_income_score=random.randint(1, 10)
    employment_history_score=random.randint(1, 10)
    educational_background_score=random.randint(1, 10)
    sms_score=random.randint(1, 10)
    email_score=random.randint(1, 10)
    demographic_based_score=random.randint(1, 10)
    insurance_score=insurance_score_generator()
    utility_score=utility_score_generator()

    matrix_score=1*tax_filing_score + \
                1*monthly_income_score + \
                1*employment_history_score + \
                1*educational_background_score + \
                2*sms_score + \
                1*email_score + \
                1*demographic_based_score + \
                1*insurance_score + \
                1*utility_score

    new_data.append(tax_filing_score)
    new_data.append(monthly_income_score)
    new_data.append(employment_history_score)
    new_data.append(educational_background_score)
    new_data.append(sms_score)
    new_data.append(email_score)
    new_data.append(demographic_based_score)
    new_data.append(insurance_score)
    new_data.append(utility_score)
    new_data.append(round(matrix_score/2,2))
    return new_data

def insurance_score_generator():
    vehicle_insurance_score=defaulter_score() + amount_score()
    health_insurance_score=defaulter_score() + amount_score()
    total_score=4*vehicle_insurance_score + 6*health_insurance_score
    return total_score/10

def utility_score_generator():
    eletricity_utility_score=defaulter_score() + amount_score()
    internet_utility_score=defaulter_score() + amount_score()
    gas_utility_score=defaulter_score() + amount_score()
    total_score=3*eletricity_utility_score + 3*internet_utility_score + 4*gas_utility_score
    return total_score/10


def defaulter_score():
    return random.randint(0,5)

def amount_score():
    return random.randint(0,5)

if __name__== "__main__":
      main()


