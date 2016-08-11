'''��Ŀ������ĳ��ĳ��ĳ�գ��ж���һ������һ��ĵڼ��죿
1.�����������3��5��Ϊ����Ӧ���Ȱ�ǰ�����µļ�������Ȼ���ټ���5�켴����ĵڼ��죬����
����������������������������·ݴ���3ʱ�迼�Ƕ��һ�졣
2.����Դ���룺
'''

#!/usr/bin/env python
#-*- coding:utf-8 -*-
year = int(raw_input('year:\n'))
month = int(raw_input('month:\n'))
day = int(raw_input('day:\n'))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 <= month <= 12:
    sum = months[month - 1]
else:
    print 'data error'
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print 'it is the %dth day.' % sum

