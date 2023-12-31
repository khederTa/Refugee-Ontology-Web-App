from flask import render_template, request
from owlready2 import *
from utils.pre_process import pre_process
from utils.buildQueries import buildQuery, WouldBeReturneeQuery, addInstance
from app import app

prefix = '''
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX ref: <http://www.semanticweb.org/ssharani/ontologies/2022/RefugeeHomeReturnOntology#>
'''

@app.get('/')
def hello():
    return render_template('index1.html'), 200

@app.route('/returnee', methods=['POST'])
def returnee():
    sparql_query, select, header = WouldBeReturneeQuery()
    onto = get_ontology("o2.owx").load()
    #onto.sync_reasoner()
    result = list(default_world.sparql(sparql_query))
    result = pre_process(result)
    # return the results
    return render_template('index1.html', sparql_query=select, result=result, header=header), 200


@app.route('/query', methods=['POST'])
def query():
    onto = get_ontology("o2.owx").load()
    sparql_query, select, header = buildQuery()
    result = list(default_world.sparql(sparql_query))
    result = pre_process(result)
    # return the results
    return render_template('index1.html', sparql_query=select, result=result, header=header), 200

@app.route('/insert', methods=['GET'])
def insert():
    return render_template('index.html')

@app.route('/insert', methods=['POST'])
def add():
     # Load your ontology
    onto_path.append("./")  # Replace with the path to your ontology

    # Load the ontology
    onto = get_ontology("o2.owx").load()

    res = addInstance(onto)
    
    # Save the ontology
    onto.save()
    return render_template('index.html', result = res), 200
    