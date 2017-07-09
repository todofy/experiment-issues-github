# POC: Data Science techniques on Github Issues Dataset

In this experiment I'm investigating different scenarios that can be solved for Github Issues using machine learning algorithms. I will be using issues for `phpmyadmin/phpmyadmin`. It has around `268 open issue` and `10,768 closed issues` - i.e. total 11K issues raised till date. The data was mined using a quick hack I wrote an year back - [mebjas/gils](https://github.com/mebjas/gils). It creates a dump of serialized JSON objects per line indicating one issue.

# Task 1 - read this file and generate standard, CSV dataset and pandas object in pickle format.
All preprocessing was done using `./preprocess.py`. Around `13730` rows were extracted. And some of them were duplicates, so upon deduplication `279 entires` were removed leaving `13450` unique issues. The output of the data is stored in `./data/data.csv`

## level 1 analysis of data
Workbook.xlsx has some of the analysis in excel sheet.

## Fields
| field_name | remarks                                                              |
|------------|----------------------------------------------------------------------|
| repo_id    | Same for all rows. No impact on any decision                         |
| repo_name  | Same for all rows. No impact on any decision                         |
| id         | Unique ID of an issues                                               |
| title      | title of the issue (string)                                          |
| body       | body of the issue (text)                                             |
| created_by | Github Handle of the user who created the issue. 962 unique values.  |
| created_at | time string                                                          |
| updated_at | time string                                                          |
| closed_at  | time string, empty for open issues                                   |
| state      | State of the issue (open|closed)                                     |
| n_comments | no of comments on the issue (int)                                    |
| locked     |                                                                      |
| milestone  | NA for all values, Serialized JSON with milestone information        |
| labels     | labels set on a issue - label text is kept as space separated string |

## Fields introduced
| field_name | remarks                                                              |
|------------|----------------------------------------------------------------------|
|actual_author| Around 9507 rows were created by Github User `pma-import`. This is a bot which imports issues from sourceforge PMA page. It follows a standard template of body, from which actual author name {sourceforge ID} can be mined.|

After mining actual author information from issue body, the distribution changes. 4318 unqieu authors were identified. However 1294 of them were created by `*anonymous` which is apparently introduced by sourceforge. `11 authors` seem to have created `>100 issues`. They are:

| author       | issues created | Is Code Contributor? |
|--------------|----------------| -------------------- |
| nijel        | 507            | true |
| lem9         | 432            | true |
| madhuracj    | 364            | true |
| ibennetch    | 319            | true |
| OlafvdSpek   | 272            | |
| devenbansod  | 139            | |
| ryandesign   | 127            | |
| tithugues    | 117            | |
| adamgsoc2013 | 114            | |
| windkiel     | 110            | |
| xmujay       | 106            | |
| roccivic     | 104            | |

So these folks would be our person of interest.




