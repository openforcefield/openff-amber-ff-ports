# OpenFF Amber FF Ports

This repository is for _distributing_ Amber force fields in the SMIRNOFF format. The work of _doing_ this porting is found [here](https://github.com/openforcefield/amber-ff-porting)

SMIRNOFF force field files (`.offxml`) can be downloaded from the assets of the following releases:

* [v0.0.1](https://github.com/openforcefield/amber-ff-porting/releases/tag/0.0.1) release.
* [v0.0.2](https://github.com/openforcefield/amber-ff-porting/releases/tag/0.0.2) release.
* [v0.0.3](https://github.com/openforcefield/amber-ff-porting/releases/tag/0.0.3) release.
* [v0.0.4](https://github.com/openforcefield/amber-ff-porting/releases/tag/0.0.4) release.

The files included in this repository should directly match these sources.

### Installation

[Conda packages](https://anaconda.org/conda-forge/openff-amber-ff-ports) are available via the `conda-forge` channel:

```shell
conda install -c conda-forge openff-amber-ff-ports
```

Note that since version 0.11.0 of the OpenFF Toolkit (August 2022), this package is installed as a dependency of the toolkit and these files may already be available on your machine. The toolkit offers an API for inspecting this:

```python
>>> from openff.toolkit.typing.engines.smirnoff.forcefield import get_available_force_fields
>>> sorted(filter(lambda f: 'ff14sb' in f, get_available_force_fields()))
['ff14sb_0.0.1.offxml', 'ff14sb_0.0.2.offxml', 'ff14sb_0.0.3.offxml', 'ff14sb_0.0.4.offxml', 'ff14sb_off_impropers_0.0.1.offxml', 'ff14sb_off_impropers_0.0.2.offxml', 'ff14sb_off_impropers_0.0.3.offxml', 'ff14sb_off_impropers_0.0.4.offxml']
```

### Release history

#### 2025.09.0 - September 18, 2025

* The `pkg_resources` API is no longer used.
* This project uses CalVer, specifically `YYYY.MM.MICRO`

#### Acknowledgements

Project based on the
[Computational Molecular Science Python Cookiecutter](https://github.com/molssi/cookiecutter-cms) version 1.0.
