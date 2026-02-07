# Job Scraper & Analyzer

A Python-based web scraping and data analysis tool that collects job listings from Remotive API and provides comprehensive insights.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Overview

This project scrapes real remote job listings using the Remotive API and analyzes the data to provide insights about:
- Top hiring companies
- Most in-demand skills
- Job categories and types
- Geographic distribution
- Salary information

## Features

- ✅ **Real Job Data** - Fetches actual remote job listings
- ✅ **No Authentication Required** - Uses free public API
- ✅ **Comprehensive Analysis** - Multiple data insights
- ✅ **CSV Export** - Data saved for further analysis
- ✅ **Clean Code** - Well-documented and beginner-friendly

## Technologies Used

- **Python 3.7+**
- **Requests** - API calls
- **Pandas** - Data manipulation and analysis
- **Collections** - Data processing

## Project Structure
```
Job-Scraper-Analyzer/
│
├── scraper.py          # Main scraping script
├── analyzer.py         # Data analysis script
├── requirements.txt    # Python dependencies
├── jobs_data.csv       # Output data (generated)
└── README.md          # Documentation
```

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ramshawork/Job-Scraper-Analyzer.git
cd Job-Scraper-Analyzer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Step 1: Scrape Jobs
```bash
python scraper.py
```

This will:
- Fetch 50+ remote job listings from Remotive API
- Parse and clean the data
- Save results to `jobs_data.csv`

**Output:**
```
JOB SCRAPER STARTING - REMOTIVE API
=====================================

 Scraping is going on...
 Sending request to Remotive API...
 API responded successfully!

 Total jobs available: 700+
 Processed 50/50 jobs...

 Successfully scraped 50 jobs!
 50 jobs saved to jobs_data.csv
```

### Step 2: Analyze Data
```bash
python analyzer.py
```

This provides insights on:
- Top job categories
- Leading companies hiring
- Job type distribution
- Popular locations
- Most in-demand skills
- Salary information

**Sample Output:**
```
JOB DATA ANALYSIS
====================================

DATASET OVERVIEW
Total Jobs: 50
Unique Companies: 45
Unique Categories: 8

🏷️  Top 10 Job Categories:
1. Software Development    15 jobs (30.0%) ███████████
2. Customer Support         8 jobs (16.0%) ████████
3. Design                   6 jobs (12.0%) ██████
...
```

## Data Schema

The scraper collects the following fields:

| Field | Description |
|-------|-------------|
| Job Title | Position name |
| Company | Company name |
| Location | Required location (or Worldwide) |
| Job Type | Full-time, Contract, etc. |
| Category | Job category/department |
| Tags | Skills and technologies |
| Salary | Salary range (if provided) |
| Description | Job description (truncated) |
| URL | Application link |
| Publication Date | When job was posted |
| Scraped On | Timestamp of data collection |

## Sample Insights

After running the analyzer, you'll get insights like:

- **Top Hiring Companies**: Which companies are hiring most
- **In-Demand Skills**: Most frequently mentioned technologies
- **Job Categories**: Distribution across different fields
- **Remote Locations**: Geographic requirements for remote work
- **Salary Transparency**: Percentage of jobs listing salaries

## Customization

### Modify Number of Jobs

Edit `scraper.py`:
```python
jobs = scrape_jobs(max_jobs=100)  # Change from 50 to 100
```

### Filter by Category

The Remotive API provides jobs across categories:
- Software Development
- Customer Support
- Design
- Sales
- Marketing
- Product
- Data Science

## Requirements
```
requests==2.31.0
pandas==2.1.0
```

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License - feel free to use it for learning and portfolio purposes.

## Acknowledgments

- Job data provided by [Remotive.io](https://remotive.com/)
- Built as a portfolio project to demonstrate web scraping and data analysis skills

## Author

**Your Name**
- GitHub: [@ramshawork](https://github.com/ramshawork)
- LinkedIn: [Your Profile](https://www.linkedin.com/in/ramshaanwar-dev/)

## Contact

For questions or feedback, please open an issue or reach out via email.

---

**If you found this project useful, please give it a star!** 🌟