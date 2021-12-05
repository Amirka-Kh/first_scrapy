# Solution and settings
## Content
> * [How will we go?](#how-will-we-go?)
> * [Items.py](#items.py)
> * [Pipeline](#pipeline)
> * [Settings](#settings)
> * [Smth else](#smth_else)

## How will we go?
I suggest the following procedure, we will touch all the files, which I editted, one by one. I will make
comment on the configurations and solution. I suggest to start with `items.py`

## Items.py
In the items.py folder you will find 2 item classes: CompItem and BusItem. Overall they keep 13 records 
such as company name, cvr number, address, postal code, city and etc. They are very basic.

I tried to create one big Item with more data, for that puspose I tried to use `ItemLoader`. This 
was logical to me because it creates an abstraction (not abstraction, but good architecture), because
it separates spider logic from item, and makes debbuging easier. However, I couldn't set this `ItemLoader`
correctly, therefore I were getting strange results (e.g. list instead of string). In the end, I gave up
and made all extraction in spiders.

## Pipeline
This pipeline stores different items by comparing their class. This pipeline uses `MongoDB` to store data.

Not lastly, I thought how to orginise insertion to database. I wanted to create simple data without nested 
structures. I had an idea to create two pipelines, but next thoughts stopped me.

all pipelines, which I create will receive all items. Therefore, it will reduce performance, therefore, it
is better to handle all items from one page in one pipeline. There was smth else, but I cannot remember (ok,
let's consider there is nothing left).

## Settings
In order to parse and extract data from [Danish Central Business Register](https://datacvr.virk.dk/data/?language=en-gb)
I specified `ROBOTSTXT_OBEY = False`.

Also to use pipelines I uncommented the line about pipeline.

Before setting `ROBOTSTXT_OBEY` to `False` I tried to use proxies, user_agent and middlewares, it didn't work.
I tried to login, but to login I need normal password and login (csr I get it), I couldn't find register page
(to be honest, I didn't tried much), therefore I used this option.

## Smth else
Now we partially covered all files, but we didn't talked about spiders,
For more details [click here](https://github.com/Amirka-Kh/first_scrapy/tree/main/comps_scraper/comps_scraper/spiders)

Also, [here](https://github.com/Amirka-Kh/first_scrapy/blob/main/comps_scraper/all_log_info.log) you can check `all_log_info.log` file (file where I was storing logs)
I implemented logs only in spiders. Why? Because it is Sunday and it is 23:43, I added 
logging around 22:00.

In chernovik is the code which I deleted from `items.py` (these are most about item loader).
