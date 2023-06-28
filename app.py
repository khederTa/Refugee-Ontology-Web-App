from flask import Flask, render_template, request, jsonify
from owlready2 import *

app = Flask(__name__)

@app.get('/')
def hello():
    return render_template('index.html'), 200

@app.route('/returnee', methods=['POST'])
def returnee():
    prefix = '''
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX ref: <http://www.semanticweb.org/ssharani/ontologies/2022/RefugeeHomeReturnOntology#>
'''
    select = '''
        SELECT DISTINCT ?refugee ?reftype
        WHERE {?refugee ref:hasAgency ?agency;
        rdf:type ?reftype;
        ref:practiceTransnationalism ?trans.
        ?agency rdf:type ref:HighAgency.}
    '''
    sparql_query = prefix+ select

    onto = get_ontology("o1.owx").load()
    result = list(default_world.sparql(sparql_query))
    # return the results
    return render_template('index.html', sparql_query=select, result=result), 200

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

    
    
    prefix = '''
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX ref: <http://www.semanticweb.org/ssharani/ontologies/2022/RefugeeHomeReturnOntology#>
'''

    select_clause = 'SELECT DISTINCT ?refugee '
    optional_clauses = [
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
        ('?weak ', weak == 'on'),
        ('?no ', no == 'on')
    ]

    where_clauses = [
        ('?refugee rdf:type ref:Refugee. ', True),
        ('?refugee ref:belongTo ?belonging. ?belonging rdf:type ref:HomeBelonging. ', homeBelonging == 'on'),
        ('?refugee ref:belongTo ?belonging. ?belonging rdf:type ref:HostBelonging. ', hostBelonging == 'on'),
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
    

    # return the results
    return render_template('index.html', sparql_query=select, result=result), 200


    
if __name__ == "__main__":
    app.run(debug=True)
