import pandas as pd
from google_play_scraper import Sort, reviews


def scrape_reviews(app_id, max_reviews, output_file="datasets.csv"):
    """Scrapes reviews from the Google Play Store."""
    try:
        result, _ = reviews(
            app_id, lang="id", country="id", sort=Sort.NEWEST, count=max_reviews
        )
        pd.DataFrame(result).to_csv(output_file, index=False)
        return True
    except Exception as e:
        print(f"Error scraping reviews: {e}")
        return False


if __name__ == "__main__":
    scrape_reviews("com.bca.mybca.omni.android", 20000)
