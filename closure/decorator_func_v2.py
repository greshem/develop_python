#coding=utf-8
def bread(func):
    def wrapper():
        print "</''''''\>"
        func()
        print "<\______/>"
    return wrapper

def ingredients(func):
    def wrapper():
        print "#tomatoes#"
        func()
        print "~salad~"
    return wrapper

def sandwich(food="--ham--"):
    print food

sandwich()
# 输出为: --ham--
#sandwich = bread(ingredients(sandwich))
#sandwich();

cc= bread(ingredients(sandwich))
cc();
