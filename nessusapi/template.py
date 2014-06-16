# template.py

class Template:
    # startTime is scan start date (ISO format)
    # rRules is recurrence frequency and interval
    def __init__(self, template_name, policy_id, target, session,
                 startTime=None, rRules=None):
        self.readable_name = template_name
        self.policy_id = policy_id
        self.target = target
        self.session = session
        self.time = startTime
        self.rRules = rRules
        params = {template_name: self.name, policy_id: self.policy,
                  target: self.target}
        if self.time:
            params['startTime'] = self.time
        if self.rRules:
            params['rRules'] = self.rRules
        self.nessus_name = self.session.request('scan/template/new', **params)['name']
 
    def edit(self, **kwargs):
        params = {template: self.nessus_name, template_name: self.nessus_name,
                  policy_id: self.policy_id, target: self.target}
        for kwarg in kwargs:
            params[kwarg] = kwargs[kwarg]
        results = self.session.request('scan/template/edit', **params)
        self.readable_name = results['readableName']
        self.policy_id = results['policy_id']
        self.target = results['target']
        # self.time and rRules?

    # returns uuid of launched scan
    def launch(self):
        return self.session.request('scan/template/launch',
                                    template=self.nessus_name)['uuid']

    def delete(self):
        return self.session.request('scan/template/new',
                                    template=self.nessus_name)['status']=='OK'
