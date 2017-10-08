#!/usr/bin/python
#reduce reduce（functionA，iterableB），
#functionA为需要两个变量的函数，并返回一个值。iterableB为可迭代变量，如 List等。
#reduce函数将B中的元素从左到右依次传入函数A中，再用函数A返回的结果替代传入的参数，反复执行，
#则可将B reduce成一个单值。在此，是将1到1000的连续整数列表传入lambda函数并用两个数的积替换列表中的数，实际的计算过程为：(... ((1×2)×3)×4)×...×1000)，最后的结果即1000的阶乘。
print    reduce ( lambda    x , y : x * y ,    range ( 1 ,    1001 ))
