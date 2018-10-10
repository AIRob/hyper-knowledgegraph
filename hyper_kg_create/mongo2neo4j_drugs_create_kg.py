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

            '''
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
            indication_list = print_extrank_out(indication)
            functions_list = print_extrank_out(functions)
            ingredients_list = print_extrank_out(ingredients)
            adverse_reactions_list = print_extrank_out(adverse_reactions)
            precautions_list = print_extrank_out(precautions)
            taboo_list = print_extrank_out(taboo)
            medicine_interactions_list = print_extrank_out(medicine_interactions)
            
            pharmacological_action_list = print_extrank_out(pharmacological_action)
            special_population_list = print_extrank_out(special_population)
            therapeutic_diseases_list = therapeutic_diseases
            #dosage_list = print_extrank_out(dosage)
            #storage_list = print_extrank_out(storage)

            #production_address_list = print_extrank_out(production_address)
            
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
            p16 = p1.append('therapeutic_disease',therapeutic_disease_node)
            p17 = p1.append('approval_rum',approval_rum_node)

            #indication 适应症
            indication_node = Node("drugsinfo", name="适应症")
            #功能主治:functions
            functions_node = Node("drugsinfo", name="功能主治")
            #成份:ingredients
            ingredients_node = Node("drugsinfo", name="成份")
            #不良反应:adverse_reactions 
            adverse_reactions_node = Node("drugsinfo", name="不良反应")
            #注意事项:precautions
            precautions_node = Node("drugsinfo", name="注意事项")
            #禁忌:taboo
            taboo_node = Node("drugsinfo", name="禁忌")
            #药物相互作用
            #medicine_interactions_node = Node("drugsinfo", name=medicine_interactions)
            medicine_interactions_node = Node("drugsinfo", name="药物相互作用")
            
            p18 = p1.append('functions',functions_node)
            p19 = p1.append('indication',indication_node)
            p20 = p1.append('ingredients',ingredients_node)
            p21 = p1.append('adverse_reactions',adverse_reactions_node)
            p22 = p1.append('precautions',precautions_node)
            p23 = p1.append('taboo',taboo_node)
            p24 = p1.append('medicine_interactions',medicine_interactions_node)
           
            #药理作用:pharmacological_action
            pharmacological_action_node = Node("drugsinfo", name="药理作用")
            #特殊人群用药:special_population
            special_population_node = Node("drugsinfo", name="特殊人群用药")
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
            p30 = p1.append('drug_form',drug_form_node)
            p31 = p1.append('drug_spec',drug_spec_node)

            manual_revision_date_node = Node("drugsinfo", name=manual_revision_date)
            manufacturer_node = Node("drugsinfo", name=manufacturer)
            business_short_name_node = Node("drugsinfo", name=business_short_name)
            production_address_node = Node("drugsinfo", name=production_address)
            business_number_node = Node("drugsinfo", name=business_number)
            #治疗病种:therapeutic_diseases
            therapeutic_diseases_node = Node("drugsinfo", name="治疗病种")
            p32 = p1.append('manufacturer',manufacturer_node)
            p33 = p1.append('manual_revision_date',manual_revision_date_node)
            p34 = p1.append('business_short_name',business_short_name_node)
            p35 = p1.append('production_address',production_address_node)
            p36 = p1.append('business_number',business_number_node)
            p37 = p1.append('therapeutic_diseases',therapeutic_diseases_node)   
            
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
            #功能主治
            for j18 in range(len(functions_list)):
                sub_functions = functions_list[j18]
                sub_functions_node = Node("functions",name=sub_functions)
                p180 = p18.append('1->n',sub_functions_node)
                graph.create(p180)
            print(j18)
            #适应症
            for j19 in range(len(indication_list)):
                sub_indication = indication_list[j19]
                sub_indication_node = Node("indication",name=sub_indication)
                p190 = p19.append('1->n',sub_indication_node)
                graph.create(p190)
            print(j19) 
            
            #成分
            for j20 in range(len(ingredients_list)):
                sub_ingredients = ingredients_list[j20]
                sub_ingredients_node = Node("ingredients",name=sub_ingredients)
                p200 = p20.append('1->n',sub_ingredients_node)
                graph.create(p200)
            print(j20)
            
            #不良反应
            for j21 in range(len(adverse_reactions_list)):
                sub_adverse_reactions = adverse_reactions_list[j21]
                sub_adverse_reactions_node = Node("adverse_reactions",name=sub_adverse_reactions)
                p210 = p21.append('1->n',sub_adverse_reactions_node)
                graph.create(p210)
            print(j21)
            #注意事项
            for j22 in range(len(precautions_list)):
                sub_precautions = precautions_list[j22]
                sub_precautions_node = Node("precautions",name=sub_precautions)
                p220 = p22.append('1->n',sub_precautions_node)
                graph.create(p220)
            print(j22)

            #禁忌
            for j23 in range(len(taboo_list)):
                sub_taboo = taboo_list[j23]
                sub_taboo_node = Node("taboo",name=sub_taboo)
                p230 = p23.append('1->n',sub_taboo_node)
                graph.create(p230)
            print(j23)
            #药物相互作用
            for j24 in range(len(medicine_interactions_list)):
                sub_medicine_interactions = medicine_interactions_list[j24]
                sub_medicine_interactions_node = Node("medicine_interactions",name=sub_medicine_interactions)
                p240 = p24.append('1->n',sub_medicine_interactions_node)
                graph.create(p240)
            print(j24)

            #特殊人群用药
            for j25 in range(len(special_population_list)):
                sub_special_population = special_population_list[j25]
                sub_special_population_node = Node("special_population",name=sub_special_population)
                p250 = p25.append('1->n',sub_special_population_node)
                graph.create(p250)
            print(j25)

            #药理作用
            for j26 in range(len(pharmacological_action_list)):
                sub_pharmacological_action = pharmacological_action_list[j26]
                sub_pharmacological_action_node = Node("pharmacological_action",name=sub_pharmacological_action)
                p260 = p26.append('1->n',sub_pharmacological_action_node)
                graph.create(p260)
            print(j26)
            #治疗病种
            for j37 in range(len(therapeutic_diseases_list)):
                sub_therapeutic_diseases = therapeutic_diseases_list[j37]
                sub_therapeutic_diseases_node = Node("therapeutic_diseases",name=sub_therapeutic_diseases)
                p370 = p37.append('1->n',sub_therapeutic_diseases_node)
                graph.create(p370)
            print(j37)
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
