# # install python package requests
# # on command line run - pip install requests
# # verify it with - pip -V
#
import requests

response_bbc = requests.get("http://www.bbc.co.uk/")
# # print(response_bbc.status_code)
# #print(response_bbc.headers)
# # print(response_bbc.content)
#
# # first iteration
# def check_response_code():
#     if response_bbc.status_code == 200:
#         return "Response successful"
#     elif response_bbc.status_code == 404:
#         return " Sorry page not found"
#     else:
#         return " Opps... something went wrong"
#
# print(check_response_code())
# # second iteration to simplify our code and make it reusable
# #
# # def check_response_code():
# #     if response_bbc.status_code == 200:
# #         print("Response successful")
# #     elif response_bbc.status_code == 404:
# #         print(" Sorry page not found")
# #     else:
# #         print(" Opps... something went wrong")
# print(check_response_code())
# #
# 3rd iteration to apply best practice

def check_response_code():

    if response_bbc.status_code:
        return "Response successful"
    elif response_bbc.status_code:
        return " Sorry page not found"
    else:
        return " Opps something went wrong"

print(check_response_code())

# requests goes one step further in simplifying this process for us.
# If you use a response_bcc instance in a conditional expression,
# It will evaluate to True if the status code was between 200 and 400, and False otherwise.
# Therefore, you can simplify the last example by rewriting the if statement as above: