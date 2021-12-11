# codeo-cli

`codeo` cli is a small utility for sending your code to [www.codeo.app](https://codeo.app/) ,  which is small website created by [Andrés Mejía](https://twitter.com/mejibyte) where you can practice algorithms and data structures.

## Installation

Before using `codeo` cli you need to create an account on [codeo.app](https://codeo.app/beta?redirect_to=%2Fusuarios%2Fcrear). Use `quieroaprender` as invitation code, then you can create your account typing a `username`, `email` and `password`.

`codeo` was written by using `Python3` that is why you need to have installed at least the python version `3.8` on your local machine.

Now you can get `codeo-cli` CLI from PyPI:


```bash

pip install codeo-cli

```

## Usage

Once you have installed `codeo` CLI you need to define two enviroment variables that will be used for authenticating you in [www.codeo.app](https://codeo.app/). Type the `username` and `password` that you used to sign up in `wwww.codeo.app`.

```bash
$ export USER_NAME=...

$ export PASSWORD=...

```

Now we are almost ready to submit our code:

1 - Go to [www.codeo.app/problemas](https://codeo.app/problemas)

2 - Look at the problem that you want to submit and write the solution in a file in your machine by using the editor and programming language that you prefer.

3 - Copy the url that the problem has on [www.codeo.app/problemas](https://codeo.app/problemas).

