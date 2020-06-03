## python packages
### pip - requests

- install python package requests
- on command line run - ``` pip install requests ```
- verify it with - ``` pip -V ```
```python
import requests

response_bbc = requests.get("http://www.bbc.co.uk/")


print(response_bbc.status_code)
print(response_bbc.headers)
print(response_bbc.content)
```
- second iteration to simplify our code and make it reusable

```python

def check_response_code():
    if response_bbc.status_code == 200:
        print("Response successful")
    elif response_bbc.status_code == 404:
        print(" Sorry page not found")
    else:
        print(" Opps some went wrong")
print(check_response_code())

```

- 3rd iteration to apply best practice
```python

def check_response_code():

    if response_bbc:
        print("Response successful")
    elif response_bbc:
        print(" Sorry page not found")
    else:
        print(" Opps some went wrong")

print(check_response_code())

```
- requests goes one step further in simplifying this process for us.
- If you use a request_bcc instance in a conditional expression,
- it will evaluate to True if the status code was between 200 and 400, and False otherwise.
- Therefore, you can simplify the last example by rewriting the if statement as above:

# Amazing!!!