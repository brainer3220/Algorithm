import numpy as np

def solution(arr1, arr2):
    # answer = []
    
    answer = type(np.array(arr1) + np.array(arr2))
    print(answer)
    
    # for i in range(len(arr1)): 
    #     tmp=[] 
    #     for j in range(len(arr1[i])): 
    #         tmp.append(arr1[i][j]+arr2[i][j]) 
    #         answer.append(tmp)

    
    # print(arr1, arr2)
    
    # for i in arr1:
        
    # answer = [[]]
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

solution(arr1, arr2)