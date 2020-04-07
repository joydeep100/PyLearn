class Class1:

    A = 100

    @classmethod
    def test_fun(cls):
        print(cls.A);
    
    @staticmethod
    def sta_fun():
        print('test')

x = Class1()
Class1.test_fun()

x.sta_fun()
