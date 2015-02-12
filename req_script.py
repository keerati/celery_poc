import requests    
import json
import sys

def req(path, n=0):
    headers  = {'content-type': 'application/json' }
    post_dict = { "test" : "req %d" % n }
    post_data = json.dumps(post_dict)
    response = requests.post(path, data=post_data, headers=headers)
    print response.text

if __name__ == '__main__':
    path = sys.argv[1]
    no_of_req = int(sys.argv[2])
    for n in xrange(no_of_req):
        req(path, n)
