#!/usr/bin/env python
# coding: utf-8



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy




class CollectSatisfyProxies:
    '''collect satisfy proxy for such url under certain respond time
    Args:
        url,                Required, in string format, the url starter you want to scrapy
        res_time_criterior, Required, the time constrains for responding,in milliseconds
        number_of_proxies,  Required, numer of proxies you needed to rotate
    Returns:
        raw proxy,          List of objects
        screend proxy,      Satisfing proxy for reaching the url,list of objects
    Raise:
        TimeoutException
        WebDriverException      
    '''
#     url = 'http://www.aogc.state.ar.us/welldata/production/default.aspx'

    
    def __init__(self,url,res_time_criterior,number_of_proxies):
        self.url = url
        self.res_time_criterior = res_time_criterior ## in milliseconds
        self.proxies= None
        self.satisfy_proxies = []
        self.numer_of_proxies = number_of_proxies
        
    def get_proxies(self):
        '''return a proxy driver
        '''
        req_proxy = RequestProxy() #random proxies
        self.proxies = req_proxy.get_proxy_list() #this will create proxy list
        return self.proxies

    def test_driver_res(self,proxy):
        '''
        code_source for navigation time = https://stackoverflow.com/questions
        /37460214/how-to-measure-response-time-for-both-loading-and-search-time-for-a-website-se
        '''
        restime = 0 #inital restime
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
            except WebDriverException as e:
                print(e)

        return restime

    def collect_satisfy_proxies(self):
        '''return satisfy proxy
        '''
        ##get proxy
        self.proxies = self.get_proxies()
        print(type(self.proxies))
        ##for proxy in proxies:
        for proxy in self.proxies:
            ####run test on proxy;
            print(dir(proxy))
            test_time = self.test_driver_res(proxy)
            ####if test satisfy the condition:
            if test_time < self.res_time_criterior:
                ####save the test proxy
                self.satisfy_proxies.append(proxy)
                if len(self.satisfy_proxies) > self.numer_of_proxies:
                    print(f'Alrady collect {len(self.satisfy_proxies)} of proxies')
                break
                    
        return self.satisfy_proxies
