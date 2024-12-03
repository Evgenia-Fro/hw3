def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

inner_function() #попробовали вызвать функцию, так не работает тк функция локальная
test_function() #работает :)
