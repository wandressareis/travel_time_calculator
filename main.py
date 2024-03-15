from selenium import webdriver
# from fastapi import FastAPI
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# app = FastAPI()

# @app.get("/")
class GoogleMapsCalculator:
  def __init__(self):
    self.driver = self._initialize_driver()
    self.driver.implicitly_wait(2)

  def _initialize_driver(self):
    # return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # PARA NÃO VISUALIZAR O NAVEGADOR 
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    return driver

  def tempo_total(self):
    xpath = '//div[@data-trip-index="0"]//div[contains(text(), "min")]'
    wait = WebDriverWait(self.driver, timeout=3)
    elemento_tempo = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return int(elemento_tempo.text.replace('min', ''))

  #---------------------------- FUNÇÃO PRINCIPAL ----------------------------------
  def gera_pares_distancia(self, bases_do_samu, qth):
    distancia_pares = {}

    for i, partida in enumerate(bases_do_samu):
      partida, 1
      for j, destino in enumerate(qth):
        destino, 2
        self.driver.get("https://www.google.com/maps/dir/" + partida + "/" + destino)
        tempo_par = self.tempo_total()
        distancia_pares[f'{i}_{j}'] = tempo_par

    return distancia_pares


if __name__ == '__main__':
  calculator = GoogleMapsCalculator()

  bases_do_samu = [
    "2.7978590095183815, -60.718581462488835",
    "2.805911769495148, -60.78350673463364",
    "2.840917101921869, -60.7562361692347",
    "2.766412595217544, -60.73516486248878",
    "2.8233817654294526, -60.754521208092285",
    "2.8607589873052603, -60.73611670998919"
  ]

  qth = ["2.824651572924736, -60.67060368260708"]

  distancia_pares = calculator.gera_pares_distancia(bases_do_samu, qth)

  print(distancia_pares)

  sleep(5)