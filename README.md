# Eye-closure-detection-EAR
Eye closure detection based on EAR

> [基于人眼纵横比计算的人眼闭合检测算法](https://jasoncaocjx.github.io/2020/04/14/%E5%9F%BA%E4%BA%8E%E4%BA%BA%E7%9C%BC%E7%BA%B5%E6%A8%AA%E6%AF%94%E8%AE%A1%E7%AE%97%E7%9A%84%E4%BA%BA%E7%9C%BC%E9%97%AD%E5%90%88%E6%A3%80%E6%B5%8B%E7%AE%97%E6%B3%95/)

# 原理
PDlib是基于现代C++的通用多平台框架，在机器学习和图像处理领域提供了一系列相关功能

它在人脸检测中，将人脸视为可分的68个数据点，部分人脸数据可根据这些数据点进行检测

![人脸68数据点](http://m.qpic.cn/psc?/V10DFE6N3uScTK/eUV4L3fpc9jygk8SN5vzkPGq6UGgQ9zrngzjoErex0Bz5*7tD9*iUcbBcP1LNNLjNmI3zbZDOJZWcqQrYsDiQA!!/b&bo=SwNHAgAAAAADBy8!&rf=viewer_4)

Tereza Soukupová于2016年发表的一篇名为Eye blink detection using facial landmarks的文章中

基于实际数据集使用面部关键点检测器作为输入，提出了简单有效的眨眼检测眨眼算法

通过定位眼睛和眼睑的轮廓得出眼睛的长宽比（Eye Aspect Ratio，EAR），用于估计睁眼状态

将访问到的左眼数据[43，48]进行编号

![右眼示意图](http://m.qpic.cn/psc?/V10DFE6N3uScTK/2aGbA7qLSN6GeC6g0ZsuRU5pFIazdWM3Z*Ljk26cfYVtxRCCzwOC2XOOe9rbovdwujw1tXPcNparFj6ySjqnBdTryKgj0DiY1q7H*IQ*Ag4!/b&bo=EwRxAQAAAAADF1U!&rf=viewer_4)

分别对应[p1,p6]得出公式：

![人眼纵横比公式](http://m.qpic.cn/psc?/V10DFE6N3uScTK/2aGbA7qLSN6GeC6g0ZsuRVjMuZ5SgZpJ7ZZXGnAcHzRCmmKiV7DevW.*VOBa2GWLzQzKZboX1xYnvCfu1L4gqwF7XJnNYHdoZ92rK9sXHN0!/b&bo=zAA6AAAAAAADF8Q!&rf=viewer_4)
 
在睁眼状态时EAR通常保持恒定，而闭眼时EAR趋近于零

右眼进行同理计算后，通过左右眼同步，将得到的左右眼两个EAR进行平均后得出最终结果

# 实验
阈值是判断睁闭眼的关键，因此合适的阈值可以提高检测的准确度

我们使阈值从0到1变化，步长为0.05，在使用数据集测试后，得到了下图

![阈值变化图](http://m.qpic.cn/psc?/V10DFE6N3uScTK/2aGbA7qLSN6GeC6g0ZsuRdoSeXalurrBOKq1SrmAVc5uogN5d9pvkxo5Q3hkkLa0aDzbCOORFpkXS*euaW1w.62pb7Pcto2iA1dNi5lrbVs!/b&bo=egLbAQAAAAARF4I!&rf=viewer_4)

测试结果显示设置0.2为阈值最合适，也可根据实际情况调整

# 源代码
本项目的[源代码](https://github.com/JasonCaoCJX/Eye-closure-detection-EAR)已完全公开