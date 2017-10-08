
def get_a():
    return 1000;
def get_b():
    return 1001;

block_device_info = {
                'swap': get_a(),
    };


block_device_info2 = {
                'swap': get_a,
    };
print block_device_info;
print "#=================\n";
print block_device_info2;
