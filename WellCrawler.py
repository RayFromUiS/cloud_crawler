#!/usr/bin/env python
# coding: utf-8

# In[10]:


import selenium
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.by import By
from CollectSatisfyProxies import CollectSatisfyProxies


# In[11]:


url = 'http://www.aogc.state.ar.us/welldata/production/default.aspx'


# In[12]:


class Well_crawler:
    '''performing well crawling
    '''
    input_id = 'input#cpMainContent_radSearch_3' #input area
    search_button_id = 'input#cpMainContent_btnGo' ## searching button
    
    def __init__(self,url,proxy):
        self.url = url
        self.proxy = proxy
        self.driver = None
        self.fields = [] #field list names
        self.wells = [] ##scrapy wells  data
    
    def sel_field_and_searching(self):
        '''return driver
        '''
        ## set proxy
        PROXY = self.proxy.get_address()
        webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,
        "proxyType":"MANUAL"}

        with webdriver.Chrome() as driver:
            driver.get(self.url)
            ## click 'field' button and go searching
            driver.find_element(By.CSS_SELECTOR,input_id).click()
            driver.find_element(By.CSS_SELECTOR,search_button_id).click()
            time.sleep(30) #sleep until it to loaded 30s
            self.driver = driver
        return self.driver 
    
    def extract_field_names(self):
        '''get the field name from above driver soup
            no action has been changed
        '''
        fields_div_id = 'cpMainContent_pnlWellRpt' ## div id name
#         field_id_common = 'cpMainContent_rptSearch_lnkList_' #field id comman name for concating 
        ## get field names and clickable id
        field_page  = self.driver.page_source #page source
        field_soup = BeautifulSoup(field_page,'lxml') #soup
    #     print(field_soup)
        fields_div = field_soup.find(id=fields_div_id) #div soup
        field_trs = fields_div.find_all('tr') # field table data,each row has two tds
        for i in range(len(field_trs)):
            tds = field_trs[i].find_all('td')
            field_name = tds[0].find('span').get_text().strip() #first td is field name
#             field_id = field_id_common + str(i) #each row corresponding to one clickable id
            self.fields.append(field_name)

        return self.fields
    
    def grap_well_name(self):
        '''grab wells name from driver page
        '''
        wells_id = []
        well_id_div = 'cpMainContent_GridID' ##wells container
        wells_clickable_id_prefix = 'ctl00_cpMainContent_rptList_ct' #clickable id prefix
        middle_start = 100
        wells_clickable_id_suffix = '_lnkList' ##wells clickable id suffix
#         well_id_locator = ''
        self.driver.find_element(By.CSS_SELECTOR,well_clickable_id).click()
        time.sleep(30) #sleep for 30s
        well_page_source = self.driver.page_source
        well_page_soup = BeautifulSoup(well_page_source,'lxml')
        wells_div = well_page_soup.find(well_id_div)
        wells_names = wells_div.find_all('a')
        
        for i in range(middle_start,middle_start+len(wells_names)):
            well_id = wells_clickable_id_prefix + str(i) + wells_clickable_id_suffix
            wells_id.append(well_id)
        return wells_id,self.driver
    
    def scrapy_well_data(self,well_id):
        '''scrapy down well data
        '''
        well = {} ##well data container
        prod_rows = [] ##prod rows data container
        prod_id = '__tab_cpMainContent_Container1_tabProd'
        
        self.driver.find_element(By.ID,well_id).click()
        self.driver.find_element(By.ID,prod_id).click()
        
        well_page = driver.page_source
        well_page_soup = BeautifulSoup(well_page)
        ## get well general information 
        well['well_name'] = well_page_soup.find('span',id = 'cpMainContent_tblWellName').text
        well['ID'] = well_page_soup.find('span',
                            id='cpMainContent_Container1_tabData_rptWellData_lblAPI_0') \
                            .text.strip()        
        well['well_lat']  = well_page_soup.find('span',                            id = 'cpMainContent_Container1_tabData_rptWellData_lblLat_0')                             .text.strip()
        well['longit']= well_page_soup.find('span',                            id = 'cpMainContent_Container1_tabData_rptWellData_lblLong_0')                             .text.strip() 
        well['well_type'] =well_page_soup.find('span',                             id  = 'cpMainContent_Container1_tabData_rptWellData_lblWellType_0')                             .text.strip()
        well['well_status'] =well_page_soup.find('span',                            id= 'cpMainContent_Container1_tabData_rptWellData_lblWellStatus_0')                             .text.strip()
        ## get well production data
        page_pro_rows = prod_page.find('table',{'class':'GridViewClass'}).find_all('tr')
        ## for each row
        for i in range(1,len(page_pro_rows)):
            page_pro_rows_cols = page_pro_rows[i].find_all('td')
            prod_row_col = list()
            for j in range(len(page_pro_rows_cols)):
                value = page_pro_rows_cols[j].text
                prod_row_col.append(value)
            prod_rows.append(prod_row_col)
        well['production_data'] = prod_row
        return well
    
    def input_field_hit_search(self):
        '''for each field,
        click the a tag with id,
        '''

        for field in self.fields:
             ##input search field name
            self.driver.find_element(By.CSS_SELECTOR,input_id).click()
            ## hit search button
            self.driver.find_element(By.CSS_SELECTOR,search_button_id).click()
            ## for each well
            wells_id,self.driver = self.grap_well_name()
            ## perform scrapy
            for well_id in wells_id:
                well_data = self.scrapy_well_data(well_id)
            ## yield well data to field container
                yield well_data
            
                
        def get_wells_from_gen(self):
            '''iterate well data from generator
            '''
            for well in self.input_field_hit_search():
                self.wells.append(well)
            return self.wells


# In[13]:


proxies = CollectSatisfyProxies(url,30000,1)


# In[15]:


satify_proxies = proxies.collect_satisfy_proxies()


# In[ ]:





# In[16]:


for proxy in satify_proxies:
    


# In[ ]:




