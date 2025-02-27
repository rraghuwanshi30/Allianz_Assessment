import openpyxl

def save_to_excel(team_data: list, summary: list, filename="hockey_stats.xlsx"):
    """Creates an Excel file with two sheets."""
    wb = openpyxl.Workbook()

    # Sheet 1: Raw Data
    sheet1 = wb.active
    sheet1.title = "NHL Stats"
    sheet1.append(["Year", "Team", "Wins"])
    
    for row in team_data:
        sheet1.append([row["year"], row["team"], row["wins"]])

    # Sheet 2: Winner & Loser Summary
    sheet2 = wb.create_sheet(title="Winners & Losers")
    sheet2.append(["Year", "Winner", "Winner Wins", "Loser", "Loser Wins"])
    
    for row in summary:
        sheet2.append([row["year"], row["winner"], row["winner_wins"], row["loser"], row["loser_wins"]])

    wb.save(filename)
    print(f"✅ Data Saved to {filename}")
