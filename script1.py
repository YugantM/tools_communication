# sender
import json
import pandas as pd

dic = {
	'hi':'demo json'

}



#json.loads(dic)

def foo():
	f = pd.DataFrame(columns=['python','apple'],index=['python','apple']).to_json(orient='index')
	
	return f

#print(type(dic))

if __name__ == '__main__':

	#print(pd.DataFrame(columns=['python','apple'],index=['python','apple']).to_json(orient='index'))
	#print(pd.DataFrame(columns=['python','apple'],index=['python','apple']).to_json(orient='index'))
	print(foo())
	
