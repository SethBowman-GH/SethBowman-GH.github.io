# Market Intelligence ETL Pipeline

## Case Use and Business Value
This project was developed to automate the collection of market-shifting news for Technical Business Analysts and Research Leads. Instead of manual daily searches, this pipeline programmatically extracts, transforms, and loads (ETL) high-value leads into a structured SQL database.

* **Primary Goal**: Reduce manual research time by 90% through automated web scraping.
* **Business Impact**: Enables data-driven decision-making by providing a historical record of market movements rather than ephemeral search results.

---

## Technical Architecture
A modular Python-to-SQLite architecture was selected to demonstrate enterprise-level data handling:
* **Extraction (Python/BeautifulSoup)**: Scrapes live headlines from Bing News to capture real-time market sentiment.
* **Transformation (Pandas)**: Cleans raw HTML into a structured format, adding metadata like scraped_at timestamps and status tags for CRM integration.
* **Storage (SQLite)**: Utilizes a Relational Database to support SQL-based filtering, reporting, and data persistence.

---

## Execution Instructions
1. **Environment Setup**: Create a virtual environment and install dependencies:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   pip install pandas requests beautifulsoup4
Run Pipeline: Execute the main scraper script:

PowerShell
python scripts/scraper.py
Data Analysis: Use the SQLTools extension in VS Code to query the market_intel.db file.

Challenges and Troubleshooting
Building this pipeline required resolving several technical hurdles common in enterprise environments:

Windows Execution Policy: Encountered a SecurityError when installing database drivers. Resolved by elevating PowerShell permissions (Set-ExecutionPolicy) to allow Node.js runtimes to execute.

Pathing Mismatches: Fixed database connection errors where SQLTools was defaulting to relative paths. Implemented os.path.abspath to ensure data integrity across different local environments.

Driver Dependency Management: Manually resolved sqlite3 driver installation failures by leveraging npm to bypass automated extension installation issues.

Future Roadmap
Automation: Integrate with n8n or GitHub Actions for daily scheduled execution.

Sentiment Analysis: Add a Natural Language Processing (NLP) layer to automatically categorize news sentiment.

Dashboarding: Connect the SQLite database to PowerBI or Tableau for visual reporting.