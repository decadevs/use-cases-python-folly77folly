# Document at least 2 use cases of generators

import requests


# A generator to provision even numbers between really large range of numbers
# def numbers_generator(start, end):
#     for item in range(start, end+1):
#         yield item

# A generator to read url contents in chunk from a website
def webpage_generator(url):
    response = requests.get(url, stream=True)
    print(response.text)
    for chunk in response.iter_content(chunk_size=512):
        yield chunk


my_gent = webpage_generator('http://')
print(next(my_gent))
