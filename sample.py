import requests, json

url= "https://api.escuelajs.co/api/v1/categories"
response= requests.get(url)
categories= json.loads(response.content)
for category in categories:
    product_url= f"https://api.escuelajs.co/api/v1/products/?categoryId={category['id']}"
    product_response= requests.get(product_url)
    products= json.loads(product_response.content)
    for product in products:
        print(product) 