# Overview
Simple API server to expose a Doctor List API for our front-end application to present the information to customers

# Installation & Use:
1) Install dependencies: github pip install -r requirements.txt
2) Start the server using app.py

# Assumptions
1) API will return json data output that can be consumed by the client for presenting information to the customers
2) Doctor & Area Attributes assumptions along with their relations as defined in models.py
3) Exposed only required API's for now can be extended to full fledged app

# Choice of Framework & Library: 
Please check requirements.txt

1) flask: 
 > Microfamework for simplicity and easy for the current usecase.
2) pymongo: 
 > MongoDB MongoDB as a persistent, searchable repository of Python dictionaries suits the purpose of fast search 
Main benifits we achieve:
 > JSON representation of data documents / industy standard
 > Easy add / change new attribute
 > Scalable
 > Simplified data modelling compared and no need to use ORM tools
 > Also selected out of comfort level
3) dataclasses & typing:
 > data modeliing 
4) unittest:
 > Unittesting the models
 > Need to add the integration tests
5) json:
 > For data serialization / Deserialization

# Potential Improvement: 
 > Using middleware like CORS
 > Adding authentication & authorization and defining api entitlements
 > Integration tests
 > Confiuguation management - Swagger/ Yaml
 > Eventing - lazy processing of bulk inserts
 > Integration with logstash, kibana for analytics
 > Integration with AI tools for fast querying
 


