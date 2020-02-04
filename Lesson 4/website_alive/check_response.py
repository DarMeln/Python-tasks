"""Get a response from make_request"""


from website_alive import make_request


def check_res(website):
    response = make_request.make_req(website)
    return bool(response.status_code == 200)
