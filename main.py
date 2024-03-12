from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# PARA NÃO VISUALIZAR O NAVEGADOR 
# options = webdriver.FirefoxOptions()
# options.add_argument('-headless')
# driver = webdriver.Firefox(options=options)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from time import sleep

# INICIALIZANDO O DRIVER E ABRINDO O SITE DO GOOGLE MAPS
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(2) # Espera Implicita
# driver.get("https://www.google.com/maps/dir/2.8607589873052603,+-60.73611670998919/2.824651572924736,+-60.67060368260708/@2.8368347,-60.7447059,13z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d-60.7361167!2d2.860759!1m3!2m2!1d-60.6706037!2d2.8246516!3e0?entry=ttu")


def tempoTotal():
  xpath = '//div[@data-trip-index="0"]//div[contains(text(), "min")]'
  wait = WebDriverWait(driver, timeout=3)
  elemento_tempo = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
  return int(elemento_tempo.text.replace('min', '')) 

def geraParesDistancia(bases_do_samu):
  distancia_pares = {} 
  
  for i, end1 in enumerate(bases_do_samu):
    end1, 1
    for j, end2 in enumerate(qth):
      end2, 2
      driver.get("https://www.google.com/maps/dir/" + end1 + "/" + end2)
      tempo_par = tempoTotal()
      distancia_pares[f'{i}_{j}'] = tempo_par 

  return distancia_pares

if __name__ == '__main__':

  bases_do_samu = [ "2.7978590095183815, -60.718581462488835",
                    "2.805911769495148, -60.78350673463364",
                    "2.840917101921869, -60.7562361692347",
                    "2.766412595217544, -60.73516486248878",
                    "2.8233817654294526, -60.754521208092285",
                    "2.8607589873052603, -60.73611670998919" ]
  
  qth = ["2.824651572924736, -60.67060368260708"]

  distancia_pares = geraParesDistancia(bases_do_samu)

  print(distancia_pares)

  sleep(500)

# print(tempoTotal())