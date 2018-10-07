# Metos3D User Manual

## Metos3D Installation

Install `metos3d` as a **shell command** with [`conda`](https://conda.io/miniconda.html):

```sh
conda install -c jpicau metos3d
```

Install `metos3d` as a **shell command** with [`pip`](https://pip.pypa.io/en/stable/quickstart/):

```sh
pip install metos3d
```

Install `metos3d` **locally** with `git`:

```sh
git clone https://github.com/metos3d/metos3d.git
# usage
cd metos3d/
./metos3d
#metos3d 
#Usage: metos3d [OPTIONS] COMMAND [ARGS]...
```

See the [Metos3D cheat sheet](metos3d-cheat-sheet.md) for a complete list of available `metos3d` commands.

## Metos3D Initialization

However used, Metos3D must be initialized **at least once** at the beginning:

```
metos3d init
```

> **Why?** Metos3D is a high-performance computing software.
> parallel,
> intended use is, on clusters, in parallel
> computing cluster,
> More precisely, a collection of source codes that needs to be compiled
> each providing its optimal set of compilers
> 

Initializes the shell environment,
MPI compilers, C, C++, Fortran,
compiles PETSc, including YAML, HDF5,
F2CBLAS,

## Metos3D Simulation

YAML [YAML](http://yaml.org/), configuration files, run files, examples, formats,

Configuration, compilation:

```sh
metos3d simpack NPZD-DOP.conf.yaml
```

Run:

```sh
./metos3d-simpack-NPZD-DOP.exe mitgcm-128x64x15x10800.3000y.run.yaml 

# sequential run
# parallel run
mpirun -n 128 ...
#metos3d simpack experiment-001.conf.yaml
#metos3d simpack my.first.experiment.conf.yaml
```


