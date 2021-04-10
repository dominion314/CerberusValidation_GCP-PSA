"""  Simple Cerberus Validator Script """
from cerberus import Validator
import yaml

with open('processed_params.yml') as f:
    DATA = yaml.load(f, Loader=yaml.FullLoader)

with open('PSA_Schema.yaml') as f:
    SCHEMA = yaml.load(f, Loader=yaml.FullLoader)

print('Hellow World')
V = Validator()
V.allow_unknown = True

if V.validate(DATA, SCHEMA):
    print('Pass')
else:
    print('Fail')
    ERR = V.errors
    print(ERR)
