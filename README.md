# KrakenFlex Back End Test

This is a small project for testing connectivity to KrakenFlex mock api and retrieving outages list and device list for a spesific site (`norwich-pear-tree`)
and posting the outages back to the API after it is enriched with the device names. The data also needs to be cleaned from the outages that began
before 2022-01-01.

## Files in the folder

kfoutages.py : API object and related access methods.
getandpostoutages.py : Actual script that retrieves the outages list and posts the enriched version.
getandpostoutages_test.py : Unit testing script for the script.

## Dependencies

pandas module need to be installed if it is not already available:
    > pip install pandas

## How to Run

Script getandpostoutages.py can be executed directly. If this is done, it will run for the site: `norwich-pear-tree`

    >!python getandpostoutages.py

It is also possible to import the script into another python file and run the function using desired site id

    from getandpostoutages import postDeviceOutages
    result = postDeviceOutages("norwich-pear-tree","EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23")
    print("result")
    
## Unit testing
The unit test script can be executed with the following command

        > !python -m unittest getandpostoutages_test.py

