from importlib.metadata import PackageNotFoundError, version

from openff.amber_ff_ports.amber_ff_ports import get_forcefield_dirs_paths

__all__ = ("get_forcefield_dirs_paths",)

try:
    __version__ = version("openff-amber-ff-ports")
except PackageNotFoundError:
    __version__ = "0+unknown"

__git_revision__ = None
