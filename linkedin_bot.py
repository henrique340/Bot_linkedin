from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://br.linkedin.com')
usuario = driver.find_element(By.ID, 'session_key')
senha = driver.find_element(By.ID, 'session_password')
usuario.send_keys('Henriqueyuji8@gmail.com')
senha.send_keys('Henriqueyuji123')
login_tentativa = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
login_tentativa.click()
elem_input = driver.find_element(By.XPATH,'//*[@id="global-nav-typeahead"]/input')
elem_input.click()
elem_input.send_keys('programador')
elem_input.send_keys(Keys.ENTER)
pessoas = driver.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[3]/button')
pessoas.click()
mensagem = driver.find_element(By.CLASS_NAME, 'artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view')
mensagem.click()
sleep(8)
driver.quit()
