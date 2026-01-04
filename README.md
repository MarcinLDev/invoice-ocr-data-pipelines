# Invoice OCR Data Pipelines

This repository contains a **public technical showcase** of production-style
Data Engineering pipelines extracted from a larger private project.

The goal of this project is to demonstrate **event-driven batch processing**,
Airflow orchestration, and a **bronze-layer data pipeline** for document ingestion.

---

## Problem

Companies receive invoices in **unstructured PDF format**, which must be:
- ingested reliably
- processed in parallel
- converted into structured, machine-readable data
- stored in a data lake for further analytics

OCR processing is CPU-heavy and requires:
- controlled parallelism
- retry handling
- idempotent execution

---

## Solution Overview

The solution is an **Airflow-based data pipeline** that:
1. Reads raw invoice PDFs from S3 (Bronze / RAW)
2. Dynamically fans out OCR processing per file
3. Stores extracted text back to S3 (Bronze / OCR)

### Key characteristics:
- Dynamic Task Mapping (scales with number of files)
- CPU throttling using Airflow Pools
- Idempotent processing (safe re-runs)
- Clean separation between orchestration and business logic

---

## Architecture
```md
S3 (raw PDFs)
|
v
[ Airflow DAG ]
|
|-- list PDF keys
|-- dynamic OCR tasks (fan-out)
|
v
S3 (OCR text output)

```
---

## Pipelines

### Bronze Invoice OCR Pipeline

**Purpose**
Convert unstructured PDF invoices into OCR-extracted text files.

**Input**
- S3 prefix: `01_bronze/.../raw_faktury/`

**Output**
- S3 prefix: `01_bronze/.../ocr_faktury/`

**Features**
- Dynamic Task Mapping (`.expand`)
- Airflow Pool for CPU-heavy OCR tasks
- Retry & failure handling
- Idempotent writes (skip if output already exists)

---

## Technology Stack

- Python
- Apache Airflow (TaskFlow API)
- Amazon S3 (data lake storage)
- pdf2image + Tesseract OCR
- Docker (local execution)

---

## Repository Structure

```text
invoice-ocr-data-pipelines/
├── dags/
│   └── bronze_invoice_ocr.py
├── pipelines/
│   └── bronze/
│       └── invoice_ocr/
│           ├── ocr.py
│           ├── process.py
│           └── s3_utils.py
└── README.md

```

## Notes

- Bucket names and paths are anonymized for public sharing
- Full production implementation is kept in a private repository

The pipeline is safe to re-run multiple times without producing duplicate outputs.


