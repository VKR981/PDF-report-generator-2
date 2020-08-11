from selenium import webdriver
import json, base64

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=options)

class htmlpdfgenerator:


    def send_devtools(self,driver, cmd, params={}):
        resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
        url = driver.command_executor._url + resource
        body = json.dumps({'cmd': cmd, 'params': params})
        response = driver.command_executor._request('POST', url, body)
        
        return response.get('value')

    def save_as_pdf(self,driver, path, options={}):    
        # https://timvdlippe.github.io/devtools-protocol/tot/Page#method-printToPDF
        result = self.send_devtools(driver, "Page.printToPDF", options)
        with open(path, 'wb') as file:
            print(path)
            file.write(base64.b64decode(result['data']))

    def convert_to_pdf(self,url,location):
        driver.get(url)
        self.save_as_pdf(driver, location, { 'landscape': False, 'printBackground': True,'paperWidth':11.7, 'paperHeight':16.5, 'pageRanges':'1-1' })




