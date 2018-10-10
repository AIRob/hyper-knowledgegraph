import py2neo
from py2neo import Graph,Node,Relationship,Rev,Path
from pymongo import MongoClient
from keywordAPI import *


POS = True
#hyper_disease_drugs_qa hyper_big_disease
def connect(ip,port):
    conn = MongoClient(ip,port)
    db = conn.hyper_disease_drugs_qa
    myset = db.hyper_big_disease
    #db = conn.xxxx
    #myset = db.xxxxx
    return myset

def print_out(text):
    seg_list = seg_to_list(text, POS)
    filter_list = word_filter(seg_list, POS)

    print('Text文本是:')
    print(text)
    print('TF-IDF模型结果：')
    print(tfidf_extract(filter_list))
    print('TextRank模型结果：')
    print(textrank_extract(text))
    print('LSI模型结果：')
    print(topic_extract(filter_list, 'LSI', POS))
    print('LDA模型结果：')
    print(topic_extract(filter_list, 'LDA', POS))
    print('HDP模型结果：')
    print(topic_extract(filter_list, 'HDP', POS))

def print_extrank_filter_out(text):
    seg_list = seg_to_list(text, POS)
    filter_list = word_filter(seg_list, POS)

    print('Text文本是:')
    print(text)
    print('TextRank模型结果：')
    print(textrank_extract(' '.join(filter_list)))

def print_extrank_out(text):
    print('Text文本是:')
    print(text)
    print('TextRank模型结果：')
    res = textrank_extract(text)
    #res_list = res if len(res) else ['null']
    res_list = res if res else ['null']
    print(res_list)
    return res_list     
    #print(res)
    #return res

def create_drugs_node(myset,graph):
    for record in myset.find():
        print(record['disease_id'])
        disease_name = record['disease_name']
        print('疾病名：')
        print(disease_name)
        disease_name_node = Node("disease_name", name=disease_name)
        drugs_node = Node("drugs", name="药品")
        p10 = Path(disease_name_node, 'drugs', drugs_node)
        graph.create(p10)
        i = 0
        for drugs in record['drugs']:
            goods_id  = drugs['goods_id'] if drugs['goods_id'] is not "null" else "null"
            goods_common_name = drugs['goods_common_name'] if drugs['goods_common_name'] is not "null" else "null"
            goods_name = drugs['goods_name'] if drugs['goods_name'] is not "null" else "null"
            goods_english_name = drugs['goods_english_name'] if drugs['goods_english_name'] is not "null" else "null"
            goods_price = drugs['goods_price'] if drugs['goods_price'] is not "null" else "null"
            therapeutic_disease = drugs['therapeutic_disease'] if drugs['therapeutic_disease'] is not "null" else "null"
            approval_rum = drugs['approval_rum'] if drugs['approval_rum'] is not "null" else "null"

            print('药品通用名：')
            print(goods_common_name)

            indication = drugs['indication'] if drugs['indication'] is not "null" else "null"
            functions = drugs['functions'] if drugs['functions'] is not "null" else "null"
            ingredients = drugs['ingredients'] if drugs['ingredients'] is not "null" else "null"
            adverse_reactions = drugs['adverse_reactions'] if drugs['adverse_reactions'] is not "null" else "null"
            precautions = drugs['precautions'] if drugs['precautions'] is not "null" else "null"
            taboo = drugs['taboo'] if drugs['taboo'] is not "null" else "null"
            medicine_interactions = drugs['medicine_interactions'] if drugs['medicine_interactions'] is not "null" else "null"

            pharmacological_action = drugs['pharmacological_action'] if drugs['pharmacological_action'] is not "null" else "null"
            special_population = drugs['special_population'] if drugs['special_population'] is not "null" else "null"
            dosage = drugs['dosage'] if drugs['dosage'] is not "null" else  "null"
            storage = drugs['storage'] if drugs['storage'] is not "null" else  "null"
            validity_period = drugs['validity_period'] if drugs['validity_period'] is not "null" else "null"
            drug_form = drugs['drug_form'] if drugs['drug_form'] is not "null" else "null"
            drug_spec = drugs['drug_spec'] if drugs['drug_spec'] is not "null" else "null"

            manual_revision_date = drugs['manual_revision_date'] if drugs['manual_revision_date'] is not "null" else "null"
            manufacturer = drugs['manufacturer'] if drugs['manufacturer'] is not "null" else "null"
            business_short_name = drugs['business_short_name'] if drugs['business_short_name'] is not "null" else "null"
            production_address = drugs['production_address'] if drugs['production_address'] is not "null" else "null"
            business_number = drugs['business_number'] if drugs['business_number'] is not "null" else "null"
            therapeutic_diseases = drugs['therapeutic_diseases'] if drugs['therapeutic_diseases'] is not "null" else "null"
            print_extrank_out(indication)
            print_extrank_out(functions)
            print_extrank_out(ingredients)
            print_extrank_out(adverse_reactions)
            print_extrank_out(precautions)
            print_extrank_out(taboo)
            print_extrank_out(medicine_interactions)

            print_extrank_out(pharmacological_action)
            print_extrank_out(special_population)
            print_extrank_out(dosage)
            print_extrank_out(storage)

            print_extrank_out(production_address)
            '''
            goods_id_node = Node("drugsinfo", name=goods_id)
            goods_common_name_node = Node("drugsinfo", name=goods_common_name)
            goods_name_node = Node("drugsinfo", name=goods_name)
            goods_english_name_node = Node("drugsinfo", name=goods_english_name)
            goods_price_node = Node("drugsinfo", name=goods_price)
            therapeutic_disease_node = Node("drugsinfo", name=therapeutic_disease)
            approval_rum_node = Node("drugsinfo", name=approval_rum)
            #p11 = p1.append('goods_common_name',goods_common_name_node)
            p1 = Path(drugs_node, '1->n', goods_common_name_node)
            graph.create(p1)
            p12 = p1.append('goods_id',goods_id_node)
            p13 = p1.append('goods_name',goods_name_node)
            p14 = p1.append('goods_english_name',goods_english_name_node)
            p15 = p1.append('goods_price',goods_price_node)
            p16 = p1.append('therapeutic_disease',therapeutic_disease)
            p17 = p1.append('approval_rum',approval_rum_node)

            indication_node = Node("drugsinfo", name=indication)
            functions_node = Node("drugsinfo", name=functions)
            ingredients_node = Node("drugsinfo", name=ingredients)
            adverse_reactions_node = Node("drugsinfo", name=adverse_reactions)
            precautions_node = Node("drugsinfo", name=precautions)
            taboo_node = Node("drugsinfo", name=taboo)
            medicine_interactions_node = Node("drugsinfo", name=medicine_interactions)
            p18 = p1.append('functions',functions_node)
            p19 = p1.append('indication',indication_node)
            p20 = p1.append('ingredients',ingredients_node)
            p21 = p1.append('adverse_reactions',adverse_reactions_node)
            p22 = p1.append('precautions',precautions_node)
            p23 = p1.append('taboo',taboo)
            p24 = p1.append('medicine_interactions',medicine_interactions_node)

            pharmacological_action_node = Node("drugsinfo", name=pharmacological_action)
            special_population_node = Node("drugsinfo", name=special_population)
            dosage_node = Node("drugsinfo", name=dosage)
            storage_node = Node("drugsinfo", name=storage)
            validity_period_node = Node("drugsinfo", name=validity_period)
            drug_form_node = Node("drugsinfo", name=drug_form)
            drug_spec_node = Node("drugsinfo", name=drug_spec)
            p25 = p1.append('special_population',special_population_node)
            p26 = p1.append('pharmacological_action',pharmacological_action_node)
            p27 = p1.append('dosage',dosage_node)
            p28 = p1.append('storage',storage_node)
            p29 = p1.append('validity_period',validity_period_node)
            p30 = p1.append('drug_form',drug_form)
            p31 = p1.append('drug_spec',drug_spec_node)

            manual_revision_date_node = Node("drugsinfo", name=manual_revision_date)
            manufacturer_node = Node("drugsinfo", name=manufacturer)
            business_short_name_node = Node("drugsinfo", name=business_short_name)
            production_address_node = Node("drugsinfo", name=production_address)
            business_number_node = Node("drugsinfo", name=business_number)
            therapeutic_diseases_node = Node("drugsinfo", name=therapeutic_diseases)
            p32 = p1.append('manufacturer',manufacturer_node)
            p33 = p1.append('manual_revision_date',manual_revision_date_node)
            p34 = p1.append('business_short_name',business_short_name_node)
            p35 = p1.append('production_address',production_address_node)
            p36 = p1.append('business_number',business_number_node)
            p37 = p1.append('therapeutic_diseases',therapeutic_diseases)   
            
            #graph.create(p11)
            graph.create(p12)
            graph.create(p13)
            graph.create(p14)
            graph.create(p15)
            graph.create(p16)
            graph.create(p17)
            graph.create(p18)
            graph.create(p19)
            graph.create(p20)
            graph.create(p21)
            graph.create(p22)
            graph.create(p23)
            graph.create(p24)
            graph.create(p25)
            graph.create(p26)
            graph.create(p27)
            graph.create(p28)
            graph.create(p29)
            graph.create(p30)
            graph.create(p31)
            graph.create(p32)
            graph.create(p33)
            graph.create(p34)
            graph.create(p35)
            graph.create(p36)
            graph.create(p37)
            '''
            i += 1
            #if i > 10:break
            '''
            graph.create(p)
            graph.create(p)
            graph.create(p)
            graph.create(p)
            graph.create(p)
            graph.create(p)
            graph.create(p)
            '''
            print(i)
            
        print(i)

def main():
    py2neo.authenticate("localhost:7474", "neo4j", "airob")   
    graph = Graph("http://localhost:7474/db/data/")
    print("Start Creating Nodes")
    ip = '127.0.0.1'
    port = 27017
    myset = connect(ip,port)
    create_drugs_node(myset,graph)

if __name__ == '__main__':
    main()

 

