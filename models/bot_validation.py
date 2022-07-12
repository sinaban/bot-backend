from models.bot_prop import BotPropModel
from models import bot_config


class WrongConfigError(RuntimeError):
    pass

class NoBotError(ValueError):
    pass

def check_bot_exists(bot):
    if not bot:
        raise NoBotError("this bot id does not exist")  

def validate_bot_by_id(botid):
    bot= BotPropModel.find_by_id(botid)
    check_bot_exists(bot)
    return bot

def is_config_exist(botid):
    if not bot_config.get_bot_config(botid):
        raise WrongConfigError(f"there is no related config for {botid}")
