from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options

import time

class GoogleMapsCalculator:
  def __init__(self):
    start_time = time.time()
    
    self.driver = self._initialize_driver()
    #self.driver.implicitly_wait(2)
    print("start drive: ", time.time() - start_time)

  def _initialize_driver(self):

    try:
      # Create Firefox Profile to disable images
      # Create Firefox Options
      options = Options()
      options.headless = True  # Run in headless mode
      options.add_argument("--headless")

      # Set preferences directly through options
      options.set_preference("permissions.default.image", 2)  # Disable images
      options.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")  # Disable Flash
      options.set_preference("permissions.default.stylesheet", 2)  # Disable CSS

      # Reduce the page load strategy
      options.page_load_strategy = 'eager'  # 'eager' means DOMContentLoaded

      # Initialize the WebDriver with options
      driver = webdriver.Firefox(options=options)

      return driver
    except Exception as erro:
      print("Erro ao inicializar o driver:", erro)
      return None

  def tempo_total(self):
    start_time = time.time()
    try:
      xpath = '//div[@data-trip-index="0"]//div[contains(text(), "min")]'
      wait = WebDriverWait(self.driver, timeout=3)
      elemento_tempo = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
      print("tempo_total: ", time.time() - start_time)
      return str(elemento_tempo.text)
    except Exception as erro:
      print("Erro ao obter tempo total: ", erro)
      return None
  
  #---------------------------- FUNÇÃO PRINCIPAL ----------------------------------
  def gera_pares_tempo_percurso(self, bases_do_samu, qth):
    start_time = time.time()
    pares_tempo_percurso = {}

    try:
      for i, base in enumerate(bases_do_samu):
        partida = base['coordenadas']  # Acessando as coordenadas da base do SAMU
        for j, destino in enumerate(qth):
          destino_coord = [float(coord) for coord in destino.split(',')]  # Convertendo as coordenadas do qth para lista de float
          try: 
            
            get_start_time = time.time()
            self.driver.get("https://www.google.com/maps/dir/" + ','.join(map(str, partida)) + "/" + ','.join(map(str, destino_coord)))
            print("get duration: ", time.time() - get_start_time)
            tempo_par = self.tempo_total()
            if tempo_par is not None:
              pares_tempo_percurso[int(base["id"])] = tempo_par
          except Exception as erro:
            print(f"Erro ao calcular a distância entre {base['id']} e destino: {erro}")
    finally:
      if self.driver:
        self.driver.quit()
    print(time.time() - start_time)
    return pares_tempo_percurso