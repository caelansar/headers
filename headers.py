header = '''
accept-ranges: bytes
age: 551803
alt-svc: hq=":443"; ma=2592000; quic=51303432; quic=51303431; quic=51303339; quic=51303335,quic=":443"; ma=2592000; v="42,41,39,35"
cache-control: public, max-age=31536000
content-length: 7325
content-type: image/png
date: Tue, 10 Apr 2018 02:55:52 GMT
expires: Wed, 10 Apr 2019 02:55:52 GMT
last-modified: Mon, 12 Dec 2016 14:45:00 GMT
server: sffe
status: 200
vary: Origin
x-content-type-options: nosniff
x-xss-protection: 1; mode=block
'''


def plain_to_dict(header, sign=None):
    l = header.split('\n')
    to_dict = {}
    keys = []
    values = []
    for item in l:
        if item == '':
            pass
        else:
            if sign:
                item = item.replace(sign, '', 1)
            keys.append(item.split(maxsplit=1)[0])
            values.append(item.split(maxsplit=1)[1])

    for k, v in zip(keys, values):
        to_dict[k] = v

    return to_dict

if __name__ == '__main__':

    print(plain_to_dict(header))
