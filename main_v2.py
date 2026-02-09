import requests


SCOREBOARD_URL = (
    "https://cdn.nba.com/static/json/liveData/scoreboard/"
    "todaysScoreboard_00.json"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

TIMEOUT = 10


def fetch(url: str) -> dict | None:
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"⚠️  Request blocked: {e}")
        return None


def get_scoreboard() -> None:
    data = fetch(SCOREBOARD_URL)

    if not data:
        print("Unable to fetch scoreboard.")
        return

    games = data.get("scoreboard", {}).get("games", [])

    if not games:
        print("No NBA games today.")
        return

    print("\n🏀 TODAY'S NBA GAMES\n")

    for game in games:
        home = game["homeTeam"]
        away = game["awayTeam"]

        print("------------------------------------------------")
        print(f"{home['teamTricode']} vs {away['teamTricode']}")
        print(f"{home['score']} - {away['score']}")
        print(f"Status: {game['gameStatusText']}")


def get_team_ppg() -> None:
    print(
        "\n📊 Team PPG data is currently unavailable.\n"
        "The NBA blocks this endpoint for non-browser requests.\n"
        "This project focuses on live game data instead.\n"
    )



def main() -> None:
    get_scoreboard()
    get_team_ppg()


if __name__ == "__main__":
    main()
