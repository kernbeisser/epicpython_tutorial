# imports as needed

def foo():
    # Lambda functions - anonymous functions
    # lambda arg1, arg2, ..., arg n: an expression using the arguments #general syntax

    a = lambda x, y: x * y # defining a lambda function

    print(a(20, 10)) # result is 200; calling the lambda function

#Instead of...
def myfunc(list):
    prod_list = []
    for x in range(10):
        for y in range(5):
            product = x * y
            prod_list.append(product)
    return prod_list + list

def use_lambda():
    # ...we can use a lambda function, a list comprehension and concatenation on a single line of code
    b = lambda list: [x * y for x in range(10) for y in range(5)] + list
    print(b([5,7,9]))

def some_func():
    a = lambda x, y: x * y
    print(a(4, 5))

def main():
    some_func()
    foo()
    print(myfunc([100,101,102]))
    use_lambda()

if __name__ == '__main__':
    main()
