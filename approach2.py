## https://medium.com/swlh/using-python-to-connect-to-stravas-api-and-analyse-your-activities-dummies-guide-5f49727aac86


import requests
import json# Make Strava auth API call with your 
# client_code, client_secret and code
response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = {
                            'client_id': 46014,
                            'client_secret': 'bf40c0b57046e081d170ed64e36851fa5a8e4813',
                            'code': '21d76d5a4979e75f1eb77b90e6fd9064e9a13599',
                            'grant_type': 'authorization_code'
                            }
                )#Save json response as a variable
strava_tokens = response.json()# Save tokens to file
with open('strava_tokens.json', 'w') as outfile:
    json.dump(strava_tokens, outfile)# Open JSON file and print the file contents 
# to check it's worked properly
with open('strava_tokens.json') as check:
  data = json.load(check)
print(data)