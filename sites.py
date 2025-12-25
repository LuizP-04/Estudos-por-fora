def click(v, a):
   if v > 1:
      return click(v-1, a*2)
   return a

n = int(input())

print(click(3, n))