
[PT](#pt)
[EN](#en)
<h1 align="center"> Pipegene Services</h1><br>
### PT <br>




**Este projeto de iniciação Científica é uma continuação de um projeto relizado em frontend e backend de uma plataforma que tem por objetivo realizar análise de datasets da área da saúde.** <br><br>
Neste trabalho pipelines foram desenvolvidas para integrar o front e backend com finalidade de processar grandes conjuntos de dados para gerar insigths. Com os serviços aqui descritos, é possível prover análises de mutações em genes de qualquer variação de mutação gênica.


O projeto foi realizado em três partes até o momento:
- [BackEnd](https://github.com/viniciuslsilva/ifsp-prj-pipegene)
- [FrontEnd](https://github.com/LucasGTeixeira/pipegene-frontend)
- [Serviços e Pipelines](https://github.com/lucas-ifsp/pipegene-services)
<br>

 ---

<h2 align="center"> Serviços e pipelines que compõem a PipeGene</h2><br>
<table align="center">
  <tr>
    <th>ID</th>
    <th> Descrição </th>
    <th>Tipo</th>
    <th>Entrada</th>
    <th>Saída</th>
    <th>Próximo</th>
  </tr>
  <tr>
    <td> S1 </td>
    <td> Preprocess dataset </td>
    <td> Pump </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2 </td>
  </tr>
   <tr>
    <td> S2 </td>
    <td> Compute gene incidence </td>
    <td> Pump </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2 </td>
  </tr>
   <tr>
    <td> S3 </td>
    <td> Plot gene bar chart </td>
    <td> Pump </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2 </td>
  </tr>
   <tr>
    <td> S4 </td>
    <td> Compute mutation incidence</td>
    <td> Pump </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2 </td>
  </tr>
   <tr>
    <td> S5 </td>
    <td> Plot mutation barchart snv </td>
    <td> Pump </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2 </td>
  </tr>  
   <tr>
    <td> S6 </td>
    <td> Compute top ten mutation </td>
    <td> Pump </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2 </td>
  </tr>
   <tr>
    <td> S7 </td>
    <td> Plot composite bar chart </td>
    <td> Pump </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2 </td>
  </tr>
    <tr>
    <td> S8 </td>
    <td> Compute mutation per patient <br> (with and without outliers) </td>
    <td> Pump </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2 </td>
  </tr>
    <tr>
    <td> S9 </td>
    <td> Plot histogram of mutations </td>
    <td> Pump </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2 </td>
  </tr>
    <tr>
    <td> S10 </td>
    <td> Compute indicators from dataset  </td>
    <td> Pump </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2 </td>
  </tr>
    <tr>
    <td> S11 </td>
    <td> Create CSV with original and preprocess data </td>
    <td> Pump </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2 </td>
  </tr> 
</table>


<table>
<table>
  <tr>
    <th>Pipeline</th>
    <th> S1 </th>
    <th> S2 </th>
    <th> S3 </th>
    <th> S4 </th>
    <th> S5 </th>
    <th> S6 </th
    <th> S7 </th>
    <th> S8 </th>
    <th> S9 </th>
    <th> S10 </th>
    <th> S11 </th>
    <th> S12 </th>
  </tr>
  <tr>
   <td> Pipeline A </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
  </tr>
    <tr>
   <td> Pipeline B </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
  </tr>
    <tr>
   <td> Pipeline C </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
  </tr>
    <tr>
   <td> Pipeline D </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
  </tr>
    <tr>
   <td> Pipeline E </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
  </tr>
    <tr>
   <td> Pipeline F </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
  </tr>
    <tr>
   <td> Pipeline G </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
  </tr>
  
</table>

<table>
  <tr>
    <th>Pipeline</th>
    <th> Descrição </th>
  </tr>
  <tr>
  <td> PA </td>
   <td> Gera gráfico com a classificação de variantes </td>
  </tr>

</table>

PA - Gera gráfico com a classificação de variantes 
PB - Gera gráfico com os tipos de variantes 
PC - 
PD -
PE - 
    

 ---
###  EN


**Repo to organize services of PipeGene IC project** <br>
<h2 align="center">  Overview de serviços a sua reutilizações em diferentes pipelines </h2>

| Pipelines | Serviços |
|-----------|----------|
| A         |  1,2,3   | 
| B         |  4,5,6   |
| C         |  7,8,9   |





<br><br><br><br><br><br>





















**Este projeto de iniciação Científica é uma continuação de um projeto relizado em frontend e backend de uma plataforma que tem por objetivo realizar análise de datasets da área da saúde.** <br><br>
Neste trabalho pipelines foram desenvolvidas para integrar o front e backend com finalidade de processar grandes conjuntos de dados para gerar insigths. Com os serviços aqui descritos, é possível prover análises de mutações em genes de qualquer variação de mutação gênica.


O projeto foi realizado em três partes até o momento:
- [BackEnd](https://github.com/viniciuslsilva/ifsp-prj-pipegene)
- [FrontEnd](https://github.com/LucasGTeixeira/pipegene-frontend)
- [Serviços e Pipelines](https://github.com/lucas-ifsp/pipegene-services)
<br>

 ---

<h2 align="center"> Serviços e pipelines que compõem a PipeGene</h2><br>
<table align="center">
  <tr>
    <th> Serviços </th>
    <th>Pipelines</th>
  </tr>
  <tr>
  <td>
    
- [x] service 1  - Preprocess dataset
- [x] service 2  - Compute gene incidence
- [x] service 3  - Plot gene bar chart
- [x] service 4  - Compute mutation incidence
- [x] service 5  - Plot mutation barchart snv
- [x] service 6  - Compute top ten mutation
- [x] service 7  - Plot composite bar chart
- [ ] service 8  - Compute mutation per patient (with and without outliers)
- [ ] service 9  - Plot histogram of mutations
- [ ] service 10 - Compute indicators from dataset
- [ ] service 11 - Create CSV with original and preprocess data
    
</td>
  <td>

- [x] Pipeline A - Gera gráfico com a classificação de variantes 
- [x] Pipeline B - Gera gráfico com os tipos de variantes 
- [x] Pipeline C - 
- [ ] Pipeline D -
- [ ] Pipeline E - 
    
  </pre>
  </td>
</tr>
</table>


 ---
###  EN


**Repo to organize services of PipeGene IC project** <br>
<h2 align="center">  Overview de serviços a sua reutilizações em diferentes pipelines </h2>

| Pipelines | Serviços |
|-----------|----------|
| A         |  1,2,3   | 
| B         |  4,5,6   |
| C         |  7,8,9   |


