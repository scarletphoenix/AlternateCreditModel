#!/usr/bin/env python
import json

def fetch_all_users_lifestyle():
  with open('./life_style_assessment_matrix/life_matrix_user_data.json', 'r') as json_file:
      data = json.load(json_file)   
      return (json.dumps(data, indent=4, sort_keys=True))

def fetch_all_users_repayment():
  with open('./life_style_assessment_matrix/life_matrix_user_data.json', 'r') as json_file:
      data = json.load(json_file)
      for p in data:
          print('Name: ' + p['user_id'])
          print('Psychometric: ' + p['psychometric_test_score'])
          print('Social media: ' + 'Facebook: ' + p['social_media_score'][0]['facebook'], 'LinkedIN: ' + p['social_media_score'][0]['linkdln'], 
          'Twitter: ' + p['social_media_score'][0]['twitter'])
          print('Web browsing history : ', 'Type of site: ' + p['browsing_history'][0]['type_of_site'], 'Time spent: ' + p['browsing_history'][0]['time_spent'], 
          'Frequency: ' + p['browsing_history'][0]['frequency_of_visit'])
          print('App history: ', 'Type of site: ' + p['app_history'][0]['type_of_site'], 'Time spent: ' + p['app_history'][0]['time_spent'], 
          'Frequency: ' + p['app_history'][0]['frequency_of_visit'])
          print('Final score: ' + p['total_score'])
          print("")
      return ""