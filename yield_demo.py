
def  get_data():
    for each in range(1,100):
        yield each;

for  each in get_data():
    print each;
