## Travel Time Calculator
Python API that calculates the travel time from multiple starting points to a destination, considering traffic conditions. This project was developed to capture travel time and distance from SAMU bases to an incident location, and from this data, gain insights for the best route to improve the agility of the emergency health service. The program essentially automates address searches on Google Maps and captures the travel time from one point to another.

### Libraries:

#### Selenium: 
- Used for automation: Searching, navigating, and web scraping.

#### WebDriver Manager:
- API used to handle the browser natively.

#### FastAPI:
- Python framework for creating REST APIs.

#### Pydantic:
- A library for static data typing in Python. Used to define the expected input model for the API.

#### Uvicorn:
- ASGI server. Used to run the FastAPI app.

#### To install the above libraries:

```sh
pip install requirements.txt
```
#### Requirements to run the program: 
- Mozilla Firefox browser installed

#### To run:
```sh
uvicorn main:app     
```
#### The output includes a line like:
```sh
INFO:     Uvicorn running on http://127.0.0.1:8000
```
##### Open your browser at the address that appears.

#### To use the API interactively, type in your browser:
```sh
http://127.0.0.1:8000/docs 
```

#### Test JSON:
```sh
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
```

##### Add the JSON to the "Request body" that appears in the interactive API mode and click execute.
