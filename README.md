# tools_communication

This repo contains source code of the Linux Command named target. This command is useful for accessing the json ouput of a function. This function can be piped with with a function and the json can be accessed.

### Usage

```sh
target
# options
# -k | key
```

Below are some exaples with tool ggraph:

```sh
ggraph -p python-cat -j|target -k packages
```

<img src="./Screenshot 2020-10-06 at 4.30.43 PM.png">

```sh
ggraph -s python-cat,python-apple -j|target -k packages
```

<img src="./Screenshot 2020-10-06 at 4.32.13 PM.png">

