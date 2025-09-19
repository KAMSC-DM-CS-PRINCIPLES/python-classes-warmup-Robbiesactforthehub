class PythagoreanTheorem:
    def __init__(self,A,B):
        self.A=A
        self.B=B
    def hypotenuse(self):
        return math.sqrt(self.A**2+self.B**2)
    
    