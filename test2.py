code = """
var test = 5;

console.log(test);


"""

import requests
import json

url = "https://minify.minifier.org/"
data = {
    'source': code,
    'type': 'js'
}

# response = requests.post(url, data=json.dumps(data))
response = requests.post(url, data=data)

response_data = json.loads(response.text)

original_size = response_data['sizes']['original']
minified_size = response_data['sizes']['minified']

print "Today you saved: {} characters!".format(original_size - minified_size)

# position_sizes = response_str.find('sizes')
# original_size_location = position_sizes + 15
# original_size_str = response_str[original_size_location: original_size_location + 2]
# original_size = int(original_size_str)
