# # x = True
# # if x:
# #     print ('you win')
# # else:
# #         print ('you lose')

# # def square(x):
# #     y = x * x 
# #     return y

# x = 10;
# print (lambda x: x*x)

class casio:
    i_d = "electronic"

    def __init__(self, part_no):
        self.part_no = part_no
    
    def sayHi(self):
        print (self.part_no)

class calculator(casio):
    properti = "buttons"
    
    def __init__(self,part_no, button_no):
        self.button_no = button_no
        super(calculator,self).__init__(part_no)

    def button_count(self):
        print ("i"+ self.button_no + self.properti)

class scientific(calculator):
    status = "digital"

    def __init__(self,part_no,button_no):
        super(scientific,self).__init__(part_no,button_no)

    def description(self):
        print("i am"+ self.status + str(casio.sayHi(self),casio.i_d, calculator.button_count(self)) + str(calculator.properti))


victor = scientific("1213","5555")
emma = calculator("167","23434")
emma.button_count()
victor.description()



# # inheritance
# #map filter and reduce

# demolist = [3,5,2,4,1]

# map(lambda x: x*x, tuple(demolist))

# list comprehension
#  not entering interactive mode
#  s sasbsc  sa sadsbsc  sad sbsc sb






            
            


