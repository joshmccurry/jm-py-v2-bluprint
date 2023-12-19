import azure.functions as func
import datetime
import json
import logging
from http_blueprint import http_blueprint
from time_blueprint import time_blueprint

app = func.FunctionApp()

app.register_functions(http_blueprint) 
app.register_functions(time_blueprint) 