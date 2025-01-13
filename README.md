# Shiwaforce Test Automation Framework - Mark Veszelka

Teat Automation Framework for Shiwaforce, written in Python using Behave and Selenium. BDD approach is used to write
test cases, with Gherkin syntax.

# Integration with Circle CI

[![CircleCI]](https://app.circleci.com/pipelines/circleci/VQR2HzuTNfT3idLNVd6ApW/Gmzun7qFdS9iBpxdZA28Yb)

When you click on this badge you will redirect to the CircleCI website. There you have a chance click last build and
explore all occurrences on different stages building the project and tests. The build is failed due to diffrent bugs in
the application

# Run the project

1. git clone repository
2. make sure that python3 installed on the server
3. create isolated virtual environment using command - python3 -m venv venv
4. activate virtual environment - .venv/bin/activate
5. install dependencies - pip install -r requirements.txt
6. run @priority-high test cases - behave --tags=priority_high
7. genereate allure report - allure generate --single-file allure-results --clean -o allure-report
8. open allure report - open allure-report/index.html  

<!-- PROJECT SHIELDS -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/markveszelka/python_bdd_behave">
    <img src="images/imf_logo.png" alt="Logo" width="20%" height="20%">
  </a>

<h3 align="center">Test Automation Framework</h3>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/markveszelka/python_bdd_behave)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Github][Github]][Github-url]
* [![Java][Java]][Java-url]
* [![Spring][Spring]][Spring-url]
* [![SpringSecurity][SpringSecurity]][SpringSecurity-url]
* [![Hibernate][Hibernate]][Hibernate-url]
* [![Docker][Docker]][Docker-url]
* [![Javascript][Javascript]][Javascript-url]
* [![React][React.js]][React-url]
* [![PostgreSQL][PostgreSQL]][Postgresql-url]
* [![IntelliJ][IntelliJ.idea]][IntelliJ-url]
* [![HTML5][HTML5]][HTML5-url]
* [![CSS][CSS]][CSS-url]
* [![Vite][Vite]][Vite-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

You can clone the project and install it to see it in action.

### Prerequisites

[![Maven][Maven]][Maven-url]

To build and manage the project dependencies, Maven is required. You can install Maven by following the steps below:

* On macOS
  ```sh
  brew install maven
  ```
* On Windows
  ```sh
  choco install maven
  ```
  
[![NPM][NPM]][NPM-url]

* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo using SSH
   ```sh
   git clone git@github.com:markveszelka/python_bdd_behave.git
   ```
2. Navigate to frontend folder and install NPM packages
   ```sh
   npm install
   ```
3. Navigate to backend folder and build the backend project using Maven, run the code from the backend folder
   ```sh
   mvn clean install
   ```
4. Run the backend using Maven from the backend directory
   ```sh
    mvn spring-boot:run
    ```
5. Run the frontend from the frontend directory
   ```sh
   npm run dev
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->


[//]: # (<p align="right">&#40;<a href="#readme-top">back to top</a>&#41;</p>)


<!-- CONTACT -->

## Contact

Mark Veszelka - [github](https://github.com/markveszelka) - [linkedin](https://www.linkedin.com/in/mark-veszelka/) - mark.veszelka@gmail.com

Project Link: https://github.com/markveszelka/blood-donation-page/

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[//]: # (<p align="right">&#40;<a href="#readme-top">back to top</a>&#41;</p>)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/nagmil2077/stackoverflow-tw/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png

<!-- STACKS -->
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[PostgreSQL]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[Postgresql-url]: https://www.postgresql.org
[IntelliJ.idea]: https://img.shields.io/badge/IntelliJ_IDEA-000000.svg?style=for-the-badge&logo=intellij-idea&logoColor=white
[IntelliJ-url]: https://www.jetbrains.com/idea/
[Github]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[Github-url]: https://github.com
[Stackoverflow]: https://img.shields.io/badge/Stack_Overflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white
[Stackoverflow-url]: https://stackoverflow.com
[Java]: https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white
[Java-url]: https://www.java.com/en/
[Spring]: https://img.shields.io/badge/Spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white
[Spring-url]: https://spring.io
[SpringSecurity]: 	https://img.shields.io/badge/Spring_Security-6DB33F?style=for-the-badge&logo=Spring-Security&logoColor=white
[SpringSecurity-url]: https://docs.spring.io/spring-security/reference/index.html
[Hibernate-url]: https://hibernate.org/
[Hibernate]: https://img.shields.io/badge/Hibernate-59666C?style=for-the-badge&logo=Hibernate&logoColor=white
[Docker]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=1D63ED&color=1D63ED
[Docker-url]: https://www.docker.com/
[Javascript]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[Javascript-url]: https://www.javascript.com
[CSS]: https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://developer.mozilla.org/en-US/docs/Web/CSS
[HTML5]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://en.wikipedia.org/wiki/HTML5
[Vite]: https://img.shields.io/badge/vite-646CFF?style=for-the-badge&logo=vite&logoColor=white&labelColor=8C72FE&color=8C72FE
[Vite-url]: https://vitejs.dev/
[NPM]: https://img.shields.io/badge/NPM-%23CB3837.svg?style=for-the-badge&logo=npm&logoColor=white
[NPM-url]: https://www.npmjs.com
[Maven]:    https://img.shields.io/badge/Apache%20Maven-C71A36?style=for-the-badge&logo=Apache%20Maven&logoColor=white
[Maven-url]: https://maven.apache.org
