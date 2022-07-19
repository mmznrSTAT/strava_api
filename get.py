from __future__ import print_function
import time
import importlib.util
import sys
sys.path.append("gitrepos/stravaAPI/python-client/")
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access toke for authorization: strava_oauth
swagger_client.configuration.access_token = '1d0f54681c937389685a3de7798c58ac7dab7802'

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
id = 7480079360 # Long | The identifier of the activity.
includeAllEfforts = true # Boolean | To include all segments efforts. (optional)

try: 
    # Get Activity
    api_response = api_instance.getActivityById(id, includeAllEfforts=includeAllEfforts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivitiesApi->getActivityById: %s\n" % e)


    