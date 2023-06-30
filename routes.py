from flask import render_template, request
from owlready2 import *
from utils import pre_process
from app import app

prefix = '''
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX ref: <http://www.semanticweb.org/ssharani/ontologies/2022/RefugeeHomeReturnOntology#>
'''

@app.get('/')
def hello():
    return render_template('index.html'), 200

@app.route('/returnee', methods=['POST'])
def returnee():
    
    select = '''
    SELECT DISTINCT ?refugee ?refAgency ?trans ?reintegrationSocialCapital ?reintegrationEconomicWellbeing ?reintegrationPoliticalProcess ?homeBelonging ?homeAttachment ?homeMaking
    WHERE {
        {
            ?refugee ref:hasAgency ?refAgency .
            ?refAgency rdf:type ref:HighAgency .
            ?refugee ref:practiceTransnationalism ?trans .
        } UNION {
            ?refugee ref:hasAgency ?refAgency .
            ?refAgency rdf:type ref:HighAgency .
            ?refugee ref:hasExpectedLevelOfReintegration ?reintegrationSocialCapital .
            ?reintegrationSocialCapital rdf:type ref:SocialCapital .
        } UNION {
            ?refugee ref:hasAgency ?refAgency .
            ?refAgency rdf:type ref:HighAgency .
            ?refugee ref:hasExpectedLevelOfReintegration ?reintegrationEconomicWellbeing .
            ?reintegrationEconomicWellbeing rdf:type ref:EconomicWellbeing .
        } UNION {
            ?refugee ref:hasAgency ?refAgency .
            ?refAgency rdf:type ref:HighAgency .
            ?refugee ref:hasExpectedLevelOfReintegration ?reintegrationPoliticalProcess .
            ?reintegrationPoliticalProcess rdf:type ref:PoliticalProcess .
        } UNION {
            ?refugee ref:belongTo ?homeBelonging .
            ?homeBelonging rdf:type ref:HomeBelonging .
        } UNION {
            ?refugee ref:isAttachedTo ?homeAttachment .
            ?homeAttachment rdf:type ref:HomeAttachment .
        } UNION {
            ?refugee ref:makePlaceOf ?homeMaking .
            ?homeMaking rdf:type ref:HomeMaking .
        }
    }
    '''

    header = ['refugee', 'refAgency', 'transnationalism', 'reintegration Social Capital', 'reintegration Economic Wellbeing', 'reintegration Political Process',
              'home Belonging', 'home Attachment', 'home Making']
    sparql_query = prefix+ select

    onto = get_ontology("o1.owx").load()
    result = list(default_world.sparql(sparql_query))
    result = pre_process(result)
    print(type(header))
    # return the results
    return render_template('index.html', sparql_query=select, result=result, header=header), 200


@app.route('/query', methods=['POST'])
def query():
    homeBelonging = request.form.get('homeBelonging')
    hostBelonging = request.form.get('hostBelonging')
    has_agency = request.form.get('hasAgency')
    economicWellbeing = request.form.get('economicWellbeing')
    politicalProcess = request.form.get('politicalProcess')
    socialCapital = request.form.get('socialCapital')
    culturalIntegration = request.form.get('culturalIntegration')
    economicIntegration = request.form.get('economicIntegration')
    socialIntegration = request.form.get('socialIntegration')
    homeAttachment = request.form.get('homeAttachment')
    hostAttachment = request.form.get('hostAttachment')
    homeMaking = request.form.get('homeMaking')
    hostMaking = request.form.get('hostMaking')
    weak = request.form.get('weak')
    no = request.form.get('no')


    select_clause = 'SELECT DISTINCT '
    optional_clauses = [
        ('?refugee ', True),
        ('?homeBelonging ', homeBelonging == 'on'),
        ('?hostBelonging ', hostBelonging == 'on'),
        ('?refAgency ', has_agency=='LowAgency' or has_agency=='HighAgency'),
        ('?reintegrationEconomicWellbeing ', economicWellbeing == 'on'),
        ('?reintegrationPoliticalProcess ', politicalProcess == 'on'),
        ('?reintegrationSocialCapital ', socialCapital == 'on'),
        ('?culturalIntegration ', culturalIntegration == 'on'),
        ('?economicIntegration ', economicIntegration == 'on'),
        ('?socialIntegration ', socialIntegration == 'on'),
        ('?homeAttachment ', homeAttachment == 'on'),
        ('?hostAttachment ', hostAttachment == 'on'),
        ('?homeMaking ', homeMaking == 'on'),
        ('?hostMaking ', hostMaking == 'on'),
        ('?weak ', weak == 'on')
        #('?no ', no == 'on')
    ]

    header_clauses = [
        ('refugee ', True),
        ('home Belonging ', homeBelonging == 'on'),
        ('host Belonging ', hostBelonging == 'on'),
        ('refAgency ', has_agency=='LowAgency' or has_agency=='HighAgency'),
        ('reintegration Economic Wellbeing ', economicWellbeing == 'on'),
        ('reintegration Political Process ', politicalProcess == 'on'),
        ('reintegration Social Capital ', socialCapital == 'on'),
        ('cultural Integration ', culturalIntegration == 'on'),
        ('economic Integration ', economicIntegration == 'on'),
        ('social Integration ', socialIntegration == 'on'),
        ('home Attachment ', homeAttachment == 'on'),
        ('host Attachment ', hostAttachment == 'on'),
        ('home Making ', homeMaking == 'on'),
        ('host Making ', hostMaking == 'on'),
        ('transnationalism ', weak == 'on')
    ]

    
    header = ([head[0] for head in header_clauses if head[1]])

    where_clauses = [
        ('?refugee rdf:type ref:Refugee. ', True),
        ('?refugee ref:belongTo ?homeBelonging. ?homeBelonging rdf:type ref:HomeBelonging. ', homeBelonging == 'on'),
        ('?refugee ref:belongTo ?hostBelonging. ?hostBelonging rdf:type ref:HostBelonging. ', hostBelonging == 'on'),
        ('?refugee ref:hasAgency ?refAgency. ?refAgency rdf:type ref:' + str(has_agency) + '. ', has_agency=='LowAgency' or has_agency=='HighAgency'),
        ('?refugee ref:hasExpectedLevelOfReintegration ?reintegrationEconomicWellbeing. ?reintegrationEconomicWellbeing rdf:type ref:EconomicWellbeing. ', economicWellbeing == 'on'),
        ('?refugee ref:hasExpectedLevelOfReintegration ?reintegrationPoliticalProcess. ?reintegrationPoliticalProcess rdf:type ref:PoliticalProcess. ', politicalProcess == 'on'),
        ('?refugee ref:hasExpectedLevelOfReintegration ?reintegrationSocialCapital. ?reintegrationSocialCapital rdf:type ref:SocialCapital. ', socialCapital == 'on'),
        ('?refugee ref:hasLevelOfIntegration ?culturalIntegration. ?culturalIntegration rdf:type ref:CulturalIntegration. ', culturalIntegration == 'on'),
        ('?refugee ref:hasLevelOfIntegration ?economicIntegration. ?economicIntegration rdf:type ref:EconomicIntegration. ', economicIntegration == 'on'),
        ('?refugee ref:hasLevelOfIntegration ?socialIntegration. ?socialIntegration rdf:type ref:SocialIntegration. ', socialIntegration == 'on'),
        ('?refugee ref:isAttachedTo ?homeAttachment. ?homeAttachment rdf:type ref:HomeAttachment. ', homeAttachment == 'on'),
        ('?refugee ref:isAttachedTo ?hostAttachment. ?hostAttachment rdf:type ref:HostAttachment. ', hostAttachment == 'on'),
        ('?refugee ref:makePlaceOf ?homeMaking. ?homeMaking rdf:type ref:HomeMaking. ', homeMaking == 'on'),
        ('?refugee ref:makePlaceOf ?hostMaking. ?hostMaking rdf:type ref:HostMaking. ', hostMaking == 'on'),
        ('?refugee ref:practiceTransnationalism ?weak. ', weak == 'on'),
        ('FILTER NOT EXISTS{?refugee ref:practiceTransnationalism ?weak.}', no == 'on')
    ]

    where_clause_str = 'WHERE {' + ' '.join([clause[0] for clause in where_clauses if clause[1]]) + '}'
    select = select_clause + ' '.join([clause[0] for clause in optional_clauses if clause[1]]) + where_clause_str
    sparql_query = prefix + select
    #print(sparql_query)

    onto = get_ontology("o1.owx").load()
    result = list(default_world.sparql(sparql_query))
    result = pre_process(result)
    print(type(header))
    # return the results
    return render_template('index.html', sparql_query=select, result=result, header=header), 200

