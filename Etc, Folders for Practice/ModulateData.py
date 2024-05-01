import csv
from collections import Counter
from datetime import datetime

def process_csv(file_path):
    total_posts = 0
    unique_authors = set()
    word_freq = Counter()
    earliest_date = float('inf')
    latest_date = 0
    total_words = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_posts += 1
            unique_authors.add(row.get('author', ''))

            created_utc_str = row.get('created_utc', '')
            if created_utc_str:
                try:
                    created_utc = int(created_utc_str)
                except ValueError:
                    continue  # Skip this row if 'created_utc' cannot be converted to an integer

                if created_utc < earliest_date:
                    earliest_date = created_utc
                if created_utc > latest_date:
                    latest_date = created_utc

            text = row.get('selftext', '')
            if text != '[removed]' and text.strip():
                words = text.split()
                total_words += len(words)
                word_freq.update(words)

    average_post_length = total_words / total_posts if total_posts else 0

    return total_posts, len(unique_authors), earliest_date, latest_date, average_post_length, word_freq


def main():
    file_path = 'depression-sampled.csv'
    total_posts, unique_authors, earliest_date, latest_date, average_post_length, word_freq = process_csv(file_path)

    earliest_date_formatted = datetime.utcfromtimestamp(earliest_date).strftime('%Y-%m-%d %H:%M:%S')
    latest_date_formatted = datetime.utcfromtimestamp(latest_date).strftime('%Y-%m-%d %H:%M:%S')

    print(f"Total number of posts: {total_posts}")
    print(f"Total number of unique authors: {unique_authors}")
    print(f"Average post length (including removed posts): {average_post_length:.2f} words")
    print(f"Date range: {earliest_date_formatted} - {latest_date_formatted}")
    print(f"Top 20 most important words: {word_freq.most_common(20)}")

if __name__ == "__main__":
    main()
