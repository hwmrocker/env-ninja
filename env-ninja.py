from jinja2 import Template
import sys
import os

template_filename = sys.argv[1]

if not template_filename.lower().endswith('.j2'):
    print("Not a jinja template: missing .j2 extension!")
    sys.exit(1)

with open(template_filename) as fh:
    template_content = fh.read()

t = Template(template_content)

with open(template_filename[:-3], 'w') as fh:
    fh.write(t.render(** os.environ))
