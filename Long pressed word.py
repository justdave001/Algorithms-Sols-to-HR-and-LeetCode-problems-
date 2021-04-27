"""
          listedt = list(typed)
          setted = set(listedt)
          typedd = list(typed)
          listedagain = list(setted)
          named = list(name)
          listedname = list(name)
          counter = 0
          arr3 = []
          arr4 = []
          dict1 = {}
          dict2 = {}
          
          arr = []
          arr1 = []
          for i in range(len(typed)-1):
                if typed[i] == typed[i+1]:
                    arr3.append(i)
          for i in range(len(named)-1):
                if named[i] == named[i+1]:
                    arr4.append(i)          
          for element in sorted(arr3, reverse=True):
            del typedd[element]
          for elements in sorted(arr4, reverse = True):
            del named[elements]
          for i in name:
                if i not in arr:
                    arr.append(i)
          for i in typed:
            if i not in arr1:
                arr1.append(i)
          for i in range(len(listedagain)):
                 for j in range(len(listedname)):
                   if listedagain[i] == name[j] and typed.count(listedagain[i]) >= name.count(name[j]):
                     counter += 1
          if counter == len(name) and arr1 == arr and typedd == named:
             return True
          else:
             return False
"""
           i = 0

           for j in range(len(typed)):

            if i < len(name) and name[i] == typed[j]:

                i += 1

            elif j == 0 or typed[j] != typed[j-1]:

                return False

           return i == len(name)
        
