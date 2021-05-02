import falcon, json
import config


class Emojis:
    emojis_data = {
        "1st_place_medal": "https://github.githubassets.com/images/icons/emoji/unicode/1f947.png?v8",
        "2nd_place_medal": "https://github.githubassets.com/images/icons/emoji/unicode/1f948.png?v8",
        "3rd_place_medal": "https://github.githubassets.com/images/icons/emoji/unicode/1f949.png?v8"
    }
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(Emojis.emojis_data)


class ResponseMiddleware:
    def process_response(self, req, resp, resource, req_succeeded):
        print("req_succ ", req_succeeded)
        if resp.status == falcon.HTTP_405:
            resp.status = falcon.HTTP_404
            resp.body = json.dumps({'message': 'Not Found', 'documentation_url': f'{config.BASE_URL}/rest'})


api = falcon.App(middleware=[ResponseMiddleware()])
api.add_route('/emojis', Emojis())

