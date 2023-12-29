def check_cache(target, cache):
    for i in range(len(cache)):
        if target == cache[i]:
            return (True, i)
    return (False, None)

def solution(cacheSize, cities):
    answer = 0
    cities = [city.lower() for city in cities]
    cache = []
    
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer 
    
    for city in cities:
        is_hit, index = check_cache(city, cache)
        if is_hit: # cache hit
            cache.append(cache.pop(index))
            answer += 1
        else: # cache miss
            if len(cache) == cacheSize:
                del cache[0]
            cache.append(city)
            answer += 5
    
    return answer