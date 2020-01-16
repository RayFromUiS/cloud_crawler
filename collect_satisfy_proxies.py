#!/usr/bin/env python
# coding: utf-8

# In[7]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy


from time import sleep
import time
import random


# In[10]:


class Collect_satisfy_proxies:
    '''collect satisfy proxy for such url
    Args:
        url and respond time criterior for screening the proxy
    Returns:
        raw proxy and satisfy time critrior standary proxy for reaching the url
    '''
#     url = 'http://www.aogc.state.ar.us/welldata/production/default.aspx'
    
    def __init__(self,url,res_time_criterior):
        self.url = url
        self.res_time_criterior = res_time_criterior ## in milliseconds
        self.proxies= None
        self.satisfy_proxies = [None]
        
    def get_proxies(self):
        '''return a proxy driver
        '''
        req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
        self.proxies = req_proxy.get_proxy_list() #this will create proxy list
        return self.proxies

    def test_driver_res(self,proxy):
        '''
        code_source for navigation time = https://stackoverflow.com/questions
        /37460214/how-to-measure-response-time-for-both-loading-and-search-time-for-a-website-se
        '''
        ## set proxy
        PROXY = proxy.get_address()
        webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,
        "proxyType":"MANUAL"}
        ## run test on proxy
        with webdriver.Chrome() as driver:
            try:
                driver.get(self.url)
                navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
                responseStart = driver.execute_script("return window.performance.timing.responseStart")
                domComplete = driver.execute_script("return window.performance.timing.domComplete")
                ##computing respond time
                backendPerformance = responseStart - navigationStart
                frontendPerformance = domComplete - responseStart
                print("Back End: %s" % backendPerformance)
                print("Front End: %s" % frontendPerformance)
                restime = backendPerformance + frontendPerformance
            except TimeoutException as e:
                print(e)

        return restime

    def collect_satisfy_proxies(self):
        '''return satisfy proxy
        '''
        ##get proxy
        self.proxies = get_proxies(self)
        ##for proxy in proxies:
        for proxy in self.proxies:
            ####run test on proxy;
            test_time = test_driver_res(self.url,proxy)
            ####if test satisfy the condition:
            if test_time < res_time:
                ####save the test proxy
                self.satisfy_proxies.append(proxy)
                if len(self.satisfy_proxies) > 10:
                    print(f'Alrady collect {len(self.satisfy_proxies)} of proxies')
                break
                    
        return self.satisfy_proxies

    


# In[ ]:


collect_satisfy_proxy = Collect_satisfy_proxies(url,30000)

