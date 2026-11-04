# Author Guidelines — RBCS (English)

The **Brazilian Journal of Computing and Scientific Software (RBCS)** publishes research focused on open-source scientific software and computational tools.

## 1. Eligibility Criteria

To be published in RBCS, a software repository must meet all the following requirements:
* **Open Source**: The software must have an [OSI-approved open source license](https://opensource.org/licenses/) (e.g., MIT, Apache 2.0, GPL 3.0, BSD).
* **Hosted on GitHub**: The code repository must be public.
* **Scientific Research Contribution**: The tool must have a clear application to scientific research (computer science, bioinformatics, biomedical computing, AI, or data science).
* **Functional & Tested**: The repository must include clean installation instructions and an automated test suite.

---

## 2. Manuscript Files

The author's repository must contain `paper.md` and `paper.bib` at the root or within a `paper/` directory.

### Example of `paper.md`
```markdown
---
title: 'PyBioFast: A high-performance Python package for genomic analysis'
tags:
  - Python
  - Bioinformatics
  - Genomics
authors:
  - name: Jane Doe
    orcid: 0000-0002-1825-0097
    affiliation: 1
affiliations:
 - name: University of Campinas, Brazil
   index: 1
date: 4 November 2026
bibliography: paper.bib
---

# Summary
PyBioFast is an open-source library built in Python and Rust to accelerate...

# Statement of Need
The exponential growth of next-generation sequencing requires...

# References
```

---

## 3. How to Submit

1. Go to **[Issues](https://github.com/rbcs-journal/reviews/issues)** in this repository.
2. Click **New Issue** and select the **Submission Form**.
3. Fill in the repository details, software version, authors, and track.
