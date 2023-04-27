import requests

api_endpoint ='https://api.openai.com/v1/chat/completions'
api_key =""


request_headers ={"Content-Type" : "application/json", "Authorization" : "Bearer " + api_key}

print(request_headers)

prompt = '''
Write HTML and Javascript code that draws a rectangle with transparent fill using fabricjs.
The canvas must be 400 by 400 pixels. The rectangle must be 50 x 100 and should be in the middle of the canvas.
The color of the canvas must be orange with an opacity of 0.5.
The stroke of the rectangle must be blue; the strokewidth of the rectangle should be 3.
Use resource: https://cdnjs.cloudflare.com/ajax/libs/fabric.js/4.5.0/fabric.min.js and set crossorigin to anonymous
'''
# prompt = "".join([p1, p2, p3, p4, p5])


request_data ={
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": prompt }],
  }

# request_data = {"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": "Hello!"}]}

response = requests.post(api_endpoint, headers = request_headers, json = request_data)

python_file ="rectangle2.html"


if response.status_code == 200:
  # print(response.json().keys())
  print(response.json()['choices'][0]['message']['content'])
  script_content = response.json()['choices'][0]['message']['content']
  with open(python_file, 'w') as f:
    f.write(script_content)
else:
  print(f"Request failed. Status code: {response.status_code}  ")

