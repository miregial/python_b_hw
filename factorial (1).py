
def fact(n):
    if n==1:
        return 1
    return(n*fact(n-1))
#print(fact(2))
for n in range(1,10): # не посчитает т.к рэнж дает числа от 0 до 9,по условию 0 никогда не будет разлагаться до 1
 #print(fact(n))
 print(f"{n}!={fact(n)}")
