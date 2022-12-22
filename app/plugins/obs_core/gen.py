#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
from six.moves.urllib.request import urlopen
from collections import OrderedDict
from pathlib import Path
import json


import_url = "https://raw.githubusercontent.com/obsproject/obs-websocket/4.x-compat/docs/generated/comments.json"  # noqa: E501


def clean_var(string):
    """
    Converts a string to a suitable variable name by removing not allowed
    characters.
    """
    string = string.replace('-', '_').replace('[]', '')
    return string


classname = {
    'requests': 'BaseRequest',
    'events': 'BaseEvent',
}

all_args = set()

unimplemented_fields = {}


class Writer:
    def __init__(self, out):
        self.out = out
        self.indent = 4
        self.level = 0

    def __iadd__(self, other):
        self.line(other)
        return self

    def raw(self, string):
        self.out(string)

    def line(self, string=''):
        if string:
            self.out(' ' * self.indent * self.level + string + '\n')
        else:
            self.out('\n')

    def __call__(self, string=''):
        self.out(' ' * self.indent * self.level + string)
    
    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, *_):
        self.level -= 1

sections = [
    'subheads', 
    'description', 
    'return', 
    'api', 
    'name', 
    'category', 
    'since', 
    'returns', 
    'names', 
    'categories', 
    'sinces', 
    'heading', 
    'lead', 
    'type', 
    'examples'
]


def collect_fields(data):
    fields = []
    known_fields = []
    try:
        if len(data['params']) > 0:
            for a in data['params']:
                a['name'] = a['name'].replace("[]", ".*")
                name = a['name'].split(".")[0]
                if name not in known_fields:
                    known_fields.append(name)
                    fields.append({
                        'original_name': name,
                        'name': clean_var(name),
                        'type': a['type'],
                        'description': a['description'],
                        'optional': 'optional' in a['type'],
                    })
    except KeyError:
        pass

    return fields

def collect_returns(data):
    returns = []
    known_returns = []
    try:
        if len(data['returns']) > 0:
            for r in data['returns']:
                r['name'] = r['name'].replace("[]", ".*")
                name = r['name'].split(".")[0]
                if name not in known_returns:
                    known_returns.append(name)
                    returns.append({
                            'name': name,
                            'clean_name': clean_var(name),
                            'type': r['type'],
                            'description': r['description']
                        })
    except KeyError:
        pass

    return returns


def build_request(w, i, event):
    # gather class info
    name = i['name']
    description = i['description']

    fields = collect_fields(i)
    returns = collect_returns(i)

    # 
    w += f"class {name}({classname[event]}):"
    with w:
        w += f'"""{description}'
        w += ''
        if fields:
            w += ":Arguments:"
        for field in fields:
            with w:
                w += f"*{clean_var(field['name'])}*"
                with w:
                    w += f"type: {field['type']}"
                    w += f"{field['description']}"

        if returns:
            w += ":Returns:"
        for ret in returns:
            with w:
                w += f"*{clean_var(ret['name'])}*"
                with w:
                    w += f"type: {ret['type']}"
                    w += f"{ret['description']}"

        w += '"""'
        w += ''

        # info
        w += f"name = '{name}'"
        w += f"category = '{i['category']}'"
        if fields:
            w += "fields = ["
            for field in fields:
                with w:
                    w += f"'{field['name']}',"
            w += "]"
        else:
            w += "fields = []"
        w += ''

        # init method
        w += "def __init__(self):"
        with w:
            w += "super().__init__()"
            # datain
            if returns:
                w += "self.datain = {}"
            for r in returns:
                w += f"self.datain['{r['name']}'] = None"

            # dataout
            if fields:
                w += "self.dataout = {}"
            for a in fields:
                if not a['optional']:
                    w += f"self.dataout['{a['name']}'] = {None}"
            for a in fields:
                if a['optional']:
                    w += f"self.dataout['{a['name']}'] = {None}"
            w += ''

        # send the request by calling
        w += "def __call__({}):".format(
            ", ".join(
                ['self']
                + [clean_var(a['name']) for a in fields if not a['optional']]
                + [clean_var(a['name']) + "=None" for a in fields if a['optional']]
                + ['cb=None']
            )
        )
        with w:
            w += "payload = {}"
            w += f"payload['request-type'] = '{i['name']}'"
            for field in fields:
                w += f"payload['{field['original_name']}'] = {field['name']}"
            w += "ObsSocket().send(payload, cb)"
            w += ''

        # build payload
        w += "@staticmethod"
        w += "def payload({}):".format(
            ", ".join(
                [clean_var(a['name']) for a in fields if not a['optional']]
                + [clean_var(a['name']) + "=None" for a in fields if a['optional']]
            )
        )
        with w:
            w += "payload = {}"
            w += f"payload['request-type'] = '{i['name']}'"
            for field in fields:
                w += f"payload['{field['original_name']}'] = {field['name']}"
            w += "return payload"
            w += ''
        w += ''


def build_request_widget(w, i, event):
    # gather class info
    name = i['name']
    description = i['description']

    fields = collect_fields(i)
    returns = collect_returns(i)

    # 
    w += f"class {name}Widget(QWidget):"
    with w:
        def field_widget(field):
            line = f"UnimplementedField('[{field['name']}: {field['type']}]')"

            if field['name'] in ['sourceName', 'source']:
                line = f"SourceSelector(changed, parent=self)"
            elif field['name'] in ['sceneName', 'scene_name']:
                line = f"SceneSelector(changed, parent=self)"
            elif field['name'] == 'filterName':
                line = f"FilterSelector(changed, self.sourceName, parent=self)"
            elif field['type'] == 'boolean' or 'Bool' in field['name'] or 'Enabled' in field['name']:
                line = f"BoolSelector(changed, parent=self)"
            elif 'String' in field['type']:
                line = f"StringSelector(changed, parent=self, placeholder='{field['name']}')"
            elif 'int' in field['type']:
                line = f"IntSelector(changed, parent=self, placeholder='{field['name']}')"
            elif 'double' in field['type']:
                line = f"DoubleSelector(changed, parent=self, placeholder='{field['name']}')"
            else:
                if name not in unimplemented_fields:
                    unimplemented_fields[name] = []
                unimplemented_fields[name].append(field)

            return line

        w += "def __init__(self, changed=None, parent=None):"
        with w:
            w += "super().__init__(parent=parent)"
            w += "self.changed = changed"
            for field in fields:
                w += f"self.{field['name']} = {field_widget(field)}"
            w += ''
            w += "with CHBoxLayout(self, margins=0) as layout:"
            with w:
                if fields:
                    for field in fields:
                        w += f"layout.add(self.{field['name']})"
                else:
                    w += "layout.add(QLabel('[ request has no fields ]'))"
        w += ''

        w += "def payload(self):"
        with w:
            w += "payload = {}"
            w += f"payload['request-type'] = '{i['name']}'"
            for field in fields:
                w += f"payload['{field['original_name']}'] = self.{field['name']}.get_data()"
            w += "return payload"
        w += ''

        w += "def refresh(self):"
        with w:
            for field in fields:
                w += f"self.{field['name']}.refresh()"
            w += "return"
        w += ''
        
        w += "def set_data(self, data):"
        with w:
            w += "self._data = data"
            for field in fields:
                w += f"self.{field['name']}.set_data(data['{field['name']}']) "
        w += ''

        w += "def get_data(self):"
        with w:
            w += "return {"
            with w:
                for field in fields:
                    w += f"'{field['name']}': self.{field['name']}.get_data(),"
            w += "}"
        w += ''

        
def build_event(w, i, event):
    # gather class info
    name = i['name']
    description = i['description']

    fields = collect_fields(i)
    returns = collect_returns(i)

    # 
    w += f"class {name}({classname[event]}):"
    with w:
        w += f'"""{description}'
        w += ''
        if fields:
            w += ":Arguments:"
        for field in fields:
            with w:
                w += f"*{clean_var(field['name'])}*"
                with w:
                    w += f"type: {field['type']}"
                    w += f"{field['description']}"

        if returns:
            w += ":Returns:"
        for ret in returns:
            with w:
                w += f"*{clean_var(ret['name'])}*"
                with w:
                    w += f"type: {ret['type']}"
                    w += f"{ret['description']}"

        w += '"""'
        w += ''

        # info
        w += f"name = '{name}'"
        w += f"category = '{i['category']}'"

        w += '' # init method
        w += "def __init__(self, payload=None):"
        # w += "def __init__({}):".format(
        #     ", ".join(
        #         ["self"]
        #         + [clean_var(a['name']) for a in fields if not a['optional']]
        #         + [clean_var(a['name']) + "=None" for a in fields if a['optional']]
        #     )
        # )
        with w:
            w += "super().__init__()"
            
            # if returns:
            #     w += "self.datain = {}"
            # for r in returns:
            #     w += f"self.datain['{r['name']}'] = None"

        w += ''
        w += ''

def build_event_widget(w, i, event):
    # gather class info
    name = i['name']
    description = i['description']

    fields = collect_fields(i)
    returns = collect_returns(i)

    w += f"class {name}Widget(QWidget):"
    with w:
        def field_widget(field):
            line = "UnimplementedField('[field not implemented]')"

            if field['name'] in ['sourceName', 'source']:
                line = f"SourceSelector(changed, parent=self)"
            elif field['name'] in ['sceneName', 'scene_name']:
                line = f"SceneSelector(changed, parent=self)"
            elif field['name'] == 'filterName':
                line = f"FilterSelector(changed, self.sourceName, parent=self)"
            elif field['type'] == 'boolean' or 'Bool' in field['name'] or 'Enabled' in field['name']:
                line = f"BoolSelector(changed, parent=self)"
            elif 'String' in field['type']:
                line = f"StringSelector(changed, parent=self, placeholder='{field['name']}')"
            elif 'int' in field['type']:
                line = f"IntSelector(changed, parent=self, placeholder='{field['name']}')"
            elif 'double' in field['type']:
                line = f"DoubleSelector(changed, parent=self, placeholder='{field['name']}')"
            else:
                if name not in unimplemented_fields:
                    unimplemented_fields[name] = []
                unimplemented_fields[name].append(field)

            return line

        w += "def __init__(self, changed=None, parent=None):"
        with w:
            w += "super().__init__(parent=parent)"
            w += "self.changed = changed"
            # for field in returns:
            #     w += f"self.{field['clean_name']} = {field_widget(field)}"
            w += ''
            w += "with CHBoxLayout(self, margins=0) as layout:"
            with w:
                w += 'pass'
            #     if returns:
            #         for field in returns:
            #             w += f"layout.add(self.{field['clean_name']})"
            #     else:
            #         w += "layout.add(QLabel('[ request has no fields ]'))"
        w += ''

        w += "def validate_event(self, event):"
        with w:
            w += f"if event['update-type'] != '{name}':"
            with w:
                w += "return False"
            # for field in returns:
            #     w += f"self.{field['name']}.refresh()"
            w += "return True"
        w += ''

        w += "def refresh(self):"
        with w:
            # for field in returns:
            #     w += f"self.{field['name']}.refresh()"
            w += "return"
        w += ''
        
        w += "def set_data(self, data):"
        with w:
            w += "self._data = data"
            # for field in returns:
            #     w += f"self.{field['name']}.set_data(data['{field['name']}']) "
        w += ''

        w += "def get_data(self):"
        with w:
            w += "return {"
            # with w:
            #     for field in returns:
            #         w += f"'{field['name']}': self.{field['name']}.get_data(),"
            w += "}"
        w += ''

def generate_classes():
    """Generates the necessary classes."""
    print("Downloading {} for last API version.".format(import_url))
    data = json.loads(urlopen(import_url).read().decode('utf-8'), object_pairs_hook=OrderedDict)
    print("Download OK. Generating python files...")

    event = 'requests'

    if event not in data:
        raise Exception("Missing {} in data.".format(event))

    with open(Path(__file__).parent / 'requests.py', 'w') as f:
        w = Writer(f.write)

        w += "from stagehand.sandbox import Sandbox"
        w += "from .obs_socket import ObsSocket"
        w += ''
        w += ''

        w += f'class {classname[event]}:'
        with w:
            w += 'def __init__(self):'
            with w:
                w += 'pass'
        w += ''
        w += ''

        classes = []
        for sec in data[event]:
            for i in data[event][sec]:
                build_request(w, i, event)
                classes.append(i['name'])

        w += ''
        w += ''
        w += "requests = {"
        with w:
            for c in classes:
                w += f"'{c}': {c}(),"
        w += "}"

    event = 'requests'
    with open(Path(__file__).parent / 'request_widgets.py', 'w') as f:
        w = Writer(f.write)

        w += "from .base_classes import *"
        w += "from qtstrap import *"
        w += "from stagehand.sandbox import Sandbox"
        w += ''
        w += ''

        classes = []
        for sec in data[event]:
            for i in data[event][sec]:
                build_request_widget(w, i, event)
                classes.append(i['name'])
                w += ''

        w += ''
        w += "widgets = {"
        with w:
            for c in classes:
                w += f"'{c}': {c}Widget,"
        w += "}"

    event = 'events'
    with open(Path(__file__).parent / 'events.py', 'w') as f:
        w = Writer(f.write)

        w += "from stagehand.sandbox import Sandbox"
        w += ''
        w += ''
        
        w += f'class {classname[event]}:'
        with w:
            w += 'def __init__(self):'
            with w:
                w += 'pass'
        w += ''
        w += ''

        classes = []
        for sec in data[event]:
            for i in data[event][sec]:
                build_event(w, i, event)
                classes.append(i['name'])

        w += ''
        w += ''
        w += "events = {"
        with w:
            for c in classes:
                w += f"'{c}': {c}(),"
        w += "}"

    event = 'events'
    with open(Path(__file__).parent / 'event_widgets.py', 'w') as f:
        w = Writer(f.write)

        w += "from .base_classes import *"
        w += "from qtstrap import *"
        w += "from stagehand.sandbox import Sandbox"
        w += ''
        w += ''

        classes = []
        for sec in data[event]:
            for i in data[event][sec]:
                build_event_widget(w, i, event)
                classes.append(i['name'])
                w += ''

        w += ''
        w += "widgets = {"
        with w:
            for c in classes:
                w += f"'{c}': {c}Widget,"
        w += "}"

    print("API classes have been generated.")


if __name__ == '__main__':
    generate_classes()