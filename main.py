#!/usr/bin/env python3

import subprocess
import argparse
import sys


def run_command(command):
    """Execute a shell command and return the output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return result.stdout.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr.decode('utf-8')}", file=sys.stderr)
        sys.exit(1)


def add_rule(chain, protocol, port, action):
    """Add a new firewall rule."""
    command = f"sudo iptables -A {chain} -p {protocol} --dport {port} -j {action}"
    print(f"Adding rule: {command}")
    return run_command(command)


def delete_rule(chain, protocol, port):
    """Delete an existing firewall rule."""
    command = f"sudo iptables -D {chain} -p {protocol} --dport {port} -j ACCEPT"
    print(f"Deleting rule: {command}")
    return run_command(command)


def list_rules():
    """List all firewall rules."""
    command = "sudo iptables -L"
    return run_command(command)


def main():
    parser = argparse.ArgumentParser(description="CLI Firewall Configuration Tool")

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Add rule command
    add_parser = subparsers.add_parser("add", help="Add a new firewall rule")
    add_parser.add_argument(
        "chain", choices=["INPUT", "OUTPUT", "FORWARD"], help="Firewall chain"
    )
    add_parser.add_argument("protocol", choices=["tcp", "udp"], help="Protocol")
    add_parser.add_argument("port", type=int, help="Port number")
    add_parser.add_argument(
        "action", choices=["ACCEPT", "DROP"], help="Action (ACCEPT or DROP)"
    )

    # Delete rule command
    delete_parser = subparsers.add_parser(
        "delete", help="Delete an existing firewall rule"
    )
    delete_parser.add_argument(
        "chain", choices=["INPUT", "OUTPUT", "FORWARD"], help="Firewall chain"
    )
    delete_parser.add_argument("protocol", choices=["tcp", "udp"], help="Protocol")
    delete_parser.add_argument("port", type=int, help="Port number")

    # List rules command
    subparsers.add_parser("list", help="List all firewall rules")

    args = parser.parse_args()

    if args.command == "add":
        print(add_rule(args.chain, args.protocol, args.port, args.action))
    elif args.command == "delete":
        print(delete_rule(args.chain, args.protocol, args.port))
    elif args.command == "list":
        print(list_rules())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
