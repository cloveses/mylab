#!/usr/bin/env python
# coding: utf-8

####导入数据，找到配对股票
# import costF
from random import uniform
from random import randint 
import math
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from jqdatasdk import *
import pandas as pd             
from numpy import nan            
import statsmodels.api as sm           
import seaborn as sns
from pandas import read_csv
import math
from keras.models import Sequential
from keras.layers import Dense,Dropout
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from keras.wrappers.scikit_learn import KerasClassifier
# In[3]:

def create_dataset(dataset, look_back):
    dataX,dataY=[],[]
    print('dataset',dataset)
    print(len(dataset))

    for i in range(len(dataset)-look_back-1):
        x=dataset[i:i+look_back,0]
        dataX.append(x)
        y=dataset[i+look_back,0]
        dataY.append(y)
        print('X:%s,Y:%s'%(x,y))
    return np.array(dataX),np.array(dataY)

def build_model(look_back):
    model=Sequential()
    model.add(LSTM(units=nest[4],input_shape=(1,look_back),return_sequences=True))
    model.add(Dropout(nest[5]))
    model.add(LSTM(units=nest[6],return_sequences=False))
    model.add(Dropout(nest[7]))
    model.add(Dense(units=1))
    model.compile(loss='mean_squared_error',optimizer='adam')
    return model


def fitness(nest):

    # 获取沪深300指数成分股 前复权后的历史股价 副本1.csv 
    index = '000300.XSHG'
    start = '2017-11-1'
    end   = '2019-10-31'
    # auth('18827513013','513013')
    # auth('19802176017','Limin123')
    # code_list = get_index_stocks(index)
    # index_df = get_price(code_list, start, end, fields='close').close
    # index_df.to_csv('./副本1.csv')
    # index_df.head()

    index_df = pd.read_csv('./aa.csv', index_col= 0, header= 0)

    len(index_df)   #总共有487行数据

    df=index_df.dropna(axis = 1)    #axis = 1代表删除缺失值所在的列，这个案例里，删除了有缺失值的股票代码    
    df.to_csv('./副本2.csv')             #dropna默认删除缺失值所在的行，也就是默认axis=0
    df.head()

    np.isnan(df).any().sum() #检查数据集里是否还有缺失值

    df_log=np.log(df)   #对数据取对数
    df_log.to_csv('./副本对数.csv')
    df_log.head()

    train=df_log.loc["2017-11-1":"2018-10-31"]#2017-11-01至2018-10-31为训练+验证数据，共244个数据（先用这部分数据选出相关系数高的股票对）  
    train.to_csv('./副本train.csv')         
    train.head()
    train.tail()

    len(train)

    test=df_log.loc["2018-11-1":,]   #用来预测
    test.head()

    len(test)

    # 计算每支股票与其余股票的相关系数，降序排列corr_df = train.corr()
    # 相关系数相等的两支股票即为配对股票corr_df[corr_df==1] = nan
    # 没有组成配对的股票是由于它与已组成配对的股票的相关系数低于已组成的股票对的相关系数
    corr_df = train.corr()
    corr_df[corr_df==1] = nan
    corr_df = pd.DataFrame(corr_df.max().sort_values(ascending=False).head(10), columns=['corr'])
    # corr_df['name'] = [get_security_info(code).display_name for code in corr_df.index]
    # corr_df['industry'] = [get_industry(code) for code in corr_df.index] 
    corr_df.to_csv('./副本配对股票1.csv')
    corr_df                    #得到配对股票
    ####检验配对股票的协整关系

    # GY=train['000728.XSHE'] #取对数后的train训练集中国元证券和东吴证券走势相近
    # DW=train['601555.XSHG']  #东吴证券
    # plot(GY);plot(DW)
    # plt.xlabel('Time');plt.ylabel('LOG(Price)')
    # plt.legend(['000728.XSHE'],['601555.XSHG'],loc='best')

    #综上可以看到  东吴证券和长江证券一阶单整  可以做协整检验
    #协整检验  先做一元回归   再对残差做单位根检验
    x = train['000728.XSHE']
    y = train['601555.XSHG']
    X = sm.add_constant(x)
    result = (sm.OLS(y,X)).fit()
    print(result.summary())

    plot(y-0.8858*x);              #根据ols的估计系数，画出y-0.8858*x的平稳序列
    # plt.axhline((y-0.8858*x).mean(), color="red", linestyle="--")
    # plt.xlabel("Time"); plt.ylabel("Stationary Series")
    # plt.legend(["Stationary Series", "Mean"])

    from statsmodels.tsa.stattools import adfuller        #单位根检验P<0.05 说明平稳
    adftest=adfuller(y-0.8858*x-0.1575)                   #东吴证券和国元证券之间存在着长期的均衡关系
    result=pd.Series(adftest[0:4],index=['Test Statistic','p-value','Lags Used','Numbers of Observations Used'])
    for key,value in adftest[4].items():
        result['Critical Value (%s)'%key]=value
    print(result)                                 #残差的单位根检验

    spread=y-0.8858*x-mean(y-0.8858*x)
    plot(spread)
    spread.head()


    spread.size

    # In[30]:
    seed=7
    batch_size=nest[0]
    epochs=nest[1]    #迭代10次
    filename=spread
    footer=3
    look_back=nest[2]   #用前十次的数据来预测下一时刻的数据 
    lr=nest[3]

    #设置随机数种子
    np.random.seed(seed)
    
    #导入数据
    data=filename
    dataset=data.values.astype('float64')
    
    #标准化数据
    scaler=MinMaxScaler()
    dataset=scaler.fit_transform(dataset.reshape(-1,1))
    train_size=len(dataset[0:200])    
    validation_size=len(dataset)-train_size
    train,validation=dataset[0: train_size, :],dataset[train_size:len(dataset), :]
    
    #创建dataset,让数据产生相关性
    X_train,y_train=create_dataset(train, nest[2])
    X_validation,y_validation=create_dataset(validation, nest[2])
    
    #将输入转化成【样本，时间步长，特征】
    X_train=np.reshape(X_train,(X_train.shape[0],1,X_train.shape[1]))
    X_validation=np.reshape(X_validation,(X_validation.shape[0],1,X_validation.shape[1]))
    
    #训练模型
    model=build_model(nest[2])
    model.fit(X_train,y_train,epochs=epochs,batch_size=batch_size,verbose=2,validation_data=(X_validation,y_validation))
    
    #模型预测数据
    predict_train=model.predict(X_train)
    predict_validation=model.predict(X_validation)
    
    #反标准化数据，目的是保证MSE的准确性
    predict_train=scaler.inverse_transform(predict_train)
    y_train=scaler.inverse_transform([y_train])
    predict_validation=scaler.inverse_transform(predict_validation)
    y_validation=scaler.inverse_transform([y_validation])
    
    #评估模型
    train_score=math.sqrt(mean_squared_error(y_train[0],predict_train[:, 0]))
    print('Train Score: %.2f RMSE' % train_score)
    validation_score=math.sqrt(mean_squared_error(y_validation[0],predict_validation[:, 0]))
    print('Validation Score: %.2f RMSE' % validation_score)
    
    #构建通过训练数据集进行预测的图表数据
    predict_train_plot=np.empty_like(dataset)
    predict_train_plot[:, :]=np.nan
    predict_train_plot[look_back:len(predict_train)+look_back, :]=predict_train
    
    #构建通过评估数据集进行预测的图表数据
    predict_validation_plot=np.empty_like(dataset)
    predict_validation_plot[:, :]=np.nan
    predict_validation_plot[len(predict_train)+look_back*2+1:len(dataset)-1, :]=predict_validation
    
    #图表显示
    dataset=scaler.inverse_transform(dataset)
    # plt.plot(dataset,color='blue')
    # plt.plot(predict_train_plot,color='green')
    # plt.plot(predict_validation_plot,color='red')
    # plt.show()


    # In[40]:


    fx=test['000728.XSHE']            #测试集的价差
    fy=test['601555.XSHG']
    fspread=fy-0.8858*fx-mean(fy-0.8858*fx)


    # In[41]:


    XY=fspread         #根据训练好的模型进行预测
    dataset=XY.values.astype('float64')
    #标准化数据
    scaler=MinMaxScaler()
    dataset=scaler.fit_transform(dataset.reshape(-1,1))
        
    #创建dataset,让数据产生相关性
    X_test,y_test=create_dataset(dataset, nest[2])
        
    #将输入转化成【样本，时间步长，特征】
    X_test=np.reshape(X_test,(X_test.shape[0],1,X_test.shape[1]))


    #模型预测数据
    predict_test=model.predict(X_test)
        
    #反标准化数据，目的是保证MSE的准确性
    predict_test=scaler.inverse_transform(predict_test)
    y_test=scaler.inverse_transform([y_test])
        
    #评估模型
    test_score=math.sqrt(mean_squared_error(y_test[0],predict_test[:, 0]))
    print('Test Score: %.2f RMSE' % test_score)

    #构建通过测试数据集进行预测的图表数据
    predict_test_plot=np.empty_like(dataset)
    predict_test_plot[:, :]=np.nan
    predict_test_plot[look_back:len(predict_test)+look_back, :]=predict_test

    #图表显示
    dataset=scaler.inverse_transform(dataset)
    # plt.plot(dataset,color='blue')
    # plt.plot(predict_test_plot,color='red')
    # plt.show()

    return validation_score

'''
根据levy飞行计算新的巢穴位置
'''
def GetNewNestViaLevy(Xt,Xbest,Lb,Ub,lamuda):
    beta = 1.5
    sigma_u = (math.gamma(1 + beta) * math.sin(math.pi * beta / 2) / (
                math.gamma((1 + beta) / 2) * beta * (2 ** ((beta - 1) / 2)))) ** (1 / beta)
    sigma_v = 1
    for i in range(Xt.shape[0]):
        s = Xt[i,:]
        u = np.random.normal(0, sigma_u, 1)
        v = np.random.normal(0, sigma_v, 1)
        Ls = u / ((abs(v)) ** (1 / beta))
        stepsize = lamuda*Ls*(s-Xbest)   #lamuda的设置关系到点的活力程度  方向是由最佳位置确定的  有点类似PSO算法  但是步长不一样
        s = s + stepsize * np.random.randn(1, len(s))  #产生满足正态分布的序列
        Xt[i, :] = s
        Xt[i,:] = simplebounds(s,Lb,Ub)
    return Xt
'''
按pa抛弃部分巢穴
'''
def empty_nests(nest,Lb,Ub,pa):
    n = nest.shape[0]
    nest1 = nest.copy()
    nest2 = nest.copy()
    rand_m =pa - np.random.rand(n,nest.shape[1])
    rand_m = np.heaviside(rand_m,0)
    np.random.shuffle(nest1)
    np.random.shuffle(nest2)
    # stepsize = np.random.rand(1,1) * (nest1 - nest)
    stepsize = np.random.rand(1,1) * (nest1 - nest2)
    new_nest = nest + stepsize * rand_m
    nest = simplebounds(new_nest,Lb,Ub)
    return nest
'''
获得当前最优解
'''
def get_best_nest(nest, newnest,Nbest,nest_best):
    fitall = 0
    for i in range (nest.shape[0]):
        temp1 = fitness(nest[i,:])
        temp2 = fitness(newnest[i,:])
        if temp1 > temp2:
            nest[i, :] = newnest[i,:]
            if temp2 < Nbest :
                Nbest = temp1
                nest_best = nest[i,:]
            fitall = fitall + temp2
        else:
            fitall = fitall + temp1
    meanfit = fitall/nest.shape[0]
    return  nest , Nbest , nest_best ,meanfit

'''
约束迭代结果
'''
def simplebounds(s,Lb,Ub):
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            if s[i][j] < Lb[j]:
                s[i][j] = Lb[j]
            if s[i][j] > Ub[j]:
                s[i][j] = Ub[j]
    return s
 
def Get_CS(Lb,Ub,maxgen):
    '''
    Lb - 优化变量下边界 eg. Lb = [-1, -1, -0.1]
    Ub - 优化变量上边界 eg. Ub = [3, 5, 10]
    maxgen - 迭代次数
    '''

    population_size = 20 # 布谷鸟种群数
    lamuda = 1
    pa =0.25
    costfmin = []
    bestpop = []
    dim = len(Lb)
    nest = np.array(Lb) + (np.array(Ub)-np.array(Lb))*np.random.uniform(0, 1,(population_size,dim))  # 初始化位置
    nest_best = nest[0,:]
    Nbest =fitness(nest_best)
    nest ,Nbest, nest_best ,fitmean = get_best_nest(nest,nest,Nbest,nest_best)
    for i in range (maxgen):
        nest_c = nest.copy()
        newnest = GetNewNestViaLevy(nest_c, nest_best, Lb, Ub,lamuda) # 根据莱维飞行产生新的位置
 
        nest,Nbest, nest_best ,fitmean = get_best_nest(nest, newnest,Nbest, nest_best) # 判断新的位置优劣进行替换
 
        nest_e = nest.copy()
        newnest = empty_nests(nest_e,Lb,Ub,pa) #丢弃部分巢穴
 
        nest,Nbest, nest_best ,fitmean = get_best_nest(nest,newnest, Nbest, nest_best)  # 再次判断新的位置优劣进行替换
 
        costfmin.append(Nbest)
        bestpop.append(nest_best)
        print("第",i,"次迭代，最优解的适应度函数值",Nbest)

    return  costfmin, bestpop


# Lb = [-10,-10]
# Ub = [10,10]

# Lb = [1, 10, 5, 0, 10, 0, 10, 0]
# Ub = [300, 500, 20, 1, 200, 1, 200, 1]

# maxgen = 30
# costfmin, bestpop = Get_CS(Lb=Lb,Ub=Ub,maxgen=maxgen)
# plt.plot(costfmin)
# plt.xlabel('time')
# plt.ylabel('cost function')
# plt.show()

if __name__ == '__main__':
    # batch_size = 1
    # epochs = 20    #迭代10次
    # look_back = 10   #用前十次的数据来预测下一时刻的数据 
    # lr = 0.0006
    # units, drop_out= 10, 0.5
    # units_1, drop_out_1 = 10, 0.5
    # nest = [batch_size, epochs, look_back, lr, units, drop_out, units_1, drop_out_1]
    # fitness(nest)


    Lb = [1, 10, 5, 0, 10, 0, 10, 0]
    Ub = [300, 500, 20, 1, 200, 1, 200, 1]

    maxgen = 30
    costfmin, bestpop = Get_CS(Lb=Lb,Ub=Ub,maxgen=maxgen)
    print('costfmin:', costfmin)
    plt.plot(costfmin)
    plt.xlabel('time')
    plt.ylabel('cost function')
    plt.show()
