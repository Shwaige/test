import base64

en_str = base64.b64encode(b'123456')


s2 = bytes.decode(en_str)
s3 = en_str.decode()
print(s3)
