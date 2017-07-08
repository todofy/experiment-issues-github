# POC: Data Science techniques on Github Issues Dataset

In this experiment I'm investigating different scenarios that can be solved for Github Issues using machine learning algorithms. I will be using issues for `phpmyadmin/phpmyadmin`. It has around `268 open issue` and `10,768 closed issues` - i.e. total 11K issues raised till date. The data was mined using a quick hack I wrote an year back - [mebjas/gils](https://github.com/mebjas/gils). It creates a dump of serialized JSON objects per line indicating one issue.

### Task 1 - read this file and generate standard, CSV dataset and pandas object in pickle format.
CSV stored in `data\data.csv` - 13729 rows


