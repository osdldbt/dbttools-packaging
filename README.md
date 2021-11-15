# dbttools packaging

This repository contains scripts, relying on `docker-compose`, used to build
`dbttools` package. Only the RPM format for centos8 is supported.

## Package building

Execute the `make` command to build the package:
```console
$ make
```

Generated package is located into the `build/` directory.
