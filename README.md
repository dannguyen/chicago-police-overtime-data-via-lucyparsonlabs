# Chicago Police Department Overtime Data and Documents

This is just a small repo mirroring and maybe parsing the Chicago PD's overtime payroll data, as [successfully FOIAed](https://twitter.com/lucyparsonslabs/status/1142130197803786241) and published by the [Lucy Parsons Labs](https://www.lucyparsonslabs.com/), a Chicago-based collaborative non-profit focused on civic data and transparency.

## Status

**[as of June 21, 2019](https://twitter.com/lucyparsonslabs/status/1142130197803786241)**

- [LPL's documents](https://www.documentcloud.org/public/search/projectid:44251-CPD-Overtime-Responsive-Records) include citywide aggregate and per unit data for 2017 through May 2018.
- This repo mirrors those PDFs, and contains their [conversions to spreadsheet form (as done by ABBYY FineReader](data/parsed/abbyy))
- TODO: Python script to wrangle the data into a tidy CSV

## The Documents

The Lucy Parsons Labs' DocumentCloud folder: https://www.documentcloud.org/public/search/projectid:44251-CPD-Overtime-Responsive-Records

- [2018 (January-May) Overtime by Unit](https://www.documentcloud.org/documents/6111024-P463184-Overtime-Citywide-by-Unit-2018.html) ([mirror](data/originals/2018-cpd-overtime-by-unit.pdf))
- [2018 (January-May) Overtime Citywide Aggregate](https://www.documentcloud.org/documents/6164468-Aggregate-Citywide-CPD-Overtime-Data-2018.html) ([mirror](data/originals/2018-cpd-overtime-aggregate.pdf))
- [2017 Overtime by Unit](https://www.documentcloud.org/documents/6111023-P463184-Overtime-Citywide-by-Unit-2017.html) ([mirror](data/originals/2017-cpd-overtime-by-unit.pdf))
- [2017 Overtime Citywide Aggregate](https://www.documentcloud.org/documents/6164469-Aggregate-Citywide-CPD-Overtime-Data-2017.html) ([mirror](data/originals/2017-cpd-overtime-aggregate.pdf))

## Some Data

The documents converted to XLSX, via ABBYY FineReader, can be found in [data/parsed/abbyy](data/parsed/abbyy):

- [2018 (January-May) Overtime by Unit](data/parsed/abbyy/2018-05-cpd-overtime-by-unit.xlsx)
- [2018 (January-May) Overtime Citywide Aggregate](data/parsed/abbyy/2018-05-cpd-overtime-aggregate.xlsx)
- [2017 Overtime by Unit](data/parsed/abbyy/2017-cpd-overtime-by-unit.xlsx)
- [2017 Overtime Citywide Aggregate](data/parsed/abbyy/2017-cpd-overtime-aggregate.xlsx)


## Background

In 2017, the Chicago Inspector General found that the Chicago Police Department spent $575 million in officer overtime over the past 6 years, and that CPD's system was prone for abuse; [via the Chicago Tribune](https://www.chicagotribune.com/news/breaking/ct-met-chicago-police-overtime-ig-report-20171004-story.html):

> The report from the office of Inspector General Joseph Ferguson found that the lax oversight has allowed officers to use "potentially abusive practices" in piling up overtime — usually at time-and-a-half pay. The report released Tuesday said officers sometimes seek out work sure to lead to overtime, such as involving themselves in numerous drunken driving arrests and then going to court frequently for those cases. One officer cited in the report appeared in court nearly two-thirds of the 943 days examined, the inspector general wrote.


In [October 2018, documents obtained by the Lucy Parsons Labs](https://twitter.com/lucyparsonslabs/status/1051918099031740416) indicated the CPD's 2017 overtime cost more than $158 million.

In [June 2019](https://twitter.com/lucyparsonslabs/status/1142130197803786241), LPL released documents containing the 2017 overtime expenditures at the unit level, as well as 2018 data through May:

> NEW DATA RELEASE! Months ago, we received the aggregate overtime data for CPD showing that the department spent $159 million citywide on overtime in 2017. We now have the unit level data. Now you can see which unit(s) in CPD spent the most: https://www.documentcloud.org/public/search/projectid:44251-CPD-Overtime-Responsive-Records

<a href="https://twitter.com/lucyparsonslabs/status/1142130197803786241">
    <img src="https://i.imgur.com/5RSGufl.png" alt="">
</a>

