class Validate(object):
   def LastLaddoo(self, Laddoo):
      if len(Laddoo) ==0:
         return 0
      if len(Laddoo) == 1:
         return 1
      while len(Laddoo)>1:
         Laddoo.sort()
         s1,s2=Laddoo[-1],Laddoo[-2]
         if s1==s2:
            Laddoo.pop(-1)
            Laddoo.pop(-1)
         else:
            s1 = abs(s1-s2)
            Laddoo.pop(-1)
            Laddoo[-1] = s1
      if len(Laddoo):
         return Laddoo[-1]
      return 0
vall = Validate()
Laddoo=list(map(int,input().split()))
print(vall.LastLaddoo(Laddoo))
