
import pandas as pd
from collections import Counter


# CSV file ko load karna hai

def load_data(filename='jobs_data.csv'):
    """CSV file ko pandas DataFrame mein load karega"""
    try:
        df = pd.read_csv(filename)
        print(f"Data loaded: {len(df)} jobs found\n")
        return df
    except FileNotFoundError:
        print(f"File '{filename}' nahi mili!")
        return None


# ANALYSIS FUNCTIONS

def analyze_top_locations(df, top_n=5):
    """
    Top N locations with most jobs

    LOGIC: Location column ko count karke sort karte hain
    """
    print(f"📍 Top {top_n} Locations with Most Jobs:")
    print("-" * 40)

    location_counts = df['Location'].value_counts().head(top_n)

    for i, (location, count) in enumerate(location_counts.items(), 1):
        print(f"{i}. {location}: {count} jobs")

    return location_counts


def analyze_top_companies(df, top_n=5):
    """Top companies hiring the most"""
    print(f"\n Top {top_n} Companies Hiring:")
    print("-" * 40)

    company_counts = df['Company'].value_counts().head(top_n)

    for i, (company, count) in enumerate(company_counts.items(), 1):
        print(f"{i}. {company}: {count} openings")

    return company_counts


def analyze_job_titles(df):
    """Most common job titles (word frequency)"""
    print(f"\n Most Common Job Keywords:")
    print("-" * 40)

    # Saare titles ko ek string mein combine 
    all_titles = ' '.join(df['Job Title'].values)

    # Words ko split karega aur count 
    words = all_titles.lower().split()

    # Common words ko filter 
    stop_words = {'and', 'or', 'the', 'a', 'an', 'in', 'of', 'for'}
    filtered_words = [
        word for word in words if word not in stop_words and len(word) > 2]

    # Top 10 keywords
    word_freq = Counter(filtered_words).most_common(10)

    for i, (word, count) in enumerate(word_freq, 1):
        print(f"{i}. {word}: {count} times")

    return word_freq

# MAIN ANALYSIS


if __name__ == "__main__":
    print("=" * 50)
    print("DATA ANALYSIS STARTING...")
    print("=" * 50 + "\n")

    # Data load 
    df = load_data()

    if df is not None:
        # Basic info
        print(f"Total Jobs: {len(df)}")
        print(f"Total Companies: {df['Company'].nunique()}")
        print(f"Total Locations: {df['Location'].nunique()}\n")

        # Analysis run hoga
        analyze_top_locations(df, top_n=5)
        analyze_top_companies(df, top_n=5)
        analyze_job_titles(df)

        print("\n" + "=" * 50)
        print("Analysis Complete!")
        print("=" * 50)
