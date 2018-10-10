
match(n) return n;
match (n:drugsinfo) return n limit 10;
#删除节点及关系
MATCH (n)-[r]-() DELETE n,r;

#单纯删除所以节点：
MATCH (n) DELETE n;

#查询
MATCH (n{name:"疾病简介"}) RETURN n
MATCH (n{name:"疾病基本知识"}) RETURN n

MATCH (n{name:"详细症状"}) RETURN n
MATCH (n{name:"疾病病因"}) RETURN n
MATCH (n{name:"疾病检查"}) RETURN n
MATCH (n{name:"复诊频率"}) RETURN n
MATCH (n{name:"疾病诊断"}) RETURN n
MATCH (n{name:"发病部位"}) RETURN n
MATCH (n{name:"治疗方法"}) RETURN n
MATCH (n{name:"常用药品"}) RETURN n

MATCH (n{name:"如何预防"}) RETURN n
#咨询药品
MATCH (n{name:"奥美沙坦酯片"}) RETURN n
MATCH (n{name:"盐酸阿罗洛尔片"}) RETURN n
MATCH (n{name:"氯沙坦钾氢氯噻..."}) RETURN n
MATCH (n{name:"氯沙坦钾氢氯噻"}) RETURN n

#查询多级
match (n1:disease_name)-[re]->(n2:disease_treat) where n1.name = "高血压" return n1,re,n2
match data=(n1:disease_name{name:"高血压"})-[re]->(n2:disease_treat) return data
match (n1:disease_name)-[re]->(n2:disease_treat) where n1.name = "高血压" WITH n1,re,n2 match (n2:disease_treat)-[re2]->(n3:treat_method) return n1,re,n2,re2,n3
match data=(n1:disease_name{name:"高血压"})-[re]->(n2:disease_treat)-[re2]->(n3:treat_method) return data
match data=(n0:disease_name{name:"高血压"})-[*1..5]->(n1:drugsinfo{name:"奥美沙坦酯片"})-[*1..3]->(n2:therapeutic_diseases) return data

match data=(n0:disease_name{name:"高血压"})-[*1..5]->(n1:drugsinfo{name:"盐酸阿罗洛尔片"})-[*1..3]->(n2:therapeutic_diseases) return data





match (na:company)-[re]->(nb:company) where na.id = '12399145' WITH na,re,nb match (nb:company)-[re2]->(nc:company) return na,re,nb,re2,nc

/*
match (n1:disease_name)-[re]->(n2{name:"药品"}) where n1.isease_name = "高血压" WITH n1,re,n2 match (n2{name:"药品"})-[re2]->(n3{name:"氯沙坦钾氢氯噻"}) return n1,re,n2,re2,n3
match data=(na:company{id:'12399145'})-[re]->(nb:company)-[re2]->(nc:company) return data
match (n2{name:"药品"})-[re2]->(n3{name:"氯沙坦钾氢氯噻"}) return n2,re2,n3
match (n2:drugs)-[re2]->(n3:drugsinfo)  where n3.goods_common_name = "氯沙坦钾氢氯噻" return n2,re2,n3
match (n2:drugs)-[re2]->(n3:drugsinfo) where n3.name = "氯沙坦钾氢氯噻" return n2,re2,n3

match (n1:drugsinfo)-[re]->(n2:therapeutic_diseases) where n1.name = "奥美沙坦酯片" return n1,re,n2
match data=(n1:drugsinfo{name:"奥美沙坦酯片"})-[re]->(n2:therapeutic_diseases) return data
match data=(n0:disease_name{name:"高血压"})-[re]->(n1:drugsinfo{name:"奥美沙坦酯片"})-[re2]->(n2:therapeutic_diseases) return data

match data=(n0:disease_name{name:"高血压"})-[re]->(n1:drugsinfo)-[re2]->(n2:therapeutic_diseases) return data

match data=(n0:disease_name{name:"高血压"})-[*1..3]->(n1:drugsinfo)-[re2]->(n2:therapeutic_diseases) return data

match data=(n0:disease_name{name:"高血压"})-[*1..3]->(n1:drugsinfo{name:"奥美沙坦酯片"})-[re2]->(n2:therapeutic_diseases) return data
match data=(n0:disease_name{name:"高血压"})-[*1..5]->(n1:drugsinfo{name:"奥美沙坦酯片"})-[re2]->(n2:therapeutic_diseases) return data

*/
match (n1:disease_name)-[re]->(n2:disease_treat) where n1.name = "高血压" return n1,re,n2
match data=(n1:disease_name{name:"高血压"})-[re]->(n2:disease_treat) return data
match (n1:disease_name)-[re]->(n2:disease_treat) where n1.name = "高血压" WITH n1,re,n2 match (n2:disease_treat)-[re2]->(n3:treat_method) return n1,re,n2,re2,n3
match data=(n1:disease_name{name:"高血压"})-[re]->(n2:disease_treat)-[re2]->(n3:treat_method) return data
match data=(n0:disease_name{name:"高血压"})-[*1..5]->(n1:drugsinfo{name:"奥美沙坦酯片"})-[*1..3]->(n2:therapeutic_diseases) return data

match data=(n0:disease_name{name:"高血压"})-[*1..5]->(n1:drugsinfo{name:"盐酸阿罗洛尔片"})-[*1..3]->(n2:therapeutic_diseases) return data

