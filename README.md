# codeo-cli

`codeo` CLI is a small utility for sending your code to [www.codeo.app](https://codeo.app/) ,  which is small website created by [Andrés Mejía](https://twitter.com/mejibyte) where you can practice algorithms and data structures.

## Installation

Before using `codeo` CLI you need to create an account on [codeo.app](https://codeo.app/beta?redirect_to=%2Fusuarios%2Fcrear). Use `quieroaprender` as invitation code, then you can create your account typing a `username`, `email` and `password`.

`codeo` was written by using `Python3` that is why you need to have installed at least the python version `3.8` on your local machine.

Now you can get `codeo-cli` CLI from PyPI:


```bash

pip install codeo

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

### Example:

Solution to `# 0x0 - Hola Codeo`, whic has the this URL: https://codeo.app/problemas/0x0-hola-codeo

*hello_codeo.py*
```py
print("Hola Codeo")
```

Submit above code to [www.codeo.app](https://codeo.app/)

```bash
$ codeo --file hello_codeo.py --url https://codeo.app/problemas/0x0-hola-codeo
```

If it went well, so you should be on your terminal the following output:

If it went well, so you should see on your terminal the following output:

```bash
Problem: 0x0 - Hola Codeo
* Author: <author name>
* Date: 2021-12-18 16:23:29 UTC (Hace menos de 1 minuto)
┏━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━┓
┃ Case ┃     Result     ┃ Time   ┃ Memory ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━┩
│  #1  │ Correcto       │ 0.006 s│ 51 KBi │
└──────┴────────────────┴────────┴────────┘
Total Score: 100 / 100
```