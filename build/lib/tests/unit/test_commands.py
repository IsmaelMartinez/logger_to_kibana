import src.commands as commands
from unittest.mock import patch
from pytest import mark


@patch.object(commands.kib, "generate_folder_visualisation")
@patch.object(commands.processor, "process_folder")
@mark.parametrize(
    "folder, process_expected, generate_expected",
    [
        ("one", 1, 1),
        (None, 1, 1),
    ]
)
def test_process_and_generate_visualisations(
        process_folder, generate_folder_visualisation,
        folder, process_expected, generate_expected):
    commands.process_and_generate_visualisations(folder)
    assert process_folder.call_count == process_expected
    assert generate_folder_visualisation.call_count == generate_expected


@patch.object(commands.kib, "generate_and_send_visualisation")
@patch.object(commands.processor, "process_folder")
@mark.parametrize(
    "folder, process_expected, generate_expected",
    [
        ("one", 1, 1),
        (None, 1, 1),
    ]
)
def test_process_generate_and_send_visualisations(
        process_folder, generate_folder_visualisation,
        folder, process_expected, generate_expected):
    commands.process_generate_and_send_visualisations(folder)
    assert process_folder.call_count == process_expected
    assert generate_folder_visualisation.call_count == generate_expected


# # # #
# # # Probably make this the "integration test"
# # # #

# # class TestCommands(unittest.TestCase):

# #     def test_command_is_command(self):
# # Test it with this http://click.palletsprojects.com/en/5.x/testing/
# #

# # if __name__ == '__name__':
# #     unittest.main()