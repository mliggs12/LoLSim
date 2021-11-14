import requests
import requests_cache

CHAMPION = "Sylas"


def get_champ_data(champion=CHAMPION):
    """Makes request to get desired champion's JSON data for the latest available patch.

    The champion's name in the request URL is case-sensitive.
    """
    url = f"http://cdn.merakianalytics.com/riot/lol/resources/latest/en-US/champions/{champion}.json"
    return requests.get(url).json()


def main():
    """Main entry point for script."""
    requests_cache.install_cache()
    print(get_champ_data())


if __name__ == "__main__":
    main()
