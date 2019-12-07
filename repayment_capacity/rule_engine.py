#!/usr/bin/env python

import json
from pathlib import Path

DATABASE='repayment_user_data.json'
script_location = Path(__file__).absolute().parent
file_location = script_location / DATABASE

def life_style_assesment_matrix_engine(user_data):
    user_id = -1
    input_data = user_data
    if 'user_id' in input_data:
        user_id = input_data['user_id']
    user_exists = False
    with open(file_location) as json_file:
        data = json.load(json_file)
        for sub_data in data:
            if user_id == sub_data['user_id']:
                user_exists = True
    if user_exists:
        update_lsamatrix(input_data)
        return "Updated"
    else:
        create_new_user(input_data,len(data))
        return "Added"


def create_new_user(user,max_id):
    print(user)
    user_id = max_id + 1
    average_amount_score = 0
    defaulter_score = 0
    tax_filing_score =0
    monthly_income_score = 0
    employment_history_score = 0
    educational_background_score = 0
    sms_score = 0
    email_score = 0
    demographic_based_score = 0
    health_insurance_score = 0
    vehicle_insurance_score = 0
    eletricity_utility_score = 0
    gas_utility_score = 0
    internet_utility_score = 0
    health_insurance_dict = {}
    vehicle_insurance_dict = {}
    electricity_dict = {}
    gas_dict = {}
    internet_dict = {}
    utility_score_dict = {}
    insurance_score_dict = {}
    utility_score = []
    insurance_score = []
    new_user = {}
    
    new_user['user_id'] = user_id
    if 'tax_filing_score' in user:
        tax_filing_score = user['tax_filing_score']
    if 'monthly_income_score' in user:
        monthly_income_score = user['monthly_income_score']
    if 'employment_history_score' in user:
        employment_history_score = user['employment_history_score']
    if 'educational_background_score' in user:
        educational_background_score = user['educational_background_score']
    if 'sms_score' in user:
        sms_score = user['sms_score']
    if 'email_score' in user:
        email_score = user['email_score']
    if 'demographic_based_score' in user:
        demographic_based_score = user['demographic_based_score']

    if 'utility_score' in user :
        if user['utility_score']['internet_utility_score']:
            if user['utility_score']['internet_utility_score']['defaulter_score']:
                defaulter_score = user['utility_score']['internet_utility_score']['defaulter_score']
            if user['utility_score']['internet_utility_score']['average_amount_score']:
                average_amount_score = user['utility_score']['internet_utility_score']['average_amount_score']
            internet_dict['defaulter_score'] = defaulter_score
            internet_dict['average_amount_score'] = average_amount_score
            defaulter_score = 0
            average_amount_score = 0
        if user['utility_score']['eletricity_utility_score']:
            if user['utility_score']['eletricity_utility_score']['defaulter_score']:
                defaulter_score = user['utility_score']['eletricity_utility_score']['defaulter_score']
            if user['utility_score']['eletricity_utility_score']['average_amount_score']:
                average_amount_score = user['utility_score']['eletricity_utility_score']['average_amount_score']
            electricity_dict['defaulter_score'] = defaulter_score
            electricity_dict['average_amount_score'] = average_amount_score
            defaulter_score = 0
            average_amount_score = 0
        if user['utility_score']['gas_utility_score']:
            if user['utility_score']['gas_utility_score']['defaulter_score']:
                defaulter_score = user['utility_score']['gas_utility_score']['defaulter_score']
            if user['utility_score']['gas_utility_score']['average_amount_score']:
                average_amount_score = user['utility_score']['gas_utility_score']['average_amount_score']
            gas_dict['defaulter_score'] = defaulter_score
            gas_dict['average_amount_score'] = average_amount_score
            defaulter_score = 0
            average_amount_score = 0
        
    utility_score_dict['gas_utility_score'] = gas_dict
    utility_score_dict['eletricity_utility_score'] = electricity_dict
    utility_score_dict['internet_utility_score'] = internet_dict
    utility_score.append(utility_score_dict)

    if 'insurance_score' in user :
        if user['insurance_score']['health_insurance_score']:
            if user['insurance_score']['health_insurance_score']['defaulter_score']:
                defaulter_score = user['insurance_score']['health_insurance_score']['defaulter_score']
            if user['insurance_score']['health_insurance_score']['average_amount_score']:
                average_amount_score = user['insurance_score']['health_insurance_score']['average_amount_score']
            health_insurance_dict['defaulter_score'] = defaulter_score
            health_insurance_dict['average_amount_score'] = average_amount_score
            defaulter_score = 0
            average_amount_score = 0
        if user['insurance_score']['vehicle_insurance_score']:
            if user['insurance_score']['vehicle_insurance_score']['defaulter_score']:
                defaulter_score = user['insurance_score']['vehicle_insurance_score']['defaulter_score']
            if user['insurance_score']['vehicle_insurance_score']['average_amount_score']:
                average_amount_score = user['insurance_score']['vehicle_insurance_score']['average_amount_score']
            vehicle_insurance_dict['defaulter_score'] = defaulter_score
            vehicle_insurance_dict['average_amount_score'] = average_amount_score
        
    insurance_score_dict['health_insurance_score'] = health_insurance_dict
    insurance_score_dict['vehicle_insurance_score'] = vehicle_insurance_dict
    insurance_score.append(insurance_score_dict)

    new_user['tax_filing_score'] = tax_filing_score
    new_user['monthly_income_score'] = monthly_income_score
    new_user['employment_history_score'] = employment_history_score
    new_user['app_hieducational_background_scorestory'] = educational_background_score
    new_user['sms_score'] = sms_score
    new_user['email_score'] = email_score
    new_user['demographic_based_score'] = demographic_based_score
    new_user['utility_score'] = utility_score
    new_user['insurance_score'] = insurance_score
    #total_score = calculate_lsamatrix(user)
    total_score = 0
    new_user['total_score'] = total_score
   
    with open(file_location) as feedsjson:
        feeds = json.load(feedsjson)
    feeds.append(new_user)
    with open(file_location, mode='w') as json_file:
        json.dump(feeds,json_file,indent=2)

def update_lsamatrix(user):
    calculate_lsamatrix(user)
    pass

def calculate_lsamatrix(user):
    
    pass
# Remove this before committing
if __name__== "__main__":
    data = {"sms_score":'10'}
    json_data = json.dumps(data)
    life_style_assesment_matrix_engine(json_data)
    

