
<h2 align="center">Fit-n-Bites API</h2>

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## 📝 Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Authors](#authors)


## 🧐 About <a name = "about"></a>
Fit-n-Bites API is a free light-weight RESTful API providing nutrition facts of common food. No redundant information is provided. Perfect for small to medium size projects, especially school demos. 

## 🏁 Getting Started <a name = "getting_started"></a>
An API key is necessary to use this API. Please contact landau@fitnbites.com to access API key.

By default, clients must pass their API key via the Authorization header. It must be formatted as follows:

> Authorization: Api-Key ********

***Example***

 curl -H 'Authorization: Api-Key ********' www.fitnbites.com/api/v1/foods/

## 🎈 Usage <a name="usage"></a>
**/foods**
 
 Listing information of all available foods (Calorie, protein, etc.)

**/foods/alcoholfree**

 Listing information of all alcohol free foods

**/foods/caffeinefree**

 Listing information of all caffeine free foods
 
**/food/id**

 Retrieving information of a specific target

**/foods/?keyword=**

 Retrieving food descriptions with given keyword
 
**/foods/?max=**

 Retrieving food with a calorie upper bound per 100 gram

**/foods/?min=**

 Retrieving food with a calorie lower bound per 100 gram
 
***Example***
 
 /api/v1/foods/alcoholfree/?keyword=cookie&max=300&min=200
 
## ⛏️ Built Using <a name = "built_using"></a>
- [Django](https://www.djangoproject.com/) - Web Framework
- [Django REST Framework](https://www.django-rest-framework.org/) - API Framework
- [Amazon RDS for Postgresql](https://aws.amazon.com/rds/) - Database
- [Heroku](www.heroku.com) - Deployment Environment

## ✍️ Authors <a name = "authors"></a>
- [@LyapunovJingci](https://github.com/LyapunovJingci) - Framework, Deployment
- [@ShuyiHuo](https://github.com/ShuyiHuo) - Idea, Data Cleaning



