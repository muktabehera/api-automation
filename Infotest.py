print("What is swagger?")
print("The World's Most Popular API Tooling. Swagger is a specification and complete framework implementation for describing, producing, consuming, and visualizing RESTful web services.")
print("https://github.com/digium/swagger-py")
print("Swagger.py is a Python library for using Swagger defined API's")

#import webbrowser
#webbrowser.get(using="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s").open("http://172.30.4.216/content/apidocs/index.html")
#webbrowser.open('http://172.30.4.216/content/apidocs/index.html')

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://172.30.4.216/content/apidocs/index.html")
elem = driver.find_element_by_id("input_apiKey")
elem.clear()
elem.send_keys("eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkZWZhdWx0Iiwic3ViIjoiYWRtaW5AMTcyLjMwLjQuMjE2LmNvbSIsImF1ZCI6InFlZDpkZWZhdWx0IiwicWVkcCI6WyJzIiwiYyIsImciLCJwIiwiZCIsIm0iLCJhIl19.3NzYb3lS8W3WMNBDRS0q5Zoh3pZJxWRUaXjvyszEsvs")
elem2 = driver.find_element_by_id("explore")
elem2.click()






