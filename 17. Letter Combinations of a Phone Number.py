#Input: digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

#進階可用DFS


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits)==0:
            return []

        dict={2:"abc",3:"def",4:"ghi",5:"jkl",
        6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

        result=[""]

        for ele in digits:
            tmp=[]
            #取出digits的數字轉成int
            for cha in dict[int(ele)]:
                for string in result:
                    tmp.append(string+cha)
            result = tmp
        return result














