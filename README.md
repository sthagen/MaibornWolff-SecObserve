![SecObserve](frontend/public/secobserve.svg)

# SecObserve

SecObserve gathers results about potential security flaws from various vulnerability scanning tools and makes them available for assessment and reporting.

![Dashboard](docs/assets/images/screenshot_dashboard.png)

## Overview

The aim of SecObserve is to make vulnerability scanning and vulnerability management as easy as possible for software development projects using open source tools. It consists of 2 major components:

* **GitLab CI templates and GitHub actions:** Integrating vulnerability scanners into a CI/CD pipeline can be tedious. Each tool has to be installed differently and is called with different parameters. To avoid having to solve this task all over again, there are repositories with GitLab CI Templates and GitHub Actions. These make the process of integrating vulnerability scanners very simple by providing uniform methods for launching the tools and uniform parameters. The tools are regularly updated in the repositories so that the latest features and bug fixes are always available.

    All templates run the scanner, upload the results into SecObserve and make the results of the scans available for download as artefacts in JSON format.

* **Vulnerability management system SecObserve:** SecObserve provides the development team with an overview of the results of all vulnerability scans for their project, which can be easily filtered and sorted. In the detailed view, the results are displayed uniformly with a wealth of information, regardless of which vulnerability scanner generated them.

    With the help of automatically executed rules and manual assessments, the results can be efficiently evaluated to eliminate irrelevant results and accept risks. This allows the development team to concentrate on fixing the relevant vulnerabilities.


![Overview](docs/assets/images/secobserve_process.svg)

This repository contains the vulnerability management system SecObserve. The GitLab CI templates and GitHub actions will be published soon.

## Documentation

The full documentation how to install and use Secobserve can be found here: [https://department-csec.maibornwolff.io/secobserve/secobserve/](https://department-csec.maibornwolff.io/secobserve/secobserve/)

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## License

SecObserve is licensed under the [3-Clause BSD License](LICENSE.txt)
