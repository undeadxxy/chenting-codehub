# 2020_08_05_01_model1_3_2
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：100   训练次数：91682   井数量：5   是否确定随机路径：0   选井方式：0  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  Deep_Net_2_M1d_Res  层数：8  节点数：    ：参数个数：1042979
# 深度复杂的卷积网络+LSTM层，训练数据集为所有道，卷积核变成一维，增加残差模块
# 结果：只有横向趋势
# 2020_08_05_02_model1_3
# 输入：单道地震数据，优选的井数据
# SMI数据：batch长度：100   训练次数：167690   井数量：5   是否确定随机路径：0   选井方式：0  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  BSsequential_net  层数：17  节点数：    ：参数个数：8444838
# 按厍师兄的想法设计了一个顺序的N型残差网
# 结果：只有横向趋势
# 2020_08_05_03_model1_2
# 输入：单道地震数据
# SMI数据：batch长度：100   训练次数：167167   井数量：0   是否确定随机路径：0   选井方式：0  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  BSsequential_net_seismic  层数：12  节点数：    ：参数个数：2194686
# 按厍师兄的想法设计了一个顺序的N型残差网
# 结果：只有横向趋势

# 2020_08_08_01_model1_3
# 输入：单道地震数据
# SMI数据：batch长度：100   训练次数：30   井数量：0   是否确定随机路径：0   选井方式：0  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  BSsequential_net  层数：17  节点数：    ：参数个数：8444838
# 按厍师兄的想法设计了一个顺序的N型残差网
# 结果：
# 2020_08_08_02_model1_3_2
# 输入：单道地震数据
# SMI数据：batch长度：100   训练次数：30   井数量：0   是否确定随机路径：0   选井方式：0  是否继承之前的模型：0   是否增加合成地震数据约束：0
# 网络：网络代替加权求和的过程  BSsequential_net_hu  层数：23  节点数：    ：参数个数：22862854
# 按厍师兄的想法设计了一个顺序的N型残差网
# 结果：


















