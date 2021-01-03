# epic-games-store-scraper
A basic scraper to get games names from différents catégories on the epic-games store, need to have downloaded chrome browser

⋅⋅* Installation :


`git clone https://github.com/ThaaoBlues/epic-games-store-scraper`


`cd epic-games-store-scraper`


`pip install selenium chromedriver_autoinstaller`

⋅⋅* Usage exemple :
```python


#import the scraper 
from epic_games_store_scrapper import epic_games_store_scrapper

if __name__ == "main":

#init the scraper
sc = epic_games_store_scraper()


#print main page categories and their content
categories, games = sc.get_main_categories()

i = 0
for j in categories:
    print("===================\ncategory : "+j+"\n===================")
    for k in games[i]:
        print(k)
    i+=1
    
    
#print the 30 first free games sorted by release date
print("===================\nfree games available:\n===================")
for i in sc.get_free_games(page_size=30) :
    print(i)


#print the free game of the week
print("===================\nfree game of the week:\n===================")
print(sc.get_free_game_of_the_week())


#get a game by name and display his price, if the game doesn't exist the function return "This game is not in the epic-games store"
ele = sc.get_game_by_name("among us")
print("name : " + ele[0])
print("price : "+ ele[1])


#connect to your epic games account and by a free game by name
if connect_and_get_a_free_game("jurassic park","email@gmail.com","password"):
    print("Game bought !")
else:
    print("error in the process")
    
```
 
