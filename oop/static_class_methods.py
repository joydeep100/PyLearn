class Class1:
    A = 100

    @classmethod
    def test_fun(cls):
        print(cls.A);
    
    @staticmethod
    def sta_fun():
        print('test')


#Class method
Class1.test_fun()

#Static method
x = Class1()
x.sta_fun()
