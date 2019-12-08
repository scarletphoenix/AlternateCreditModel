#!/usr/bin/env python
from flask import Blueprint, request
import json
from fetch_data import fetch_user_score
from life_style_assessment_matrix.rule_engine import life_style_assesment_matrix_engine
from repayment_capacity.rule_engine import repayment_capacity_engine
urls_blueprint = Blueprint('urls', __name__,)

@urls_blueprint.route('/creditscore/user/<id>')
def repayment_data_all_users(id):
    return fetch_user_score(id)

@urls_blueprint.route('/lifestyle/user/create',methods=['POST'])
def create_new_user_lifestyle():
    return life_style_assesment_matrix_engine(request.get_json())

@urls_blueprint.route('/repayment/user/create',methods=['POST'])
def create_new_user_repayment():
    return repayment_capacity_engine(request.get_json())

@urls_blueprint.route('/lifestyle/user/update',methods=['POST'])
def update_user_lifestyle():
    return life_style_assesment_matrix_engine(request.get_json())

@urls_blueprint.route('/repayment/user/update',methods=['POST'])
def update_user_repayment():
    return repayment_capacity_engine(request.get_json())