import subprocess
import os
import pipes
import sublime
import sublime_plugin

EXTENSIONS = ["js", "jsx"]


class TradeshipCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        dir_path = self.get_dir_path()
        if not dir_path:
            sublime.error_message(
                "tradeship: file must be saved to a path or be in a workspace")
            return

        region = sublime.Region(0, self.view.size())
        code = self.view.substr(region)

        proc = subprocess.Popen(
            "tradeship -s " + pipes.quote(dir_path),
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
            executable=os.getenv("SHELL")
        )
        stdout, stderr = proc.communicate(code.encode())

        if proc.returncode != 0:
            message = ("tradeship: couldn't import dependencies, see console " +
                "for details")

            # If this file is being saved, the status line will immediately be overwritten
            # to "Saved ..." after this method returns. We add a timeout to ensure our
            # message is set after the "Saved ..." message.
            sublime.set_timeout(lambda: sublime.status_message(message), 1)
            print("tradeship: couldn't import dependencies:")
            print(stderr.decode("utf8"))
        else:
            encoding = self.view.encoding()
            if encoding == "Undefined":
                encoding = "utf-8"
            self.view.replace(edit, region, stdout.decode(encoding))

    def get_dir_path(self):
        file_name = self.view.file_name()
        if file_name:
            return os.path.dirname(file_name)

        folders = self.view.window().folders()
        if len(folders) > 0:
            return folders[0]
        return None


class TradeshipListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        ext = os.path.splitext(view.file_name())[1][1:]
        settings = sublime.load_settings("tradeship.sublime-settings")
        if ext in EXTENSIONS and settings.get("import_on_save", False):
            view.run_command("tradeship")
