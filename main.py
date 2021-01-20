from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
import pandas as pd

df = pd.read_csv("dataframes/musicas.csv")
dfFilmes = pd.read_csv("dataframes/filmesTOP.csv")
# print(df.sample(1))
app = FastAPI()


@app.get("/git/")
async def redireciona():
    return RedirectResponse("https://github.com/RAS-UFPB")


@app.get("/music/")
async def randomMusic():
    musica = df.sample(1)
    return musica.to_json(orient='index')


@app.get("/movie/")
async def randomMovie():
    movie = dfFilmes.sample(1)
    return movie.to_json(orient='index')
