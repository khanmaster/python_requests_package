import requests

response_chucknorris = requests.get("https://api.chucknorris.io/jokes/random")
response_chucknorris_category = requests.get("https://api.chucknorris.io/jokes/categories")
response_chucknorris_category_dev = requests.get("https://api.chucknorris.io/jokes/random?category={['dev]'}")

print(response_chucknorris.status_code)
if response_chucknorris.status_code:
    return " response success "
elif response_chucknorris.status_code:
    return "OPPs sorry - better luck next time"
else:
    print(" The site is offline TODAY - please try later")

# if response_chucknorris.status_code == 200:
#     print(" response success ")
# elif response_chucknorris.status_code == 400:
#     print("OPPs sorry - better luck next time")
# else:
#     print(" The site is offline TODAY - please try later")
# #print(response_chucknorris_category.content)
#print(response_chucknorris_category_dev)