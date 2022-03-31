"""
Created on Thu Mar 31
@author: Alper Böke Önder

1. Retrieves all outages from the `GET /outages` endpoint
2. Retrieves information from the `GET /site-info/{siteId}` endpoint for the site with the ID `norwich-pear-tree`
3. Filters out any outages that began before `2022-01-01T00:00:00.000Z` or don't have an ID that is in the list of
   devices in the site information
4. For the remaining outages, it should attach the display name of the device in the site information to each appropriate outage
5. Sends this list of outages to `POST /site-outages/{siteId}` for the site with the ID `norwich-pear-tree`

"""
import pandas as pd
from kfoutages import OutagesAPI


def postDeviceOutages(siteId, apikey):
    # initializing parameters
    if type(siteId) != str:
        return("Site Id needs to be a string")
    if type(apikey) != str:
        return("Apikey needs to be a string")
    o = OutagesAPI(apikey)
    
    # Let's get outages list, status is -1 if something goes wrong
    status, allOutages = o.get_outages()
    if status<0:
        return(f"Error : {allOutages}")
    
    # Let's get the device list, status is -1 if something goes wrong
    status, deviceList = o.get_devicelist(siteId)
    if status<0:
        return(f"Error : {deviceList}")
    
    allOutages = pd.DataFrame(allOutages)
    allOutages = allOutages[allOutages['begin']>='2022-01-01']
    deviceList = pd.DataFrame(deviceList['devices'])
 
    enrichedOutages = pd.merge(allOutages, deviceList).loc[:,["id","name","begin","end"]]
    enrichedOutages = enrichedOutages.to_json(orient="records")

    status, message = o.post_outages(siteId, enrichedOutages)
    if status < 0:
        return(f"Error : {message}")
    
    return("Success")
    
    
def main():
    result = postDeviceOutages("norwich-pear-tree","EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23")
    print(result)
    
if __name__ == "__main__":
    main()