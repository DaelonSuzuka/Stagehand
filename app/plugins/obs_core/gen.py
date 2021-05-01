#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
from six.moves.urllib.request import urlopen
from collections import OrderedDict
from pathlib import Path

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


def write_class(f, i, event):
    f.write(f"class {i['name']}({classname[event]}):\n")
                    
    f.write("    \"\"\"{}\n\n".format(i['description']))

    fields = []
    arguments_default = []
    arguments = []
    try:
        if len(i['params']) > 0:
            f.write("    :Arguments:\n")
            for a in i['params']:
                
                a['name'] = a['name'].replace("[]", ".*")
                f.write("       *{}*\n".format(clean_var(a['name'])))
                f.write("            type: {}\n".format(a['type']))
                f.write("            {}\n".format(a['description']))
                name = a['name'].split(".")[0]
                if name in arguments or name in arguments_default:
                    continue
                if 'optional' in a['type']:
                    arguments_default.append(name)
                    fields.append({
                        'name': clean_var(name),
                        'type': a['type'],
                    })
                else:
                    arguments.append(name)
                    fields.append({
                        'name': clean_var(name),
                        'type': a['type'],
                    })
                    all_args.add(name)
    except KeyError:
        pass

    returns = []
    try:
        if len(i['returns']) > 0:
            f.write("    :Returns:\n")
            for r in i['returns']:
                r['name'] = r['name'].replace("[]", ".*")
                f.write("       *{}*\n".format(clean_var(r['name'])))
                f.write("            type: {}\n".format(r['type']))
                f.write("            {}\n".format(r['description']))
                name = r['name'].split(".")[0]
                if name in returns:
                    continue
                returns.append(name)
    except KeyError:
        pass

    f.write("    \"\"\"\n\n")

    # fields
    f.write("    fields = [\n")
    for field in fields:
        f.write(f"        '{field['name']}',\n")
    f.write("    ]\n\n")

    # category
    f.write(f"    category = '{i['category']}'\n")
    f.write("    \n")

    # init method
    f.write("    def __init__({}):\n".format(
        ", ".join(
            ["self"]
            + [clean_var(a) for a in arguments]
            + [clean_var(a) + "=None" for a in arguments_default]
        )
    ))
    f.write("        super().__init__()\n")
    f.write("        self.name = '{}'\n".format(i['name']))
    # for r in returns:
    #     f.write("        self.datain['{}'] = None\n".format(r))

    if fields:
        f.write("        self.dataout = {}\n")

    for a in arguments:
        f.write("        self.dataout['{}'] = {}\n".format(a, None))
    for a in arguments_default:
        f.write("        self.dataout['{}'] = {}\n".format(a, None))
    f.write("\n")

    # build payload
    f.write("    @staticmethod\n")
    f.write("    def payload({}):\n".format(
        ", ".join(
            [clean_var(a) for a in arguments]
            + [clean_var(a) + "=None" for a in arguments_default]
        )
    ))
    f.write("        payload = {}\n")
    f.write(f"        payload['request-type'] = '{i['name']}'\n")
    for field in fields:
        name = clean_var(field['name'])
        arg = clean_var(field['name'])
        if 'Bool' in field['type']:
            arg = f"bool({clean_var(field['name'])})"
        f.write(f"        payload['{name}'] = {arg}\n")
    f.write("        return payload\n\n")
    
    # create widget
    f.write("    @staticmethod\n")
    f.write("    def widget(changed):\n")
    # f.write("    def widget({}):\n".format(
    #     ", ".join(
    #         [clean_var(a) for a in arguments]
    #         + [clean_var(a) + "=None" for a in arguments_default]
    #     )
    # ))
    f.write("        w = QWidget()\n")
    for field in fields:
        if field['name'] == 'sourceName':
            f.write(f"        {field['name']} = SourceSelector(changed)\n")
        if field['name'] in ['sceneName', 'scene_name']:
            f.write(f"        {field['name']} = SceneSelector(changed)\n")
        if field['name'] == 'filterName':
            f.write(f"        {field['name']} = FilterSelector(changed)\n")
        if 'Bool' in field['name'] or 'Enabled' in field['name']:
            f.write(f"        {field['name']} = BoolSelector(changed)\n")
    if fields:
        f.write("        with CHBoxLayout(w, margins=(0,0,0,0)) as layout:\n")
    for field in fields:
        if field['name'] in ['sourceName', 'sceneName', 'scene_name', 'filterName']:
            f.write(f"            layout.add({field['name']})\n")
        elif 'Bool' in field['name'] or 'Enabled' in field['name']:
            f.write(f"            layout.add({field['name']})\n")
        else:
            f.write(f"            layout.add(QLabel('{field['name']}'))\n")
    f.write("        \n")
    f.write("        return w\n")

    f.write("\n")


def generate_classes():
    """Generates the necessary classes."""
    print("Downloading {} for last API version.".format(import_url))
    data = json.loads(urlopen(import_url).read().decode('utf-8'), object_pairs_hook=OrderedDict)
    print("Download OK. Generating python files...")

    for event in ['requests', 'events']:
        if event not in data:
            raise Exception("Missing {} in data.".format(event))
        with open(Path(__file__).parent / '{}.py'.format(event), 'w') as f:
            f.write("from .base_classes import *\n")
            f.write("from qtstrap import *\n")
            f.write("\n\n")

            f.write("categories = [\n")
            for sec in data[event]:
                f.write(f"    '{sec}',\n")
            f.write("]\n")
            f.write("\n\n")

            for sec in data[event]:
                for i in data[event][sec]:
                    # if i['name'] != 'SetMute':
                    #     continue

                    write_class(f, i, event)
                    

    print("API classes have been generated.")


if __name__ == '__main__':
    generate_classes()