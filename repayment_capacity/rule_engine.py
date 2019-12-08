#!/usr/bin/env python

import json
from pathlib import Path
import math

DATABASE='repayment_user_data.json'
script_location = Path(__file__).absolute().parent
file_location = script_location / DATABASE

bad_keywords = ["is overdue",
"has bounced",
"bounce",
"has not been honoured",
"severely overdue",
"is still pending",
"overdue hai",
"overdue of",
"despite several reminders",
"is still due",
"is still unpaid",
"payment overdue",
"overdues",
"is unpaid",
"remains unpaid",
"is outstanding",
"in overdue",
"have not received",
"still not received",
"are overdue",
"towards overdue"
]

def sms_score_calc(sms):
    for keyword in bad_keywords:
        if (keyword in sms.lower()):
            return 0
    return 1

def calculate_sms_score_all(all_sms):
    total_score = 0
    for sms in all_sms:
        total_score += sms_score_calc(sms)
    return math.ceil(total_score/len(all_sms)*10)


def repayment_capacity_engine(user_data):
    user_id = -1
    input_data = user_data
    if 'user_id' in input_data:
        user_id = input_data['user_id']
    user_exists = False
    if 'all_sms' in input_data:
        input_data['sms_score'] = calculate_sms_score_all(input_data['all_sms'])
    with open(file_location) as json_file:
        data = json.load(json_file)
        for sub_data in data:
            if user_id == sub_data['user_id']:
                user_exists = True
                existing_user_data = sub_data
    if user_exists:
        update_rcamatrix(existing_user_data, input_data)
        return "Updated"
    else:
        return create_new_user(input_data,len(data))


def create_new_user(user,max_id):
    #print(user)
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
    if 'all_sms' in user:
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
    new_user['educational_background_score'] = educational_background_score
    new_user['sms_score'] = sms_score
    new_user['email_score'] = email_score
    new_user['demographic_based_score'] = demographic_based_score
    new_user['utility_score'] = utility_score
    new_user['insurance_score'] = insurance_score
    total_score = calculate_rcamatrix(user)

    new_user['total_score'] = total_score
   
    with open(file_location) as feedsjson:
        feeds = json.load(feedsjson)
    feeds.append(new_user)
    with open(file_location, mode='w') as json_file:
        json.dump(feeds,json_file,indent=2)
    return str(user_id)

def update_rcamatrix(user,new_data):
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

    
    if 'monthly_income_score' in new_data:
        monthly_income_score = int(new_data['monthly_income_score'])
    else:
        monthly_income_score = int(user['monthly_income_score'])
        
    if 'employment_history_score' in new_data:
        employment_history_score = int(new_data['employment_history_score'])
    else:
        employment_history_score = int(user['employment_history_score'])
    if 'sms_score' in new_data:
        sms_score = int(new_data['sms_score'])
    else:
        sms_score = int(user['sms_score'])

    new_user = {}
    user_id = user['user_id']
    new_user['user_id'] = user_id
    new_user['monthly_income_score'] = monthly_income_score
    new_user['employment_history_score'] = employment_history_score
    new_user['sms_score'] = sms_score

    new_user['insurance_score'] =  {
        "vehicle_insurance_score": {
          "defaulter_score": 3,
          "average_amount_score": 5
        },
        "health_insurance": {
          "defaulter_score": 3,
          "average_amount_score": 4
        }
      }
    
    new_user["tax_filing_score"]= 6
    new_user["educational_background_score"]= 10
    new_user["demographic_based_score"]= 2

    new_user['utility_score'] =  {
        "gas_utility_score": {
          "defaulter_score": 4,
          "average_amount_score": 1
        },
        "eletricity_utility_score": {
          "defaulter_score": 5,
          "average_amount_score": 1
        },
        "internet_utility_score": {
          "defaulter_score": 2,
          "average_amount_score": 1
        }
      }
    

    total_score = calculate_rcamatrix(new_user)
    new_user['total_score'] = total_score
   


    with open(file_location) as feedsjson:
        feeds = json.load(feedsjson)
    for sub_data in feeds:
        if new_user['user_id'] == sub_data['user_id']:
            feeds.remove(sub_data)

    feeds.append(new_user)
    with open(file_location, mode='w') as json_file:
        json.dump(feeds,json_file,indent=2)

def calculate_rcamatrix(user):
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
    utility_score = 0
    insurance_score = 0
    total_score = 0

    if 'tax_filing_score' in user:
        tax_filing_score = int(user['tax_filing_score'])
    if 'monthly_income_score' in user:
        monthly_income_score = int(user['monthly_income_score'])
    if 'employment_history_score' in user:
        employment_history_score = int(user['employment_history_score'])
    if 'educational_background_score' in user:
        educational_background_score = int(user['educational_background_score'])
    if 'sms_score' in user:
        sms_score = int(user['sms_score'])
    if 'email_score' in user:
        email_score = int(user['email_score'])
    if 'demographic_based_score' in user:
        demographic_based_score = int(user['demographic_based_score'])
   

    
    if sms_score==0 and employment_history_score==0:
        total_score = 5 * monthly_income_score
    elif sms_score==0:
        total_score = 2.5 * monthly_income_score + 2.5 * employment_history_score
    elif employment_history_score==0:
        total_score = 3.5 * sms_score + 1.5 * monthly_income_score
    else:
        total_score = 3 * sms_score + 1 * monthly_income_score + 1 * employment_history_score

    return round(total_score,2)

# Remove this before committing
# if __name__== "__main__":
#     data = {"sms_score":'10'}
#     json_data = json.dumps(data)
#     repayment_capacity_engine(json_data)
    


