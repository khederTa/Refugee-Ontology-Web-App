from flask import request
def passIt():
  pass

prefix = '''
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX ref: <http://www.semanticweb.org/ssharani/ontologies/2022/RefugeeHomeReturnOntology#>

'''
def WouldBeReturneeQuery():
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
    # select = '''
    #     SELECT DISTINCT ?refugee  ?transnationalism WHERE {?refugee rdf:type ref:Refugee. FILTER NOT EXISTS {?refugee ref:practiceTransnationalism ?transnationalism}}
    # '''
    header = ['refugee', 'refAgency', 'transnationalism', 'reintegration Social Capital', 'reintegration Economic Wellbeing', 'reintegration Political Process',
              'home Belonging', 'home Attachment', 'home Making']
    
    sparql_query = prefix+ select

    return sparql_query, select, header

def buildQuery():
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
    transnationalism = request.form.get('transnationalism')
    

    select_clause = 'SELECT DISTINCT '
    optional_clauses = [
        ('?refugee ', True),
        ('?homeBelonging ', homeBelonging == 'on'),
        ('?hostBelonging ', hostBelonging == 'on'),
        ('?refAgency ', has_agency=='LowAgency' or has_agency=='HighAgency'),
        ('?reintegrationEconomicWellbeing ', economicWellbeing == 'High Econ Wellbeing Inhome' or economicWellbeing == 'Medium Econ Wellbeing Inhome' or economicWellbeing == 'Low Econ Wellbeing Inhome'),
        ('?reintegrationPoliticalProcess ', politicalProcess == 'Stable Political Process' or politicalProcess == 'Unstable Political Process'),
        ('?reintegrationSocialCapital ', socialCapital == 'Good Social Capital Inhome' or socialCapital == 'Medium Social Capital Inhome' or socialCapital == 'Bad Social Capital Inhome'),
        ('?culturalIntegration ', culturalIntegration == 'High Cultural Integration' or culturalIntegration == 'Medium Cultural Integration' or culturalIntegration == 'Low Cultural Integration'),
        ('?economicIntegration ', economicIntegration == 'High Econ Integration' or economicIntegration == 'Medium Econ Integration' or economicIntegration == 'Low Econ Integration'),
        ('?socialIntegration ', socialIntegration == 'High Socio Integration' or socialIntegration == 'Medium Socio Integration' or socialIntegration == 'Low Socio Integration'),
        ('?homeAttachment ', homeAttachment == 'on'),
        ('?hostAttachment ', hostAttachment == 'on'),
        ('?homeMaking ', homeMaking == 'on'),
        ('?hostMaking ', hostMaking == 'on'),
        ('?transnationalism ', transnationalism == 'yes')
    ]

    header_clauses = [
        ('refugee ', True),
        ('home Belonging ', homeBelonging == 'on'),
        ('host Belonging ', hostBelonging == 'on'),
        ('refAgency ', has_agency=='LowAgency' or has_agency=='HighAgency'),
        ('reintegration Economic Wellbeing ', economicWellbeing == 'High Econ Wellbeing Inhome' or economicWellbeing == 'Medium Econ Wellbeing Inhome' or economicWellbeing == 'Low Econ Wellbeing Inhome'),
        ('reintegration Political Process ', politicalProcess == 'Stable Political Process' or politicalProcess == 'Unstable Political Process'),
        ('reintegration Social Capital ', socialCapital == 'Good Social Capital Inhome' or socialCapital == 'Medium Social Capital Inhome' or socialCapital == 'Bad Social Capital Inhome'),
        ('cultural Integration ', culturalIntegration == 'High Cultural Integration' or culturalIntegration == 'Medium Cultural Integration' or culturalIntegration == 'Low Cultural Integration'),
        ('economic Integration ', economicIntegration == 'High Econ Integration' or economicIntegration == 'Medium Econ Integration' or economicIntegration == 'Low Econ Integration'),
        ('social Integration ', socialIntegration == 'High Socio Integration' or socialIntegration == 'Medium Socio Integration' or socialIntegration == 'Low Socio Integration'),
        ('home Attachment ', homeAttachment == 'on'),
        ('host Attachment ', hostAttachment == 'on'),
        ('home Making ', homeMaking == 'on'),
        ('host Making ', hostMaking == 'on'),
        ('?transnationalism ', transnationalism == 'yes')
    ]

    
    header = ([head[0] for head in header_clauses if head[1]])

    where_clauses = [
        ('?refugee rdf:type ref:Refugee. ', True),
        ('?refugee ref:belongTo ?homeBelonging. ?homeBelonging rdf:type ref:HomeBelonging. ', homeBelonging == 'on'),
        ('?refugee ref:belongTo ?hostBelonging. ?hostBelonging rdf:type ref:HostBelonging. ', hostBelonging == 'on'),
        ('?refugee ref:hasAgency ?refAgency. ?refAgency rdf:type ref:' + str(has_agency) + '. ', has_agency=='LowAgency' or has_agency=='HighAgency'),
        ('?refugee ref:hasExpectedLevelOfReintegration ?reintegrationEconomicWellbeing. ?reintegrationEconomicWellbeing rdf:type ref:EconomicWellbeing. ', economicWellbeing == 'High Econ Wellbeing Inhome' or economicWellbeing == 'Medium Econ Wellbeing Inhome' or economicWellbeing == 'Low Econ Wellbeing Inhome'),
        ('?refugee ref:hasExpectedLevelOfReintegration ?reintegrationPoliticalProcess. ?reintegrationPoliticalProcess rdf:type ref:PoliticalProcess. ', politicalProcess == 'Stable Political Process' or politicalProcess == 'Unstable Political Process'),
        ('?refugee ref:hasExpectedLevelOfReintegration ?reintegrationSocialCapital. ?reintegrationSocialCapital rdf:type ref:SocialCapital. ', socialCapital == 'Good Social Capital Inhome' or socialCapital == 'Medium Social Capital Inhome' or socialCapital == 'Bad Social Capital Inhome'),
        ('?refugee ref:hasLevelOfIntegration ?culturalIntegration. ?culturalIntegration rdf:type ref:CulturalIntegration. ', culturalIntegration == 'High Cultural Integration' or culturalIntegration == 'Medium Cultural Integration' or culturalIntegration == 'Low Cultural Integration'),
        ('?refugee ref:hasLevelOfIntegration ?economicIntegration. ?economicIntegration rdf:type ref:EconomicIntegration. ', economicIntegration == 'High Econ Integration' or economicIntegration == 'Medium Econ Integration' or economicIntegration == 'Low Econ Integration'),
        ('?refugee ref:hasLevelOfIntegration ?socialIntegration. ?socialIntegration rdf:type ref:SocialIntegration. ', socialIntegration == 'High Socio Integration' or socialIntegration == 'Medium Socio Integration' or socialIntegration == 'Low Socio Integration'),
        ('?refugee ref:isAttachedTo ?homeAttachment. ?homeAttachment rdf:type ref:HomeAttachment. ', homeAttachment == 'on'),
        ('?refugee ref:isAttachedTo ?hostAttachment. ?hostAttachment rdf:type ref:HostAttachment. ', hostAttachment == 'on'),
        ('?refugee ref:makePlaceOf ?homeMaking. ?homeMaking rdf:type ref:HomeMaking. ', homeMaking == 'on'),
        ('?refugee ref:makePlaceOf ?hostMaking. ?hostMaking rdf:type ref:HostMaking. ', hostMaking == 'on'),
        ('?refugee ref:practiceTransnationalism ?transnationalism. ', transnationalism == 'yes'),
        ('?refugee rdf:type ref:Refugee. FILTER NOT EXISTS {?refugee rdf:type ref:Refugee; ref:practiceTransnationalism ?transnationalism.}', transnationalism == 'no')
#        ('?refugee ref:practiceTransnationalism ?transnationalism. ', transnationalism == 'yes' or transnationalism == 'no')
    ]

    where_clause_str = 'WHERE {' + ' '.join([clause[0] for clause in where_clauses if clause[1]]) + '}'
    select = select_clause + ' '.join([clause[0] for clause in optional_clauses if clause[1]]) + where_clause_str
    sparql_query = prefix + select  
    print(sparql_query)
    return sparql_query, select, header
# ref_dict = {
#     'homeBelonging': 'belongTo', 'hostBelonging': 'belongTo', 'hasAgency': 'hasAgency', 
#     'economicWellbeing': 'reintegrationEconomicWellbeing', 'politicalProcess': 'hasExpectedLevelOfReintegration',
#     'socialCapital': 'hasExpectedLevelOfReintegration', 'culturalIntegration': 'hasLevelOfIntegration',
#     'economicIntegration': 'hasLevelOfIntegration', 'socialIntegration': 'hasLevelOfIntegration',
#     'homeAttachment': 'isAttachedTo', 'hostAttachment': 'isAttachedTo', 'homeMaking': 'makePlaceOf', 'hostMaking': 'makePlaceOf',
#     'transnationalism': 'practiceTransnationalism',
# }
# def buildQuery():
#     form_data = request.form

#     # Define SPARQL SELECT clause
#     select_clause = 'SELECT DISTINCT '
#     header_clauses = []
#     where_clauses = ['?refugee rdf:type ref:Refugee.']
#     filter_clause = ''  # Initialize filter_clause here

#     for key, value in form_data.items():
#         if key in ['homeBelonging', 'hostBelonging', 'hasAgency', 'economicWellbeing', 'politicalProcess',
#                    'socialCapital', 'culturalIntegration', 'economicIntegration', 'socialIntegration',
#                    'homeAttachment', 'hostAttachment', 'homeMaking', 'hostMaking']:
#             if value == 'on':
#                 variable_name = key.lower()
#                 optional_clause = f'?{variable_name} rdf:type ref:{ref_dict[key]}.'
#                 header_clauses.append(f'{variable_name} ')
#                 where_clauses.append(optional_clause)
#         elif key == 'transnationalism':
#             if value == 'yes':
#                 optional_clause = f'?transnationalism rdf:type ref:{ref_dict[key]}.'
#                 header_clauses.append('transnationalism ')
#                 where_clauses.append(optional_clause)
#             elif value == 'no':
#                 filter_clause = 'FILTER NOT EXISTS { ?refugee ref:practiceTransnationalism ?transnationalism. }'

#     # Combine SPARQL clauses
#     header = [header_clause for header_clause in header_clauses]
    
#     # Check if filter_clause has content
#     if filter_clause:
#         where_clause_str = 'WHERE {' + ' '.join(where_clauses) + ' ' + filter_clause + '}'
#     else:
#         where_clause_str = 'WHERE {' + ' '.join(where_clauses) + '}'

#     sparql_query = prefix + select_clause + ' '.join(header) + where_clause_str
#     print(100*'#')
#     print(sparql_query)
    
#     return sparql_query, select_clause, header

def addInstance(onto):
    # Get data from the form
    refugee = request.form.get('refugee')
    homeBelonging = request.form.get('homeBelonging')
    hostBelonging = request.form.get('hostBelonging')
    homeAttachment = request.form.get('homeAttachment')
    hostAttachment = request.form.get('hostAttachment')
    homeMaking = request.form.get('homeMaking')
    hostMaking = request.form.get('hostMaking')
    highagency = request.form.get('highagencyfield')
    lowagency = request.form.get('lowagencyfield')
    economicWellbeing = request.form.get('economicWellbeing')
    politicalProcess = request.form.get('politicalProcess')
    socialCapital = request.form.get('socialCapital')
    culturalIntegration = request.form.get('culturalIntegration')
    economicIntegration = request.form.get('economicIntegration')
    socialIntegration = request.form.get('socialIntegration')
    transnationalism = request.form.get('transnationalism')

    # Create a new individual in the ontology
    with onto:
        # Add more properties to the individual as needed
        # For example: refugee_individual.hasProperty = [onto.Property(value)]
        refugee_individual = onto.Refugee(refugee)
        refugee_individual.hasHomeBelonging = [onto.HomeBelonging(homeBelonging)] if homeBelonging else passIt()
        refugee_individual.hasHostBelonging = [onto.HostBelonging(hostBelonging)] if hostBelonging else passIt()
        refugee_individual.hasHomeAttachment = [onto.HomeAttachment(homeAttachment)] if homeAttachment else passIt()
        refugee_individual.hasHostAttachment = [onto.HostAttachment(hostAttachment)] if hostAttachment else passIt()
        refugee_individual.hasHomeMaking = [onto.HomeMaking(homeMaking)] if homeMaking else passIt()
        refugee_individual.hasHostMaking = [onto.HostMaking(hostMaking)] if hostMaking else passIt()
        refugee_individual.refugeeAgency = [onto.RefugeeAgency(highagency)] if highagency else passIt()
        refugee_individual.refAgency = [onto.RefugeeAgency(lowagency)] if lowagency else passIt()
        refugee_individual.reintegration = [onto.Reintegration(economicWellbeing)] if economicWellbeing else passIt()
        refugee_individual.reintegration = [onto.Reintegration(politicalProcess)] if politicalProcess else passIt()
        refugee_individual.reintegration = [onto.Reintegration(socialCapital)] if socialCapital else passIt()
        refugee_individual.integration = [onto.Integration(culturalIntegration)] if culturalIntegration else passIt()
        refugee_individual.integration = [onto.Integration(economicIntegration)] if economicIntegration else passIt()
        refugee_individual.integration = [onto.Integration(socialIntegration)] if socialIntegration else passIt()
        refugee_individual.transnationalism = [onto.Transnationalism(transnationalism)] if transnationalism else passIt()

    
    return "Data inserted into the ontology"

    # return render_template("your_form.html")
