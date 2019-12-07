#!/usr/bin/env python

import json

DATABASE='life_matrix_user_data.json'

def life_style_assesment_matrix_engine(user_data):
    input_data = json.loads(user_data)
    user_id = input_data['user_id']
    user_exists = False
    with open(DATABASE) as json_file:
        data = json.load(json_file)
        for sub_data in data:
            if user_id == sub_data['user_id']:
                user_exists = True
    if user_exists:
        update_lsamatrix(input_data)
    else:
        create_new_user(input_data,len(data))
    print(data)

def create_new_user(input_data,max_id):

    calculate_lsamatrix(input_data)
    pass 

def update_lsamatrix(input_data):
    calculate_lsamatrix(input_data)
    pass

def calculate_lsamatrix(user):
    pass
# Remove this before committing
if __name__== "__main__":
    data = {"user_id":'1'}
    json_data = json.dumps(data)
    life_style_assesment_matrix_engine(json_data)
    

