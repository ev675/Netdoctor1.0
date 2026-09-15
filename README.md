<div align="center">



 NetDoctor



 Intelligent Internet Fault Diagnosis \& Root-Cause Analysis Platform



Find WHERE the Internet Problem Starts — Not Just How Fast It Is



<br/>



!\[Status](https://img.shields.io/badge/status-in%20development-orange)

!\[Python](https://img.shields.io/badge/Python-3.12+-blue)

!\[FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)

!\[Next.js](https://img.shields.io/badge/Next.js-Frontend-black)

!\[PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791)

!\[Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)

!\[License](https://img.shields.io/badge/license-MIT-green)



</div>



\---



Project Overview



NetDoctor is an intelligent network diagnosis and root-cause analysis platform designed to identify where an Internet connection is failing.



Traditional speed-test applications primarily answer:



> "How fast is my Internet?"



NetDoctor focuses on a different question:



> "Why is my Internet connection degraded, and where does the problem start?



The system collects measurements from multiple network layers including:



\- Device / Network Interface

\- Local Gateway / Router

\- Wi-Fi / LAN

\- DNS

\- ISP Access Network

\- Upstream Network

\- Destination Server



These measurements are correlated with historical baselines and diagnostic rules to determine the most likely failure domain.



\---



 Problem Statement



When users experience:



\- High latency

\- Packet loss

\- DNS failures

\- Intermittent connectivity

\- Video-call problems

\- Gaming lag

\- Slow websites

\- Random disconnections



most conventional tools provide isolated measurements such as:



```text

Ping

Speed

DNS lookup

Traceroute

```



However, these measurements are rarely combined into a single explainable diagnosis.



NetDoctor attempts to bridge this gap by correlating multiple network measurements and producing an \*\*evidence-backed diagnosis\*\*.



\---



Core Idea



```text

                INTERNET PROBLEM
                          │

                         ▼

             ┌─────────────────────┐

            │    NetDoctor Agent  │

              └──────────┬──────────┘
                      │

          ┌─────────────┼─────────────┐

           │             │             │

            ▼             ▼             ▼

        Gateway         DNS        Traceroute

           │             │             │

            └─────────────┼─────────────┘
                          │

                        ▼
                  FastAPI Backend

                        │

                         ▼

                 Measurement Storage

                          │

          ┌─────────────┴─────────────┐

           │                           │

           ▼                           ▼

     Rule-Based Engine            ML Analysis

          │                           │

          └─────────────┬─────────────┘

                         │
                      ▼

                Root Cause Analysis

                         │
                          ▼

               Human-Readable Diagnosis

```



\---



\ System Architecture



```mermaid

flowchart TB


  USER\["👤 User"]



  DASH\["🖥️ Web Dashboard<br/>Next.js + TypeScript"]



  AGENT\["🐍 Local Diagnostic Agent<br/>Python"]



   DEVICE\["💻 Device Tests"]

  GATEWAY\["📡 Gateway / Router Tests"]

  DNS\["🌐 DNS Tests"]

   PING\["📶 Ping / Latency"]

   TRACE\["🛣️ Traceroute"]

   HTTP\["🔗 HTTP / HTTPS Tests"]



   API\["⚡ FastAPI Backend"]



   DB\[("🗄️ PostgreSQL")]



   RULE\["🧠 Rule-Based Diagnosis"]

  ML\["🤖 ML / Anomaly Detection"]



   REPORT\["📄 Diagnostic Report"]



  USER --> DASH

   DASH --> API



   AGENT --> DEVICE

   AGENT --> GATEWAY

   AGENT --> DNS

  AGENT --> PING

  AGENT --> TRACE

  AGENT --> HTTP



  AGENT --> API



   API --> DB



   DB --> RULE

  DB --> ML



  RULE --> REPORT

   ML --> REPORT



   REPORT --> API

  API --> DASH

```



\---



\ Diagnostic Layers



NetDoctor analyzes the network progressively.



```mermaid

flowchart LR



  A\["💻 Device"]

  B\["📡 Router / Gateway"]

  C\["📶 Wi-Fi / LAN"]

  D\["🌐 DNS"]

   E\["🏢 ISP Network"]

   F\["🛣️ Upstream Network"]

  G\["☁️ Destination"]



   A --> B

   B --> C

   C --> D

   D --> E

   E --> F

   F --> G

```



The objective is to determine the \*\*first layer at which abnormal behavior appears\*\*.



\---



\ Example Diagnosis



Suppose the measurements are:



```text

Device → Router        GOOD

Router → ISP           GOOD

DNS                    GOOD

ISP → Destination      PROBLEM

```



Traceroute:



```text

Hop 1      2 ms

Hop 2      5 ms

Hop 3      8 ms

Hop 4     12 ms

Hop 5     18 ms

Hop 6    180 ms   ← abnormal

Hop 7    185 ms

```



NetDoctor may produce:



```text

┌──────────────────────────────────────────┐

│          🩺 NETDOCTOR DIAGNOSIS          │

├──────────────────────────────────────────┤

│ Failure Domain : UPSTREAM NETWORK        │

│ Severity       : HIGH                    │

│ Confidence     : 81%                     │

├──────────────────────────────────────────┤

│ Evidence:                                 │

│                                          │

│ ✓ Local gateway is healthy               │

│ ✓ DNS response is normal                 │

│ ✓ Initial hops show normal latency       │

│ ⚠ Latency increases significantly        │

│   after hop 6                            │

│ ⚠ Packet loss begins downstream          │

└──────────────────────────────────────────┘

```



\---



\# 🧠 Diagnosis Engine



NetDoctor does not depend entirely on Machine Learning.



The diagnosis pipeline is:



```mermaid

flowchart TD



  M\["📊 Network Measurements"]



   F\["Feature Extraction"]



   R\["Rule Engine"]



   B\["Historical Baseline"]



   ML\["Machine Learning<br/>Anomaly Detection"]



   C\["Correlation Engine"]



  D\["Final Diagnosis"]



   E\["Evidence"]



  M --> F

   F --> R

   F --> B

  F --> ML



   R --> C

   B --> C

   ML --> C



   C --> D

   D --> E

```



\ Initial approach



\*\*Phase 1\*\*



Rule-based diagnosis.



\*\*Phase 2\*\*



Historical baseline detection.



\*\*Phase 3\*\*



Machine-learning anomaly detection.



\*\*Phase 4\*\*



Combined evidence-based diagnosis.



This makes the system explainable instead of simply returning:



```text

"AI says Internet is bad."

```



\---



\# 🤖 Machine Learning



The ML subsystem will learn the user's normal network behavior.



Example historical features:



```text

timestamp

ISP

ASN

destination

latency

jitter

packet\_loss

DNS\_latency

gateway\_latency

HTTP\_latency

hop\_latency

Wi-Fi\_signal

time\_of\_day

```



The first ML objective is:



\### Anomaly Detection



Example:



```text

Normal baseline



Latency       25–35 ms

Jitter         3–7 ms

Packet Loss   <1%



Current



Latency       148 ms

Jitter         39 ms

Packet Loss   7.4%

```



The system can identify this as a significant deviation from the user's normal baseline.



Potential models:



\- Isolation Forest

\- Random Forest

\- Gradient Boosting

\- Logistic Regression



Model selection will be based on actual experimental evaluation rather than simply choosing the most complex model.



\---



\# 🌐 Multi-Destination Analysis



A major component of NetDoctor is comparing different destinations.



Example:



```text

Google        → 28 ms

Cloudflare    → 31 ms

GitHub        → 30 ms

YouTube       → 29 ms



One specific destination:



Game Server   → 150 ms

```



This can indicate a \*\*destination-specific problem\*\* rather than a complete ISP failure.



Conversely:



```text

Google        → 150 ms

Cloudflare    → 160 ms

GitHub        → 145 ms

YouTube       → 155 ms

```



This provides stronger evidence of a broader network problem.



\---



\#  Network Comparison



NetDoctor can compare network conditions across different networks.



Example:



| Network | Latency | Jitter | Packet Loss | DNS |

|---|---:|---:|---:|---:|

| Airtel | 28 ms | 4 ms | 0.2% | 19 ms |

| Jio | 44 ms | 11 ms | 1.4% | 25 ms |

| Campus Wi-Fi | 91 ms | 22 ms | 3.1% | 41 ms |



The comparison should be performed using comparable:



\- destinations

\- time periods

\- test duration

\- measurement methodology



\---



\ ISP Complaint Report



NetDoctor can generate an evidence-based report that users can share with their ISP.



Example:



```text

==================================================

&#x20;             NETDOCTOR DIAGNOSTIC REPORT

==================================================



ISP:

XYZ Internet



Test Duration:

15 minutes



Observed Issue:

Intermittent packet loss



Average Packet Loss:

7.4%



Historical Baseline:

< 1%



Average Latency:

148 ms



Historical Baseline:

32 ms



Affected Services:

\- HTTPS

\- Video Calls

\- Gaming



Likely Failure Domain:

ISP / Upstream Network



Confidence:

81%



Evidence:

\- Local gateway healthy

\- DNS healthy

\- Packet loss begins after hop 6

\- RTT increases significantly downstream

\- Multiple destinations affected



==================================================

```



\---



\# 🧩 Main Components



| Component | Technology | Purpose |

|---|---|---|

| Frontend | Next.js + TypeScript | User dashboard |

| Backend | FastAPI | API + business logic |

| Agent | Python | Local network diagnostics |

| Database | PostgreSQL | Measurement storage |

| ML | Scikit-learn | Anomaly detection |

| Monitoring | Prometheus | Metrics collection |

| Visualization | Grafana | Developer monitoring |

| Containers | Docker | Reproducible deployment |

| CI/CD | GitHub Actions | Automated testing |

| Version Control | Git + GitHub | Source management |



\---



\# 🔄 Complete System Flow



```mermaid

sequenceDiagram



&#x20;   participant U as User

&#x20;   participant F as Frontend

&#x20;   participant A as Local Agent

&#x20;   participant B as FastAPI

&#x20;   participant DB as PostgreSQL

&#x20;   participant D as Diagnosis Engine



&#x20;   U->>F: Start Diagnosis



&#x20;   F->>A: Start diagnostic session



&#x20;   A->>A: Test gateway

&#x20;   A->>A: Test DNS

&#x20;   A->>A: Test latency

&#x20;   A->>A: Test packet loss

&#x20;   A->>A: Run traceroute

&#x20;   A->>A: Test HTTP/HTTPS



&#x20;   A->>B: Send measurements



&#x20;   B->>DB: Store measurements



&#x20;   DB->>D: Provide measurements



&#x20;   D->>D: Apply rules

&#x20;   D->>D: Compare baseline

&#x20;   D->>D: Run ML analysis



&#x20;   D->>B: Diagnosis + evidence



&#x20;   B->>F: Diagnosis result



&#x20;   F->>U: Display explanation

```



\---



\# 🏥 Why a Local Agent?



A browser cannot reliably perform all low-level network diagnostics because browsers operate inside a security sandbox.



Therefore NetDoctor uses:



```text

&#x20;                NETDOCTOR

&#x20;                    │

&#x20;       ┌────────────┴────────────┐

&#x20;       │                         │

&#x20;  Web Dashboard             Local Agent

&#x20;     Browser                    Python

&#x20;       │                         │

&#x20;       │                    Network Access

&#x20;       │                         │

&#x20;       └──────────┬──────────────┘

&#x20;                  │

&#x20;               Backend

```



The local Python agent performs operations such as:



\- Gateway detection

\- ICMP/ping measurements

\- DNS measurements

\- Traceroute

\- HTTP/HTTPS testing

\- Network interface information



The agent sends only structured measurements to the backend.



\---



\# 🔐 Security Principles



NetDoctor will follow these principles:



\- Never expose database credentials to frontend

\- Never allow arbitrary shell commands from users

\- Validate all diagnostic targets

\- Apply subprocess timeouts

\- Validate API input

\- Use environment variables for secrets

\- Implement CORS correctly

\- Add authentication before public deployment

\- Apply rate limiting

\- Use HTTPS in production

\- Keep structured logs

\- Never store unnecessary sensitive network information



\### Secure architecture



```text

❌ Browser → Database



❌ Agent → Database



❌ User Input → os.system()



✅ Browser → FastAPI → PostgreSQL



✅ Agent → FastAPI → PostgreSQL



✅ Validated Input → Safe subprocess → Result

```



\---



\# 📁 Repository Structure



```text

netdoctor/

│

├── agent/

│   ├── netdoctor\_agent/

│   └── tests/

│

├── backend/

│   ├── app/

│   └── tests/

│

├── frontend/

│

├── ml/

│

├── database/

│

├── monitoring/

│

├── docs/

│   ├── architecture.md

│   ├── api.md

│   ├── database.md

│   ├── agent.md

│   ├── diagnosis-engine.md

│   ├── ml.md

│   ├── deployment.md

│   ├── security.md

│   ├── testing.md

│   └── decisions/

│

├── tests/

│

├── scripts/

│

├── .github/

│   └── workflows/

│

├── .gitignore

├── .env.example

├── docker-compose.yml

├── LICENSE

└── README.md

```



\---



\# 🛠️ Development Roadmap



```mermaid

flowchart LR



  P0\["Phase 0<br/>Foundation"]

   P1\["Phase 1<br/>Network Agent"]

  P2\["Phase 2<br/>FastAPI"]

 P3\["Phase 3<br/>PostgreSQL"]

   P4\["Phase 4<br/>Agent ↔ API"]

   P5\["Phase 5<br/>Diagnosis Engine"]

   P6\["Phase 6<br/>Dashboard"]

   P7\["Phase 7<br/>Historical Baseline"]

   P8\["Phase 8<br/>Machine Learning"]

   P9\["Phase 9<br/>Network Comparison"]

  P10\["Phase 10<br/>ISP Report"]

   P11\["Phase 11<br/>Monitoring"]

   P12\["Phase 12<br/>Docker"]

   P13\["Phase 13<br/>CI/CD"]

   P14\["Phase 14<br/>Deployment"]

   P15\["Phase 15<br/>Security + Demo"]



   P0 --> P1

   P1 --> P2

   P2 --> P3

   P3 --> P4

P4 --> P5

   P5 --> P6

   P6 --> P7

   P7 --> P8

  P8 --> P9

   P9 --> P10

   P10 --> P11

  P11 --> P12

   P12 --> P13

   P13 --> P14

   P14 --> P15

```



\---



\#  Development Philosophy



NetDoctor will be developed incrementally.



We will not build everything at once.



Each component will go through:



```text

Design

&#x20;  ↓

Implementation

&#x20;  ↓

Unit Test

&#x20;  ↓

Integration Test

&#x20;  ↓

Documentation

&#x20;  ↓

Git Commit

&#x20;  ↓

Pull Request

&#x20;  ↓

Merge

```



\---



\# 🧪 Testing Strategy



\### Unit Testing



Examples:



\- Ping parser

\- DNS parser

\- Jitter calculation

\- Packet-loss calculation

\- Health score

\- Diagnosis rules



\### Integration Testing



```text

Agent

&#x20; ↓

FastAPI

&#x20; ↓

PostgreSQL

&#x20; ↓

Diagnosis Engine

```



\### End-to-End Testing



```text

User

&#x20;↓

Dashboard

&#x20;↓

Agent

&#x20;↓

Backend

&#x20;↓

Database

&#x20;↓

Diagnosis

&#x20;↓

Dashboard

```



\---



\# 📈 Observability



NetDoctor will use:



```text

FastAPI

&#x20;  │

&#x20;  ▼

Prometheus

&#x20;  │

&#x20;  ▼

Grafana

```



Developer/admin metrics may include:



\- API health

\- API response time

\- HTTP error rate

\- Diagnostic requests

\- Diagnostic duration

\- Agent status

\- Database errors

\- System metrics



Grafana is intended for \*\*developers/administrators\*\*, not as the primary user dashboard.



\---



\# 🐳 Deployment Architecture



Eventually:



```mermaid

flowchart TB



   USER\["👤 User"]



   FRONT\["Next.js"]



   API\["FastAPI"]



   DB\[("PostgreSQL")]



   PROM\["Prometheus"]



   GRAF\["Grafana"]



  DOCKER\["Docker"]



&#x20;   CLOUD\["☁️ Cloud Deployment"]



&#x20;   USER --> FRONT

&#x20;   FRONT --> API

&#x20;   API --> DB



&#x20;   API --> PROM

&#x20;   PROM --> GRAF



&#x20;   FRONT --> DOCKER

&#x20;   API --> DOCKER

&#x20;   DB --> DOCKER

&#x20;   PROM --> DOCKER

&#x20;   GRAF --> DOCKER



&#x20;   DOCKER --> CLOUD

```



Cloud deployment will be added only after the local system is stable.



\---



\# 🆓 Cost Philosophy



NetDoctor is designed to be developed with \*\*₹0 initial software cost\*\*.



Preferred technologies are open-source or free-tier services.



```text

Development

&#x20;   ↓

Local Machine

&#x20;   ↓

Docker

&#x20;   ↓

PostgreSQL

&#x20;   ↓

Open Source ML

&#x20;   ↓

GitHub

&#x20;   ↓

Free deployment options

```



Paid infrastructure will not be introduced unless it becomes technically necessary.



\---



\# 🎓 Academic Value



NetDoctor combines multiple areas of Computer Science:



```text

Computer Networks

&#x20;      +

Python

&#x20;      +

Backend Engineering

&#x20;      +

Database Systems

&#x20;      +

Machine Learning

&#x20;      +

Distributed Systems

&#x20;      +

DevOps

&#x20;      +

Observability

&#x20;      +

Cybersecurity

```



This makes it suitable as a substantial final-year engineering project.



\---



\# 🚀 Future Scope



Potential future extensions include:



\- Advanced network anomaly detection

\- ISP outage detection

\- Community network intelligence

\- Autonomous diagnosis

\- Network incident prediction

\- Explainable AI

\- LLM-assisted diagnostic explanations

\- Mobile diagnostic agent

\- Network health forecasting

\- ISP route comparison

\- Enterprise network monitoring

\- AIOps integration



These features will be considered only after the core diagnostic system is stable.



\---



\# 📚 Documentation



Detailed technical documentation will be maintained under:



```text

docs/

├── architecture.md

├── api.md

├── database.md

├── agent.md

├── diagnosis-engine.md

├── ml.md

├── deployment.md

├── security.md

├── testing.md

└── decisions/

```



\---



\# 👥 Development Team



NetDoctor is being developed as a collaborative engineering project.



Responsibilities will be divided across:



\- Network Diagnostics / Python Agent

\- Backend / Database

\- Frontend / UX

\- ML / Diagnosis / DevOps



The exact ownership structure will be documented as the project progresses.



\---



\# 📜 License



This project is licensed under the MIT License.



\---



\# ⭐ Vision



> \*\*NetDoctor is not another speed-test application.\*\*

>

> It is an explainable network diagnosis platform designed to answer:

>

> \*\*"Where does the Internet problem actually start?"\*\*



\---



<div align="center">



\NetDoctor



\*\*Measure → Correlate → Diagnose → Explain\*\*



</div>

