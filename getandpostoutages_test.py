"""
Created on Thu Mar 31
@author: Alper Böke Önder

Unit tests for getandpostoutages module
"""
import unittest
from getandpostoutages import *


class TestpostDeviceOutages(unittest.TestCase):
    def test_post(self):
        self.assertAlmostEqual(postDeviceOutages("wrong-site","EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23"),"Error : API Returned error code 404 - Site not found")
        self.assertAlmostEqual(postDeviceOutages("norwich-pear-tree","wrong_api_key"),"Error : API Returned error code 403 - Forbidden")
        self.assertAlmostEqual(postDeviceOutages("norwich-pear-tree","EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23"),"Success")
        self.assertAlmostEqual(postDeviceOutages(3,"EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23"),"Site Id needs to be a string")
        self.assertAlmostEqual(postDeviceOutages("norwich-pear-tree",["this is a list"]),"Apikey needs to be a string")

