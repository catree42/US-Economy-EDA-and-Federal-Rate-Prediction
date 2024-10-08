# 평가 지표 계산 함수 정의
import numpy as np

def mae(pred, actual) :
    return np.abs(pred-actual).mean()

def mse(pred,actual):
    return ((pred-actual)**2).mean()

def rmse(pred,actual):
    return np.sqrt(mse(pred,actual))