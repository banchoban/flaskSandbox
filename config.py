import os
from decouple import config

class Config(object):
    SECRET_KEY = config('SECRET_KEY')

