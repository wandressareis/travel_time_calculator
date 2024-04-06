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
  uvicorn.run(app, host='127.0.0.1', port=8000)