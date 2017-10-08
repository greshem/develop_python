def gen_path_with(size):
    output_dir="%s"%((size));
    ret_dir="%s/%s/%s/%s/%s"%( output_dir[0:1], output_dir[0:2], output_dir[0:3], output_dir[0:4], output_dir);
    return ret_dir;

print gen_path_with(33333);
print gen_path_with("love");
