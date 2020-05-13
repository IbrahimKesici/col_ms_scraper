import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent # Will keep real user agents database updated
"""
class Url():
    def __init__(self, base_url):
        self.base_url = base_url
 
    def get_base_url(self):
        return self.base_url

    def get_full_url(self, href):
        return self.url + href
"""
class Webpage():

    def __init__(self):
        pass

    @staticmethod
    def get_source_code(url):
        #try:
        #    user_agent = UserAgent(cache=False)
        #except FakeUserAgentError:
        #    print("""ERROR - Unable to create fake user agent, it will default to
        #    'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'""")
            #logger.critical("""Unable to create fake user agent, it will default to
            #'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'""")
        #    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
        
        #for counter in range(0,10):
            #headers = {"User-Agent": user_agent.random,
            #        "referer": url}
        data = requests.get(url) 
            #if data.status_code == 403 and not isinstance(user_agent, str):
            #    print(f"Attempt #{counter} Access forbiden with this headers {headers}")
                # logger.warning(f"Attempt #{counter} Access forbiden with this headers {headers}")
        if data.status_code != 200:
            print(f"Error code {data.status_code}")
            # logger.critical(f"Error code {data.status_code}")
            # raise ResponseException(data.status_code)
            #break
            
            # elif url != data.url:
            #     break
            # else:
            #     return BeautifulSoup(data.content, 'html.parser')
            #     break
        return BeautifulSoup(data.content, 'html.parser')
        
    @staticmethod
    def get_element(soup, tag, selector="", selector_name=""):
        elements = []
        for element in soup.find_all(tag, {selector:selector_name}): 
            elements.append(element)

        if len(elements) == 1:
            return elements[0]
        return elements

