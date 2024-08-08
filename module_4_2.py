def test_function():
    def inner_function():
        print("Я в области видимости test_function!!!")
        return

    inner_function()


test_function()
#inner_function() - если вызвать вне функции test_function, функция inner_function будет не определена
#NameError : name 'inner_function' is not defined. Did you mean: 'test_function'?