from ninja import Router

router = Router(tags=['MyAPI'])

@router.get('/hello')
def	hello(request):
	return { 'data' : 'hello' }
