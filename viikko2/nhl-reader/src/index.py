"""Index used to run the program"""
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats


def display_players(console, season, value, players):
    """Display the selected players in a table."""
    table = Table(title=f"Season {season} players from {value}")
    table.add_column("Names", style="cyan")
    table.add_column("Teams", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="bold")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )

    console.print(table)


def main():
    """Main function for running program"""
    console = Console()
    years = ["2018-19", "2019-20", "2020-21", "2021-20", "2022-23", "2023-24", "2024-25", "2025-26"]
    countries = [
        "USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK",
        "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS",
    ]
    season = Prompt.ask("Season", choices=years, default="2024-25")
    search_by = Prompt.ask(
        "Search by", choices=["nationality", "team"], default="nationality"
    )

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))
    if search_by == "nationality":
        value = Prompt.ask("Nationality", choices=countries, default="FIN")
        players = stats.top_scorers_by_nationality(value)
    else:
        value = Prompt.ask("Team")
        players = stats.top_scorers_by_team(value)

    display_players(console, season, value, players)

if __name__ == "__main__":
    main()
