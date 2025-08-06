"""
amber_ff_ports.py
This module only contains the function that will be the entry point that
will be used by the OpenFF Toolkit to find the installed forcefield files.

"""

from importlib.resources import files


def get_forcefield_dirs_paths() -> list[str]:
    """
    Return the paths to the directories including the forcefield files.

    This function is set as an entry point in setup.py. It will be called
    by the openforcefield toolkit when discovering the installed folders
    including offxml files.

    Returns
    -------
    dir_paths
        The list of directory paths containing the SMIRNOFF files.

    """
    return [(files("openff.amber_ff_ports") / "offxml").as_posix()]
