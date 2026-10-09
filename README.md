[![](https://img.shields.io/badge/Network_Meta-Analysis-white?style=for-the-badge&logo=influxdb)][1]

[1]: https://d-wkim-project.readthedocs.org



<div align = "center">
Jagiellonian University<br>
Medical College<br>
Doctoral School of Medical and Health Sciences<br>
</div>
</br>
<div  align="center" ><a href="https://github.com/d-wkim/phd"><img alt = "" src="https://raw.githubusercontent.com/d-wkim/assets/refs/heads/main/icons/uj_black.jpg" width="100" height="150"></a></div>

<hr>

<h2 align="center">
Comparative analysis of outcome measures using the most common grafts<br>
for primary anterior cruciate ligament reconstruction surgery.<br>
A systematic review and network meta-analysis
</h2>

<hr> 

<div align = "center">
A dissertation submitted in partial fulfillment of the requirements for the award of the degree of:<br><br>
Doctor of Philosophy (Ph.D.)<br><br>
<sup>submitted by:</sup><br>
<strong>Dong Woon Kim</strong>, M.D.<br><br>
<sup>supervised by:</sup><br>
Konrad Malinowski, M.D. Ph.D.<br>
<br<br>Kraków, 2026
</div>


**Create folders**. Python script was written to create all project directories and subdirectories, and set these folders as global variables.

```python
import os
folders = {
    "systematic_review": f".//1_systematic_review",
    "data_collection": f".//2_data_collection",
    "meta-analysis": f".//3_meta-analysis",
    "manuscript": f".//4_manuscript"
}

for x, y in folders.items():
    os.makedirs(y, exist_ok = True)
    globals()[x] = y
```

```python

```
