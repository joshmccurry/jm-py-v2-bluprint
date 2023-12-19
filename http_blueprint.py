# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(blueprint) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints
import azure.functions as func
import logging

http_blueprint = func.Blueprint()

@http_blueprint.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(
            "This HTTP triggered function executed successfully.",
            status_code=200
    )

@http_blueprint.route(route="http_trigger2", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger2 function processed a request.')
    return func.HttpResponse(
            "This HTTP triggered 2 function executed successfully.",
            status_code=200
    )