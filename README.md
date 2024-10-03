
# FireCLI

FireCLI is a command-line tool designed to help manage firewall configurations. It allows you to add, remove, and list firewall rules via an intuitive command-line interface. Currently, the tool supports `iptables` on Linux and can be extended to work with other platforms (e.g., Windows, macOS).

## Features

- Add firewall rules to allow or block traffic.
- Remove existing firewall rules.
- List all active firewall rules.
- Supports both TCP and UDP protocols.

## Logo

![FireCLI Logo](assets/fireCLI.jpg)

## Requirements

- Python 3.x
- Linux system with `iptables` installed
- `sudo` privileges to modify firewall rules

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/firecli.git
   cd firecli
   ```

2. Make the Python script executable:

   ```bash
   chmod +x firewall_tool.py
   ```

3. (Optional) Add the tool to your PATH to use it globally:

   ```bash
   sudo ln -s $(pwd)/firewall_tool.py /usr/local/bin/firecli
   ```

## Usage

### Add a Firewall Rule

To add a new rule, use the `add` command:

```bash
firecli add [CHAIN] [PROTOCOL] [PORT] [ACTION]
```

- **CHAIN**: Choose from `INPUT`, `OUTPUT`, or `FORWARD`
- **PROTOCOL**: `tcp` or `udp`
- **PORT**: Port number (e.g., 80 for HTTP)
- **ACTION**: `ACCEPT` or `DROP`

Example:

```bash
firecli add INPUT tcp 80 ACCEPT
```

### Delete a Firewall Rule

To remove an existing rule, use the `delete` command:

```bash
firecli delete [CHAIN] [PROTOCOL] [PORT]
```

Example:

```bash
firecli delete INPUT tcp 80
```

### List Firewall Rules

To list all the active firewall rules:

```bash
firecli list
```

### Help

For help with commands and usage:

```bash
firecli --help
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

