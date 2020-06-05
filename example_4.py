class SomeClass:
    class_var = 111

    def method(self):
        print('self.class_var - before:', self.class_var)
        self.class_var = 33
        print('self.class_var - after:', self.class_var)


print('SomeClass.class_var:', SomeClass.class_var)

instance = SomeClass()
print('instance.class_var:', instance.class_var)

instance.method()

print('instance.class_var:', instance.class_var)

print('SomeClass.class_var:', SomeClass.class_var)

other_instance = SomeClass()
print('other_instance.class_var:', other_instance.class_var)


