def MurmurHash2_32bits(key: bytes, seed: int =0x9747b28c) -> int:
    key = key
    seed = seed

    m = 0x5bd1e995
    r = 24
    h = seed ^ len(key)

    for i in range(0, len(key) // 4):
        k = int.from_bytes(key[i*4:(i+1)*4], byteorder='little')
        k *= m
        k ^= k >> r
        k *= m

        h *= m
        h ^= k
    
    tail = key[(len(key) // 4) * 4:]
    if len(tail) >= 3:
        h ^= tail[2] << 16
    if len(tail) >= 2:
        h ^= tail[1] << 8
    if len(tail) >= 1:
        h ^= tail[0]
        h = (h * m) & 0xFFFFFFFF

    # Mix final
    h ^= h >> 13
    h = (h * m) & 0xFFFFFFFF
    h ^= h >> 15

    return h