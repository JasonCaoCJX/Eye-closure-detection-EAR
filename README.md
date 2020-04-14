# Eye-closure-detection-EAR
Eye closure detection based on EAR

> 基于人眼纵横比计算的人眼闭合检测算法

# 基本原理
PDlib是基于现代C++的通用多平台框架，在机器学习和图像处理领域提供了一系列相关功能

它在人脸检测中，将人脸视为可分的68个数据点，部分人脸数据可根据这些数据点进行检测

![人脸68数据点](http://m.qpic.cn/psc?/V10DFE6N3uScTK/eUV4L3fpc9jygk8SN5vzkBvlIdCwZuWiVJUBiAtp.SMCJb4G6KRhE4dB7RggiWA79WgHKu03o9Tk0uORY*h5zA!!/b&bo=lQIbAgAAAAARB74!&rf=viewer_4)

Tereza Soukupová于2016年发表的一篇名为Eye blink detection using facial landmarks的文章中

基于实际数据集使用面部关键点检测器作为输入，提出了简单有效的眨眼检测眨眼算法

通过定位眼睛和眼睑的轮廓得出眼睛的长宽比（Eye Aspect Ratio，EAR），用于估计睁眼状态

将访问到的左眼数据[43，48]进行编号

![右眼示意图](http://m.qpic.cn/psc?/V10DFE6N3uScTK/2aGbA7qLSN6GeC6g0ZsuRY9xNL92dr5s602jgIVx7ksqpIG5qn78YJYy6K2MYtuj25funZDdRbxU7gdYhqSszlV1DPFGf*SYZdYjoPG1oWI!/b&bo=iQPFAQAAAAADF3w!&rf=viewer_4)

分别对应[p1,p6]得出公式：

![人眼纵横比公式](http://m.qpic.cn/psc?/V10DFE6N3uScTK/2aGbA7qLSN6GeC6g0ZsuRSMEdOoP7pvx5Pag3*2g*XYjqLQ8T5tBqbvB6r3XdzSPCpXCHyvBARrUx3UIg85jjyl*BBMFdiX0VgPhlwhfVI4!/b&bo=zAA6AAAAAAADF8Q!&rf=viewer_4)
 
在睁眼状态时EAR通常保持恒定，而闭眼时EAR趋近于零

右眼进行同理计算后，通过左右眼同步，将得到的左右眼两个EAR进行平均后得出最终结果

# 实验
阈值是判断睁闭眼的关键，因此合适的阈值可以提高检测的准确度

我们使阈值从0到1变化，步长为0.05，在使用数据集测试后，得到了下图

![阈值变化图](http://m.qpic.cn/psc?/V10DFE6N3uScTK/2aGbA7qLSN6GeC6g0ZsuRd6Yd7cppRonRXXABC1YD1PR1GOeXSukMuCPCRmUCj1Qe8k6OWHr4f1m.zkHgRBKHOSPMSR1QRjmFklzk4OzQN8!/b&bo=egLbAQAAAAARF4I!&rf=viewer_4)

测试结果显示设置0.2为阈值最合适，也可根据实际情况调整

# 源代码
本项目的[源代码](https://github.com/JasonCaoCJX/Eye-closure-detection-EAR)已完全公开