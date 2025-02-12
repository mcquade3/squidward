# Squidward

![Squidward.png](./images/README/Squidward.png)

A red team tool which takes gathered credentials and sends them out to other devices on the network. The tool checks if other machines can be logged into with these credentials.

## Usage:

```
source .venv/bin/activate
python3 squidward.py hosts.txt creds.txt
```

- Store list of hosts to connect to in txt file. This prevents program from attempting to connect out of scope.

```
127.0.0.1
10.0.0.1
```

- Store retrieved credentials in txt file.
- Store username on one line, password on next line, then skip a line before entering next credential pair. (Included creds.txt file shows proper syntax.)

```
alice
password123

bob
alejandra42

charlie
1w+4lO[-Z,{
```
