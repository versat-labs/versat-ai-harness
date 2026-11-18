def charge(seen, key, amount):
    if not key or amount <= 0:
        raise ValueError("key and positive amount required")
    if key in seen:
        return False
    seen.add(key)
    return True
