## Calculador de Tempo de Percursos
API em Python que calcula o tempo de n pontos de partida até um objetivo, considerando tráfego. Projeto originalmente realizado para efetuar a captura de tempo de percurso e distância das bases do SAMU até um ponto de ocorrência e, a partir destes dados, obter insights de melhor trajeto de forma a contribuir com a agilidade do serviço de saúde de emergência. O programa, efetivamente, é uma automação que realiza buscas de endereços no Google Maps e captura o tempo de deslocamento de um ponto ao outro.

### Bibliotecas:

#### Selenium: 
- Utilizada para automação: Busca, navegação e web scraping.

#### WebDriver Manager:
- API utilizada para manipulação do navegador de forma nativa.

#### FastAPI:
- Framework Python para criação de APIs REST

#### Pydantic:
-  Uma biblioteca para tipagem estática de dados Python. Utilizado para definir o modelo de entrada esperado pela API.

#### Uvicorn:
- Servidor ASGI. É usado para executar o app FastAPI. 

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
          {"id": 2, "coordenadas": [2.4419088075792965, -60.91876568947235]},
          {"id": 3, "coordenadas": [2.164913408340161, -61.04689836849074]},
          {"id": 4, "coordenadas": [2.766412595217544, -60.73516486248878]},
          {"id": 5, "coordenadas": [4.348585615593088, -61.141598892426686]},
          {"id": 6, "coordenadas": [2.8607589873052603, -60.73611670998919]}
      ],
      "qth": [
          "2.824651572924736, -60.67060368260708"
      ]
    }

##### Adicione o JSON ao "Request body" que aparece no modo API interativa e clique em executar.