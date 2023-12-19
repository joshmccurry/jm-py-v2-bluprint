import azure.functions as func
import logging

time_blueprint = func.Blueprint()

@time_blueprint.timer_trigger(schedule="0 * * * * *", arg_name="myTimer", use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')

@time_blueprint.timer_trigger(schedule="0 * * * * *", arg_name="myTimer2", use_monitor=False) 
def timer_trigger2(myTimer2: func.TimerRequest) -> None:
    if myTimer2.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')