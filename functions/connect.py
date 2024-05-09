import requests


def authorization(client_id: str, redirect_uri: str):
    '''
    Input: Strava API client ID and redirect URL
    Output: Request url string
    Function to generate the strava request url
    '''

    # Generate request url
    request_url = f'http://www.strava.com/oauth/authorize?client_id={client_id}' \
                  f'&response_type=code&redirect_uri={redirect_uri}' \
                  '&approval_prompt=force' \
                  '&scope=profile:read_all,activity:read_all'

    return request_url


def get_access_token(client_id: str, client_secret: str, code: str):
    '''
    Input: Strava API client ID, client secret and refresh token
    Output: Strava API access token
    Function to fetch strava API access token
    '''

    # Collect access token for user
    token = requests.post(url='https://www.strava.com/oauth/token',
                          data={'client_id': client_id,
                                'client_secret': client_secret,
                                'code': code,
                                'grant_type': 'authorization_code'},
                          headers={})

    # Collect access token from response
    access_token = token.json()['access_token']

    return access_token
