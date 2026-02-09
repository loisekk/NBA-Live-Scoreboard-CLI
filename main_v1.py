import requests
import urllib3

# ---------------- CONFIG ----------------
BASE_URL = "https://data.nba.net/10s"   # ✅ FIXED
ALL_JSON = "/prod/v2/today.json"

TIMEOUT = 10

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ---------------- HELPERS ----------------
def fetch(url: str) -> dict:
    response = requests.get(
        url,
        headers=HEADERS,
        verify=False,
        timeout=TIMEOUT
    )
    response.raise_for_status()
    return response.json()


# ---------------- API FUNCTIONS ----------------
def get_links() -> dict:
    data = fetch(BASE_URL + ALL_JSON)
    return data.get("links", {})


def get_scoreboard() -> None:
    scoreboard_path = get_links().get("currentScoreboard")

    if not scoreboard_path:
        print("Scoreboard data not available.")
        return

    games = fetch("https://data.nba.net" + scoreboard_path).get("games", [])

    if not games:
        print("\nNo NBA games scheduled today.\n")
        return

    print("\n🏀 LIVE NBA GAMES\n")

    for game in games:
        home = game.get("hTeam", {})
        away = game.get("vTeam", {})
        clock = game.get("clock", "N/A")
        period = game.get("period", {}).get("current", "N/A")

        print("------------------------------------------------")
        print(f"{home.get('tricode')} vs {away.get('tricode')}")
        print(f"{home.get('score')} - {away.get('score')}")
        print(f"Clock: {clock} | Period: {period}")


def get_stats() -> None:
    stats_path = get_links().get("leagueTeamStatsLeaders")

    if not stats_path:
        print("Stats data not available.")
        return

    teams = (
        fetch("https://data.nba.net" + stats_path)
        .get("league", {})
        .get("standard", {})
        .get("regularSeason", {})
        .get("teams", [])
    )

    teams = [t for t in teams if t.get("name") != "Team"]
    teams.sort(key=lambda x: float(x.get("ppg", 0)), reverse=True)

    print("\n📊 NBA TEAM SCORING LEADERS (PPG)\n")

    for i, team in enumerate(teams, start=1):
        print(
            f"{i:>2}. "
            f"{team.get('name', 'N/A'):<22} "
            f"({team.get('nickname', '')}) — "
            f"{team.get('ppg', '0')} PPG"
        )


# ---------------- MAIN ----------------
def main() -> None:
    get_stats()
    # get_scoreboard()


if __name__ == "__main__":
    main()
