# Homework3
## 摘要

用字符表示字母，目标：
 
- [x] 作业L1 在屏幕上用字符拼出自己姓名的英文
- [x] 作业L2 在屏幕上用字符拼出任意次序的姓名
- [x] 作业L3 在80*80点阵上用字符拼出你想画的东西，希望脑洞大开！（比如字符，火柴人，实现移动、旋转等等）


## 正文
### 作业L1 在屏幕上用字符拼出自己英文姓名的首字母
效果如图
![3-2](https://github.com/daijiahe/computationalphysics_N2013301020073/blob/master/Letter.png)
代码如下
```python
print '**** * *                       **********                    *         *      ' 
print '*        *                          *                        *         *     '
print '*         *                         *                        *         *     ' 
print '*         *                         *                        ***********       '
print '*        *                          *                        *         *  '
print '***  * *                         ***                         *         * '
raw_input('Press Enter to exit...')
```


### 作业L2 在屏幕上用字符拼出任意次序的姓名

可以任意输出5*5的矩阵字符，
支持自动换行
只支持26个英文字母（不区分大小写），以及逗号，句点，单双引号，冒号，分号，感叹号，问号。


先正序和反序显示自己的名字，接下来可以输入任意的字母（包括空格），然后用字符显示出来。

效果如图：
![3-2](https://github.com/daijiahe/computationalphysics_N2013301020073/blob/master/Letter.png)

代码如下：
```python
# Type any word you want,including your name
voc={
'A' : ('   #    ',' #   #  ','#     # ','# ### # ','#     # ','#     # ','#     # '),
'B' : (' #####  ','#     # ','#     # ','######  ','#     # ','#     # ',' #####  '),
'C' : (' #####  ','#     # ','#       ','#       ','#       ','#     # ',' #####  '),
'D' : ('######  ','#     # ','#     # ','#     # ','#     # ','#     # ','######  '),
'E' : ('####### ','#       ','#       ','######  ','#       ','#       ','####### '),
'F' : ('####### ','#       ','#       ','#####   ','#       ','#       ','#       '),
'G' : (' #####  ','#       ','#       ','#   ### ','#     # ','#    ## ',' #### # '),
'H' : ('#     # ','#     # ','#     # ','####### ','#     # ','#     # ','#     # '),
'I' : (' #####  ','   #    ','   #    ','   #    ','   #    ','   #    ',' #####  '),
'J' : ('  ##### ','     #  ','     #  ','     #  ','     #  ',' #   #  ','  ###   '),
'K' : ('#     # ','#    #  ','#   #   ','####    ','#   #   ','#    #  ','#     # '),
'L' : (' #      ',' #      ',' #      ',' #      ',' #      ',' #      ',' #####  '),
'M' : ('#     # ','##   ## ','# # # # ','#  #  # ','#     # ','#     # ','#     # '),
'N' : ('#     # ','##    # ','# #   # ','#  #  # ','#   # # ','#    ## ','#     # '),
'O' : (' #####  ','#     # ','#     # ','#     # ','#     # ','#     # ',' #####  '),
'P' : ('######  ','#     # ','#     # ','######  ','#       ','#       ','#       '),
'Q' : (' #####  ','#     # ','#     # ','#     # ','#   # # ','#    #  ',' #### # '), 
'R' : ('######  ','#     # ','#     # ','######  ','#   #   ','#    #  ','#     # '),
'S' : (' ###### ','#       ','#       ',' #####  ','      # ','      # ','######  '),
'T' : ('####### ','   #    ','   #    ','   #    ','   #    ','   #    ','   #    '), 
'U' : ('#     # ','#     # ','#     # ','#     # ','#     # ','#     # ',' #####  '),
'V' : ('#     # ','#     # ','#     # ',' #   #  ',' #   #  ','  # #   ','   #    '),
'W' : ('#     # ','#     # ','#  #  # ','#  #  # ','#  #  # ','# # # # ',' #   #  '), 
'X' : ('#     # ',' #   #  ','  # #   ','   #    ','  # #   ',' #   #  ','#     # '), 
'Y' : ('#     # ','#     # ',' #   #  ','  # #   ','   #    ','   #    ','   #    '),
'Z' : ('####### ','     #  ','    #   ','   #    ','  #     ',' #      ','####### '),
' ' : ('        ','        ','        ','        ','        ','        ','        '),
}
doc=raw_input('Please input your document here:')
doc=doc.upper()
len=len(doc)
def type(voc,word):
    for a in range(0,7):
        for i in word:
            print voc[i] [a],
        print ''
for line in range(0,len/18):    
    word=doc[line*18:(line+1)*18]
    type(voc,word)
    print ''
word=doc[len/18*18:len+1]
type(voc,word)
```


### 作业L3 在80*80点阵上用字符拼出你想画的东西，希望脑洞大开！（比如字符，火柴人，实现移动、旋转等等）

#### 第一版
画了一个斜眼图（静态的）。
代码如下：
```python
print '                     .;;hShhhhhh5s;;.                      '
print '                  ,:;rr:;,       .:irrr:                   '
print '             .i1hi:,                 .:s1hh:               '
print '          ,59hi:.  ..                    .rs1r             '
print '        rS9hs;;iiiii1s1i:                   ;35,           '
print '      ,9B@MS         .:iS5,                   18i          '
print '      39B@#H,  . .       r9;                   :8r         '
print '    ,3sh33hrrrrrrrsh1:    :G;                   ,8s        '
print '   ;As  . .        ,r35    i8:     ,:riiii::,    ,8r       '
print '  .8r                 59    hS   1ss      ^rh51i  :8,      '
print '  5h                   59.  5S  58sr.        .;S3; 13      '
print ' .8.                    h9s59; 18h@@h           ;S1 9i     '    
print ' s1 .r                   ;5r   ;Gs9G1rhsrsshr:   .81i9     '    
print ' sr i9                          ::888;     :s8S   ,G,9.    '    
print ' 1r 91                                        85   9G9.    '    
print ' 1r r9                          .h1:iSi       ;9, ;MH&     '    
print ' 1r ,9                          iS   iXr       s55H5S1     '    
print ' ,S,.8s                         ;3    ;95ss:        &:     '    
print '  19 ,9i                         r8s,   ,:sS1111h5i9A;.    '    
print '   8h iXh                         :1ShSsir...   .::is133i  '    
print '   :8S .99i                           ,;:ss1SSs        iX5 '    
print '     39. i9S:.                          ,i:  GAX5        HG'   
print '      ;8h  :;hhs.                   .;158r  58.8@1      :#8'   
print '       ,1Ss.  ,is5s1;;.      .,;rh1Ssir,  r9S. r@8     .AB.'   
print '         .11hs:   .iihsssssssshhri,     r9S:  ;HB.    rAX. '   
print '            .iisS1:,               ,:55rr:   rH3.    3@5   '   
print '               rXhshrhsiirririis515rr.      i:      X@G    '  
print '                 i&.  .:::::,::::.                    h@X. '   
print '                  13                                   5@S '   
print '                   h1                                   &#.'   
print '                   55                                   5#.'   
print '                   ;X,                                  5@,'   
print '                    G&                                 .&B.'   
print '                   :H9                                .&#; '   
print '                   1#                                .MM.  '   
```

#### 第二版
下面让这幅图可以横向移动30格

效果如图

![3-3](https://raw.githubusercontent.com/newton2ndlaw/computationalphysics_N2013301510086/master/Homework3/Homework3-3.jpg)

代码如下：
```python
import os
#              123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789
picture=['                     .;;hShhhhhh5s;;.                      '] #0
picture.append('                  ,:;rr:;,       .:irrr:                   ') #1
picture.append('             .i1hi:,                 .:s1hh:               ') #2
picture.append('          ,59hi:.  ..                    .rs1r             ') #3
picture.append('        rS9hs;;iiiii1s1i:                   ;35,           ') #4
picture.append('      ,9B@MS         .:iS5,                   18i          ') #5
picture.append('      39B@#H,  . .       r9;                   :8r         ') #6
picture.append('    ,3sh33hrrrrrrrsh1:    :G;                   ,8s        ') #7
picture.append('   ;As  . .        ,r35    i8:     ,:riiii::,    ,8r       ') #8
picture.append('  .8r                 59    hS   1ss      ^rh51i  :8,      ') #9
picture.append('  5h                   59.  5S  58sr.        .;S3; 13      ') #10
picture.append(' .8.                    h9s59; 18h@@h           ;S1 9i     ') #11
picture.append(' s1 .r                   ;5r   ;Gs9G1rhsrsshr:   .81i9     ') #12
picture.append(' sr i9                          ::888;     :s8S   ,G,9.    ') #13  
picture.append(' 1r 91                                        85   9G9.    ') #14 
picture.append(' 1r r9                          .h1:iSi       ;9, ;MH&     ') #15  
picture.append(' 1r ,9                          iS   iXr       s55H5S1     ') #16   
picture.append(' ,S,.8s                         ;3    ;95ss:        &:     ') #17   
picture.append('  19 ,9i                         r8s,   ,:sS1111h5i9A;.    ') #18
picture.append('   8h iXh                         :1ShSsir...   .::is133i  ') #19
picture.append('   :8S .99i                           ,;:ss1SSs        iX5 ') #20
picture.append('     39. i9S:.                          ,i:  GAX5        HG') #21
picture.append('      ;8h  :;hhs.                   .;158r  58.8@1      :#8') #22
picture.append('       ,1Ss.  ,is5s1;;.      .,;rh1Ssir,  r9S. r@8     .AB.') #23
picture.append('         .11hs:   .iihsssssssshhri,     r9S:  ;HB.    rAX. ') #24
picture.append('            .iisS1:,               ,:55rr:   rH3.    3@5   ') #25
picture.append('               rXhshrhsiirririis515rr.      i:      X@G    ') #26 
picture.append('                 i&.  .:::::,::::.                    h@X. ') #27
picture.append('                  13                                   5@S ') #28
picture.append('                   h1                                   &#.') #29
picture.append('                   55                                   5#.') #30
picture.append('                   ;X,                                  5@,') #31
picture.append('                    G&                                 .&B.') #32
picture.append('                   :H9                                .&#; ') #33
picture.append('                   1#                                .MM.  ') #34

import os

for i0 in range(30):
    i = os.system('cls')
    for i1 in range(35):
        for i2 in range(i0):
            print '',
        print picture[i1]

raw_input()
```

#### 第三版
接下来还会继续制作其他移动方式。

## 结论

待会弄个图片上去。

## 致谢

* 这次作业没有参考别人的结果。
