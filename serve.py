import sys
from string import join
from subprocess import Popen, PIPE, call

import bobo
from cli import Controller

# Simple URL to application mapping
@bobo.query("/")
def index():
    html = "<html><head></head><body>"
    html = "<h2>Adapt (to the command line)</h2>"
    cmds = Controller().read_options_commands().keys()
    html = html + "<ul>"
    for cmd in cmds:
        snippet = """<li><a href="/cmd/%s">%s</a></li>""" % (cmd, cmd)
        html = html + snippet
    html = html + "</ul>"
    html = html + "</body</html>"
    return html

def create_callable(urlpath, cmd):
    """Creates callable objects that routed to URLS"""

    @bobo.query(urlpath)
    def func():
        out = Popen(cmd, shell=True, stdout = PIPE)
        return str(out.stdout.read())
    return func

#initialize url to callable
cmd_list = Controller().read_options_commands().items()
for name, cmd in cmd_list:
    urlpath = '/cmd/%s' % name
    globals()[name] = create_callable(urlpath, cmd)

if __name__ == "__main__":
    """Entry Point to Adapt CLI to Web"""
    app_root = Controller().application_root()
    call("python %sboboserver.py -f %sserve.py" % \
                                (app_root, app_root), shell=True)
