## CTF_STU026 Solution Repository: AI Detective Challenge

This repository contains the complete solution for the Capture the Flag (CTF) challenge, which required simulating an AI detective to find and analyze a manipulated book rating in a dataset.

### Project Overview

The core objective was to uncover a hidden clue planted in a fake 5-star review, identify the targeted book, and use machine learning to distinguish genuine user reviews from suspicious ones.

### Detailed Solution Methodology

The challenge was completed in three distinct steps:

1.  **Data Forensics (FLAG1 & FLAG2):** Located a manipulated book rating using a hidden SHA256 hash key within the review text. The hash of the student ID revealed the fake review, which identified the target book "The Ice Child."
2.  **Machine Learning (FLAG3):** Trained a Logistic Regression classifier to separate genuine reviews from spam.
3.  **SHAP Analysis:** Used SHAP (SHapley Additive exPlanations) to extract the specific vocabulary that characterized "genuine" user feedback (words like "write", "stories", and "continues") to construct the final flag.