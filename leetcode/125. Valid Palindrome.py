class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        
        for i in s : 
            if i.isalnum() : 
                temp.append(i.lower())
        answer = True
        for i in range(int(len(temp) / 2)) : 
            if temp[i] == temp[-1-i] :
                pass
            else : 
                answer = False
                break       
        
        return answer