
""""""
"""
    이런 Hash 알고리즘을 불러올 수 있다고 한다 
"""

import hashlib

data = input()
encodedData = data.encode()

result = hashlib.sha256(encodedData).hexdigest()
print(result)