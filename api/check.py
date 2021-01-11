from fastapi import Header, HTTPException
from typing import Optional
import pandas as pd
import os

class check_req(object):
	
	def __init__(self, key: Optional[str] = Header(None,  convert_underscores=False), email: Optional[str] = Header(None,  convert_underscores=False)):
		if not key or not email:
			print('Incomplet headers')
			raise HTTPException(status_code=401)
		data = pd.read_csv('./data/access.csv')
		for i in range(len(data)):
			if data.values[i][1] == email:
				if data.values[i][2] == key:
					return (None)
				else:
					print('Wrong key')
					raise HTTPException(status_code=401)		
		print('Not email key')
		raise HTTPException(status_code=401)