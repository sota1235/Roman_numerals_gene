#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created by sota1235
# Date 2014/2/27

num_list = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
s_list = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

def main(r_num):
    ans = 0
    # 4,9,40,90,400,900をreplace
    for n in s_list:
        if n in r_num:
            r_num = r_num.replace(n, '')
            ans += s_list[n]
    # 残りを計算
    res = list(r_num)
    for n in res:
        ans += num_list[n]
    print ans

main('XLIX')
main('MDCCCLXXXVIII')
main('MCMXLV')
main('MMMCMXCIX')
