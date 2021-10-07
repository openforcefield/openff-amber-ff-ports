"""
Unit tests for the openff-amber-ff-ports package.

Note that exhaustive testing of the entrypoints infrastructure
is excluded here but found in gh/openforcefield/openff-forcefields
"""

import glob
import os

import pytest

from openff.amber_ff_ports.amber_ff_ports import get_forcefield_dirs_paths

try:
    import openff.toolkit

    has_off_toolkit = True
except ModuleNotFoundError:
    has_off_toolkit = False


def find_all_offxml_files():
    """Return a list of the offxml files shipped with the package."""
    file_names = []
    for dir_path in get_forcefield_dirs_paths():
        file_pattern = os.path.join(dir_path, "*.offxml")
        file_paths = [file_path for file_path in glob.glob(file_pattern)]
        file_names.extend([os.path.basename(file_path) for file_path in file_paths])
    return file_names


@pytest.mark.skipif(not (has_off_toolkit), reason="Test requires OFF toolkit")
@pytest.mark.parametrize("offxml_file_name", find_all_offxml_files())
def test_forcefield_data_is_loadable(offxml_file_name):
    """Test that the OpenFF Toolkit can find and parse the files."""
    from openff.toolkit.typing.engines.smirnoff import ForceField

    if "_off_impropers" in offxml_file_name:
        ForceField(offxml_file_name)
    else:
        # Current implementation requires a handler not shipped with the toolkit
        with pytest.raises(KeyError, match="AmberImproperTorsions"):
            ForceField(offxml_file_name)
