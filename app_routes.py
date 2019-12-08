#!/usr/bin/env python
from flask import Blueprint, request
import json
from fetch_data import fetch_all_users_lifestyle, fetch_all_users_repayment
from life_style_assessment_matrix.rule_engine import life_style_assesment_matrix_engine
from repayment_capacity.rule_engine import repayment_capacity_engine
urls_blueprint = Blueprint('urls', __name__,)

@urls_blueprint.route('/userids/all/lifestyle')
def lifestyle_data_all_users():
    return fetch_all_users_lifestyle()

@urls_blueprint.route('/userids/all/repayment')
def repayment_data_all_users():
    return fetch_all_users_repayment()

@urls_blueprint.route('/lifestyle/user/create',methods=['POST'])
def create_new_user():
    return life_style_assesment_matrix_engine(request.get_json())

@urls_blueprint.route('/repayment/user/create',methods=['POST'])
def create_new_user():
    return repayment_capacity_engine(request.get_json())