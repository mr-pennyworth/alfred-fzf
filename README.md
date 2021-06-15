<h1 align="center">

<a href="https://github.com/mr-pennyworth/alfred-fzf/releases/latest/">
  <img src="icon.png" width="16%"><br/>
  <img alt="Download"
       src="https://img.shields.io/github/downloads/mr-pennyworth/alfred-fzf/total?color=purple&label=Download"><br/>
</a>
  Instant Fuzzy File Search for Alfred
</h1>

List all the files inside a folder using [`fd`][1],
and instantly fuzzy-search through all of them using [`fzf`][2],
all from inside [Alfred][3] with a single keyword: `fzf`.

## Screenshots
<h4 align="center">Invoke with <code>fzf</code></h4>

![invocation](screenshots/invocation.png)

<h4 align="center">Search through tens of thousands of files</h4>

![filecount](screenshots/filecount.png)

<h4 align="center">Fuzzy search shows most relevant results</h4>

![search results](screenshots/search-results.png)

<h4 align="center">There's a folder action too!</h4>

![folder actions](screenshots/folder-actions.png)

<h4 align="center">Search even inside apps</h4>

![app bundle search](screenshots/app-bundle-search.png)

<h4 align="center">Manually create folder-specific keywords</h4>

![examples](screenshots/examples.png)

## Alternative and comparison
[Fuzzy Folders][4] is another fuzzy search workflow that is more
configurable and customizable. Instant Fuzzy File Search doesn't
have any plans to match all the features supported by Fuzzy Folders.
Neither does it aim to be as easy to customize. Take a look at the
table below for a quick comparison between the two.

|         | Instant Fuzzy File Search  | [Fuzzy Folders][4]  |
|--------:|:--------------------------:|:-------------------:|
| Detailed help section           | :x: | ✅ |
| Dedicated settings interface    | :x: | ✅ |
| Configurable query length       | :x: | ✅ |
| Configurable excludes           | :x: | ✅ |
| Search only folders             | :x: | ✅ |
| Folder action for fuzzy search  | ✅ | ✅ |
| Folder-specific keywords        | ✅ | ✅ |
| Search hidden files             | ✅ | :x: |
| Search inside symlinked folders | ✅ | :x: |
| Search inside apps              | ✅ | :x: |
| Independent of spotlight        | ✅ | :x: |
| Order-independent matching      | ✅ | :x: |
| Speed       | [Instant! 🚀][5] | [Slow][6] |


[1]: https://github.com/sharkdp/fd
[2]: https://github.com/junegunn/fzf
[3]: https://www.alfredapp.com
[4]: https://github.com/deanishe/alfred-fuzzyfolders#readme
[5]: https://www.alfredforum.com/topic/17011-fuzzy-file-search-bring-powers-of-fzf-to-alfred/?do=findComment&comment=87359
[6]: https://www.alfredforum.com/topic/17011-fuzzy-file-search-bring-powers-of-fzf-to-alfred/?do=findComment&comment=87357
