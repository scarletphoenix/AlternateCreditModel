#!/usr/bin/env python
import json

def fetch_all_users_lifestyle():
  with open('./life_style_assessment_matrix/life_matrix_user_data.json', 'r') as json_file:
      data = json.load(json_file)   
      return (json.dumps(data, indent=4, sort_keys=True))

def fetch_all_users_repayment():
  with open('./repayment_capacity/repayment_user_data.json', 'r') as json_file:
      data = json.load(json_file)   
      return (json.dumps(data, indent=4, sort_keys=True))