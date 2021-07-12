import json as jsonlib

class Response:
    def __init__(self, status, message, headers, content):
        self.status_code = status
        self.reason = message
        self.headers = headers
        self.content = content

    def __repr__(self):
        return f"<Response [{self.status_code}]>"
    
    def json(self):
        return jsonlib.loads(self.content)
    
    @property
    def text(self):
        return self.content.decode("UTF-8", errors="ignore")
