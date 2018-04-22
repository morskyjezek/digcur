import json

with open('loc-101-kittens.json','r') as f:
    data = json.load(f)

    print(type(data))

count = 0
for result in data['results']:
    del result['digitized'], result['mime_type'],result['language'],result['other_title']
    print(result['description'])
    count = count + 1

print('Counted',count,'items')

with open('loc-101-kittens-readable-results.json','w') as f:
    json.dump(data['results'], f, indent=2)
