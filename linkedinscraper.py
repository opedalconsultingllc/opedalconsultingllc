# TO DO:

# add the bin bash line above
# create bash script that activates the virtual environment
# create cron job that activates the bash script or Airflow or both
# create data base table


from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
firefoxOptions = Options()
firefoxOptions.add_argument("-headless")
browser = webdriver.Firefox(executable_path='./drivers/geckodriver', options=firefoxOptions)
# browser.get("https://www.google.ro/?safe=active&ssui=on")
# browser.get('https://www.linuxhint.com')

link_city = 'https://www.linkedin.com/jobs/programmer-jobs-greater-seattle-area'


link = 'https://www.linkedin.com/jobs/search?keywords=programmer&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
safe = '/?safe=active&ssui=on'
browser.get(link_city+safe)


print('Title:: %s' %browser.title)
browser.quit() 
