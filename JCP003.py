#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
������3��
��Ŀ��һ��������������100����һ����ȫƽ�������ټ���168����һ����ȫƽ���������ʸ����Ƕ��٣�
1.�����������10�������жϣ��Ƚ���������100���ٿ������ٽ���������268���ٿ��������������
�������������Ľ�������������������ǽ�����뿴���������
2.����Դ���룺

#include "math.h"
main()
{
long int i,x,y,z;
for (i=1;i<100000;i++)
��{ x=sqrt(i+100); ����/*xΪ����100�󿪷���Ľ��*/
����y=sqrt(i+268); ����/*yΪ�ټ���168�󿪷���Ľ��*/
������if(x*x==i+100&&y*y==i+268)/*���һ������ƽ������ƽ�����ڸ�������˵����������ȫƽ����*/
��������printf("\n%ld\n",i);
��}
} 
'''
import math
for i in range(10000):
    #ת��Ϊ����ֵ
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print i
