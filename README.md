# StructDamage-CV-Venezuela
An open-source structural engineering and data science initiative to catalog, analyze, and model seismic damage following the June 24 earthquake in Venezuela.
# 🏗️ OpenSeismic-VE: Structural Damage Image Dataset & Analytics
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data Science](https://img.shields.io/badge/Data%20Science-Python-blue)]()
[![Open Data](https://img.shields.io/badge/Open-Data-green)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

> **An open-source structural engineering and data science initiative to catalog, analyze, and model seismic damage following the June 24 earthquake in Venezuela.**

## 🌍 The Project Context
Following the June 24 earthquake in Venezuela, there is a critical need to document and analyze structural failures to improve local building codes and disaster resilience. 

Maintained by the Structural Engineering and Data Science faculty at the School of Architecture, this repository houses an open-source, crowd-sourced dataset of post-earthquake structural damage. It is actively built by engineering students, researchers, and local professionals.

## 🎯 Objectives
1. **Open Image Dataset:** Provide a highly detailed, expert-labeled dataset of structural damage (shear failure, node failure, masonry collapse, etc.) for Computer Vision (CV) and Machine Learning training.
2. **Data-Driven Analytics:** Use Data Science to find correlations between construction typologies, age, and failure modes based on local codes (COVENIN).
3. **Open Science:** Democratize access to disaster analytics for developing nations.

## 📂 Repository Structure
- `/dataset`: Contains the image dataset and the `.csv` metadata file detailing failure mechanisms, location, and severity.
- `/notebooks`: Jupyter Notebooks for Exploratory Data Analysis (EDA) and preliminary machine learning models.
- `/docs`: Structural engineering field guides and data collection protocols.

## 👥 How to Contribute (For Students and Researchers)
We are actively collecting data. If you are an engineering student or field researcher:
1. Fork this repository.
2. Upload your field images to the `/dataset/images/` folder.
3. Add the corresponding metadata to the `metadata.csv` file.
4. Submit a **Pull Request (PR)**. 

Please read our [`CONTRIBUTING.md`](CONTRIBUTING.md) for detailed guidelines on image formats and structural classification criteria.

## 🚀 Future Roadmap & AI Integration
We are currently integrating Large Language Models (LLMs) and advanced data processing to automate the extraction of insights from unstructured field reports. Our next step is to build an automated diagnostic tool using Open Source AI to assist first responders and structural evaluators in real-time.

## 📄 License
This dataset and code are released under the [MIT License](LICENSE). Free to use for academic, research, and humanitarian purposes.
