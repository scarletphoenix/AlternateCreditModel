#!/usr/bin/env python

import json

DATABASE='life_matrix_user_data.json'

def life_style_assesment_matrix_engine(user_data):
    user_id = -1
    input_data = json.loads(user_data)
    if 'user_id' in input_data:
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

def create_new_user(user,max_id):
    print(user)
    user_id = max_id + 1
    facebook = 0
    twitter = 0
    linkdln = 0
    type_of_site = 0
    time_spent=0
    frequency_of_visit=0
    psychometric_test_score = 0
    app_type_site = 0
    app_time_spent = 0
    app_frequency_of_visit = 0
    social_media_dict = {}
    browsing_history_dict = {}
    app_history_dict = {}
    social_media_score = []
    browsing_history = []
    app_history=[]
    new_user = {}
    
    new_user['user_id'] = user_id
    if 'psychometric_test_score' in user:
        psychometric_test_score = user['psychometric_test_score']
    if 'social_media_score' in user :
        if user['social_media_score']['facebook']:
            facebook = user['social_media_score']['facebook']
        if user['social_media_score']['twitter']:
            twitter = user['social_media_score']['twitter']
        if user['social_media_score']['linkdln']:
            linkdln = user['social_media_score']['linkdln']
    social_media_dict['facebook']=facebook
    social_media_dict['twitter']=twitter
    social_media_dict['linkdln']=linkdln
    social_media_score.append(social_media_dict)
    if 'browsing_history' in user :
        if user['browsing_history']['type_of_site']:
            type_of_site = user['browsing_history']['type_of_site']
        if user['browsing_history']['time_spent']:
            time_spent = user['browsing_history']['time_spent']
        if user['browsing_history']['frequency_of_visit']:
            frequency_of_visit = user['browsing_history']['frequency_of_visit']

    browsing_history_dict['type_of_site']=type_of_site
    browsing_history_dict['time_spent']=time_spent
    browsing_history_dict['frequency_of_visit']=frequency_of_visit
    browsing_history.append(browsing_history_dict)

    if 'app_history' in user:
        if user['app_history']['type_of_site']:
            app_type_site = user['app_history']['type_of_site']
        if user['app_history']['time_spent']:
            app_time_spent = user['app_history']['time_spent']
        if user['app_history']['frequency_of_visit']:
            app_frequency_of_visit = user['app_history']['frequency_of_visit']
    
    app_history_dict['type_of_site']=app_type_site
    app_history_dict['time_spent']=app_time_spent
    app_history_dict['frequency_of_visit']=app_frequency_of_visit
    app_history.append(app_history_dict)

    new_user['psychometric_test_score'] = psychometric_test_score
    new_user['social_media_score'] = social_media_score
    new_user['browsing_history'] = browsing_history
    new_user['app_history'] = app_history
    #total_score = calculate_lsamatrix(user)
    total_score = 0
    new_user['total_score'] = total_score
   
    with open(DATABASE) as feedsjson:
        feeds = json.load(feedsjson)
    feeds.append(new_user)
    with open(DATABASE, mode='w') as json_file:
        json.dump(feeds,json_file,indent=2)

def update_lsamatrix(user):
    calculate_lsamatrix(user)
    pass

def calculate_lsamatrix(user):
    
    pass
# Remove this before committing
if __name__== "__main__":
    data = {"psychometric_test_score":'10'}
    json_data = json.dumps(data)
    life_style_assesment_matrix_engine(json_data)
    

