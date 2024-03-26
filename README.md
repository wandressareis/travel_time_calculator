## Calculador de Tempo de Percursos
Script em python que calcula o tempo de n pontos de partida até um objetivo, considerando tráfego.

### Bibliotecas:

#### Selenium: 
- Utilizada para automação: Busca, navegação e web scraping.

#### WebDriver Manager:
- API utilizada para manipulação do navegador de forma nativa.

#### FastAPI:
- Framework Python para criação de APIs REST

#### Pydantic:
- 

#### Para instalar as bibliotecas acima:

        pip install requirements.txt
#### Requisitos para a execução do programa: 
- Navegador Mozilla Firefox instalado.

#### Para executar:

        uvicorn principal:app --reload

#### Na saída há uma linha como: 
        INFO:     Uvicorn running on http://127.0.0.1:8000
##### Abra o seu navegador no endereço que aparece.

#### Para usar a API no modo interativo, digite no navegador:
        http://127.0.0.1:8000/docs 

#### JSON para teste:
    {
      "bases_do_samu": [
          {"id": 1, "coordenadas": [2.7978590095183815, -60.718581462488835]},
          {"id": 2, "coordenadas": [2.805911769495148, -60.78350673463364]},
          {"id": 3, "coordenadas": [2.840917101921869, -60.7562361692347]},
          {"id": 4, "coordenadas": [2.766412595217544, -60.73516486248878]},
          {"id": 5, "coordenadas": [2.8233817654294526, -60.754521208092285]},
          {"id": 6, "coordenadas": [2.8607589873052603, -60.73611670998919]}
      ],
      "qth": [
          "2.824651572924736, -60.67060368260708"
      ]
    }

##### Adicione o JSON ao "Request body" que aparece no modo API interativa e clique em executar.