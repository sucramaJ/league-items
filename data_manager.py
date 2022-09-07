#All methods return dictionaries representing the json objects described by the official
#Riot API. Any HTTP errors that are returned by the API are raised as HTTPError exceptions 
# from the Requests library.

from utils import credentials
from riotwatcher import LolWatcher
import json

def save_data(api_key, champ=True, item=True):
    lol_watcher = LolWatcher(api_key=api_key)
    region = 'euw1'
    versions = lol_watcher.data_dragon.versions_for_region(region)
    if champ:  
        champion_version = versions['n']['champion']
        champ_data = lol_watcher.data_dragon.champions(champion_version)
        with open(f'data/champ_{champion_version.replace(".", "_")}', 'w') as file:
            json.dump(champ_data['data'], file)
    
    if item:
        item_version = versions['n']['item']
        item_data = lol_watcher.data_dragon.items(item_version)
        with open(f'data/item_{item_version.replace(".", "_")}', 'w') as file:
            json.dump(item_data['data'], file)


if __name__ == "__main__":
    api_key = credentials.get_key()
    save_data(api_key)
    print("Done!")


