from requests import get
from pprint import PrettyPrinter


BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()


def get_links():
    data = get(BASE_URL + ALL_JSON ).json()
    links = data['links']
    return links


def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = [BASE_URL + scoreboard].json()['games']


    for game in games:
        Home_team = game['hTeam'] 
        away_team = game['vTeam']
        clock     = game['clock']
        period    = game['period']

        print("------------------------------------------------")
        print(f"{Home_team['tricode']} vs {away_team['tricode']} ")
        print(f"{Home_team['score']} vs {away_team['score']} ")
        print(f"{clock} - {period['current']}")
    
def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = [BASE_URL + stats].json()['league']['standard']['regularSeason']['teams']
    printer.pprint(teams[0].keys()) # for list object has no attribute 'keys' -> passing through an [0] 


    teams = list(filter(lambda x: x['name'] != "Team" , team)) # -> return the filter objects 
    # filter -> it will run a fun againt every single element in in our teams if the fun return True it will keep the elements 
    # unless it will remove it . x: -> parameters 
    for i ,team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg'] # points per game 
        print(f"{i + 1 } . {name} , {nickname} , {ppg}")
get_stats()
