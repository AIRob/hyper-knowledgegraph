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

def print_extrank_out(text):
    print('Text文本是:')
    print(text)
    print('TextRank模型结果：')
    res = textrank_extract(text)
    #res_list = res if len(res) else ['null']
    res_list = res if res else ['null']
    print(res_list)
    return res_list  

def create_drugs_node(myset,graph):
    count = 0
    i = 0
    for record in myset.find():
        print(record['disease_id'])
        disease_name = record['disease_name']
        print('疾病名：')
        print(disease_name)
        disease_name_node = Node("disease_name", name=disease_name)
        drugs_node = Node("drugs", name="药品")
        p10 = Path(disease_name_node, 'drugs', drugs_node)
        graph.create(p10)
        
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
            
            #适应症
            for j19 in range(len(indication_list)):
                sub_indication = indication_list[j19]
                sub_indication_node = Node("indication",name=sub_indication)
                p190 = p19.append('1->n',sub_indication_node)
                graph.create(p190)
             
            
            #成分
            for j20 in range(len(ingredients_list)):
                sub_ingredients = ingredients_list[j20]
                sub_ingredients_node = Node("ingredients",name=sub_ingredients)
                p200 = p20.append('1->n',sub_ingredients_node)
                graph.create(p200)
            
            #不良反应
            for j21 in range(len(adverse_reactions_list)):
                sub_adverse_reactions = adverse_reactions_list[j21]
                sub_adverse_reactions_node = Node("adverse_reactions",name=sub_adverse_reactions)
                p210 = p21.append('1->n',sub_adverse_reactions_node)
                graph.create(p210)
            #注意事项
            for j22 in range(len(precautions_list)):
                sub_precautions = precautions_list[j22]
                sub_precautions_node = Node("precautions",name=sub_precautions)
                p220 = p22.append('1->n',sub_precautions_node)
                graph.create(p220)
            #禁忌
            for j23 in range(len(taboo_list)):
                sub_taboo = taboo_list[j23]
                sub_taboo_node = Node("taboo",name=sub_taboo)
                p230 = p23.append('1->n',sub_taboo_node)
                graph.create(p230)
            #药物相互作用
            for j24 in range(len(medicine_interactions_list)):
                sub_medicine_interactions = medicine_interactions_list[j24]
                sub_medicine_interactions_node = Node("medicine_interactions",name=sub_medicine_interactions)
                p240 = p24.append('1->n',sub_medicine_interactions_node)
                graph.create(p240)
            #特殊人群用药
            for j25 in range(len(special_population_list)):
                sub_special_population = special_population_list[j25]
                sub_special_population_node = Node("special_population",name=sub_special_population)
                p250 = p25.append('1->n',sub_special_population_node)
                graph.create(p250)
            #药理作用
            for j26 in range(len(pharmacological_action_list)):
                sub_pharmacological_action = pharmacological_action_list[j26]
                sub_pharmacological_action_node = Node("pharmacological_action",name=sub_pharmacological_action)
                p260 = p26.append('1->n',sub_pharmacological_action_node)
                graph.create(p260)
            #治疗病种
            for j37 in range(len(therapeutic_diseases_list)):
                sub_therapeutic_diseases = therapeutic_diseases_list[j37]
                sub_therapeutic_diseases_node = Node("therapeutic_diseases",name=sub_therapeutic_diseases)
                p370 = p37.append('1->n',sub_therapeutic_diseases_node)
                graph.create(p370)
            i += 1
            if i > 3:break
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

        print(record['disease_id'])
        disease_id = record['disease_id']
        #disease_name = record['disease_name']
        disease_profile = record['disease_profile']
        disease_base = record['disease_base']

        disease_diagnosis = record['disease_diagnosis']
        disease_check = record['disease_check']
        disease_symptoms = record['disease_symptoms']
        disease_cause = record['disease_cause']
        disease_treat = record['disease_treat']
        how_prevent = record['how_prevent']
        qa_corpus = record['qa_corpus']
        create_time = record['create_time']
        update_time = record['update_time']
        source = record['source']

        #disease_name_node = Node("disease_name", name=disease_name)
        disease_base_node = Node("disease_base",name="疾病基本知识")
        #Multiple Nodes can be created in a single Graph command
        disease_id_node = Node("disease_id", name=disease_id)
        #疾病简介:disease_profile
        disease_profile_list = print_extrank_out(disease_profile)
        disease_profile_node = Node("disease_profile", name="疾病简介")


        disease_alias = disease_base['disease_alias']
        is_medical = disease_base['is_medical']
        incidence_site = disease_base['incidence_site']
        contagious = disease_base['contagious']
        multiple_people = disease_base['multiple_people']
        typical_symptoms = disease_base['typical_symptoms']
        complication = disease_base['complication']
        contagious_node = Node("disease_base", name=contagious)
        #别名:disease_alias
        disease_alias_node = Node("disease_base", name="别名")
        disease_alias_list = disease_alias.split(',')

        is_medical_node = Node("disease_base", name=is_medical)
        #发病部位:incidence_site
        incidence_site_node = Node("disease_base", name="发病部位")
        incidence_site_list = incidence_site.split(',')

        #多发人群:multiple_people
        multiple_people_node = Node("disease_base", name="多发人群")
        sub_multiple_people = multiple_people.split(',')[0][0]

        #典型症状:typical_symptoms
        typical_symptoms_node = Node("disease_base", name=typical_symptoms)
        typical_symptoms_list = typical_symptoms.split(',')[:-2]

        #并发症:complication
        complication_node = Node("disease_base", name="complication")
        complication_list = complication.split(',')[:-2]

        p1 = Path(disease_name_node, 'disease_base',disease_base_node)
        p11 = p1.append('disease_alias',disease_alias_node)
        p12 = p1.append('contagious',contagious_node)
        p13 = p1.append('is_medical',is_medical_node)
        p14 = p1.append('incidence_site',incidence_site_node)
        p15 = p1.append('multiple_people',multiple_people_node)
        p16 = p1.append('typical_symptoms',typical_symptoms_node)
        p17 = p1.append('complication',complication_node)
        #r11 = Path(disease_name_node, 'disease_base',disease_base_node,'disease_alias',disease_alias_node)
        p2 = Path(disease_name_node, 'disease_id', disease_id_node)
        p3 = Path(disease_name_node,'disease_profile',disease_profile_node)
        graph.create(p1)
        graph.create(p11)
        graph.create(p12)
        graph.create(p13)
        graph.create(p14)
        graph.create(p15)
        graph.create(p16)
        graph.create(p17)
        graph.create(p2)
        graph.create(p3)
        for i3 in range(len(disease_profile_list)):
            sub_disease_profile = disease_profile_list[i3]
            sub_disease_profile_node = Node("disease_profile",name=sub_disease_profile)
            p30 = p3.append('1->n',sub_disease_profile_node)
            graph.create(p30)

        for i11 in range(len(disease_alias_list)):
            sub_disease_alias = disease_alias_list[i11]
            sub_disease_alias_node = Node("disease_alias",name=sub_disease_alias)
            p110 = p11.append('1->n',sub_disease_alias_node)
            graph.create(p110)

        for i14 in range(len(incidence_site_list)):
            sub_incidence_site = incidence_site_list[i14]
            sub_incidence_site_node = Node("incidence_site",name=sub_incidence_site)
            p140 = p14.append('1->n',sub_incidence_site_node)
            graph.create(p140)

        sub_multiple_people_node = Node("multiple_people",name=sub_multiple_people)
        p150 = p15.append('1->n',sub_multiple_people_node)
        graph.create(p150)

        for i16 in range(len(typical_symptoms_list)):
            sub_typical_symptoms = typical_symptoms_list[i16]
            sub_typical_symptoms_node = Node("typical_symptoms",name=sub_typical_symptoms)
            p160 = p16.append('1->n',sub_typical_symptoms_node)
            graph.create(p160)

        for i17 in range(len(complication_list)):
            sub_complication = complication_list[i17]
            sub_complication_node = Node("complication",name=sub_complication)
            p170 = p17.append('1->n',sub_complication_node)
            graph.create(p170)
        #4 疾病诊断
        best_time = disease_diagnosis['best_time']
        duration_visit = disease_diagnosis['duration_visit']
        followup_freq = disease_diagnosis['followup_freq']
        pre_treat = disease_diagnosis['pre_treat']
        #最佳就诊时间:best_time
        best_time_node = Node("disease_diagnosis", name="最佳就诊时间")
        best_time_list = incidence_site.strip().split(',')
        #就诊时长:duration_visit
        duration_visit_node = Node("disease_diagnosis", name="就诊时长")
        duration_visit_list = duration_visit.split(',')
        #复诊频率:followup_freq
        followup_freq_node = Node("disease_diagnosis", name="复诊频率")
        followup_freq_list = print_extrank_out(followup_freq)
        #就诊前准备:pre_treat
        pre_treat_node = Node("disease_diagnosis", name="就诊前准备")
        pre_treat_list = pre_treat.split(',')
        disease_diagnosis_node = Node("disease_diagnosis",name="疾病诊断")
        p4 = Path(disease_name_node, 'disease_diagnosis',disease_diagnosis_node)
        p41 = p4.append('best_time',best_time_node)
        p42 = p4.append('duration_visit',duration_visit_node)
        p43 = p4.append('followup_freq',followup_freq_node)
        p44 = p4.append('pre_treat',pre_treat_node)
        graph.create(p4)
        graph.create(p41)
        graph.create(p42)
        graph.create(p43)
        graph.create(p44)
        for i41 in range(len(best_time_list)):
            sub_best_time = best_time_list[i41]
            sub_best_time_node = Node("best_time",name=sub_best_time)
            p410 = p41.append('1->n',sub_best_time_node)
            graph.create(p410)
        for i42 in range(len(duration_visit_list)):
            sub_duration_visit = duration_visit_list[i42]
            sub_duration_visit_node = Node("duration_visit",name=sub_duration_visit)
            p420 = p42.append('1->n',sub_duration_visit_node)
            graph.create(p420)
        for i43 in range(len(followup_freq_list)):
            sub_followup_freq = followup_freq_list[i43]
            sub_followup_freq_node = Node("followup_freq",name=sub_followup_freq)
            p430 = p43.append('1->n',sub_followup_freq_node)
            graph.create(p430)
        for i44 in range(len(pre_treat_list)):
            sub_pre_treat = pre_treat_list[i44]
            sub_pre_treat_node = Node("pre_treat",name=sub_pre_treat)
            p440 = p44.append('1->n',sub_pre_treat_node)
            graph.create(p440)
        #5 疾病检查
        check_url = disease_check['check_url']
        common_check = disease_check['common_check']
        checks = disease_check['checks']
        check_updatetime = disease_check['check_updatetime']
        check_browse_count = disease_check['browse_count']
        check_collect_count = disease_check['collect_count']
        check_url_node = Node("disease_check", name=check_url)
        #常见检查:common_check
        common_check_node = Node("disease_check", name="常见检查")
        common_check_list = print_extrank_out(common_check)
        #检查:checks
        checks_node = Node("disease_check", name="检查")
        checks_list = print_extrank_out(checks)
        check_updatetime_node = Node("disease_check", name=check_updatetime)
        check_browse_count_node = Node("disease_check", name=check_browse_count)
        check_collect_count_node = Node("disease_check", name=check_collect_count)
        disease_check_node = Node("disease_check",name="疾病检查")
        p5 = Path(disease_name_node, 'disease_check',disease_check_node)
        p51 = p5.append('check_url',check_url_node)
        p52 = p5.append('common_check',common_check_node)
        p53 = p5.append('checks',checks_node)
        p54 = p5.append('check_updatetime',check_updatetime_node)
        p55 = p5.append('check_browse_count_node',check_browse_count_node)
        p56 = p5.append('check_collect_count_node',check_collect_count_node)
        graph.create(p5)
        graph.create(p51)
        graph.create(p52)
        graph.create(p53)
        graph.create(p54)
        graph.create(p55)
        graph.create(p56)
        for i52 in range(len(common_check_list)):
            sub_common_check = common_check_list[i52]
            sub_common_check_node = Node("common_check",name=sub_common_check)
            p520 = p52.append('1->n',sub_common_check_node)
            graph.create(p520)
        for i53 in range(len(checks_list)):
            sub_checks = checks_list[i53]
            sub_checks_node = Node("checks",name=sub_checks)
            p530 = p53.append('1->n',sub_checks_node)
            graph.create(p530)
        #6 疾病症状disease_symptoms
        #6.1详细症状:detail_symptoms
        symptoms_url = disease_symptoms['detail_symptom']['symptoms_url']
        common_symptoms = disease_symptoms['detail_symptom']['common_symptoms']
        links_symptoms = disease_symptoms['detail_symptom']['links_symptoms']
        symptoms = disease_symptoms['detail_symptom']['symptoms']
        symptoms_updatetime = disease_symptoms['detail_symptom']['symptoms_updatetime']
        symptoms_browse_count = disease_symptoms['detail_symptom']['browse_count']
        symptoms_collect_count = disease_symptoms['detail_symptom']['collect_count']
        symptoms_url_node = Node("detail_symptom", name=symptoms_url)
        common_symptoms_node = Node("detail_symptom", name="主要症状")
        #主要症状:common_symptoms
        common_symptoms_list = print_extrank_out(common_symptoms)

        links_symptoms_node = Node("detail_symptom", name="相关症状")
        #相关症状:links_symptoms
        links_symptoms_list = links_symptoms.split(' ')[1:]

        symptoms_node = Node("detail_symptom", name="症状")
        #症状:symptoms
        symptoms_list = print_extrank_out(symptoms)

        symptoms_updatetime_node = Node("detail_symptom", name=symptoms_updatetime)
        symptoms_browse_count_node = Node("detail_symptom", name=symptoms_browse_count)
        symptoms_collect_count_node = Node("detail_symptom", name=symptoms_collect_count)
        disease_symptoms_node = Node("detail_symptom",name="疾病检查")
        detail_symptom_node = Node("disease_symptoms",name="详细症状")
        #complication_node = Node("complication",name="详细并发症")
        p600 = Path(disease_name_node, 'disease_symptoms',disease_symptoms_node)
        p6 = p600.append('detail_symptom',detail_symptom_node)
        p61 = p6.append('symptoms_url',symptoms_url_node)
        p62 = p6.append('common_symptoms',common_symptoms_node)
        p63 = p6.append('links_symptoms',links_symptoms_node)
        p64 = p6.append('symptoms',symptoms_node)
        p65 = p6.append('symptoms_updatetime',symptoms_updatetime_node)
        p66 = p6.append('symptoms_browse_count',symptoms_browse_count_node)
        p67 = p6.append('symptoms_collect_count',symptoms_collect_count_node)
        graph.create(p600)
        graph.create(p6)
        graph.create(p61)
        graph.create(p62)
        graph.create(p63)
        graph.create(p64)
        graph.create(p65)
        graph.create(p66)
        graph.create(p67)
        for i62 in range(len(common_symptoms_list)):
            sub_common_symptoms = common_symptoms_list[i62]
            sub_common_symptoms_node = Node("common_symptoms",name=sub_common_symptoms)
            p620 = p62.append('1->n',sub_common_symptoms_node)
            graph.create(p620)
        for i63 in range(len(links_symptoms_list)):
            sub_links_symptoms = links_symptoms_list[i63]
            sub_links_symptoms_node = Node("links_symptoms",name=sub_links_symptoms)
            p630 = p63.append('1->n',sub_links_symptoms_node)
            graph.create(p630)
        for i64 in range(len(symptoms_list)):
            sub_symptoms = symptoms_list[i64]
            sub_symptoms_node = Node("symptoms",name=sub_symptoms)
            p640 = p64.append('1->n',sub_symptoms_node)
            graph.create(p640)

        #6.2并发症:complication
        complication_url = disease_symptoms['complication']['complication_url']
        common_complication = disease_symptoms['complication']['common_complication']
        complication_detail = disease_symptoms['complication']['complication']
        complication_updatetime = disease_symptoms['complication']['complication_updatetime']
        complication_browse_count = disease_symptoms['complication']['browse_count']
        complication_collect_count = disease_symptoms['complication']['collect_count']
        complication_url_node = Node("complication", name=complication_url)
        common_complication_node = Node("complication", name="常见并发症")
        #常见并发症:common_complication
        common_complication_list = common_complication.split(' ')

        complication_detail_node = Node("complication", name="并发症")
        #并发症:complication
        complication_detail_list = print_extrank_out(complication_detail)

        complication_updatetime_node = Node("complication", name=complication_updatetime)
        complication_browse_count_node = Node("complication", name=complication_browse_count)
        complication_collect_count_node = Node("complication", name=complication_collect_count)
        complication_node = Node("complication",name="详细并发症")
        #p60 = Path(disease_name_node, 'disease_symptoms',disease_symptoms_node,'complication',complication_node)
        p60 = p600.append('complication',complication_node)
        p601 = p60.append('complication_url',complication_url_node)
        p602 = p60.append('common_complication',common_complication_node)
        p603 = p60.append('complication_detail',complication_detail_node)
        p604 = p60.append('complication_updatetime',complication_updatetime_node)
        p605 = p60.append('complication_browse_count',complication_browse_count_node)
        p606 = p60.append('complication_collect_count',complication_collect_count_node)
        graph.create(p60)
        graph.create(p601)
        graph.create(p602)
        graph.create(p603)
        graph.create(p604)
        graph.create(p605)
        graph.create(p606)
        for i602 in range(len(common_complication_list)):
            sub_common_complication = common_complication_list[i602]
            sub_common_complication_node = Node("common_complication",name=sub_common_complication)
            p6020 = p602.append('1->n',sub_common_complication_node)
            graph.create(p6020)
        for i603 in range(len(complication_detail_list)):
            sub_complication_detail = complication_detail_list[i603]
            sub_complication_detail_node = Node("complication_detail",name=sub_complication_detail)
            p6030 = p603.append('1->n',sub_complication_detail_node)
            graph.create(p6030)
        #7疾病病因:disease_cause
        disease_cause_node = Node("disease_cause", name="疾病病因")
        disease_cause_list = print_extrank_out(disease_cause)
        p7 = Path(disease_name_node, 'disease_cause', disease_cause_node)
        graph.create(p7)
        for i7 in range(len(disease_cause_list)):
            sub_disease_cause = disease_cause_list[i7]
            sub_disease_cause_node = Node("disease_cause",name=sub_disease_cause)
            p70 = p7.append('1->n',sub_disease_cause_node)
            graph.create(p70)
        #8疾病治疗:disease_treat
        treat_method = disease_treat['treat_method']
        treat_costs = disease_treat['treat_costs']
        cure_rate = disease_treat['cure_rate']
        treat_cycle = disease_treat['treat_cycle']
        common_drugs = disease_treat['common_drugs']
        visit_department = disease_treat['visit_department']
        treat_method_node = Node("disease_treat", name="治疗方法")
        #治疗方法:treat_method
        treat_method_list = print_extrank_out(treat_method)

        treat_costs_node = Node("disease_treat", name=treat_costs)

        cure_rate_node = Node("disease_treat", name=cure_rate)

        treat_cycle_node = Node("disease_treat", name=treat_cycle)

        common_drugs_node = Node("disease_treat", name="常用药品")
        #常用药品:common_drugs
        common_drugs_list = common_drugs.split(',')[:-2]

        visit_department_node = Node("disease_treat", name="就诊科室")
        #就诊科室:visit_department
        visit_department_list = visit_department.split(',')[:-1]

        disease_treat_node = Node("disease_treat",name="疾病治疗")
        p8 = Path(disease_name_node, 'disease_treat',disease_treat_node)
        p81 = p8.append('treat_method',treat_method_node)
        p82 = p8.append('treat_costs',treat_costs_node)
        p83 = p8.append('cure_rate',cure_rate_node)
        p84 = p8.append('treat_cycle',treat_cycle_node)
        p85 = p8.append('common_drugs',common_drugs_node)
        p86 = p8.append('visit_department',visit_department_node)
        graph.create(p8)
        graph.create(p81)
        graph.create(p82)
        graph.create(p83)
        graph.create(p84)
        graph.create(p85)
        graph.create(p86)
        for i81 in range(len(treat_method_list)):
            sub_treat_method = treat_method_list[i81]
            sub_treat_method_node = Node("treat_method",name=sub_treat_method)
            p810 = p81.append('1->n',sub_treat_method_node)
            graph.create(p810)
        for i85 in range(len(common_drugs_list)):
            sub_common_drugs = common_drugs_list[i85]
            sub_common_drugs_node = Node("common_drugs",name=sub_common_drugs)
            p850 = p85.append('1->n',sub_common_drugs_node)
            graph.create(p850)
        for i86 in range(len(visit_department_list)):
            sub_visit_department = visit_department_list[i86]
            sub_visit_department_node = Node("visit_department",name=sub_visit_department)
            p860 = p86.append('1->n',sub_visit_department_node)
            graph.create(p860)
        #9durgs药品

        #9如何预防:how_prevent
        how_prevent_node = Node("how_prevent", name="如何预防")
        how_prevent_list = print_extrank_out(how_prevent)
        p10 = Path(disease_name_node, 'how_prevent', how_prevent_node)
        graph.create(p10)
        for i10 in range(len(how_prevent_list)):
            sub_how_prevent = how_prevent_list[i10]
            sub_how_prevent_node = Node("how_prevent",name=sub_how_prevent)
            p100 = p10.append('1->n',sub_how_prevent_node)
            graph.create(p100)

        #11问答语料:qa_corpus
        '''
        qa_corpus_node = Node("qa_corpus", name=qa_corpus)
        p11 = Path(disease_name_node, 'qa_corpus', qa_corpus_node)
        graph.create(p11)
        '''
        qa_corpus_node = Node("qa_corpus",name="问答语料")
        #p10 = Path(disease_name_node, '1->n',disease_treat_node)
        p11 = Path(disease_name_node, 'qa_corpus', qa_corpus_node)
        graph.create(p11)
        for i in range(len(qa_corpus)):
            sub_qa_data = qa_corpus[i]
            sub_qa_data_node = Node("qa_corpus",name="预料对")
            sub_qa_data_list = print_extrank_out(sub_qa_data)

            p110 = p11.append('1->n',sub_qa_data_node)
            graph.create(p110)
            for i110 in range(len(sub_qa_data_list)):
                sub_sub_qa_data = sub_qa_data_list[i110]
                sub_sub_qa_data_node = Node("sub_qa_data",name=sub_sub_qa_data)
                p1100 = p110.append('1->n',sub_sub_qa_data_node)
                graph.create(p1100)

        #12入库时间:create_time
        create_time_node = Node("create_time", name=create_time)
        p12 = Path(disease_name_node, 'create_time', create_time_node)
        graph.create(p12)
        #13更新时间:update_time
        update_time_node = Node("update_time", name=update_time)
        p13 = Path(disease_name_node, 'update_time', update_time_node)
        graph.create(p13)
        #14来源:source
        source_node = Node("source", name=source)
        p14 = Path(disease_name_node, 'source', source_node)
        graph.create(p14)
        count += 1
        #if count > 3:break
    print(count)

def main():
    py2neo.authenticate("localhost:7474", "neo4j", "airob")   
    graph = Graph("http://localhost:7474/db/data/")
    print("Start Creating Nodes")
    ip = '127.0.0.1'
    port = 27017
    myset = connect(ip,port)
    create_drugs_node(myset,graph)


if __name__ == '__main__':
    import time
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    main()
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    