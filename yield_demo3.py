
def  get_data():
    for each in range(1,100):
        for each2  in range(100,1000):
            yield (each,each2);

for each,each2 in get_data():
    print each,each2;
