from click.testing import CliRunner

from . import BaseCMLTest


class TestCMLHelp(BaseCMLTest):
    def test_cml_help(self):
        runner = CliRunner()
        virl = self.get_virl()
        result = runner.invoke(virl, ["--help"])
        self.assertEqual(0, result.exit_code)
        for command in [
            "clear",
            "cockpit",
            "command",
            "console",
            "definitions",
            "down",
            "extract",
            "generate",
            "groups",
            "id",
            "license",
            "ls",
            "nodes",
            "pull",
            "rm",
            "save",
            "search",
            "ssh",
            "start",
            "stop",
            "telnet",
            "tmux",
            "ui",
            "up",
            "use",
            "users",
            "version",
            "wipe",
        ]:
            self.assertIn(command, result.output)
