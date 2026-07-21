# Threat Intel Triage Tool

## Overview

A Python command-line tool that checks an IP address against the VirusTotal v3 API and returns a clear clean/malicious verdict, pulling from VirusTotal's aggregated multi-vendor threat data. Built to save a SOC analyst the manual step of looking up an indicator by hand during alert triage — feed it an IP, get a readable report back.

---

## Tech Stack

- **Language:** Python 3
- **HTTP requests:** `requests` library, calling the VirusTotal v3 REST API
- **Secrets handling:** `python-dotenv` to keep the API key out of the codebase, with `.gitignore` excluding `.env` from version control

### Local Development Setup

[![VS Code Environment Setup](https://github.com/TheCptNubs30/threat-intel-automation/raw/main/vscode_workspace.png)](/TheCptNubs30/threat-intel-automation/blob/main/vscode_workspace.png)

---

## How It Works

1. Takes an IP address as input
2. Queries the VirusTotal API for that IP's reputation data
3. Parses the JSON response and counts malicious/suspicious/clean flags across vendors
4. Handles common failure cases cleanly — invalid API key (`401`), IP not found (`404`) — instead of crashing
5. Prints a formatted report with a clear verdict and, if malicious, a suggested next action

---

## Validation

I tested the tool against two scenarios to confirm the classification logic works correctly on both ends:

### Scenario A: Clean IP (8.8.8.8)

Queried a known trusted public DNS resolver to confirm the tool correctly identifies clean addresses without raising false alarms.

[![Command Prompt Clean Run Output](https://github.com/TheCptNubs30/threat-intel-automation/raw/main/terminal_clean_run.png)](/TheCptNubs30/threat-intel-automation/blob/main/terminal_clean_run.png)

```
[+] Querying VirusTotal for telemetry on: 8.8.8.8...
=========================================
📊 REPORT FOR IP: 8.8.8.8
=========================================
🔴 Malicious Flags: 0
🟡 Suspicious Flags: 0
🟢 Clean/Harmless Flags: 74
-----------------------------------------
✅ STATUS: 8.8.8.8 appears clean. No malicious signatures detected.
=========================================
```

### Scenario B: Malicious IP (1.117.214.34)

Queried a known-bad IP to confirm the tool correctly flags a threat and surfaces actionable guidance.

[![Command Prompt Malicious Run Output](https://github.com/TheCptNubs30/threat-intel-automation/raw/main/terminal_malicious_alert.png)](/TheCptNubs30/threat-intel-automation/blob/main/terminal_malicious_alert.png)

```
[+] Querying VirusTotal for telemetry on: 1.117.214.34...
=========================================
📊 REPORT FOR IP: 1.117.214.34
=========================================
🔴 Malicious Flags: 14
🟡 Suspicious Flags: 0
🟢 Clean/Harmless Flags: 60
-----------------------------------------
🚨 ALERT: 1.117.214.34 has been flagged as MALICIOUS by 14 security vendors!
[ACTION REQUIRED] Isolate endpoint and block this IP on the perimeter firewall.
=========================================
```

---

## What I'd Add Next

- Batch lookup support (list of IPs from a CSV instead of one at a time)
- Support for hash and domain lookups, not just IPs
- Export results to CSV/JSON for use in a ticketing system

---

## About

Built as a hands-on project to practice API integration, error handling, and threat intelligence enrichment — the kind of lookup step a Tier 1 SOC analyst does dozens of times a shift, automated.
