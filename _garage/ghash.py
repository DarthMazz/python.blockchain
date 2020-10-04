import hashlib


h = hashlib.sha256()
h.update(b"python")
print(h.hexdigest())


dat = "python"
print(hashlib.sha256(dat.encode()).hexdigest())
print(hashlib.sha256(b'python').hexdigest())
