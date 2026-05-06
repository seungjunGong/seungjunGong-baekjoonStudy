def solution(data, ext, val_ext, sort_by):
    index_map = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }
    
    ext_idx = index_map[ext]
    sort_idx = index_map[sort_by]
    
    filtered_data = []
    
    for item in data:
        if item[ext_idx] < val_ext:
            filtered_data.append(item)
    
    filtered_data.sort(key=lambda x: x[sort_idx])
    
    return filtered_data