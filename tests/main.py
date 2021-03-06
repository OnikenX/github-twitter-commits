from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config, view_defaults
from pyramid.response import Response
from github import Github

me = Github().get_user('OnikenX')

for repo in me.get_repos():
    webhook = repo.create_hook()


ENDPOINT = "webhook"

@view_defaults(
    route_name=ENDPOINT, renderer="json", request_method="POST"
)
class PayloadView(object):
    """
    View receiving of Github payload. By default, this view it's fired only if
    the request is json and method POST.
    """

    def __init__(self, request):
        self.request = request
        # Payload from Github, it's a dict
        self.payload = self.request.json

    @view_config(header="X-Github-Event:push")
    def payload_push(self):
        """This method is a continuation of PayloadView process, triggered if
        header HTTP-X-Github-Event type is Push"""
        print("No. commits in push:", len(self.payload['commits']))
        return Response("success")

    @view_config(header="X-Github-Event:pull_request")
    def payload_pull_request(self):
        """This method is a continuation of PayloadView process, triggered if
        header HTTP-X-Github-Event type is Pull Request"""
        print("PR", self.payload['action'])
        print("No. Commits in PR:", self.payload['pull_request']['commits'])

        return Response("success")

    @view_config(header="X-Github-Event:ping")
    def payload_else(self):
        print("Pinged! Webhook created with id {}!".format(self.payload["hook"]["id"]))
        return {"status": 200}


def create_webhook():
    """ Creates a webhook for the specified repository.

    This is a programmatic approach to creating webhooks with PyGithub's API. If you wish, this can be done
    manually at your repository's page on Github in the "Settings" section. There is a option there to work with
    and configure Webhooks.
    """

    USERNAME = ""
    PASSWORD = ""
    OWNER = ""
    REPO_NAME = ""
    EVENTS = ["push", "pull_request"]
    HOST = ""

    config = {
        "url": "http://{host}/{endpoint}".format(host=HOST, endpoint=ENDPOINT),
        "content_type": "json"
    }

    repo.create_hook("web", config, EVENTS, active=True)


if __name__ == "__main__":
    config = Configurator()
    create_webhook()
    config.add_route(ENDPOINT, "/{}".format(ENDPOINT))
    config.scan()
    app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 80, app)
    server.serve_forever()
