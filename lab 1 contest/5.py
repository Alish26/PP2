class rectangl:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def sq(self):
      return self.a*self.b

x = rectangl(3,4)
print(x.sq())