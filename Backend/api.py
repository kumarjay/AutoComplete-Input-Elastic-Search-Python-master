try:
    from flask import Flask, render_template
    from flask_restful import Resource, Api, reqparse
    import elasticsearch
    from elasticsearch import Elasticsearch, helpers
    import datetime
    import concurrent.futures
    import requests
    import json

except Exception as e:
    print("Modules Missing {}".format(e))

import pandas as pd

print('Hello World....!!!....')

app = Flask(__name__)
api = Api(app)

print('Hello World')


# @app.route('/', methods=["GET", "POST"])
# def index():
#     return render_template('home.html')

#------------------------------------------------------------------------------------------------------------

NODE_NAME = 'my-python'
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}],
                   http_auth=('elastic', 'changeme'))

#------------------------------------------------------------------------------------------------------------

print('Passed elastic search....', es)
"""
{
"wildcard": {
    "title": {
        "value": "{}*".format(self.query)
    }
}
}

"""
print('Entering Controller....')

class Controller(Resource):
    def __init__(self):
        self.query = parser.parse_args().get("query", None)
        print('Entered....................')
        self.baseQuery ={
            "_source": [],
            "size": 0,
            "min_score": 0.5,
            "query": {
                "bool": {
                    "must": [
                        {
                            "wildcard": {
                                "title": {
                                    "value": "{}*".format(self.query)
                                }
                            }
                        }
                    ],
                    "filter": [],
                    "should": [],
                    "must_not": []
                }
            },
            "aggs": {
                "auto_complete": {
                    "terms": {
                        "field": "title.keyword",
                        "order": {
                            "_count": "desc"
                        },
                        "size": 25
                    }
                }
            }
        }

    def generator(self, df2):
        for c, line in enumerate(df2):
            print(line)
            yield {
                '_index': 'my-python',
                '_type': '_doc',
                '_id': c,
                '_source': {
                    'title': line.get('title', ''),
                    'year': line.get('year', ''),
                    'genre': line.get('genre', ''),
                    'director': line.get('director', ''),
                    'production_company': line.get('production_company', None),
                    'actors': line.get('actors', None),
                    'description': line.get('description', ''),
                    'avg_vote': line.get('avg_vote', '')

                }
            }
        raise StopIteration

    def get(self):
        print('searching.........')
        es.indices.create(index='my-python', ignore=400)

        e1 = {'name': 'Jay',
              'address': ' Ranchi'}

        es.index(index='my-python', doc_type='my-python', body=e1, id=1)
        movie = pd.read_csv('IMDb movies.csv')
        movies = movie.to_dict('records')

        # my_movie = self.generator(movies)

        try:
            res = helpers.bulk(es, self.generator(movies))
            print('Working')
        except Exception as e:
            pass

        # res = es.search(index=NODE_NAME, size=10, body=self.baseQuery, ignore= 400)
        res = es.search(index=NODE_NAME, size=10, body=self.baseQuery, ignore=400)
        print(res)
        return res


print('passed Controller....')
parser = reqparse.RequestParser()
parser.add_argument("query", type=str, required=True, help="query parameter is Required ")

api.add_resource(Controller, '/autocomplete')
print('End......')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=4000)
