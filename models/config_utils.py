import json
from models import bot_config
from models.bot_validation import is_config_exist
from exceptions.bot_exceptions import WrongConfigError


def is_bot_in_dryrun_mode(botid):
    try:
        is_config_exist(botid)
        config = json.loads(bot_config.get_bot_config(botid))
        if config['dryrun_config']['dryrun_enable']==True:
            return True
        return False
    except WrongConfigError as e :
            return  {'message': 'bot has no config'}, 501