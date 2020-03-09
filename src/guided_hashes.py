import hashlib


key = b"my_value"
key2 = "string1".encode()
key3 = b"lunchtime"

index = hash(key) % 8
index2 = hash(key2) % 8
index3 = hash(key3) % 8
print(index)
print(index2)
print(index3)

# for i in range(n):
#     print(hash(key))
    # print(hashlib.sha256(key).hexdigest())
 
# for i in range(n):
#     print(hash(key)
​
# for i in range(n):
