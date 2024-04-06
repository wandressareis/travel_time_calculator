from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleMapsCalculator:
  def __init__(self):
    self.driver = self._initialize_driver()
    self.driver.implicitly_wait(2)

  def _initialize_driver(self):
    try:
      # return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
      # PARA NÃO VISUALIZAR A INTERFACE DO GOOGLE MAPS 
      options = webdriver.FirefoxOptions()
      options.add_argument('-headless')
      driver = webdriver.Firefox(options=options)
      return driver
    except Exception as erro:
      print("Erro ao inicializar o driver:", erro)
      return None

  def tempo_total(self):
    try:
      xpath = '//div[@data-trip-index="0"]//div[contains(text(), "min")]'
      wait = WebDriverWait(self.driver, timeout=3)
      elemento_tempo = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
      return str(elemento_tempo.text.replace('', ''))
    except Exception as erro:
      print("Erro ao obter tempo total: ", erro)
      return None
  
  #---------------------------- FUNÇÃO PRINCIPAL ----------------------------------
  def gera_pares_tempo_percurso(self, bases_do_samu, qth):
    pares_tempo_percurso = {}

    for i, base in enumerate(bases_do_samu):
      partida = base['coordenadas']  # Acessando as coordenadas da base do SAMU
      for j, destino in enumerate(qth):
        destino_coord = [float(coord) for coord in destino.split(',')]  # Convertendo as coordenadas do qth para lista de float
        try:  
          self.driver.get("https://www.google.com/maps/dir/" + ','.join(map(str, partida)) + "/" + ','.join(map(str, destino_coord)))
          tempo_par = self.tempo_total()
          if tempo_par is not None:
            pares_tempo_percurso[f'{base["id"]}'] = tempo_par
        except Exception as erro:
          print(f"Erro ao calcular a distância entre {base['id']} e destino: {erro}")

    return pares_tempo_percurso