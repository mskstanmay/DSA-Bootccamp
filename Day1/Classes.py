class Cookie:
    def __init__(self,color):
        self.color = color
    def getColor(self):
        return self.color
    def setColor(self,color):
        self.color = color

green_cookie = Cookie("green")
blue_cookie = Cookie("blue")

print(green_cookie.getColor(), id(green_cookie))
green_cookie.setColor("blue")
print(green_cookie.getColor(),id(blue_cookie))
print(id(green_cookie),id(blue_cookie))
