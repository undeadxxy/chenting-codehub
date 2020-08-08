# 2020_07_03_1_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：1 000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  LSTM_1
# 复杂的LSTM网络
# 结果： 只有大致趋势，横向变化小

# 2020_07_06_1_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：10000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_1
# 深度复杂的卷积+LSTM网络
# 结果： 整体趋势符合，横向的趋势也符合，细节有些差异
# 2020_07_06_2_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：2000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_1
# 深度复杂的卷积+LSTM网络
# 结果：只有大致趋势，横向变化小
# 2020_07_06_3_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：20000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_1
# 深度复杂的卷积+LSTM网络，在上一次的基础上修复bug，原来的卷积层后有两个relu层，,训练数据集为所有道
# 结果：整体趋势符合，横向的趋势也符合，细节有些差异
# 2020_07_06_4_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：50000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_2
# 深度复杂的卷积+LSTM网络，在上一次的基础上再增加卷积层数量和LSTM层数量,线性层数量，,训练数据集为所有道
# 结果：整体趋势符合，横向的趋势也符合，细节比上一次好些，但是还是和SMI结果有差异

# 2020_07_17_01_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：50000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_3
# 深度复杂的卷积+LSTM网络，在上一次的基础上再增加卷积层数量和LSTM层数量,线性层数量,训练数据集为所有道
# 结果：整体趋势符合，横向无变化了，
# 2020_07_17_02_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：11947   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_3
# 深度复杂的卷积+LSTM网络，在上一次的基础上再增加卷积层数量和LSTM层数量,线性层数量,训练数据集为5×5的网格上的道
# 结果：整体趋势符合，横向无变化了，
# 2020_07_17_03_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：16218   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_2
# 深度复杂的卷积+LSTM网络，训练数据集为5×5的网格上的道
# 结果：整体趋势符合，横向的趋势也符合，有细节差异。断网，只跑了16218次
# 2020_07_17_04_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：20000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_2
# 深度复杂的卷积+LSTM网络，训练数据集为所有道
# 结果：整体趋势符合，横向的趋势也符合，有细节差异。
# 2020_07_17_05_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：20000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_2
# 深度复杂的卷积+LSTM网络，训练数据集为所有道，每道重复训练10次
# 结果：整体趋势符合，横向基本无变化。
# 2020_07_17_06_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：200000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_2
# 深度复杂的卷积+LSTM网络，训练数据集为所有道
# 结果：整体趋势符合，横向的趋势也符合，有细节差异。
# 2020_07_17_07_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：50000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：1
# 网络：网络代替加权求和的过程  Deep_Net_2
# 深度复杂的卷积+LSTM网络，训练数据集为所有道
# 结果：整体趋势符合，横向基本无变化。

# 2020_07_20_01_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：50000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_2_M1 去掉了lstm的dropout
# 深度复杂的卷积+LSTM网络，训练数据集为所有道
# 结果：整体趋势符合，横向的趋势也符合，有细节差异。横向连续性比之前的更好一些
# 2020_07_20_02_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：140930   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  CNN_SMI
# 深度复杂的卷积网络，训练数据集为所有道
# 结果：整体趋势符合，横向的趋势也符合，有细节差异。CNN_SMI网络结果与Deep_Net_2_M1网络结果各有优势

# 2020_07_21_01_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：100000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  增加深度和宽度的CNN_SMI  层数：18  节点数：415  ：参数个数：406786
# 深度复杂的卷积，训练数据集为所有道
# 结果：和原来的好的相比，细节更好，横向连续性稍差
# 2020_07_21_02_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：50000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_2_M1 去掉了所有的dropout  层数：8  节点数：101  ：参数个数：380034
# 深度复杂的卷积网络+LSTM层，训练数据集为所有道
# 结果：和原来的好的相比，横向连续性好一点，细节差一点

# 2020_07_22_01_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：104474   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  增加深度和LSTM层的CNN_SMI2  层数：22  节点数：516  ：参数个数：8419066
# 深度复杂的卷积网络+LSTM层，训练数据集为所有道
# 结果：只有纵向趋势，横向无变化
# 2020_07_22_02_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：50000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_2_M1，将卷积核有些改为4，LSTM层数有些增加  层数：8  节点数：94  ：参数个数：532597
# 深度复杂的卷积网络+LSTM层，训练数据集为所有道
# 结果：只有纵向趋势，横向无变化

# 2020_07_23_01_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：35444   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  增加深度和LSTM层的Deep_CNN_SMI2  层数：36  节点数：1275  ：参数个数：3859768
# 深度复杂的卷积网络，训练数据集为所有道
# 结果：只有纵向趋势，横向无变化
# 2020_07_23_02_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：50000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_2_M1，将卷积核有些改为3  层数：8  节点数：85  ：参数个数：379957
# 深度复杂的卷积网络+LSTM层，训练数据集为所有道
# 结果：和原来的好的相比，横向连续性好一点，细节也好点，只是有一个较大的断裂
# 2020_07_23_03_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：5812   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_CNN_SMI2_relu,线性层后也有激活函数  层数：36  节点数：1275  ：参数个数：3859768
# 深度复杂的卷积网络，训练数据集为所有道
# 结果：只有纵向趋势，横向无变化


# 2020_07_24_01_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：43320,200000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  CNN_SMI_1d_Res  层数：18  节点数：415  ：参数个数：389700
# 深度复杂的卷积网络+LSTM层，训练数据集为所有道，卷积核变成一维，增加残差模块
# 结果：43320,效果比之前的更好，但是还是没有一模一样，继续训练.    200000,横向连续性和细节更好一些
# 2020_07_24_02_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：27710   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_2_M1d_Res  层数：8  节点数：85  ：参数个数：378859
# 深度复杂的卷积网络+LSTM层，训练数据集为所有道，卷积核变成一维，增加残差模块
# 结果：效果比CNN_SMI_1d_Res网络的结果更好，更连续，细节更好

# 2020_07_27_01_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：100000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  BSsequential_net  层数：17  节点数：    ：参数个数：3059998
# 按厍师兄的想法设计了一个顺序的N型残差网，只有卷积层和线性层
# 结果：效果和原来的差不多，横向连续性变好了。有些剖面在细节上还是对不上
# 2020_07_27_02_model1_4
# 输入：单道地震数据，优选的井数据，标签为井数据
# SMI数据：batch长度：60   训练次数：1000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：1   是否增加合成地震数据约束：1
# 网络：网络代替加权求和的过程  BSsequential_net  层数：17  节点数：    ：参数个数：3059998
# 继承上一个训练好的网络，用井数据训练，加地震约束
# 结果：横向连续性，分辨率都在下降，还有单道异常，整体差异

# 2020_07_28_01_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：100000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  BSsequential_net_D  层数：18  节点数：    ：参数个数：339336
# 按厍师兄的想法设计了一个顺序的降采样残差网，每个小模块里还是一个N型网只有卷积层和线性层
# 结果：效果和原来的差不多，横向连续性变好了。有些剖面在细节上还是对不上
# 2020_07_28_02_model1_4
# 输入：单道地震数据，优选的井数据，标签为井数据
# SMI数据：batch长度：60   训练次数：10000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  BSsequential_net_D  层数：18  节点数：    ：参数个数：339336
# 按厍师兄的想法设计了一个顺序的降采样残差网，每个小模块里还是一个N型网只有卷积层和线性层
# 结果：只有纵向趋势，横向基本无变化

# 2020_07_29_01_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：30   训练次数：200000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  BSsequential_net  层数：17  节点数：    ：参数个数：787468
# 按厍师兄的想法设计了一个顺序的N型残差网，只有卷积层和线性层
# 结果：连续性，准确率都不行，但是还是有趋势的

# 2020_07_31_01_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：60   训练次数：100000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  BSsequential_net_lstm  层数：17  节点数：    ：参数个数：24253198
# 按厍师兄的想法设计了一个顺序的N型残差网，将线性层换成LSTM层
# 结果：结果和LSTM网络结果差不多，和N型网络还是有差距
# 2020_07_31_02_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：30   训练次数：50000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  BSsequential_net_lstm  层数：17  节点数：    ：参数个数：6092068
# 按厍师兄的想法设计了一个顺序的N型残差网，将线性层换成LSTM层
# 结果：和向基本无变化，不得行

# 2020_08_03_01_model1_2
# 输入：单道地震数据
# SMI数据：batch长度：60   训练次数：50000   井数量：5   是否确定随机路径：0   选井方式：1  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  BSsequential_net_seismic  层数：12  节点数：    ：参数个数：789329
# 按厍师兄的想法设计了一个顺序的N型残差网，
# 结果：只有大致的趋势，基本没学到东西

