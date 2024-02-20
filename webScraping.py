import pandas as pd
import requests

url = "https://statusinvest.com.br/category/advancedsearchresultpaginated"

querystring = {"search":"{\"Sector\":\"\",\"SubSector\":\"\",\"Segment\":\"\",\"my_range\":\"-20;100\",\"forecast\":{\"upsidedownside\":{\"Item1\":null,\"Item2\":null},\"estimatesnumber\":{\"Item1\":null,\"Item2\":null},\"revisedup\":true,\"reviseddown\":true,\"consensus\":[]},\"dy\":{\"Item1\":null,\"Item2\":null},\"p_l\":{\"Item1\":null,\"Item2\":null},\"peg_ratio\":{\"Item1\":null,\"Item2\":null},\"p_vp\":{\"Item1\":null,\"Item2\":null},\"p_ativo\":{\"Item1\":null,\"Item2\":null},\"margembruta\":{\"Item1\":null,\"Item2\":null},\"margemebit\":{\"Item1\":null,\"Item2\":null},\"margemliquida\":{\"Item1\":null,\"Item2\":null},\"p_ebit\":{\"Item1\":null,\"Item2\":null},\"ev_ebit\":{\"Item1\":null,\"Item2\":null},\"dividaliquidaebit\":{\"Item1\":null,\"Item2\":null},\"dividaliquidapatrimonioliquido\":{\"Item1\":null,\"Item2\":null},\"p_sr\":{\"Item1\":null,\"Item2\":null},\"p_capitalgiro\":{\"Item1\":null,\"Item2\":null},\"p_ativocirculante\":{\"Item1\":null,\"Item2\":null},\"roe\":{\"Item1\":null,\"Item2\":null},\"roic\":{\"Item1\":null,\"Item2\":null},\"roa\":{\"Item1\":null,\"Item2\":null},\"liquidezcorrente\":{\"Item1\":null,\"Item2\":null},\"pl_ativo\":{\"Item1\":null,\"Item2\":null},\"passivo_ativo\":{\"Item1\":null,\"Item2\":null},\"giroativos\":{\"Item1\":null,\"Item2\":null},\"receitas_cagr5\":{\"Item1\":null,\"Item2\":null},\"lucros_cagr5\":{\"Item1\":null,\"Item2\":null},\"liquidezmediadiaria\":{\"Item1\":null,\"Item2\":null},\"vpa\":{\"Item1\":null,\"Item2\":null},\"lpa\":{\"Item1\":null,\"Item2\":null},\"valormercado\":{\"Item1\":null,\"Item2\":null}}","orderColumn":"","isAsc":"","page":"0","take":"15","CategoryType":"1"}

payload = ""
headers = {
    "cookie": "suno_checkout_userid=73f2efe8-0260-4379-a19d-44137429473f; _adasys=31446aac-ee0f-4e4a-99ef-41c4d3a94cab; _gcl_au=1.1.2020741719.1708356656; .StatusAdThin=1; _fbp=fb.2.1708356656639.335439645; _ga=GA1.1.119893359.1708356657; _clck=15d3n3w%7C2%7Cfje%7C0%7C1510; G_ENABLED_IDPS=google; __hstc=176625274.a2e339dc7d66220ab9a613cc8720a22c.1708356663955.1708356663955.1708356663955.1; hubspotutk=a2e339dc7d66220ab9a613cc8720a22c; __hssrc=1; G_AUTHUSER_H=0; .StatusInvest=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJBY2NvdW50SWQiOiIxMDg2NjciLCJOYW1lIjoiR3VzdGF2byBNYWNpZWwiLCJFbWFpbCI6ImNhc3Ryb21hY2llbDE3QGdtYWlsLmNvbSIsIkludGVyZmFjZVR5cGUiOiJXZWIiLCJJcCI6Ijo6ZmZmZjoxMC4xMDAuMTMuMTM5IiwibmJmIjoxNzA4MzU2NjY0LCJleHAiOjE3MDg0NDMwNjQsImlhdCI6MTcwODM1NjY2NCwiaXNzIjoiU3RhdHVzSW52ZXN0IiwiYXVkIjoiU3RhdHVzSW52ZXN0In0.0_JcM9SMU9-XbJlnZXatWAC89GwqDPzoPnkxCUBw6rsbbSsiWeQT5nCrSEIxmTH_vrmHKleDalY-OoSWVOc1Kw; messagesUtk=0b2d813ac9704dfca15b85d754febb9c; _hjSessionUser_1931042=eyJpZCI6ImI5NGVmYWRhLWRhNjYtNTgxYS04MmQwLWFiNTJiYWQzNzI1YSIsImNyZWF0ZWQiOjE3MDgzNTY2NTY5MDgsImV4aXN0aW5nIjp0cnVlfQ==; _clsk=18wsffm%7C1708356852122%7C4%7C1%7Cy.clarity.ms%2Fcollect; _ga_69GS6KP6TJ=GS1.1.1708356656.1.1.1708356907.60.0.0; SLG_G_WPT_TO=pt; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; cf_clearance=s45HnuSPOu9sL_rQ5S2_K2yLNinIdZyuD2DM4qdF.Hk-1708392827-1.0-ASvGsuxWnjPywP/8evXJzwDDq1m93oXEXT689/oQUaSbR5zGEld8BmVcEzW6HsDBcpAMjh/qW7XRX79wUtNaZG0=",
    "authority": "statusinvest.com.br",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "referer": "https://statusinvest.com.br/acoes/busca-avancada",
    "sec-ch-ua": "'Not A(Brand;v=99, Opera GX;v=107, Chromium;v=121)'",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}


response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

json_res = response.json()

lista=[]

for i in json_res:
    lista.append(i)

df = pd.json_normalize(lista)
df = pd.DataFrame(df)
df.to_csv("Ações.csv", encoding='utf-8', index=False, sep=';', decimal=',')