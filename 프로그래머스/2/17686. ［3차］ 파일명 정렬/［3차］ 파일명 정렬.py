def solution(files):
    dict_files = []
    # 딕셔너리로 분리해 구분하기
    for file in files:
        # NUMBER 첫번째 idx 찾기
        start = 0
        while not file[start].isdigit():
            start += 1

        # NUMBER 마자믹 idx 찾기
        end = start
        while end < len(file) and file[end].isdigit():
            end += 1
                    
        head = file[:start]
        number = file[start:end]
        tail = file[end:]
            
        dict_file = {'head':head, 'number':number, 'tail':tail}
        
        dict_files.append(dict_file)
        
    # HEAD 사전순 정렬하기
    dict_files.sort(key = lambda x: (x['head'].lower(), int(x['number'])))
    
    answer = ["".join(dic_file.values()) for dic_file in dict_files]
        
    return answer