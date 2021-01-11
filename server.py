from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
import pandas as pd

from api.check import check_req

app = FastAPI()

@app.post('/')
async def post(request: Request, check_req = Depends(check_req)):
	try:
		form = dict(await request.form())
		if 'email' not in form:
			raise HTTPException(status_code=401, detail='Incomplet form, missing email')
		data = pd.read_csv('data/users.csv')
		tmp = {}
		for i in range(len(data)):
			if data.values[i][1].replace(' ', '').lower() == form['email'].lower():
				tmp['id'] = data.values[i][0]
				tmp['email'] = data.values[i][1].replace(' ', '')
				break
		return JSONResponse({'res': True, 'data': tmp})
	except Exception as e:
		print(e)
		raise HTTPException(status_code=401)