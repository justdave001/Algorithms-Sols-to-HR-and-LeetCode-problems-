class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicted = {}
        for i in strs:
           sortedd = ''.join(sorted(i))  
           if sortedd not in dicted:
                dicted[sortedd] = [i]
           elif sortedd in dicted:
            dicted[sortedd].append(i)
        arr = []
        for values in dicted:
            
            arr.append(dicted[values])
        return arr
        
