#coding=utf-8

#这是个简单的例子，稍微复杂点可以有多个闭包，比如经常使用的那个LRUCache的装饰器，装饰器上可以接受参数@lru_cache(expire=500)这样。实现起来就是两个闭包的嵌套:
#复制代码 代码如下:

def lru_cache(expire=5):
    # 默认5s超时
    def func_wrapper(func):
        def inner(*args, **kwargs):
            # cache 处理 bala bala bala
            print  "bala bala bala  and  expire =%s\n"%(expire);
            return func(*args, **kwargs)
        return inner
    return func_wrapper

@lru_cache(expire=10*60)
def get():
    # 省略具体代码
    #return response()
    print "get things ";


get();
