#kira bokachuda ay khane ki,,,,,,tor chudlingpong,,,,,,,vag ante

import base64 as __B, zlib as __Z, marshal as __M, types as __T, sys as __S

__X = b'eJxLzs8tKEotLkktLlFIyS9NTU4sKMlMTlKyMjIw1U8uzi9KzFeKBQA1axlP'

try:
    __D = __Z.decompress(__B.b64decode(__X))
except Exception:
    raise SystemExit("Error: Corrupted encrypted block.")

__mod = __D.decode()

try:
    __core = __import__(__mod)
except Exception as e:
    raise SystemExit("Core Import Failed: %s" % e)

for __k in ("__file__", "__loader__", "__spec__", "__cached__"):
    if hasattr(__core, __k):
        try: setattr(__core, __k, None)
        except: pass

if hasattr(__core, "main"):
    __core.main()
else:
    raise SystemExit("Error: main() not found in core")