from selenium import webdriver
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class epic_games_store_scraper():
    
    def __init__(self):
        chromedriver_autoinstaller.install()


        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("window-size=1920,1080")
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.epicgames.com/store/fr/")

    #list main categories
    def get_main_categories(self):
        '''
        return a list containing the categories names and a list containing the highlighted games sublisted by category 
        
        '''
        cat = []
        cat_games = []
        ele = self.driver.find_elements_by_class_name("css-1v0ifgl-ModuleHeading__smallTitle")
        s=0
        for i1 in ele:

            if "nouvelles sorties" in str(i1.text).lower():
                s += 2

            if "fortnite" in str(i1.text).lower():
                continue
                
            if "saison" in str(i1.text).lower():
                continue
            
            if "soldes" in str(i1.text).lower():
                continue

            if "catalogue" in str(i1.text).lower():
                continue

            cat.append(i1.text)
            ele = self.driver.find_elements_by_class_name("css-2ucwu")
            sub_cat = []
            for i2 in range(s,s+5):
                sub_cat.append(ele[i2].text)
            s = s+5
            cat_games.append(sub_cat)

        return cat, cat_games

    def get_free_games(self,page_size=100):
        '''
        return a list of all the free games availables sorted by release date
        '''
        self.driver.get(f"https://www.epicgames.com/store/fr/browse?sortBy=releaseDate&sortDir=DESC&priceTier=tierFree&pageSize={str(page_size)}")
        sleep(5)
        self.driver.find_element_by_xpath("//*[contains(text(), 'Gratuit')]").click()
        sleep(5)
        ele = self.driver.find_elements_by_class_name("css-2ucwu")
        cat = []
        for i in ele:
            cat.append(i.text)
        return cat

    def get_free_game_of_the_week(self):
        '''
        return the free game of the week
        '''
        self.driver.get("https://www.epicgames.com/store/fr/browse?sortBy=releaseDate&sortDir=DESC&priceTier=tierFree&pageSize=30")
        sleep(5)
        return self.driver.find_element_by_class_name("css-2ucwu").text

    def get_game_by_name(self,name):
        '''
        return the game name, the developpement studio and price if the game exist, 
        else return \"This game is not in the epic-games store\"
        '''
        self.driver.get("https://www.epicgames.com/store/fr/")
        sleep(5)
        self.driver.find_element_by_id("searchInput").send_keys(name)
        self.driver.find_element_by_id("searchInput").send_keys(Keys.RETURN)
        sleep(3)
        try :
            info = []
            ele = self.driver.find_element_by_class_name("css-2ucwu")
            info.append(ele.text)
            ele = self.driver.find_element_by_class_name("css-r6gfjb-PurchasePrice__priceContainer")
            info.append(ele.text)
            ele =  self.driver.find_element_by_class_name("css-657o8l-StoreOfferTitleInfo__ellipsis")
            info.append(ele.text)
            return info
        except:
            return ["This game is not in the epic-games store",""]

    def connect_and_get_a_free_game(self,game,email,password)
        '''
        connect to your epic games account and buy a free game for you by credit card only
        return True if the operation has succeed and False if not
        '''
        #find game by name
        self.driver.get("https://www.epicgames.com/store/fr/")
        sleep(5)
        self.driver.find_element_by_id("searchInput").send_keys(name)
        self.driver.find_element_by_id("searchInput").send_keys(Keys.RETURN)
        sleep(3)
        self.driver.find_element_by_class("css-1lozana").click()
        sleep(5)
        self.driver.find_element_by_class("css-zyz3yg").click()
        self.driver.find_element_by_id("login-with-epic").click()

        #write username
        ele = self.driver.find_element_by_id("email")
        ele.click()
        ele.send_keys(username)
        #write password
        ele = self.driver.find_element_by_id("password")
        ele.click()
        ele.send_keys(password)
        #disable rembember-me
        ele = self.driver.find_element_by_id("rememberMe")
        ele.click()
        #connect
        ele = self.driver.find_element_by_class("MuiButton-label")
        ele.click()
        sleep(5)
        #buy game
        ele = self.driver.find_element_by_class("css-14rsasn")
        ele.click()
        sleep(3)
        #confirm
        self.driver.find_element_by_xpath("//*[contains(text(), 'Paiement')]").click()
        sleep(5)
        return True


