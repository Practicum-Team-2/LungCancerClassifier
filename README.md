# Lung Cancer Classifier

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Practicum-Team-2/LungCancerClassifier" >
    <img  src="img/banner_1.png" alt="Logo" width = "800" hight = "250">
  </a>

  <h3 align="center">Lung Cancer Classifier</h3>
  <p align="center">
  A Machine Learning Classifier of Lung Cancer Genomics Datasets.
    <br />
    <a href="https://github.com/Practicum-Team-2/LungCancerClassifier"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Practicum-Team-2/LungCancerClassifier">View Demo</a>
    ·
    <a href="https://github.com/Practicum-Team-2/LungCancerClassifier/issues">Report Bug</a>
    ·
    <a href="https://github.com/Practicum-Team-2/LungCancerClassifier/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#data">Data</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contributor">Contributor</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
  
  Lung cancer is one of the most common malignant diseases worldwide and is a major cause of death from cancer. We chose to classify three major lung cancers: **Lung Adenocarcinoma, Lung Squamos and Small Cell Lung Cancer**.

  Lung carcinomas are classified by histopathologic subtype (the Fig below). Non–small cell lung cancers account for around 85% of cases and of these adenocarcinomas (LAC) are the most common. Incidence of LAC has increased over the past 30 years and it presents frequently in asymptomatic females especially those from East Asia, and often in nonsmokers. 

![image](https://user-images.githubusercontent.com/78892787/155035824-e055b78c-14c4-4c9f-89b2-1af2f73c48ae.png)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python 3.8


<!-- DATA -->
## Data

| Value                   | Type | Description |  Cleaned |
| :---                    | --- | --- | --- |
| Cancer Type Detailed    | Categorical| Type of lung cancers     | 1 | 
| Mutation Count          | Numerical | Tumor mutation count  | 0 |
| Diagnosis Age           | Integer | Patient's age at diagnosis | 1 |
| Sex                     | Categorical | Gender of patient (0 = Female, 1 = male)| 1 |
| Survival Stage          | Binary | Patient survival status (0 = Living, 1 = Deceased) | 1 |
| Somatic Status          |  Binary | (0 = Unmatched, 1 = Matched) | 1 | 
| Smoking History         | Categorical | Patient smoking behavior(0 = Non-smoker, 1 = Former Smoker, 2 = Current Smoker and 3 = Reformed Smoke) | 1 |
| Person Cigarette Smoking History Pack Year Value    | Numerical | Amount of packs of cigarettes smoked of a lifetime; 1 pack-year is equal to 7305 cigarettes smoked in the past | 1 |
| TMB Nonsynonymous       | Numerical | The total number of mutations (changes) found in the DNA of cancer cells | 0 |

**the TNM staging system** : see explanation of the "M/N/T stage" variables in https://www.cancerresearchuk.org/about-cancer/lung-cancer/stages-types-grades/tnm-staging

<!-- ROADMAP -->
## Roadmap
- [x] Mapping out dependencies

- [x] Selecting the dataset

- [x] Cleaning, exploring, and analyzing data

- [ ] Modeling the data and selecting best ML model

- [ ] Synthesizing the results

- [ ] Presentation materials: tailor the message for medical audience, visualizations

- [ ] Presentation materials: create a manual-like code book

- [ ] Presentation materials: prepare the slide deck via PowerPoint to share results to class and medical professionals

- [ ] Presentation materials: dashboard for sample model output along with a user manual

- [ ]  Review all materials and prepare for presentation day


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- CONTRIBUTOR -->
## Contributor

<p align="center">
<a href="https://github.com/Practicum-Team-2/LungCancerClassifier/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=Practicum-Team-2/LungCancerClassifier" />
</a>
</p>

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
  
* [cBioPortal for Cancer Genomics by Memorial Sloan Kettering Cancer Center ](https://www.cbioportal.org/)

