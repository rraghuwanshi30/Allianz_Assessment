import asyncio
from scraper import scrape_hockey_data
from utils import save_html_to_zip
from processor import extract_team_data, calculate_winners_losers
from excel_writer import save_to_excel

async def main():
    print("🔄 Fetching hockey team data...")
    html_pages = scrape_hockey_data()

    print("💾 Saving raw HTML data into a ZIP file...")
    save_html_to_zip(html_pages)

    print("📊 Extracting team statistics...")
    team_data = extract_team_data(html_pages)

    print("🏆 Calculating winners and losers per year...")
    summary = calculate_winners_losers(team_data)

    print("📂 Saving data to an Excel file...")
    save_to_excel(team_data, summary)

    print("✅ Process completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
