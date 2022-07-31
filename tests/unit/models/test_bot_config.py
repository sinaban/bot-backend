import pytest
from pytest_mock import mocker
from models import bot_config
from models.indicators import config_template
from exceptions.pair_exceptions import NoPriceFound,NoConfigFoundError,\
    NoWhiteListError


def hget_sideeffect(key,botid=1):
    if key == "SOLUSDTM":
        return "b'2.3'"
    elif key == "bots:config" and botid == 1: 
        return config_template.config 
    else:
        return None

def get_config_sideeffect(key):
    if key == 0:
        return key
    else :
        return key

def get_white_sideeffect(key):
    if key == 0:
        return {}
    else :
        return config_template.config

@pytest.fixture
def mock_redis_client_hget(mocker):
        return mocker.patch('models.bot_config.redis_client.hget',
        side_effect = hget_sideeffect)

@pytest.fixture
def check_and_get_bot_configs(mocker):
    return mocker.patch('models.bot_config.check_and_get_bot_configs',
    side_effect = get_white_sideeffect)

@pytest.fixture
def get_whitelist(mocker,check_and_get_bot_configs):

    return mocker.patch('models.bot_config.json.loads',
    side_effect = get_config_sideeffect)


def test_except_check_get_price_ready(mock_redis_client_hget):
    """
    input is None
    test raise NoPriceFound Excepton
    """    
    with pytest.raises(NoPriceFound):
        bot_config.check_and_get_price_ready("","_askPrice")

def test_check_get_price_ready(mock_redis_client_hget):
    """
    input is binary
    return exact input
    """
    mock_redis_client_hget("SOLUSDTM")
    assert bot_config.check_and_get_price_ready("SOLUSDTM","_askPrice") == "b'2.3'"


def test_get_price(mocker):
    """
    test get price correctly
    """
    mocker.patch('models.bot_config.get_price_with_type',return_value = 0.3)
    assert bot_config.getPrice('ADAUSDTM') == 0.3

def test_get_askprice(mocker):
    """
    test get ASK price correctly
    """
    mocker.patch('models.bot_config.get_price_with_type',return_value = 0.3)
    assert bot_config.getAskPrice('ADAUSDTM') == 0.3

def test_check_and_get_bot_configs_exception(mock_redis_client_hget):
    with pytest.raises(NoConfigFoundError):
        bot_config.check_and_get_bot_configs(0)

def test_check_and_get_bot_configs(mock_redis_client_hget):
    assert bot_config.check_and_get_bot_configs(1) == config_template.config 

def test_check_and_get_whitelist(mocker,check_and_get_bot_configs):
    mocker.patch('models.bot_config.json.loads',
    return_value = config_template.config)

    assert bot_config.check_and_get_pair_whitelist(1) == \
    config_template.config['pair_whitelist']

def test_check_and_get_whitelist(get_whitelist):
    assert bot_config.check_and_get_pair_whitelist(1) == \
    config_template.config['pair_whitelist']

def test_check_and_get_whitelist(get_whitelist):
    with pytest.raises(NoWhiteListError):
        bot_config.check_and_get_pair_whitelist(0)