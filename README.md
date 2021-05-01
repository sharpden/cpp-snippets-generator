# C++ Snippets Generator

Add to `snippets.txt` snippet like:

```
================================================================================
// #shortcut
code
$end$ - where to place cursor
================================================================================
```

(delimiter is 80 chars `=`)

Run `python snippets.py`.

It will re-generate files `*.snippet` in folder `~\My Documents\Visual Studio 2019\Code Snippets\Visual C++\My Code Snippets\` for Visual Studio 2019 and file `cpp.json` in folder `~\AppData\Roaming\Code\User\snippets\` for VS Code.

Visual Studio automatically detects new files `*.snippet`. If no, look Tools > Code Snippets Manager.

Now you can start print `#shortcut` in IDE and press Tab when menu appears. Snippet name will be expanded to full code.
