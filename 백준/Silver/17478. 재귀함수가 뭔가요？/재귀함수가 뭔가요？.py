def fun(count, n, recursion):
    if count != n:
        for line in recursion:
            print(f"{'____' * count}{line}") # 악! 언더바였음..
        return fun(count+1,n, recursion) # 반복횟수를 충족하지 않으면 한번 더 카운팅
    elif count == n:
        print(f"{'____' * count}\"재귀함수가 뭔가요?\"")
        print(f"{'____' * count}\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        for time in range(count,-1,-1):
            print(f"{'____' * time}라고 답변하였지.")
        
        
n = int(input())
count = 1
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
what_is_recursion = '''"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'''
print(what_is_recursion)
what_is_recursion = what_is_recursion.split("\n")
fun(count, n, what_is_recursion)