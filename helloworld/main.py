'''
First Google Cloud function Hello World
'''
def hello_world(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return '', 204, headers

    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    request_args = request.args
    request_json = request.get_json(silent=True)
    if request_args and 'name' in request_args:
        name = request_args['name']
        if 'lastName' in request_args:
            lastName = request_args['lastName']
        else: lastName=''
    elif request_json and 'name' in request_json:
        name = request_json['name']
        if 'lastName' in request_json:
            lastName = request_json['lastName']
        else: lastName=''
    else:
        name='World'
        lastName='Nothing'

    return f'Hey {name} {lastName}', 200, headers
