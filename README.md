# Tradeship for Sublime Text 2 and 3
Sublime Text package to run [tradeship](https://github.com/karthikv/tradeship),
which automatically imports missing JS dependencies and removes unused ones.

## Installation
Ensure you have tradeship installed:

```sh
$ npm install -g tradeship
# or use yarn:
$ yarn global add tradeship
```

Navigate to your Sublime Text packages directory:

- OS X: `~/Library/Application Support/Sublime Text 3/Packages`
- Linux: `~/.Sublime Text 3/Packages`
- Windows: `%APPDATA%/Sublime Text 3/Packages`

If you're using Sublime Text 2, replace 3 with 2 in the paths above.

Then clone this repository:
`git clone https://github.com/karthikv/tradeship-sublime.git ./tradeship`.

## Usage
To run tradeship, you may either:

- Open the command palette <kbd>super</kbd> + <kbd>shift</kbd> + <kbd>p</kbd>
  and type "tradeship"
- Press <kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>i</kbd>
- To run on save, go to settings (Preferences > Package Settings > tradeship >
  Settings - Default) and set `import_on_save` to `true`.

You may also add
[custom key bindings](https://www.sublimetext.com/docs/3/settings.html)
for the `tradeship` command.

The first time tradeship runs in a project directory with many JavaScript files,
it'll take some time to parse and cache dependencies. Future runs will be much
faster.

## License
[MIT](LICENSE.md)
