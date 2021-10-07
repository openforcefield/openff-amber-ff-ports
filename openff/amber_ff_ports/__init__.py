from openff.amber_ff_ports.amber_ff_ports import get_forcefield_dirs_paths

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
