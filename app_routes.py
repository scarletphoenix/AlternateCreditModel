from flask import Blueprint
from fetch_data import fetch_all_users_lifestyle
urls_blueprint = Blueprint('urls', __name__,)

@urls_blueprint.route('/userids')
def run():
    return fetch_all_users_lifestyle()

@urls_blueprint.route('/')
def main():
    return 'Welcome to credit risk assessment, alternate modelling'