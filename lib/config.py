import configparser
config = None
config_file = 'config.ini'

def get_config(section, reload=False):
    global config
    global config_file
    if config is None or reload:
        loc_config = configparser.ConfigParser()
        loc_config.read(config_file)
        config = loc_config
    return config[section]
