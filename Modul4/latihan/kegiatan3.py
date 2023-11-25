def title_decoration(function):
  def wrapper():
    func = function()
    make_title = func.title()
    print(make_title + " " + "- Data is convert to title case")
    return make_title
  
  return wrapper

#decorator 
def split_string(function):
  def wrapper():
    func = function()
    splitted_string = func.split()
    print(str(splitted_string) + " " + "- Then Data is splitted")
    return splitted_string
  
  return wrapper

@split_string
@title_decoration
def say_hello():
  return 'ini hello'

print(say_hello())