"""

"""

import hashlib

data = input()
encodedData = data.encode()

result = hashlib.sha256(encodedData).hexdigest()
print(result)