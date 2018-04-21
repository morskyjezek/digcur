import requests
import json

#create variables to construct a REST API call; we could use these later to make this more reusable using input() or command line tags
endpoint = 'https://loc.gov/photos/'
q = input('Type your query here: ')
fo = 'json'
c = 101

#construct & check our request ("call") to the API 
APIcall = endpoint+'?'+'q='+q+'&fo='+fo+'&c='+str(c)
print('You requested: ',APIcall)

#send response
response = requests.get(APIcall).content

#use commented-out lines below for checking: get the headers of the response in a dictionary, print headers, print response
#headers = requests.get(APIcall).headers
#print(headers)
#print(response)

#load the json response into a python object 
data = json.loads(response)
#commented-out line below can be used to check if you got all the results
#print(len(data['results']))

#write the results out to a clean json file
with open('kittens.json','w') as f:
    json.dump(data['results'], f, indent=2)