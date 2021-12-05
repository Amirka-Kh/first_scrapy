# Scra-Pa-Pa

***

## Content
1. [Description](#description)
> * [Intro](#intro)
> * [Task description](#task-description)
> * [What I did](#what-i-did)

***

## Description
### Intro
Scra-Pa-Pa is a scrapy project dedicated to parse [Danish Central Business Register](https://datacvr.virk.dk/data/?language=en-gb). This parser does not boast good architecture or abstraction, but it works nonetheless, which means it can get better.

### Task description
I had to write a parser for [Danish Central Business Register](https://datacvr.virk.dk/data/?language=en-gb), where approximate number of companies in the register is 1859950. I had to extract around 1000 random company samples. There was no description of data to be extracted, the format in which the extracted data should be stored. I had to come up with my own format and this is considered as part of the assignment. However, there were some restrictions on the technology stack to be used and overall requirements to the solution, see below.

Another consideration what had to be taken is associated companies and individuals. The association information can be represented in a different way, for example there can be provided an Individual Taxpayer Number that can be used to associate the same person with multiple companies. I had to find an identifier, if exists, that can be used for such purpose and describe in the solution  how the association information is captured.

#### Technology stack
* The parser should be written in python 3.8 and based on Scrapy framework
* No restrictions on the database, but MongoDB 4.4 is strongly recommended

### What I did
I created 2 items to extract data, I could not create a data format like in the assignment doc. I tried different methods, but they were working unstraight, therefore I left with the easiest, but less abstract solution. More details about my solution you can read [here](https://github.com/Amirka-Kh/first_scrapy/tree/main/comps_scraper/comps_scraper)

I did not consider associated companies and individual. I did not thought anything about it.

