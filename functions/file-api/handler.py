import base64

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    try:
        bytes = req.encode('ascii')
    except:
        bytes = req.encode('utf-8')

    res = base64.b64encode(bytes)
    return 10*res
