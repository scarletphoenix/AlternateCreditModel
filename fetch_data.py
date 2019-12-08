#!/usr/bin/env python
import json

def fetch_all_users_lifestyle():
  with open('./life_style_assessment_matrix/life_matrix_user_data.json', 'r') as json_file:
      data = json.load(json_file)   
      return (json.dumps(data, indent=4, sort_keys=True))

# def fetch_all_users_repayment():
#   with open('./repayment_capacity/repayment_user_data.json', 'r') as json_file:
#       data = json.load(json_file)   
#       return (json.dumps(data, indent=4, sort_keys=True))

def fetch_all_users_repayment():
  user-id = 1
  with open('./repayment_capacity/repayment_user_data.json', 'r') as json_file: 
      data = json.load(json_file)
      for sub_data in data:
          if user_id == int(sub_data['user_id']):
              repayment = sub_data
              #print(sub_data)

  with open('./life_style_assessment_matrix/life_matrix_user_data.json', 'r') as json_file_1: 
      data_1 = json.load(json_file_1)
      for sub_data_1 in data_1:
          if user_id == int(sub_data_1['user_id']):
              lifestyle = sub_data_1

  return str(int(repayment['total_score']) + int(lifestyle['total_score']))

