def decorative_funtion(func):
    def ichki(malumotlar):
        return [fun(val[0], val[1]) for val in malumotlar]
    return ichki

@decorative_funtion
def raqam(a, b):
    print(a + b)

print(raqam([(10,10), (20,20), (50, 50)]))





















