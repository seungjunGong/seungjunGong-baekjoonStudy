def date_to_days(date):
    y, m, d = map(int, date.split('.'))
    y = y * 12 * 28
    m = m * 28
    days = y + m + d
    return days
    
def solution(today, terms, privacies):
    answer = []
    
    period = {}
    
    for term in terms:
        t, m = term.split()
        period[t] = int(m)
    
    tdays = date_to_days(today)
    for i, priv in enumerate(privacies):
        date, term = priv.split()
        peri_days = period[term] * 28
        days = date_to_days(date)
        
        days += peri_days
        
        if tdays >= days:
            answer.append(i + 1)
            
    return answer