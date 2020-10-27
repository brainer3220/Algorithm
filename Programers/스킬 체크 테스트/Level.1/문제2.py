def solution(s):
    if len(s) % 2 != 0:
        tmp = int((len(s)/2)-1+0.5)
        # answer = tmp
        answer = s[tmp:-tmp]
    else:
        tmp = int((len(s)/2)-1)
        # answer = tmp
        answer = s[tmp:-tmp]
        
    return answer