import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from app import GoogleMapsCalculator

app  = FastAPI()

class Inputs(BaseModel):
  bases_do_samu: list
  qth: list

@app.post("/resposta")
def resposta(inputs: Inputs):
  calculator = GoogleMapsCalculator()
  distancia_pares = calculator.gera_pares_distancia(inputs.bases_do_samu, inputs.qth)
  return distancia_pares


if __name__ == '__main__':
  uvicorn.run(app, port=8000)
  # calculator = GoogleMapsCalculator()

  # bases_do_samu = [
  #   "2.7978590095183815, -60.718581462488835",
  #   "2.805911769495148, -60.78350673463364",
  #   "2.840917101921869, -60.7562361692347",
  #   "2.766412595217544, -60.73516486248878",
  #   "2.8233817654294526, -60.754521208092285",
  #   "2.8607589873052603, -60.73611670998919"
  # ]

  # qth = ["2.824651572924736, -60.67060368260708"]

  # distancia_pares = calculator.gera_pares_distancia(bases_do_samu, qth)

  # print(distancia_pares)