#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, sys
'''
������1��
��Ŀ����1��2��3��4�����֣�����ɶ��ٸ�������ͬ�����ظ����ֵ���λ�������Ƕ��٣�
1.��������������ڰ�λ��ʮλ����λ�����ֶ���1��2��3��4��������е����к���ȥ
�����������������������������С� 
2.����Դ���룺
'''
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print i,j,k
