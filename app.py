from flask import Flask
app = Flask(__name__)

from routes import *


if __name__ == "__main__":
    app.run(debug=True)



# write an insert sparql query for these data using python owlready2:
#  refugee = request.form.get('refugee')
#     homeBelonging = request.form.get('homeBelonging')
#     hostBelonging = request.form.get('hostBelonging')
#     homeAttachment = request.form.get('homeAttachment')
#     hostAttachment = request.form.get('hostAttachment')
#     homeMaking = request.form.get('homeMaking')
#     hostMaking = request.form.get('hostMaking')
#     highagency = request.form.get('highagencyfield')
#     lowagency = request.form.get('lowagencyfield')
#     economicWellbeing = request.form.get('economicWellbeing')
#     politicalProcess = request.form.get('politicalProcess')
#     socialCapital = request.form.get('socialCapital')
#     culturalIntegration = request.form.get('culturalIntegration')
#     economicIntegration = request.form.get('economicIntegration')
#     socialIntegration = request.form.get('socialIntegration')
#     transnationalism = request.form.get('transnationalism')
# where economicWellbeing , politicalProcess , socialCapital , culturalIntegration , economicIntegration , and socialIntegration have a constant values inside the Ontology file.
# and this is query example for our ontology:
#     PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#     PREFIX ref: <http://www.semanticweb.org/ssharani/ontologies/2022/RefugeeHomeReturnOntology#>
# SELECT DISTINCT ?refugee ?refAgency ?trans ?reintegrationSocialCapital ?reintegrationEconomicWellbeing ?reintegrationPoliticalProcess ?homeBelonging ?homeAttachment ?homeMaking
#     WHERE {
#         {
#             ?refugee ref:hasAgency ?refAgency .
#             ?refAgency rdf:type ref:HighAgency .
#             ?refugee ref:practiceTransnationalism ?trans .
#         } UNION {
#             ?refugee ref:hasAgency ?refAgency .
#             ?refAgency rdf:type ref:HighAgency .
#             ?refugee ref:hasExpectedLevelOfReintegration ?reintegrationSocialCapital .
#             ?reintegrationSocialCapital rdf:type ref:SocialCapital .
#         } UNION {
#             ?refugee ref:hasAgency ?refAgency .
#             ?refAgency rdf:type ref:HighAgency .
#             ?refugee ref:hasExpectedLevelOfReintegration ?reintegrationEconomicWellbeing .
#             ?reintegrationEconomicWellbeing rdf:type ref:EconomicWellbeing .
#         } UNION {
#             ?refugee ref:hasAgency ?refAgency .
#             ?refAgency rdf:type ref:HighAgency .
#             ?refugee ref:hasExpectedLevelOfReintegration ?reintegrationPoliticalProcess .
#             ?reintegrationPoliticalProcess rdf:type ref:PoliticalProcess .
#         } UNION {
#             ?refugee ref:belongTo ?homeBelonging .
#             ?homeBelonging rdf:type ref:HomeBelonging .
#         } UNION {
#             ?refugee ref:isAttachedTo ?homeAttachment .
#             ?homeAttachment rdf:type ref:HomeAttachment .
#         } UNION {
#             ?refugee ref:makePlaceOf ?homeMaking .
#             ?homeMaking rdf:type ref:HomeMaking .
#         }
#     }