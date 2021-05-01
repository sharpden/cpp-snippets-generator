from ultra import *


sn = file_get('snippets.txt')

# Visual Studio
fmt = '''\
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


result = {}

for note in sn.split('=' * 80 + '\r\n'):
    head = note.splitlines()[0]
    body = '\r\n'.join(note.splitlines()[1:])
    if head.startswith('// '):
        short = head[3:]
        print '[%s]' % short
        print note
        print '-' * 80
        result[short[1:]] = body


for k, v in result.items():
    fn = os.path.expanduser('~\\Documents\\Visual Studio 2019\\Code Snippets\\Visual C++\\My Code Snippets\\%s.snippet' % k)
    content = fmt % ('#' + k, '#' + k, v)
    if not os.path.exists(fn) or file_get(fn) != v:
        file_put(fn, content)


fn = os.path.expanduser('~\\AppData\\Roaming\\Code\\User\\snippets\\cpp.json')
content = {}
for k, v in result.items():
    content[k] = {
        'prefix': '#' + k,
        'body': v.replace('$end$', '$0').splitlines(),
        'description': k,
    }
content = json.dumps(content)
if not os.path.exists(fn) or file_get(fn) != content:
    file_put(fn, content)
