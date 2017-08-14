#!/usr/bin/python

total = 0; # This is global variable.
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2; # total在这里是局部变量.
   print ("Inside the function local total : ", total)
   return total;

#调用sum函数
sum( 10, 20 );
print ("Outside the function global total : ", total)
#以上实例输出结果：
#Inside the function local total :  30
#Outside the function global total :  0
