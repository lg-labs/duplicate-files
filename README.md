# 🛠️ Duplicate Files Management 

[![lg-labs][0]][1]
[![License][2]][LIC]

<img src="https://avatars.githubusercontent.com/u/105936384?s=400&u=290ae673580a956864a07d4aef8e4448372a836b&v=4" align="left" width="172px" height="172px"/>
<img align="left" width="0" height="172px" hspace="10"/>

> 👋 Duplicate files can be found, removed and ordered.
>

From **LgLabs**! Get [Duplicate-Files][4] to a files mng faster.

For more information, check this pages [https://lufgarciaqu.medium.com][1].
<h1></h1>

> <h1> ⚠️ Be careful with some scripts, it'll remove or change files definitely. ⚠️</h1> 


# Using Duplicate Files Scripts, `Python 3`

[Repository][4].

## 🚀 Run locally
Using `makefile`

Step 1/2: Find duplicates.

```bash
make find-duplicates
```

Step 2/2: Delete duplicates.

```bash
make delete-duplicates
```

## 🚀 Bonus: Order files by day

The files ordered on set by day and generate folders with the following format `YYYY-MM-DD` as a result.

```shell
make reorder-files
```

## 📚Contents

1. [x] [01_find_duplicates.py](01_find_duplicates.py)
2. [x] [02_delete_duplicates.py](02_delete_duplicates.py)
3. [x] [03_reorder_files.py](03_reorder_files.py)

## 📊 Metrics or Results

To scenario 1/3: Find duplicates.
```shell
Statistics:
Total files processed: 1677
Unique files: 1634
Duplicate files found: 43
Percentage of unique files: 97.44%
Percentage of duplicate files: 2.56%
Total space occupied by unique files: 352872.07 MB
Total space occupied by duplicates (could be freed): 15474.60 MB
```
To scenario 1/3: Delete duplicates.
```shell
Statistics:
Total duplicates deleted: 43
Total space freed: 15474.60 MB
```
To scenario 1/3: Delete duplicates.
```shell
Directory structure and file counts:
/local/path/2023-11-12: 1 files
/local/path/2023-11-23: 24 files
/local/path/2023-11-22: 19 files
/local/path/2023-11-21: 12 files
/local/path/2023-11-25: 77 files
/local/path/2023-11-20: 3 files

Summary:
Total files found: 136
Total files moved: 136

No invalid files found.
```

## ⚖️ License

The MIT License (MIT). Please see [License][LIC] for more information.


[0]: https://img.shields.io/badge/LgLabs-community-blue?style=flat-square

[1]: https://lufgarciaqu.medium.com

[2]: https://img.shields.io/badge/license-MIT-green?style=flat-square

[4]: https://github.com/lg-labs/duplicate-files


[LIC]: LICENSE

[img1]: https://github.com/lg-labs-pentagon/lg-labs-boot-parent/assets/105936384/31c27db8-1e77-478d-a38e-7acf6ba2571c
