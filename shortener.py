BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode_base62(num: int) -> str:
    if num == 0:
        return BASE62[0]
    
    result = []
    base = len(BASE62)
    
    while num > 0:
        result.append(BASE62[num % base])
        num //= base
        
    return ''.join(reversed(result))