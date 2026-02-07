
import requests
import pandas as pd
from datetime import datetime

# IMPORTANT: Remotive API JSON deta hai, HTML nahi!


def scrape_jobs(max_jobs=100):
    """
    Remotive API se jobs scrape karega

    Parameters:
    - max_jobs: Kitne jobs chahiye (default 100)

    Returns:
    - List of dictionaries (har job ek dictionary)
    """

    all_jobs = []

    # Remotive API URL
    api_url = "https://remotive.com/api/remote-jobs"

    print("🔍 Scraping is going on...\n")

    try:
        # API ko request bhejega
        print("Sending request to Remotive API...")
        response = requests.get(api_url, timeout=10)

        # Status check
        if response.status_code == 200:
            print("API responded successfully!\n")

            # JSON data parse karega (ye automatically dictionary banata hai)
            data = response.json()

            # 'jobs' key mein saare jobs hain
            jobs_data = data.get('jobs', [])

            print(f"Total jobs available: {len(jobs_data)}\n")

            # Limit tak jobs process karega
            jobs_to_process = jobs_data[:max_jobs]

            print(f"Processing {len(jobs_to_process)} jobs...\n")

            # Har job ko process karega
            for idx, job in enumerate(jobs_to_process, 1):
                try:
                    # Job data extract karega
                    job_data = {
                        'Job Title': job.get('title', 'N/A'),
                        'Company': job.get('company_name', 'N/A'),
                        'Location': job.get('candidate_required_location', 'Worldwide'),
                        'Job Type': job.get('job_type', 'N/A'),
                        'Category': job.get('category', 'N/A'),
                        'Tags': ', '.join(job.get('tags', [])),
                        'Salary': job.get('salary', 'Not specified'),
                        'Description': job.get('description', 'N/A')[:200] + '...',
                        'URL': job.get('url', 'N/A'),
                        'Publication Date': job.get('publication_date', 'N/A'),
                        'Scraped On': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }

                    all_jobs.append(job_data)

                    # Progress show
                    if idx % 10 == 0:
                        print(
                            f"   ✓ Processed {idx}/{len(jobs_to_process)} jobs...")

                except Exception as e:
                    print(f"⚠️ Error in job {idx}: {e}")
                    continue

            print(f"\n Successfully scraped {len(all_jobs)} jobs!")

        else:
            print(f"❌ API Error! Status code: {response.status_code}")
            print(f"Response: {response.text[:200]}")

    except requests.exceptions.Timeout:
        print("❌ Request timeout - API too slow")

    except requests.exceptions.ConnectionError:
        print("❌ Connection error - Check your internet")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    return all_jobs


# STEP 2: Data ko CSV mein save karna hai ab

def save_to_csv(jobs_list, filename='jobs_data.csv'):
    """
    Jobs list ko CSV file mein save karega

    Parameters:
    - jobs_list: List of job dictionaries
    - filename: Output CSV ka naam
    """

    if jobs_list:
        # Pandas DataFrame banate hain
        df = pd.DataFrame(jobs_list)

        # CSV mein save karte hain
        df.to_csv(filename, index=False, encoding='utf-8')

        print("\n" + "=" * 70)
        print(f"{len(jobs_list)} jobs saved to {filename}")
        print(f"Columns: {', '.join(list(df.columns)[:5])}...")
        print("=" * 70)

        return df
    else:
        print("\n❌ NO Jobs found in scraping!")
        return None

# MAIN EXECUTION

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("JOB SCRAPER STARTING - REMOTIVE API")
    print("=" * 70 + "\n")

    # Scraping shuru hogi (50 jobs)
    jobs = scrape_jobs(max_jobs=50)

    # CSV mein save 
    df = save_to_csv(jobs)

    # Quick preview 
    if df is not None:
        print("\n" + "=" * 70)
        print("PREVIEW (First 5 jobs):")
        print("=" * 70)
        print(df[['Job Title', 'Company', 'Category', 'Job Type']].head())

        print("\n" + "=" * 70)
        print("QUICK STATS:")
        print("=" * 70)
        print(f"Total Jobs: {len(df)}")
        print(f"Unique Companies: {df['Company'].nunique()}")
        print(f"Categories: {', '.join(df['Category'].unique()[:5])}")
        print(f"Job Types: {', '.join(df['Job Type'].unique())}")
        print("\n" + "=" * 70)
        print("DONE! Now run analyzer.py")
        print("=" * 70 + "\n")
