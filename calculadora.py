from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleMapsCalculator:
  def __init__(self):
    self.driver = self._initialize_driver()
    self.driver.implicitly_wait(2)

  def _initialize_driver(self):
    # return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # PARA NÃO VISUALIZAR A INTERFACE DO GOOGLE MAPS 
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

    for i, base in enumerate(bases_do_samu):
      partida = base['coordenadas']  # Acessando as coordenadas da base do SAMU
      for j, destino in enumerate(qth):
        destino_coord = [float(coord) for coord in destino.split(',')]  # Convertendo as coordenadas do qth para lista de float
        self.driver.get("https://www.google.com/maps/dir/" + ','.join(map(str, partida)) + "/" + ','.join(map(str, destino_coord)))
        tempo_par = self.tempo_total()
        distancia_pares[f'{base["id"]}_{j}'] = tempo_par

    return distancia_pares
