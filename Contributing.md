# Contributing to OpenSeismic-VE-Dataset

Thank you for contributing to our open-source structural damage dataset for the June 24, 2026, Venezuela earthquake. This guide is primarily for engineering students and researchers helping us build this database.

## 1. How to Contribute Data (The GitHub Workflow)
We use a standard Pull Request (PR) workflow. Please do not send images via email.
1. **Fork** this repository to your GitHub account.
2. **Clone** it locally or use GitHub Web.
3. Upload your authorized field images to the `/dataset/images/` folder. Name them using the ID (e.g., `VE-2026-004_front.jpg`).
4. Update the `/dataset/metadata.csv` file with the building's technical details.
5. Commit your changes and submit a **Pull Request**.

## 2. Technical Data Requirements (Part A)
When filling out the `metadata.csv`, ensure you verify at least **three independent sources**. 
Pay special attention to the Architectural Configuration:
- **plan_configuration:** Is it regular or irregular? Is there eccentricity?
- **soft_story:** Identify if there is a soft story (Planta baja blanda).
- **certainty_level:** Use strictly `Confirmed` (official statement), `Expert_Hypothesis` (engineers in media), or `General_Typology`.

## 3. Image Licensing & Permissions (Part B) - STRICT POLICY
To maintain this dataset as Open Source for Machine Learning/Computer Vision:
- **DO NOT** upload copyrighted press images (AP, Reuters, CNN) without written permission.
- Preferred sources: [Wikimedia Commons 2026 Earthquakes in Venezuela](https://commons.wikimedia.org/wiki/Category:2026_earthquakes_in_Venezuela), USGS, NASA, or original photos taken by you.
- If you obtain permission from a photographer, record it in the `image_license_status` column as `Authorized` and include the credit in the PR description.
- If permission is pending, set the status to `Pending` and do not upload the image file yet (provide only the URL to the source).

*Note: For the educational PPTX/PDF internal reports, fair use applies, but for this public GitHub dataset, we must respect global open-source licensing.*
