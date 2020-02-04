"""Checking if website is alive"""


from website_alive import check_response


print('Enter web adress:')
URL = input()
if check_response.check_res(URL):
    print('Website is available')
else:
    print('Website is unavailable')
