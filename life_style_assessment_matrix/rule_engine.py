#!/usr/bin/env python

import json
from pathlib import Path

DATABASE='life_matrix_user_data.json'
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
            if int(user_id) == int(sub_data['user_id']):
                user_exists = True
                existing_user_data = sub_data
    if user_exists:
        update_lsamatrix(existing_user_data,input_data)
        return "Updated"
    else:
        return  create_new_user(input_data,len(data))


def create_new_user(user,max_id):
    print(user)
    user_id = str(max_id + 1)
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
        if 'facebook' in user['social_media_score'][0]:
            facebook = user['social_media_score'][0]['facebook']
        if 'twitter' in user['social_media_score'][0]:
            twitter = user['social_media_score'][0]['twitter']
        if 'linkdln' in user['social_media_score']:
            linkdln = user['social_media_score'][0]['linkdln']
    social_media_dict['facebook']=facebook
    social_media_dict['twitter']=twitter
    social_media_dict['linkdln']=linkdln
    social_media_score.append(social_media_dict)
    if 'browsing_history' in user :
        if 'type_of_site' in user['browsing_history'][0]:
            type_of_site = user['browsing_history'][0]['type_of_site']
        if 'time_spent' in user['browsing_history'][0]:
            time_spent = user['browsing_history'][0]['time_spent']
        if 'frequency_of_visit' in user['browsing_history'][0]:
            frequency_of_visit = user['browsing_history'][0]['frequency_of_visit']

    browsing_history_dict['type_of_site']=type_of_site
    browsing_history_dict['time_spent']=time_spent
    browsing_history_dict['frequency_of_visit']=frequency_of_visit
    browsing_history.append(browsing_history_dict)

    if 'app_history' in user:
        if 'type_of_site' in user['app_history'][0]:
            app_type_site = user['app_history'][0]['type_of_site']
        if 'time_spent' in user['app_history'][0]:
            app_time_spent = user['app_history'][0]['time_spent']
        if 'frequency_of_visit' in user['app_history'][0]:
            app_frequency_of_visit = user['app_history'][0]['frequency_of_visit']
    
    app_history_dict['type_of_site']=app_type_site
    app_history_dict['time_spent']=app_time_spent
    app_history_dict['frequency_of_visit']=app_frequency_of_visit
    app_history.append(app_history_dict)

    new_user['psychometric_test_score'] = psychometric_test_score
    new_user['social_media_score'] = social_media_score
    new_user['browsing_history'] = browsing_history
    new_user['app_history'] = app_history
    total_score = calculate_lsamatrix(user)
    new_user['total_score'] = total_score
   
    with open(file_location) as feedsjson:
        feeds = json.load(feedsjson)
    feeds.append(new_user)
    with open(file_location, mode='w') as json_file:
        json.dump(feeds,json_file,indent=2)
    
    return user_id

def update_lsamatrix(user,new_data):
    social_media_score = []
    browsin_history = []
    app_history = []
    if 'psychometric_test_score' in new_data:
        psychometric_test_score = int(new_data['psychometric_test_score'])
    else:
        psychometric_test_score = int(user['psychometric_test_score'])

    if 'social_media_score' in new_data :
        if 'facebook' in new_data['social_media_score'][0]:
            facebook = new_data['social_media_score'][0]['facebook']
        else:
            facebook = user['social_media_score'][0]['facebook']
        if 'twitter' in new_data['social_media_score'][0]:
            twitter = new_data['social_media_score'][0]['twitter']
        else:
            twitter = user['social_media_score'][0]['twitter']
        if 'linkdln' in new_data['social_media_score'][0]:
            linkdln = new_data['social_media_score'][0]['linkdln']
        else:
            linkdln = user['social_media_score'][0]['linkdln']
        social_media_dict = {}
        social_media_dict['facebook']=facebook
        social_media_dict['twitter']=twitter
        social_media_dict['linkdln']=linkdln
        social_media_score.append(social_media_dict)
    else:
        social_media_score = user['social_media_score']

    if 'browsing_history' in new_data :
        if 'type_of_site' in new_data['browsing_history'][0]:
            type_of_site = new_data['browsing_history'][0]['type_of_site']
        else:
            type_of_site = user['browsing_history'][0]['type_of_site']
        if 'time_spent' in new_data['browsing_history'][0]:
            time_spent = new_data['browsing_history'][0]['time_spent']
        else:
            time_spent = user['browsing_history'][0]['time_spent']
        if 'frequency_of_visit' in new_data['browsing_history'][0]:
            frequency_of_visit = new_data['browsing_history'][0]['frequency_of_visit']
        else:
            frequency_of_visit = user['browsing_history'][0]['frequency_of_visit']
        browsing_history_dict = {}
        browsing_history_dict['type_of_site']=type_of_site
        browsing_history_dict['time_spent']=time_spent
        browsing_history_dict['frequency_of_visit']=frequency_of_visit
        browsing_history.append(browsing_history_dict)
    else:
        browsing_history = user['browsing_history']

    if 'app_history' in new_data:
        if 'type_of_site' in new_data['app_history'][0]:
            app_type_site = new_data['app_history'][0]['type_of_site']
        else:
            app_type_site = user['app_history'][0]['type_of_site']
        if 'time_spent' in new_data['app_history'][0]:
            app_time_spent = new_data['app_history'][0]['time_spent']
        else:
            app_time_spent = user['app_history'][0]['time_spent']
        if 'frequency_of_visit' in new_data['app_history'][0]   :
            app_frequency_of_visit = new_data['app_history'][0]['frequency_of_visit']
        else:
            app_frequency_of_visit = user['app_history'][0]['frequency_of_visit']
        
        app_history_dict = {}
        app_history_dict['type_of_site']=app_type_site
        app_history_dict['time_spent']=app_time_spent
        app_history_dict['frequency_of_visit']=app_frequency_of_visit
        app_history.append(app_history_dict)

    else:
        app_history = user['app_history']
    
    new_user = {}
    user_id = user['user_id']
    new_user['user_id'] = user_id
    new_user['psychometric_test_score'] = psychometric_test_score
    new_user['social_media_score'] = social_media_score
    new_user['browsing_history'] = browsing_history
    new_user['app_history'] = app_history
    total_score = calculate_lsamatrix(new_user)
    new_user['total_score'] = total_score
   
    with open(file_location) as feedsjson:
        feeds = json.load(feedsjson)
    for sub_data in feeds:
        if new_user['user_id'] == sub_data['user_id']:
            feeds.remove(sub_data)


    feeds.append(new_user)
    with open(file_location, mode='w') as json_file:
        json.dump(feeds,json_file,indent=2)

 
def calculate_lsamatrix(user):
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
    social_media_score = 0
    browsing_history = 0
    app_history = 0
    total_score = 0

    print(user)
    if 'psychometric_test_score' in user:
        psychometric_test_score = int(user['psychometric_test_score'])

    if 'social_media_score' in user :
        if 'facebook' in user['social_media_score'][0]:
            facebook = int(user['social_media_score'][0]['facebook'])
        if 'twitter' in user['social_media_score']:
            twitter = int(user['social_media_score'][0]['twitter'])
        if 'linkdln' in user['social_media_score']:
            linkdln = int(user['social_media_score'][0]['linkdln'])
    social_media_score = (facebook + twitter + linkdln)    

    if 'browsing_history' in user :
        if type_of_site in user['browsing_history'][0]:
            type_of_site = int(user['browsing_history'][0]['type_of_site'])
        if 'time_spent' in user['browsing_history'][0]:
            time_spent = int(user['browsing_history'][0]['time_spent'])
        if 'frequency_of_visit' in user['browsing_history'][0]:
            frequency_of_visit = int(user['browsing_history'][0]['frequency_of_visit'])
    browsing_history = (type_of_site + time_spent + frequency_of_visit)

    if 'app_history' in user:
        if 'type_of_site' in user['app_history'][0]:
            app_type_site = int(user['app_history'][0]['type_of_site'])
        if 'time_spent' in user['app_history'][0]:
            app_time_spent = int(user['app_history'][0]['time_spent'])
        if 'frequency_of_visit' in user['app_history'][0]:
            app_frequency_of_visit = int(user['app_history'][0]['frequency_of_visit'])
    app_history = app_type_site + app_time_spent + app_frequency_of_visit

    if social_media_score==0 and browsing_history==0 and app_history==0:
        total_score = 5 * psychometric_test_score
    elif social_media_score==0 and browsing_history==0:
        total_score = 3 * psychometric_test_score + 2 * app_history
    elif browsing_history==0 and app_history==0:
        total_score = 3 * psychometric_test_score + 2 * social_media_score
    elif social_media_score==0 and app_history==0:
        total_score = 3 * psychometric_test_score + 2 * browsing_history
    elif social_media_score==0:
        total_score = 2.33 * psychometric_test_score + 1.33 * browsing_history + 1.33 * app_history
    elif app_history==0:
        total_score = 2.33 * psychometric_test_score + 1.33 * browsing_history + 1.33 * social_media_score
    elif browsing_history==0:
        total_score = 2.33 * psychometric_test_score + 1.33 * app_history + 1.33 * social_media_score
    else:
        total_score = 2 * psychometric_test_score + 1 * browsing_history + 1 * app_history + 1 * social_media_score

    
    return round(total_score,2)



# Remove this before committing
#if __name__== "__main__":
#    data = {"user_id":1,"psychometric_test_score":"7"}
#    json_data = json.dumps(data)
#    life_style_assesment_matrix_engine(json_data)
    

