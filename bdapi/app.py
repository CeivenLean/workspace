from aip import AipOcr


def getClient():
    APP_ID = '15681435'
    API_KEY = 'vxhg86ulPWm9S530UFvEGAZc'
    SECRET_KEY = '1XdbG8fFqFGGlvG3Merx3M2CoWQDzGnX'
    return AipOcr(APP_ID, API_KEY, SECRET_KEY)

def translateConfig():
    APPID = '20190305000273757'
    MIYUE = 'mYkv8e9zyLmxQMHzcnnt'
    return APPID, MIYUE
