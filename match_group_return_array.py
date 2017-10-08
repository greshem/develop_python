#coding=utf-8
#!/usr/bin/python
import re;
#命令组的语法是 Python 专用扩展之一： (?P<name>...)。名字很明显是组的名字。除了该组有个名字之外，命名组也同捕获组是相同的。`MatchObject` 的方法处理捕获组时接受的要么是表示组号的整数，要么是包含组名的字符串。命名组也可以是数字，所以你可以通过两种方式来得到一个组的信息：
#!python

str="5/results/";
reg=re.compile(r'^(?P<question_id>[0-9]+)/results/$');
print(reg.match(str).group('question_id'));
print(reg.match(str).groups());

str="_1010_compute_panel_group.py"

