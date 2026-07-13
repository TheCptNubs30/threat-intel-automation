# Threat Intelligence Triage Automation Tool

## 📌 Executive Summary
Manual triage of Security Operations Center (SOC) alerts significantly impacts incident response lifecycle metrics. Tier 1 analysts frequently waste valuable operational cycles copy-pasting Indicators of Compromise (IoCs) across disjointed threat intelligence web consoles. 

This project solves that operational bottleneck. It is a production-ready **Python-driven Threat Intelligence Automation Script** that communicates securely via API with the **VirusTotal v3 engine**. It programmatically ingests external IP addresses, aggregates multi-vendor security telemetry, evaluates malicious thresholds, and automatically outputs actionable perimeter defensive instructions to accelerate incident triage.

---

## 🏗️ Technical Architecture & Core Tools
* **Language:** Python 3.x
* **Libraries:** `requests` (API integration), `python-dotenv` (Secure environment variables management)
* **Threat Intelligence Provider:** VirusTotal v3 Core API Engine
* **Target Scope:** External IPv4 Threat Analysis, Vendor Telemetry Parsing

---

## 🖥️ Development Workspace & Environment Setup
To ensure proper structural configuration, the local environment isolates administrative variables from the raw source code. 

### Local Repository Architecture:
Below is the verified production workspace configuration inside Visual Studio Code, displaying the isolated `.env` file and programmatic script placement:

![VS Code Environment Setup](vscode_workspace.png)

---

## 🔒 Security Architecture (Zero-Leak Policy)
To adhere to enterprise-grade DevSecOps standards, this repository implements a strict **Zero-Leak API Key Policy**. The core application isolates private infrastructure keys within a localized `.env` file. A programmatic `.gitignore` layer ensures sensitive access credentials are never synchronized or leaked to public source control.

---

## ⚙️ Installation & Deployment

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/TheCptNubs30/threat-intel-automation.git](https://github.com/TheCptNubs30/threat-intel-automation.git)
   cd threat-intel-automation
