#Chaper1  1.3(Answering for terminal velocity)
##摘要
此题为求解跳伞运动员在考虑重力摩擦力的条件下，计算运动员速度随时间的变化关系，由经典力学知识知道，它会趋于一个最终平衡速度
##计算原理
1.运用Euler method，先展开V-t关系式  

2.将质量所给的求导子带入到1中的V-T展开式中  

3.参数设置
总时间t_total  

时间分段长度dt  

分段数n=t_total/dt  

常数a,b  

计算v  
##实现思路
i从1循环到n，每次增加dt的时间  

每次的速度增加近似认为是匀加速  

每次的位移增加近似看成匀加速运动  

把每一次的t、v分别储存在三个数组中 
##绘图工具
本次作业使用作图工具为matplotlib库
##程序实现
Python源代码：[terminal velocity.py](https://github.com/daijiahe/computationalphysics_N2013301020073/blob/master/terminal%20velocity.py)
##V-t图
效果图：![alt text](https://github.com/daijiahe/computationalphysics_N2013301020073/blob/master/chapter1.png) 
##结果分析
*由python数据可知，一段时间后，速度达到平衡点约为9.9999.....m/s，但由于系统误差，即：每次时间段不是无限小。导致小数点后第八位开始是不断变化的，即速度不是完全不变的。但是结果在误差范围之内。*  
##致谢
感谢隔壁老王67号的悉心指导
