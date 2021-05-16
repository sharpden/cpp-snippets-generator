from __future__ import print_function
import json
import os
import sys

from settings import folders


def S(s):
    if sys.version_info.major == 3:
        return s.decode('utf-8')
    return s

def B(s):
    if sys.version_info.major == 3:
        return s.encode('utf-8')
    return s

def file_put(filename, text):
    with open(filename, 'wb') as fp:
        fp.write(B(text))

def file_get(filename):
    with open(filename, 'rb') as fp:
        return S(fp.read())


sn = file_get('snippets.txt')

# Visual Studio
# https://docs.microsoft.com/en-us/visualstudio/ide/code-snippets?view=vs-2019
# May support placeholders like $Width$ by
# <Declarations>
#   <Literal>
#     <ID>Width</ID>
#     <Type>Integer</Type>
#     <ToolTip>Replace by width</ToolTip>
#     <Default>150</Default>
#   </Literal>
# </Declarations>
VS_fmt = '''\
<?xml version="1.0" encoding="utf-8"?>
<CodeSnippets xmlns="http://schemas.microsoft.com/VisualStudio/2005/CodeSnippet">
    <CodeSnippet Format="1.0.0">
        <Header>
            <Title>%s</Title>
            <Author>Myself</Author>
            <Description></Description>
            <Shortcut>%s</Shortcut>
        </Header>
        <Snippet>
            <Code Language="cpp">
                <![CDATA[%s]]>
            </Code>
        </Snippet>
    </CodeSnippet>
</CodeSnippets>
'''

# VSCode
# https://code.visualstudio.com/docs/editor/userdefinedsnippets
'''
// Place your snippets for cpp here. Each snippet is defined under a snippet name and has a prefix, body and 
// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
// same ids are connected.
// Example:
// "Print to console": {
// 	"prefix": "log",
// 	"body": [
// 		"console.log('$1');",
// 		"$2"
// 	],
// 	"description": "Log output to console"
// }
'''

# Sublime
# https://docs.sublimetext.io/guide/extensibility/snippets.html
# ${1:this} like in VS Code are supported
Sublime_fmt = '''\
<snippet>
	<tabTrigger>%s</tabTrigger>
	<content><![CDATA[%s]]></content>
</snippet>
'''

# TODO:
# IDEA: File | Settings | Live Templates; https://www.jetbrains.com/help/idea/using-live-templates.html
# Notepad++: No support yet https://github.com/ffes/nppsnippets/issues/33


result = {}

for note in sn.split('=' * 80 + '\r\n'):
    head = note.splitlines()[0]
    body = '\r\n'.join(note.splitlines()[1:])
    if head.startswith('// '):
        short = head[3:]
        print('[%s]' % short)
        print(note)
        print('-' * 80)
        result[short[1:]] = body


if 'VS' in folders:
    for k, v in result.items():
        fn = os.path.expanduser(os.path.join(folders['VS'], '%s.snippet' % k))
        content = VS_fmt % ('#' + k, '#' + k, v)
        if not os.path.exists(fn) or file_get(fn) != content:
            file_put(fn, content)


if 'VSCODE' in folders:
    fn = os.path.expanduser(os.path.join(folders['VSCODE'], 'cpp.json'))
    content = {}
    for k, v in result.items():
        content[k] = {
            'prefix': '#' + k,
            'body': v.replace('$end$', '$0').replace('$selected$', '$TM_SELECTED_TEXT').splitlines(),
            'description': k,
        }
    content = json.dumps(content)
    if not os.path.exists(fn) or file_get(fn) != content:
        file_put(fn, content)


if 'SUBLIME' in folders:
    for k, v in result.items():
        fn = os.path.expanduser(os.path.join(folders['SUBLIME'], '%s.sublime-snippet' % k))
        content = Sublime_fmt % ('#' + k, v.replace('$end$', '$0').replace('$selected$', '$SELECTION'))
        if not os.path.exists(fn) or file_get(fn) != content:
            file_put(fn, content)
