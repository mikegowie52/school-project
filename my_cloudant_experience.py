import requests
import json

url="https://e39314fb-f9f8-4763-96b8-92cc2de72f87-bluemix:de2f3568e5a56011401b02a9436701905e84bd98818558c4e92448479bfdfe4f@e39314fb-f9f8-4763-96b8-92cc2de72f87-bluemix.cloudant.com/{0}"


def get_from_db(endpoint):
    get = requests.get(url.format(endpoint))
    print (get.json())


def put_db(db_name):
    put = requests.put(url.format(db_name))
    print (put.json())


def delete_db(db_name):
    delete = requests.delete(url.format(db_name))
    print(delete.json())


def post_db(db_name , doc_body):
    post = requests.post(url.format(db_name),
                         headers={"Content-Type" :"application/json"},
                         data=json.dumps(doc_body))
    print(post.json())

# doc_body = {"_id" : "Profile", "Name" : "Mike", "Age" : "14", "Height" : "172"}
docs = {"doc_1" : {"_id" : "1", "name" :"joel", "age" : "15", "height" : "178"}, "doc_2" : {"_id" : "2", "name" : "mike", "age" : "15", "height" : "172"}}

get_from_db("_all_dbs")
put_db("mike")
get_from_db("_all_dbs")
for d in docs:
    post_db("mike",docs[d])
#post_db("mike", doc_body)
get_from_db("mike/_all_docs")
#get_from_db("mike/Profile")
delete_db("mike")
get_from_db("_all_dbs")
