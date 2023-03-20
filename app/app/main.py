from fastapi import FastAPI

api = FastAPI()

@api.get('/test')
async def hello():
	data = {
		'message' : 'new'
	}
	return data
