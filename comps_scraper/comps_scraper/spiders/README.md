# Spiders

## Not much to explain
They are similar, the only changes are in number of records they extract. Why so? I have explained 
[here](https://github.com/Amirka-Kh/first_scrapy/tree/main/comps_scraper/comps_scraper), in **items.py**
section.

In last moment I added logging, they don't do much, and record to many things. Therefore, the usefulness of 
it is questionable. 

Logic in spider is the following, go to page, visit all companies and extract data about them, then go to the
next page.

`mytools` is special module which I had to create in order to extract data. Firstly, it was implemented in
`items.py`, but failed with ItemLoader. Then I copied it to these to spiders, but it were creating 
a lot text, and reducing "abstaction". Therefore, I made it as separate module.
