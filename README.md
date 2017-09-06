# ansible-vault-search
Query an Ansible Vault for secrets

## Description:
Ever wanted to query an Ansible Vault from another program, for example to grab a secret in a CI build? ansible-vault-search helps to do that easily.

## Requirements

```
pip install -r requirements.txt
```

## Usage:

```
python vault_search.py -h
usage: vault_search.py [-h] --vault VAULT --password PASSWORD --query QUERY
                       [--raw]

Perform queries on an Ansible Vault

optional arguments:
  -h, --help            show this help message and exit
  --vault VAULT, -v VAULT
                        Path to Ansible Vault
  --password PASSWORD, -p PASSWORD
                        Password to unlock Ansible Vault
  --query QUERY, -q QUERY
                        Query string to look for in ansible vault, '.'
                        separated
  --raw, -r             Return a raw string, opposed to json
```

## Example:

```
json format:
python vault_search.py -v test_vault.yml -p test1234 -q database.postgres.host.d1.password

{"password": "xyz123"}

raw format:
python vault_search.py -v test_vault.yml -p test1234 -q database.postgres.host.d1.password -r

xyz123
```

## Limitations:
This application can only grab dictionary values from the yaml vault file at the moment, take a look at the example vault for supported data structures.
