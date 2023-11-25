def uppercase_decorator(function):
  def wrapper(): 
    func = function()
    make_uppercase = func.upper()
    return func.upper()
  
  return wrapper

@uppercase_decorator
def say_hello():
  return 'ini hello'

print(say_hello())