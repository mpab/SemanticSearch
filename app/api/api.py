from context_types import Features
from features_extract import features_extract_by_identifier_hash_and_result_hash
from utilities import Folders
from word_document_create import word_document_create_by_identifier_hash
import flask
from flask import render_template, Response, send_from_directory, abort
from flask_cors import CORS

from context_query import *
from context_create import *
from context_execute import *
from context_delete import *

app = flask.Flask(__name__, template_folder='./html')
app.config["DEBUG"] = True
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/api/contexts', methods=['GET'])
def api_context_query_all():
    print ("/api/context GET")
    json = context_query()
    return Response(json, status=200, mimetype='application/json')

@app.route('/api/context/<identifier_hash>', methods=['GET'])
def api_context_query(identifier_hash: str):
    print ("/api/context GET: " + identifier_hash)
    json = context_query(identifier_hash)
    return Response(json, status=200, mimetype='application/json')

@app.route('/api/context/<identifier_hash>', methods=['DELETE'])
def api_context_delete_by_identifier_hash(identifier_hash: str):
    print ("/api/context DELETE: " + str(identifier_hash))
    
    if identifier_hash:
        succeeded, msg = context_delete_by_identifier_hash(identifier_hash)
        if succeeded:
            return Response(msg, status=200, mimetype='application/text')

        return Response(msg, status=201, mimetype='application/text')

    return Response('missing identifier_hash', status=201, mimetype='application/text')

@app.route('/api/context/<terms>', methods=['PUT'])
def api_contexts_create(terms: str):
    print ("/api/context PUT: " + terms)
    
    if str:
        terms = terms.split(' ')
        succeeded, msg = contexts_create(terms)
        if succeeded:
            return Response(msg, status=200, mimetype='application/text')

        return Response(msg, status=201, mimetype='application/text')

    return Response('missing terms', status=201, mimetype='application/text')

@app.route('/api/context/<identifier_hash>', methods=['POST'])
def api_context_execute(identifier_hash: str):
    print ("/api/context POST: " + identifier_hash)
    
    if identifier_hash:
        status, msg = context_execute_by_identifier_hash(identifier_hash)
        if status == 0:
            return Response(msg, status=200, mimetype='application/text')

        return Response(msg, status=201, mimetype='application/text')

    return Response('missing terms', status=201, mimetype='application/text')

######################################################################################################
# documents
######################################################################################################

@app.route('/api/word_document/<identifier_hash>', methods=['PUT'])
def api_word_document_create_by_identifier_hash(identifier_hash: str):
    print ("/api/word_document PUT: " + identifier_hash)
    
    if str:
        succeeded, msg = word_document_create_by_identifier_hash(identifier_hash)
        if succeeded == 0:
            return Response(msg, status=200, mimetype='application/text')
        
        return Response(msg, status=201, mimetype='application/text')

    return Response('missing terms', status=201, mimetype='application/text')

@app.route("/pdf/<file_name>")
def get_pdf(file_name):
    try:
        return send_from_directory(Folders.reference(), filename=file_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)
        
@app.route("/doc/<file_name>")
def get_doc(file_name):
    try:
        return send_from_directory(Folders.generated_word_documents(), filename=file_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)
        
######################################################################################################
# features and feature analysis
######################################################################################################

@app.route("/api/features_extract/<identifier_hash>/<result_hash>", methods=['PUT'])
def features_extract(identifier_hash, result_hash):
    print ("/api/features_extract/ PUT: " + identifier_hash + "/" + result_hash)
    try:
        status, info, result = features_extract_by_identifier_hash_and_result_hash(identifier_hash, result_hash)
        if status:
            return Response(info, status=200, mimetype='application/text')
        return Response(info, status=201, mimetype='application/text')       
    except:
        abort(404)
        
@app.route("/feature/counts/<identifier_hash>/<result_hash>", methods=['GET'])
def get_feature_counts(identifier_hash, result_hash):
    
    print ("/feature/counts/ GET: " + identifier_hash + "/" + result_hash)
    
    try:
        features: Features = features_extract_by_identifier_hash_and_result_hash(identifier_hash, result_hash)
        print (features)
        if features.isValid:
            return send_from_directory(Folders.features(), filename=features.feature_counts_filename, as_attachment=True)
        return Response(features.info, status=201, mimetype='application/text')       
    except FileNotFoundError:
        print ("FileNotFoundError - /feature/counts/ GET: " + identifier_hash + "/" + result_hash)
        abort(404)
        
@app.route("/feature/extract/<identifier_hash>/<result_hash>", methods=['GET'])
def get_feature_extract(identifier_hash, result_hash):
    try:
        features: Features = features_extract_by_identifier_hash_and_result_hash(identifier_hash, result_hash)
        if features.isValid:
            return send_from_directory(Folders.features(), filename=features.feature_extract_filename, as_attachment=True)
        return Response(features.info, status=201, mimetype='application/text')       
    except FileNotFoundError:
        abort(404)
        
@app.route("/feature/tags/<identifier_hash>/<result_hash>", methods=['GET'])
def get_feature_tags(identifier_hash, result_hash):
    try:
        features: Features = features_extract_by_identifier_hash_and_result_hash(identifier_hash, result_hash)
        if features.isValid:
            return send_from_directory(Folders.features(), filename=features.feature_tags_filename, as_attachment=True)
        return Response(features.info, status=201, mimetype='application/text')         
    except FileNotFoundError:
        abort(404)

@app.route("/feature/tokens/<identifier_hash>/<result_hash>", methods=['GET'])
def get_feature_tokens(identifier_hash, result_hash):
    try:
        features: Features = features_extract_by_identifier_hash_and_result_hash(identifier_hash, result_hash)
        if features.isValid:
            return send_from_directory(Folders.features(), filename=features.feature_tokens_filename, as_attachment=True)
        return Response(features.info, status=201, mimetype='application/text')      
    except FileNotFoundError:
        abort(404)
        
@app.route("/feature/tokens_graph/<identifier_hash>/<result_hash>", methods=['GET'])
def get_feature_tokens_graph(identifier_hash, result_hash):
    try:
        features: Features = features_extract_by_identifier_hash_and_result_hash(identifier_hash, result_hash)
        if features.isValid:
            return send_from_directory(Folders.features(), filename=features.feature_tokens_graph_filename, as_attachment=True)
        return Response(features.info, status=201, mimetype='application/text')         
    except FileNotFoundError:
        abort(404)

app.run()
