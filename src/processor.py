from bs4 import BeautifulSoup
from typing import List, Dict

def extract_team_data(html_pages: List[str]) -> List[Dict]:
    """Parses HTML pages and extracts hockey team statistics."""
    teams = []
    
    for html in html_pages:
        soup = BeautifulSoup(html, 'html.parser')
        
        # Find the correct table containing team stats
        table = soup.find("table", class_="table")
        if not table:
            print("⚠ No table found on page!")
            continue  

        rows = table.select("tbody tr")
        
        for row in rows:
            columns = row.find_all("td")
            
            if len(columns) < 3:
                continue  

            try:
                team_data = {
                    "year": int(columns[0].text.strip()),
                    "team": columns[1].text.strip(),
                    "wins": int(columns[2].text.strip()),
                }
                teams.append(team_data)
            except ValueError as e:
                print(f"⚠ Error parsing row: {e}")
    
    return teams

def calculate_winners_losers(team_data: List[Dict]) -> List[Dict]:
    """Finds the winner and loser team for each year."""
    years = set(d["year"] for d in team_data)
    summary = []

    for year in years:
        teams_of_year = [t for t in team_data if t["year"] == year]

        if not teams_of_year:
            continue

        winner = max(teams_of_year, key=lambda t: t["wins"])
        loser = min(teams_of_year, key=lambda t: t["wins"])

        summary.append({
            "year": year,
            "winner": winner["team"],
            "winner_wins": winner["wins"],
            "loser": loser["team"],
            "loser_wins": loser["wins"],
        })

    return summary
