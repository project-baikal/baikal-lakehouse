# Project Baikal

## What is Project Baikal

Project Baikal is a modern data lakehouse architecture designed to showcase best practices in data modeling, transformation, and governance using the medallion architecture (bronze, silver, gold). With tools like Apache Iceberg, Nessie, and dbt, it demonstrates how to unify batch and streaming data in a scalable, version-controlled environment.

## Why Project Baikal Exists

As the data ecosystem evolves, organizations need flexible architectures that scale, support diverse data sources, and maintain high data quality. Yet, resources for building a complete data lakehouse or modern analytics platform are limited. Project Baikal exists to demonstrate how modern tools and open standards—like Apache Iceberg, Project Nessie, and dbt—can be combined with the medallion architecture to build a robust, modular, and future-proof lakehouse. It serves as both a learning resource and a practical blueprint for teams ready to implement real solutions.

# The Baikal Lakehouse Architecture

### Tech Stack

| Layer/Component| Tool        |
| -------------- | ----------- |
| Storage        | S3          |
| Table Format      | Iceberg        |
|Metadata Catalog|Nessie|
|Orchestration & Data Ingestion|Dagster|
|Transformation| dbt|
|Query Enginer| trino|
|Data Quality| dbt tests|
|Security| tbd|
|Monitoring| tbd|
|Visualization/Serving| Tableau/DuckDB etc.

### Medallion Architecture for Data Organzation

- Bronze -> Raw data lake data in its raw form
- Silver -> Transformations/data cleansing/data processing
- Gold -> Curated data with business logic applied, ready to be served 