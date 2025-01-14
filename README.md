<!-- PROJECT SHIELDS -->

<!-- PROJECT LOGO -->
<br />
<div style="text-align: center;">
  <a href="https://github.com/markveszelka/python_bdd_behave">
  </a>

<h1 style="text-align: center;">Test Automation Framework</h1>

### About The Project

Test Automation Framework, written in Python using Behave and Selenium.
BDD approach is used to write test cases, with Gherkin syntax.

### Built With

[![Python][Python]][Python-url]
[![Selenium][Selenium]][Selenium-url]
[![Behave][Behave]][Behave-url]
[![CircleCI][CircleCI]][CircleCI-url]
[![Allure][Allure]][Allure-url]
[![Docker][Docker]][Docker-url]

### CircleCI integration

[![CircleCI][CircleCI]][CircleCI-mark-veszelka-url]

CircleCI is a CI/CD platform that automates build, test, and delivery,
helping teams release code quickly and confidently.
Click the badge to view the project's build status.

# Allure Reports

Allure is a lightweight, multi-language tool that provides concise,
web-based test reports to help teams gain insights from test results.

**TODO:** Add screenshots

[//]: # (![Image alt]&#40;  add image link  ;)

[//]: # (![Image alt]&#40;  add image link  ;)

### Run the project

</div>

1. Git clone the repo using SSH:
   ```sh
   git clone git@github.com:markveszelka/python_bdd_behave.git
   ```
2. Make sure that Python 3 is installed on the system.
3. create isolated virtual environment using command:
   ```sh
   python3 -m venv venv
   ```
4. Activate virtual environment:
   ```sh
    .venv/bin/activate
    ```
5. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
6. Run @priority-high test cases
   ```sh
   behave --tags=priority_high
   ```
7. Generate allure report:
   ```sh
   allure generate --single-file allure-results --clean -o allure-report
   ```
8. Open the Allure report in your browser:
   ```sh
   open allure-report/index.html
   ```

<!-- CONTACT -->
<div style="text-align: center;">

## Contact

Mark Veszelka - [github](https://github.com/markveszelka) - [linkedin](https://www.linkedin.com/in/mark-veszelka/) -
mark.veszelka@gmail.com

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- STACKS -->
</div>

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

[Python-url]: https://www.python.org/

[Selenium]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white

[Selenium-url]: https://www.selenium.dev

[Behave]: https://img.shields.io/badge/Behave-802045?style=for-the-badge&logo=python&logoColor=white

[Behave-url]: https://behave.readthedocs.io/en/latest/

[CircleCI]: https://img.shields.io/badge/CircleCI-1d3b55?style=for-the-badge&logo=circleci&logoColor=white

[CircleCI-url]: https://circleci.com/

[CircleCI-mark-veszelka-url]: https://app.circleci.com/pipelines/circleci/VQR2HzuTNfT3idLNVd6ApW/Gmzun7qFdS9iBpxdZA28Yb

[Allure]: https://img.shields.io/badge/Allure-ff5000?style=for-the-badge&logo=allure&logoColor=white

[Allure-url]: https://allurereport.org/

[Docker]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=1D63ED&color=1D63ED

[Docker-url]: https://www.docker.com/



