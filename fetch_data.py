#!/usr/bin/env python
import json

def fetch_user_score(id):
  user_id = id
  with open('./repayment_capacity/repayment_user_data.json', 'r') as json_file: 
      data = json.load(json_file)
      for sub_data in data:
          if int(user_id) == int(sub_data['user_id']):
              repayment = sub_data
              #print(sub_data)

  with open('./life_style_assessment_matrix/life_matrix_user_data.json', 'r') as json_file_1: 
      data_1 = json.load(json_file_1)
      for sub_data_1 in data_1:
          if int(user_id) == int(sub_data_1['user_id']):
              lifestyle = sub_data_1

  score = str(int(repayment['total_score']) + int(lifestyle['total_score']))
  total_data = []
  total_data.append(lifestyle)
  total_data.append(repayment)
  data_dict={'alternate_credit_score':score}
  total_data.append(data_dict)
  json_data = json.dumps(total_data,indent=2)
  return json_data, score

