#!/usr/bin/env python
from ansible_vault import Vault
import argparse
import json

class AnsibleVaultSearch(object):
    def __init__(self, vault_password, vault_path):
        try:
            self.vault = Vault(vault_password)
            self.data = self.vault.load(open(vault_path).read())
        except Exception as e:
            raise e

    def search(self, query, raw_structure):
        obj = None
        last_attr = None
        for attr in query.split("."):
            try:
                if not obj:
                    last_attr = attr
                    obj = self.data[attr]
                else: 
                    last_attr = attr
                    obj = obj[attr]
            except (TypeError, KeyError):
                # Type not dictionary, so fail as not implemented
                obj = getattr(obj, attr)

        if raw_structure:
            print obj
        else:
            json_obj = json.dumps({last_attr: obj})
            print json_obj

def main():
    parser = argparse.ArgumentParser(description="Perform queries on an Ansible Vault")
    parser.add_argument("--vault", "-v", help="Path to Ansible Vault", required=True)
    parser.add_argument("--password", "-p", help="Password to unlock Ansible Vault", required=True)
    parser.add_argument("--query", "-q", help="Query string to look for in ansible vault, '.' separated", required=True)
    parser.add_argument("--raw", "-r", help="Return a raw string, opposed to json", action="store_true", default=False)
    args = parser.parse_args()

    vault = AnsibleVaultSearch(args.password, args.vault)
    vault.search(args.query, args.raw)

if __name__ == "__main__":
    main()




