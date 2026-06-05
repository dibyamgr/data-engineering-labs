<div align="center">

# 🚀 Data Engineering Bootcamp

**From raw data to production pipelines — one module at a time.**

![Status](https://img.shields.io/badge/status-in_progress-F59E0B?style=flat-square)
![Modules](https://img.shields.io/badge/modules-9-6366F1?style=flat-square)
![Made by](https://img.shields.io/badge/engineer-Dibya_Rani_Saru_Magar-0EA5E9?style=flat-square)

</div>

---

> *"Data engineering is the foundation that makes everything else in AI, analytics, and machine learning possible.  
> Without clean pipes, nothing flows."*

This repository is my structured learning journal as I work through a comprehensive data engineering bootcamp — going from SQL fundamentals all the way to cloud-native pipelines on AWS, Azure, and Snowflake.

Every module has its own folder with code, notebooks, diagrams, and my personal notes. This isn't just a course dump — it's a living document of how I think, build, and grow as an engineer.

---

## What I'm building toward

By the end of this bootcamp, I'll be able to:

- Design and build **end-to-end ETL/ELT pipelines** from raw ingestion to analytical layer
- Work confidently with **distributed systems** (Hadoop, Spark, Kafka)
- Deploy **cloud-native data infrastructure** on AWS, Azure, and Snowflake
- Handle **structured, semi-structured, and streaming data** at scale
- Architect data warehouses and lakehouses that actually perform

---

## Learning path

| # | Module | Tools & Tech | Status          |
|---|--------|-------------|-----------------|
| 01 | **Intro to Data Engineering — SQL & Python** | Python, Pandas, SQL, PostgreSQL | 🔄 In progress  |
| 02 | **Data Warehousing with Hadoop & Hive** | HDFS, MapReduce, Hive, HiveQL | 🔄 In progress  |
| 03 | **Data Processing with Apache Spark** | PySpark, Spark SQL, MLlib | ⏳ Upcoming      |
| 04 | **Spark Transformations & ETL Functions** | PySpark, Delta Lake | ⏳ Upcoming      |
| 05 | **AWS Data Services** | Lambda, Glue, Redshift, S3 | ⏳ Upcoming      |
| 06 | **Snowflake & MongoDB** | Snowflake, MongoDB Atlas, NoSQL | ⏳ Upcoming      |
| 07 | **Azure Data Factory, Synapse & Databricks** | ADF, Synapse Analytics, Databricks | ⏳ Upcoming      |
| 08 | **Database Design & Kafka** | PostgreSQL, Apache Kafka, event streaming | ⏳ Upcoming      |
| 09 | **Capstone Project — End-to-End AWS Pipeline** | Full AWS stack | ⏳ Upcoming      |

---

## Module breakdowns

### 01 — Intro to Data Engineering: SQL & Python
> *The craft starts here.*

Learning to manipulate, clean, and analyze data the right way. This module covers Python scripting with Pandas, SQL for real-world queries, data normalization, integrity constraints, and quality checks — all grounded in practical case studies.

**Key concepts:** data types, normalization (1NF → 3NF → BCNF), data quality frameworks, joins and window functions, exploratory data analysis

---

### 02 — Data Warehousing with Hadoop & Hive
> *When your data is too big for one machine.*

Stepping into the world of distributed storage and processing. Learning how Hadoop's HDFS splits data across clusters and how Hive lets you query it with SQL-like syntax. Building data models, designing ETL pipelines, and understanding data cubes and query optimization at scale.

**Key concepts:** HDFS architecture, MapReduce, Hive metastore, partitioning, bucketing, ORC/Parquet formats, data cubes

---

### 03 — Data Processing with Apache Spark
> *Speed, scale, and elegance.*

Apache Spark is the engine that powers most modern data platforms. Learning Spark DataFrames, Spark SQL, and touching MLlib for machine learning pipelines. Practical projects that simulate real production workloads.

**Key concepts:** RDDs vs DataFrames, lazy evaluation, Spark execution model, partitioning, caching, Spark SQL, MLlib pipelines

---

### 04 — Spark Transformations & ETL Functions
> *Going deeper into the engine room.*

Mastering the transformation layer — joins, aggregations, UDFs, window functions in Spark, and building reusable ETL patterns. This is where pipelines go from working to production-grade.

**Key concepts:** transformation vs action, UDFs, groupBy/agg, window functions, broadcasting, Delta Lake

---

### 05 — AWS Data Services: Lambda, Glue & Redshift
> *The cloud is not optional anymore.*

Learning the AWS data ecosystem: serverless processing with Lambda, managed ETL with Glue, and analytical querying with Redshift. Understanding when to use each service and how they wire together.

**Key concepts:** S3 data lake, Lambda triggers, Glue crawlers and jobs, Redshift distribution styles, Spectrum, IAM roles

---

### 06 — Snowflake & MongoDB
> *The best of both worlds — warehouse and document store.*

Snowflake for cloud-native analytics (virtual warehouses, time travel, zero-copy cloning) and MongoDB for flexible, schema-less document storage. Two very different tools solving two very different problems.

**Key concepts:** Snowflake architecture, semi-structured data with VARIANT, MongoDB documents and collections, aggregation pipeline, indexing

---

### 07 — Azure Data Factory, Synapse & Databricks
> *The Microsoft data stack, fully explored.*

Building pipelines in Azure Data Factory, querying at scale with Synapse Analytics, and unifying data engineering and data science with Databricks. Learning how these three tools compose into a full analytics platform.

**Key concepts:** ADF pipelines and triggers, Synapse dedicated SQL pools, Delta Lake on Databricks, Unity Catalog, collaborative notebooks

---

### 08 — Database Design & Apache Kafka
> *Real-time data changes everything.*

Proper relational database design from the ground up, then moving into event-driven architecture with Kafka. Understanding producers, consumers, topics, partitions, and how streaming data flows through a modern system.

**Key concepts:** ER modeling, referential integrity, Kafka architecture, topics and partitions, consumer groups, Kafka Connect, stream processing

---

### 09 — Capstone Project: End-to-End AWS Pipeline
> *Putting it all together.*

A full production-style data pipeline built on AWS — ingestion, transformation, storage, orchestration, and analytics. Every concept from every module converges here.

**Stack:** S3 · Lambda · Glue · Redshift · Step Functions · CloudWatch · Athena

---

## Tech stack

```
Languages     Python · SQL · HiveQL · Bash
Processing    Apache Spark · Hadoop · Kafka
Warehouses    Redshift · Snowflake · Azure Synapse · Hive
Databases     PostgreSQL · MongoDB
Cloud         AWS (S3, Lambda, Glue, Redshift) · Azure (ADF, Databricks)
Formats       Parquet · ORC · Delta Lake · JSON · CSV
Tools         Jupyter · Docker · Git · VS Code
```

---

## Repository structure

```
data-engineering-bootcamp/
├── README.md
├── requirements.txt
├── .gitignore
├── NOTES.md                   ← cross-module insights and patterns
│
├── 01-sql-and-python/
│   ├── README.md
│   ├── scripts/
│   ├── notebooks/
│   └── data/
│
├── 02-hadoop-and-hive/
├── 03-spark-fundamentals/
├── 04-spark-etl/
├── 05-aws-data-services/
├── 06-snowflake-mongodb/
├── 07-azure-databricks/
├── 08-database-design-kafka/
│
└── 09-capstone-aws-project/
    ├── README.md
    ├── architecture/          ← diagrams
    ├── pipeline/              ← all pipeline code
    ├── infra/                 ← IaC / CloudFormation
    └── docs/
```

---

## How to use this repo

```bash
git clone https://github.com/dibyamgr/data-engineering-labs/
cd ...
pip ...
```

Each module folder has its own `README.md` explaining what was covered, key commands, gotchas, and how to run the code. Start there.

---

## Progress tracker

```
[██░░░░░░░░░░░░░░░░░░] Module 2 of 9 — just getting started
```

---

<div align="center">

*Built with curiosity, late nights, and a lot of coffee.*  
*Follow the journey — every commit is a step forward.*

</div>