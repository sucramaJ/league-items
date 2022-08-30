from utils import credentials
import cassiopeia as cass
import os

credentials.set_environ()

champions = cass.Champions(region="NA")
for champion in champions:
    print(champion.name, champion.id)