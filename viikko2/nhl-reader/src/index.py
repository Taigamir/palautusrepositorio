from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    console = Console()
    years = ["2018-19","2019-20","2020-21","2021-20","2022-23","2023-24","2024-25","2025-26"]
    countries = ["USA","FIN","CAN","SWE","CZE","RUS","SLO","FRA","GBR","SVK","DEN","NED","AUT","BLR","GER","SUI","NOR","UZB","LAT","AUS"]
    season = Prompt.ask("Season", choices=years, default="2024-25")
    nationality = Prompt.ask("Nationality", choices=countries, default=("FIN"))

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))
    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"Season {season} players from {nationality}")
    table.add_column("Names", style="cyan")
    table.add_column("Teams", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="bold")

    for p in players:
        table.add_row(p.name, p.team, str(p.goals),
            str(p.assists), str(p.points))

    console.print(table)

if __name__ == "__main__":
    main()
