# Metos3D User Manual

> **PREAMBLE:**
> 
> Metos3D is a high-performance computing software.
> combines two worlds
> the interface are the compilers that needs to be set by the user
> More precisely, a collection of source codes that needs to be compiled
> parallel,
> intended use is, on clusters, in parallel
> computing cluster,
> 
> each providing its optimal set of compilers
> shell command `metos3d` that manages everything
> and an environment that needs to be set up,
> in the convinient case, Metos3D recognizes the system,
> in the the other case, you as a user must provide compilers,
> **C, C++, Fortran compilers**
> 

## Metos3D Installation

Metos3D
package management system,
depends on a Python ecosystem called [Conda](https://conda.io/docs/),
[Anaconda](https://www.anaconda.com/),
[Miniconda](https://conda.io/miniconda.html)

`conda` command, installer, 
Install `metos3d` as a **shell command** with [`conda`](https://conda.io/miniconda.html):

```sh
curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
> **Note:** Let the installer, `.bashrc`, add the installation path to your environment variable
>

The `metos3d` command is part of a PyPI and usually ... 

```sh
conda install -c jpicau metos3d
```

From now on, a shell command `metos3d` is installed, can be used as, 

```sh
metos3d
```

See the [Metos3D cheat sheet](metos3d-cheat-sheet.md) for a complete list of available `metos3d` commands.

## Metos3D Environment

Initializes the shell environment,
MPI compilers, C, C++, Fortran,
compiles PETSc, including YAML, HDF5,
F2CBLAS,

```
metos3d env
metos3d petsc
```

## Metos3D Data and Models

```
metos3d data
metos3d model
```

## Metos3D Simulation

YAML [YAML](http://yaml.org/), configuration files, run files, examples, formats,

Configuration, compilation:

```sh
metos3d simpack model/NPZD-DOP/NPZD-DOP.conf.yaml
```

Run:

```sh
./metos3d-simpack-NPZD-DOP.exe experiment/mitgcm-128x64x15x10800.3000y.run.yaml 

# sequential run
# parallel run
mpirun -n 128 ...
#metos3d simpack experiment-001.conf.yaml
#metos3d simpack my.first.experiment.conf.yaml
```


## Metos3D Optimization



