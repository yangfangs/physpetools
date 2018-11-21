# Install PhySpeTree in your favorite ways

# For the linux platform
## 1. PyPI

```bash
$ pip install PhySpeTree
```

or [download](https://pypi.python.org/pypi/PhySpeTree/) and install:

```bash
$ pip install PhySpeTree-*.tar.gz
```

To upgrade to the latest version:

```bash
$ pip install --upgrade PhySpeTree
```

## 2. GitHub

```bash
$ git clone git@github.com:yangfangs/physpetools.git
$ cd physpetools
$ python setup.py install
```
or [download](https://github.com/yangfangs/physpetools/releases) and install:

```bash
$ pip install physpetools-*.tar.gz
```

# For other operating systems

* for other operating systems such as Windows OS or Mac OS, we packaged all PhySpeTree run environment as a Docker image
by [docker][https://www.docker.com/] technology.

## Dependence

* If you want to use PhySpeTree on other platforms, above all need to install docker on the appropriate platform.
* For Windows OS, you can [install Docker for Windows](https://docs.docker.com/docker-for-windows/install/).
* For Mac OS, you can [install Docker for Mac](https://docs.docker.com/docker-for-mac/install/).

## Get PhySpeTree image

* When Docker are running in your operating system, you can use Docker command to pull the PhySpeTree latest version image as follow:

```bash
$ docker pull yangfangs/physpetree:v0.3.4
```


