import json



# Write to a JSON file
data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:  
    json.dump(data, outfile)



# Read from a JSON file

with open('data.txt') as json_file:  
    data = json.load(json_file)
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')


# first non-repeating character of a string
s = 'aabccbdcbe'

data=[a for a in s if s.count(a) == 1]
print(data)

# Using generator
data=[a for a in s if s.count(a) == 1].next()













