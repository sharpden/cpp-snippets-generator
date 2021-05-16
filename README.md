# C++ Snippets Generator

Add to `snippets.txt` snippet like:

```
================================================================================
// #shortcut
code
$selected$ - selected text before snippet was used
code
$end$ - where to place cursor
================================================================================
```

(delimiter is 80 chars `=`)

Run `python snippets.py`.

It will re-generate (all editors should automatically detect changes):
* for **Visual Studio 2019**: files `*.snippet` in folder `~\My Documents\Visual Studio 2019\Code Snippets\Visual C++\My Code Snippets\`. See Tools > Code Snippets Manager.
* for **VS Code**: file `cpp.json` in folder `~\AppData\Roaming\Code\User\snippets\`. See File > Preferences > User Snippets.
* for **Sublime**: files `*.sublime-snippet` in folder `~\AppData\Roaming\Sublime Text 3\Packages\User\`. See Tools > Snippets.

Paths could be overriden in `settings.py` file, `settings.py-sample` included.

Now you can start print `#shortcut` in IDE and press Tab when menu appears. Snippet name will be expanded to full code.
