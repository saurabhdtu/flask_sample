def getFileExt(fileName):
    splits = fileName.split(".")
    return splits[len(splits) - 1]


def generate_hash(password):
    password = password + HASH_SALT_SECRET
    hashed = hashlib.md5(password.encode())
    print(hashed.hexdigest())