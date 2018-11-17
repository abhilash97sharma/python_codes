class myclass:
    i = 0  # when we declare a variable here it will be treated as global.

    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city
        myclass.i = myclass.i + 1

    def myfun(self,str):
        print('You entered a',str)


if __name__ == "__main__":
    print('In the main class')
    m1 = myclass(12, "Abhilash", "Gwalior")
    print(m1.i)
    m2 = myclass(14, "Sharmaji", "Bhopal")
    print(m2.i)
    m1.myfun('Namasta')
