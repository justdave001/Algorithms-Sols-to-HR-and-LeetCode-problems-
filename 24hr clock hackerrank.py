
s = input()
def timeConversion(s):
    #
    # Write your code here.
    #
    news = s.strip(s[len(s)-2] + s[len(s)-1])
    news0 = s[len(s)-2] + s[len(s)-1]
    integers = news[0]+news[1]
    addition = int(integers)
    #variable = news.replace(integers, str(addition+12))
    if news0 == "AM" and addition<12:
       print(news)
    if news0 == "PM" and addition < 12:
        midnight = addition + 12
        variable2 = news.replace(integers, str(midnight))
        print(variable2)
    if s[0]+s[1] == "12" and news0 == "AM":
        variable1 = news.replace(integers, "00")
        print(variable1)
    if addition == 12 and news0 == "PM":
        print(news)
  
    
if __name__ == '__main__':
   timeConversion(s)
