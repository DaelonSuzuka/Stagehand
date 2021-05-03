#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
from six.moves.urllib.request import urlopen
from collections import OrderedDict
from pathlib import Path
import json


import_url = "https://raw.githubusercontent.com/Palakis/obs-websocket/4.x-current/docs/generated/comments.json"  # noqa: E501


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
    w.line(f"class {name}({classname[event]}):")
    with w:
        w.line(f'"""{description}')
        w.line()
        if fields:
            w.line(":Arguments:")
        for field in fields:
            with w:
                w.line(f"*{clean_var(field['name'])}*")
                with w:
                    w.line(f"type: {field['type']}")
                    w.line(f"{field['description']}")

        if returns:
            w.line(":Returns:")
        for ret in returns:
            with w:
                w.line(f"*{clean_var(ret['name'])}*")
                with w:
                    w.line(f"type: {ret['type']}")
                    w.line(f"{ret['description']}")

        w.line('"""')
        w.line()

        # info
        w.line(f"name = '{name}'")
        w.line(f"category = '{i['category']}'")
        if fields:
            w.line("fields = [")
            for field in fields:
                with w:
                    w.line(f"'{field['name']}',")
            w.line("]")
        else:
            w.line("fields = []")
        w.line()

        # init method
        w.line("def __init__(self):")
        with w:
            w.line("super().__init__()")
            # datain
            if returns:
                w.line("self.datain = {}")
            for r in returns:
                w.line(f"self.datain['{r['name']}'] = None")

            # dataout
            if fields:
                w.line("self.dataout = {}")
            for a in fields:
                if not a['optional']:
                    w.line(f"self.dataout['{a['name']}'] = {None}")
            for a in fields:
                if a['optional']:
                    w.line(f"self.dataout['{a['name']}'] = {None}")
            w.line()

        # send the request by calling
        w.line("def __call__({}):".format(
            ", ".join(
                ['self']
                + [clean_var(a['name']) for a in fields if not a['optional']]
                + [clean_var(a['name']) + "=None" for a in fields if a['optional']]
                + ['cb=None']
            )
        ))
        with w:
            w.line("payload = {}")
            w.line(f"payload['request-type'] = '{i['name']}'")
            for field in fields:
                w.line(f"payload['{field['original_name']}'] = {field['name']}")
            w.line("ObsSocket().send(payload, cb)")
            w.line()

        # build payload
        w.line("@staticmethod")
        w.line("def payload({}):".format(
            ", ".join(
                [clean_var(a['name']) for a in fields if not a['optional']]
                + [clean_var(a['name']) + "=None" for a in fields if a['optional']]
            )
        ))
        with w:
            w.line("payload = {}")
            w.line(f"payload['request-type'] = '{i['name']}'")
            for field in fields:
                w.line(f"payload['{field['original_name']}'] = {field['name']}")
            w.line("return payload")
            w.line()
        w.line()


def build_event(w, i, event):
    # gather class info
    name = i['name']
    description = i['description']

    fields = collect_fields(i)
    returns = collect_returns(i)

    # 
    w.line(f"class {name}({classname[event]}):")
    with w:
        w.line(f'"""{description}')
        w.line()
        if fields:
            w.line(":Arguments:")
        for field in fields:
            with w:
                w.line(f"*{clean_var(field['name'])}*")
                with w:
                    w.line(f"type: {field['type']}")
                    w.line(f"{field['description']}")

        if returns:
            w.line(":Returns:")
        for ret in returns:
            with w:
                w.line(f"*{clean_var(ret['name'])}*")
                with w:
                    w.line(f"type: {ret['type']}")
                    w.line(f"{ret['description']}")

        w.line('"""')

        w.line() # init method
        w.line("def __init__(self):")
        # w.line("def __init__({}):".format(
        #     ", ".join(
        #         ["self"]
        #         + [clean_var(a['name']) for a in fields if not a['optional']]
        #         + [clean_var(a['name']) + "=None" for a in fields if a['optional']]
        #     )
        # ))
        with w:
            w.line("super().__init__()")
        w.line()
        w.line()


def build_widget(w, i, event):
    # gather class info
    name = i['name']
    description = i['description']

    fields = collect_fields(i)
    returns = collect_returns(i)

    # 
    w.line(f"class {name}Widget(QWidget):")
    with w:
        def field_widget(field):
            w = "UnimplementedField('[field not implemented]')"

            if field['name'] in ['sourceName', 'source']:
                w = f"SourceSelector(changed, parent=self)"
            elif field['name'] in ['sceneName', 'scene_name']:
                w = f"SceneSelector(changed, parent=self)"
            elif field['name'] == 'filterName':
                w = f"FilterSelector(changed, self.sourceName, parent=self)"
            elif field['type'] == 'boolean' or 'Bool' in field['name'] or 'Enabled' in field['name']:
                w = f"BoolSelector(changed, parent=self)"
            else:
                if name not in unimplemented_fields:
                    unimplemented_fields[name] = []
                unimplemented_fields[name].append(field)

            return w

        w.line("def __init__(self, changed=None, parent=None):")
        with w:
            w.line("super().__init__(parent=parent)")
            w.line("self.changed = changed")
            for field in fields:
                w.line(f"self.{field['name']} = {field_widget(field)}")
            w.line()
            w.line("with CHBoxLayout(self, margins=(0,0,0,0)) as layout:")
            with w:
                if fields:
                    for field in fields:
                        w.line(f"layout.add(self.{field['name']})")
                else:
                    w.line("layout.add(QLabel('[ request has no fields ]'))")
        w.line()

        w.line("def payload(self):")
        with w:
            w.line("payload = {}")
            w.line(f"payload['request-type'] = '{i['name']}'")
            for field in fields:
                w.line(f"payload['{field['original_name']}'] = self.{field['name']}.get_data()")
            w.line("return payload")
        w.line()

        w.line("def refresh(self):")
        with w:
            for field in fields:
                w.line(f"self.{field['name']}.refresh()")
            w.line("return")
        w.line()
        
        w.line("def from_dict(self, data):")
        with w:
            w.line("self._data = data")
            for field in fields:
                w.line(f"self.{field['name']}.set_data(data['{field['name']}']) ")
        w.line()

        w.line("def to_dict(self):")
        with w:
            w.line("return {")
            with w:
                for field in fields:
                    w.line(f"'{field['name']}': self.{field['name']}.get_data(),")
            w.line("}")
        w.line()


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

        w.line("from stagehand.sandbox import Sandbox")
        w.line("from .obs_socket import ObsSocket")
        w.line()
        w.line()
        
        w.line(f'class {classname[event]}:')
        with w:
            w.line('def __init__(self):')
            with w:
                w.line('pass')
        w.line()
        w.line()

        classes = []
        for sec in data[event]:
            for i in data[event][sec]:
                build_request(w, i, event)
                classes.append(i['name'])

        w.line()
        w.line()
        w.line("requests = {")
        with w:
            for c in classes:
                w.line(f"'{c}': {c}(),")
        w.line("}")

    event = 'requests'
    with open(Path(__file__).parent / 'request_widgets.py', 'w') as f:
        w = Writer(f.write)

        w.line("from .base_classes import *")
        w.line("from qtstrap import *")
        w.line("from stagehand.sandbox import Sandbox")
        w.line()
        w.line()

        classes = []
        for sec in data[event]:
            for i in data[event][sec]:
                build_widget(w, i, event)
                classes.append(i['name'])
                w.line()

        w.line()
        w.line("widgets = {")
        with w:
            for c in classes:
                w.line(f"'{c}': {c}Widget,")
        w.line("}")

    event = 'events'
    with open(Path(__file__).parent / 'events.py', 'w') as f:
        w = Writer(f.write)

        w.line("from stagehand.sandbox import Sandbox")
        w.line()
        w.line()
        
        w.line(f'class {classname[event]}:')
        with w:
            w.line('def __init__(self):')
            with w:
                w.line('pass')
        w.line()
        w.line()

        classes = []
        for sec in data[event]:
            for i in data[event][sec]:
                build_event(w, i, event)
                classes.append(i['name'])

        w.line()
        w.line()
        w.line("events = {")
        with w:
            for c in classes:
                w.line(f"'{c}': {c}(),")
        w.line("}")

    print("API classes have been generated.")


if __name__ == '__main__':
    generate_classes()