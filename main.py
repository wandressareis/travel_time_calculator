import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calculadora import GoogleMapsCalculator

app = FastAPI()

class Inputs(BaseModel):
  bases_do_samu: list
  qth: list

@app.post("/resposta")
def resposta(inputs: Inputs):
  calculator = GoogleMapsCalculator()
  try:
    pares_tempo_percurso = calculator.gera_pares_tempo_percurso(inputs.bases_do_samu, inputs.qth)
    return pares_tempo_percurso
  except Exception as erro:
    raise HTTPException(status_code=500, detail=str(erro))

if __name__ == '__main__':
  uvicorn.run(app, port=8000)
  # calculator = GoogleMapsCalculator()

  # bases_do_samu = [
  #   {"id": 1, "coordenadas": [2.7978590095183815, -60.718581462488835]},
  #   {"id": 2, "coordenadas": [2.805911769495148, -60.78350673463364]},
  #   {"id": 3, "coordenadas": [2.840917101921869, -60.7562361692347]},
  #   {"id": 4, "coordenadas": [2.766412595217544, -60.73516486248878]},
  #   {"id": 5, "coordenadas": [2.8233817654294526, -60.754521208092285]},
  #   {"id": 6, "coordenadas": [2.8607589873052603, -60.73611670998919]}
  # ]

  # qth = [
  #   {"coordenadas": [2.824651572924736, -60.67060368260708]}
  # ]

  # pares_tempo_percurso = calculator.gera_pares_distancia(bases_do_samu, qth)

  # print(pares_tempo_percurso)