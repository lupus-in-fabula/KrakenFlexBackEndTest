"""
Created on Thu Mar 31
@author: Alper Böke Önder

Accesses the KrakenFlex Interview Tests Mock API

"""
import requests

class OutagesAPI:
    
    def __init__(self, apikey):
        if type(apikey) != str:
            apikey = ""
            print("Invalid API Key")
        self.apikey = apikey
                
    def get_outages(self):
        return self.__call_api("outages", "get")
    
    def get_devicelist(self, siteId):
        if type(siteId) != str:
            return((-1,"Site Id needs to be a string"))
        return self.__call_api("site-info/"+siteId, "get")
    
    def post_outages(self, siteId, outages):
        if type(siteId) != str:
            return((-1,"Site Id needs to be a string"))
        return self.__call_api("site-outages/"+siteId, "post", outages)
    
    
    def __call_api(self, function, method, outages = None):
        apiurl="https://api.krakenflex.systems/interview-tests-mock-api/v1/"+function
     
        try:
            res_status = 500
            while res_status == 500:
                if method == "get":
                    headers = {"x-api-key" : self.apikey}
                    response = requests.get(apiurl, headers=headers)
                elif method == "post":
                    headers = {"x-api-key" : self.apikey}
                    response = requests.post(apiurl, headers = headers, data=outages)
                else:
                    return (-1, "Unknown Method")
                res_status = response.status_code
        except:
            return (-1, "Exception connecting to service " + apiurl)
        if res_status != 200:
            errormessage = f"API Returned error code {response.status_code} - {response.json()['message']}"
            return (-1, errormessage)
        return (0, response.json())