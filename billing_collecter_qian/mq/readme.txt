#2015_09_22_11:15:58   星期二   add by greshem
#重发: 
1.   resend.py                  #

#fake 的 收集系统, 这里只负责 把using_id  通过ack 再转发一下.
2.   fake_billing_ack_srv.py    


#启动的另外一个进程, 用于接受 已经 处理掉的billing_id 的包, 
3.   receiver_ack.py  
