import requests


def get_data(access_token: str, url: str, per_page: int = 200, page: int = 1):

    # Define request headers and parameters
    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': per_page, 'page': page}

    # Collect data from api
    data = requests.get(
        url,
        headers=header,
        params=param
    ).json()

    return data


def get_segment_data(id: int, access_token: str):

    # Define segment url
    segment_url = f"https://www.strava.com/api/v3/segments/{id}"

    # Define request header
    header = {'Authorization': 'Bearer ' + access_token}

    # Send out request and collect data
    data = requests.get(
        segment_url,
        headers=header
    ).json()

    return data
