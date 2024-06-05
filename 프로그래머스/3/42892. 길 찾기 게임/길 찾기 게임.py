# 문풀 실패(24-06-05)
import sys
sys.setrecursionlimit(10**6)    # 재귀함수 리밋 해제

# info ([x, y], 인덱스)
class Node:
    def __init__(self, info):
        self.x = info[0][0]
        self.data = info[1]
        self.left = None
        self.right = None
        
# 노드와 삽입할 정보를 입력 받는다.
def insert(node, info):
    if node is None:    # 새 노드 삽입
        return Node(info)
    if info[0][0] < node.x: # x 좌표로 비교
        node.left = insert(node.left, info)
    else:
        node.right = insert(node.right, info)
    return node

# 이진 탐색트리 만들기
def make_tree(nodeinfo):
    # (x, y) + 인덱스 nodes 리스트 생성
    nodes = []
    for i, node in enumerate(nodeinfo, start=1):
        nodes.append((node, i))
    
    nodes.sort(key=lambda x: x[0][0]) # x 좌표 정렬
    nodes.sort(key=lambda x: x[0][1], reverse=True) # y 좌표 정렬
    
    # nodes 를 돌면서 이진 탐색 트리 만들기
    root = None
    for node in nodes:
        root = insert(root, node)
    return root

# 전위 순회
def preorder(root):
    def _preorder(node): # 재귀
        if node:
            res.append(node.data)
            _preorder(node.left)
            _preorder(node.right)
    res = []
    _preorder(root)
    return res 

# 후위 순회
def postorder(root):
    def _postorder(node): # 재귀
        if node:
            _postorder(node.left)
            _postorder(node.right)            
            res.append(node.data)
    res = []
    _postorder(root)
    return res 

def solution(nodeinfo):
    answer = []
    root = make_tree(nodeinfo)
    answer.append(preorder(root))
    answer.append(postorder(root))
    
    return answer