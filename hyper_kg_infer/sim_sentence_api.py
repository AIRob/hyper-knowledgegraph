from __future__ import unicode_literals, print_function, division
from simhash import Simhash 
import numpy as np 
import math
import Levenshtein as ls
import pandas as pd 
from bot_doc2vec_models import doc2vec_calc_sim,doc2vec_train
from question_siamese import siamese_calc_sim,siamese_train


class SimWord(object):
    """docstring for SimWord"""
    def __init__(self):
        pass
        
    def simhash_func(self,str1,str2):
        '''
        simhash计算唯一性
        '''
        res =  Simhash(str1).distance(Simhash(str2))
        return res

    def numsim_func(self,num1,num2):
        '''
        数值大小唯一性识别，比如0.87与0.88是非常接近的
        '''
        mid = (num1 + num2)/2.0
        numres = np.sqrt((math.pow(num1-mid,2)+math.pow(num2-mid,2)) / 2.0) / mid
        return numres

    def jaro_winkler_func(self,str1,str2):
        '''
        编辑距离jaro_winkler算法
        参考https://www.cnblogs.com/zangrunqiang/p/6752430.html
        针对多字错字错位的情况相似度特高测试代码dis_test.py效果挺好
        '''
        res = ls.jaro_winkler(str1,str2)
        return res

    def dislocation_func(self,str1,str2):
        '''
        编辑距离jaro_winkler算法
        参考https://www.cnblogs.com/zangrunqiang/p/6752430.html
        针对多字错字错位的情况相似度效果不佳
        '''   
        res = ls.ratio(str1,str2)
        return res

    def distance_func(self,str1,str2):
        '''
        编辑距离jaro_winkler算法
        参考https://www.cnblogs.com/zangrunqiang/p/6752430.html
        针对多字错字错位的情况相似度效果不佳
        '''
        res = ls.distance(str1,str2)
        return res

def simhash_x(sentence):
    pass
    

def doc2vec_sim_reply(sentence,metadata):
    doc2vec_sim = doc2vec_calc_sim(sentence,metadata)
    print(doc2vec_sim)
    if doc2vec_sim > 0.9:
        return '1'
    else:
        return '0'

def simhash_sim_reply(sentence,metadata):
    sw = SimWord()
    simhash_sim = sw.simhash_func(sentence,metadata)
    print(simhash_sim)
    if simhash_sim < 0.1:
        return '1'
    else:
        return '0'

def jaro_winkler_sim_reply(sentence,metadata):
    sw = SimWord()
    jaro_winkler_sim = sw.jaro_winkler_func(sentence,metadata)
    print(jaro_winkler_sim)
    if jaro_winkler_sim > 0.95:
        return '1'
    else:
        return '0'

def siamese_sim_reply(sentence,metadata):
    siamese_sim = siamese_calc_sim(sentence,metadata)
    print(siamese_sim)
    if siamese_sim > 0.9 and siamese_sim < 1.0:
        return '1'
    else:
        return '0'

def vote_sim_reply(sentence,metadata):
    doc2vec_sim = doc2vec_sim_reply(sentence,metadata)
    simhash_sim = simhash_sim_reply(sentence,metadata)
    jaro_winkler_sim = jaro_winkler_sim_reply(sentence,metadata)
    siamese_sim = jaro_winkler_sim_reply(sentence,metadata)
    sum_sim = doc2vec_sim + simhash_sim + jaro_winkler_sim + siamese_sim
    if float(sum_sim) > 1.0:
        return metadata
    else:
        return sentence
    
def main():
    str1 = '高血压，动脉硬化失眠.，怎么办？'
    str2 = '高血压，动脉硬化失眠，怎么办？'
    str3 = '朋友是高血压引发的肾病患者，想知道高血压导致的肾病的患者需要怎么饮食？'
    str4 = '朋友是高血压引发的肾病患者，想知道高血压引发的肾病患者的危害有哪些呢？'
    str5 = '失眠会引起高血压吗'
    str6 = '高血压者偶尔失眠怎么办？'
    str7 = '高血压心脏病能做飞机吗'
    str8 = '高血压心脏病能坐飞机吗'
    sentence = '高血压，失眠，怎么办？'
    metadata = '高血压，动脉硬化失眠，怎么办？'
    simhash_x(str1)
    simhash_x(str2)
    simhash_x(str5)
    print(vote_sim_reply(sentence,metadata))
    print(vote_sim_reply(str1,metadata))
    print(vote_sim_reply(str3,metadata))
    print(vote_sim_reply(str5,metadata))
    print(vote_sim_reply(str7,metadata))
    
if __name__ == '__main__':
    #siamese_train()
    #doc2vec_train()
    main()
