import yaml

with open("config/config.yaml", "r") as ymlfile:
    config_file = yaml.load(ymlfile, Loader=yaml.FullLoader) 
    