from riotwatcher import LolWatcher
from riotwatcher._apis.league_of_legends.SummonerApiV4 import SummonerApiV4

import API_KEY 

watcher = LolWatcher(API_KEY.key)

def printStats(summonerName):
    
    summoner = watcher.summoner.by_name('eune1', summonerName)
    stats = watcher.league.by_summoner('eune1', summoner['id'])

    tier = stats[0]['tier']
    print(tier)

printStats("yechiel")