from openff.amber_ff_ports.amber_ff_ports import get_forcefield_dirs_paths

from ._version import get_versions

__all__ = (get_forcefield_dirs_paths,)

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
