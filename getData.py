## https://towardsdatascience.com/using-the-strava-api-and-pandas-to-explore-your-activity-data-d94901d9bfde


import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "46014",
    'client_secret': 'bf40c0b57046e081d170ed64e36851fa5a8e4813',
    'refresh_token': 'ae5cfc2fb172479dbcea49604f68b64b5bf9d56a',
    'grant_type': "refresh_token",
    'f': 'json'
}

x = requests.post("https://www.strava.com/oauth/token?client_id=46014&client_secret=bf40c0b57046e081d170ed64e36851fa5a8e4813&code=b53917bbed91d0e5cd437de1d7c877111b07b252&grant_type=authorization_code")
print(x.text)




print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

print(my_dataset[0]["name"])
print(my_dataset[0]["map"]["summary_polyline"])