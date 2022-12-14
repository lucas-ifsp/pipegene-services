
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

Os serviços que compõem a PipeGene estão todos na tabela abaixo. Cada qual tem seu ID; descrição do que o seviço realizado; tipo, seja Pump, Filter ou Sink; a entrada que pode ser TSV ou json; sua saída, png ou CSV e o próximo serviço que será usado na sequência para finalizar uma pipeline.


<h3 align="center"> Tabela de serviços que compõem a PipeGene</h3><br>
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
    <td> S00 </td>
    <td> Original and preprocess data </td>
    <td> Filter </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S8, S10 </td>
  </tr>
  <tr>
    <td> S01 </td>
    <td> Remove columns </td>
    <td> Filter </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S1, S2, S4, S6, S8, S10 </td>
  </tr>
  <tr>
    <td> S1 </td>
    <td> Preprocess dataset </td>
    <td> Filter </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2, S4, S6 </td>
  </tr>
   <tr>
    <td> S2 </td>
    <td> Compute gene incidence </td>
    <td> Filter </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S3 </td>
  </tr>
   <tr>
    <td> S3 </td>
    <td> Plot gene bar chart </td>
    <td> Sink </td>
    <td> json </td>
    <td> png </td>
    <td> - </td>
  </tr>
   <tr>
    <td> S4 </td>
    <td> Compute mutation incidence</td>
    <td> Filter </td>
    <td> TSV </td>
    <td> json </td>
    <td> S5 </td>
  </tr>
   <tr>
    <td> S5 </td>
    <td> Plot mutation barchart snv </td>
    <td> Sink </td>
    <td> json </td>
    <td> png </td>
    <td> - </td>
  </tr>  
   <tr>
    <td> S6 </td>
    <td> Compute top ten mutation </td>
    <td> Filter </td>
    <td> TSV </td>
    <td> json </td>
    <td> S7 </td>
  </tr>
   <tr>
    <td> S7 </td>
    <td> Plot composite bar chart </td>
    <td> Sink </td>
    <td> json </td>
    <td> png </td>
    <td> - </td>
  </tr>
    <tr>
    <td> S8 </td>
    <td> Compute mutation per patient <br> (with and without outliers) </td>
    <td> Filter </td>
    <td> TSV </td>
    <td> json </td>
    <td> S9 </td>
  </tr>
    <tr>
    <td> S9 </td>
    <td> Plot histogram of mutations </td>
    <td> Sink </td>
    <td> json </td>
    <td> png </td>
    <td> - </td>
  </tr>
    <tr>
    <td> S10 </td>
    <td> Compute indicators from dataset  </td>
    <td> Filter </td>
    <td> TSV </td>
    <td> json </td>
    <td> S11 </td>
  </tr>
    <tr>
    <td> S11 </td>
    <td> Create CSV with original and preprocess data </td>
    <td> Sink </td>
    <td> json </td>
    <td> CSV </td>
    <td> - </td>
  </tr> 
</table>
<br><br>

A tabelas que seguem possuem as pipelines geradas pelo conjunto de serviços acima descritos. A primeira tabela temos as pipelines e suas descrições, a segunda temos um overview de como cada serviço pode ser usado em cada pipeline.
<br><br>

<h3 align="center"> Descrição das pipelines </h3>


<table align="center">
  <tr>
    <th>Pipeline</th>
    <th> Descrição </th>
  </tr>
  <tr>
  <td> PA </td>
   <td> Gera gráfico com a classificação de variantes </td>
  </tr>
 
  <tr>
  <td> PB </td>
   <td> Gera gráfico com os tipos de variantes  </td>
  </tr>
 
  <tr>
  <td> PC </td>
   <td> Gera gráfico de incidência de mutações </td>
  </tr>
 
  <tr>
  <td> PD </td>
   <td> Gera gráfico das top-10 mutações </td>
  </tr>
 
  <tr>
  <td> PE </td>
   <td> Gera CSV com dados originais e pré-processados </td>
  </tr>
  <td> PF </td>
   <td> Gera png com dados originais e pré-processados </td>
  </tr>

</table>
<br><br>

<h3 align="center">  Overview de serviços a sua reutilizações em diferentes pipelines </h3>

<table align="center">
 
  <tr>
    <th>Pipeline</th>
    <th> S00 </th>
    <th> S01 </th>
    <th> S1 </th>
    <th> S2 </th>
    <th> S3 </th>
    <th> S4 </th>
    <th> S5 </th>
    <th> S6 </th>
    <th> S7 </th>
    <th> S8 </th>
    <th> S9 </th>
    <th> S10 </th>
    <th> S11 </th>
   
  </tr>
  <tr>
   <td> Pipeline A </td>
   <td>   </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓ </td>
   <td>  </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
  </tr>
    <tr>
   <td> Pipeline B </td>
   <td>    </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓ </td>
   <td> ✓ </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
  </tr>
    <tr>
   <td> Pipeline C </td>
   <td>    </td>
   <td> ✓ </td>
   <td> ✓ </td>
   <td>   </td>
   <td>   </td>
   <td> ✓ </td>
   <td> ✓  </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
  </tr>
    <tr>
   <td> Pipeline D </td>
   <td>   </td>
   <td> ✓ </td>
   <td> ✓ </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
  </tr>
    <tr>
   <td> Pipeline E </td>
   <td> ✓ </td>
   <td> ✓ </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>  ✓ </td>
   <td>  ✓ </td>
   <td>   </td>
   <td>   </td>
   
  </tr>
    <tr>
   <td> Pipeline F </td>
   <td> ✓  </td>
   <td> ✓ </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>  </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td> ✓  </td>
   <td> ✓  </td>
  </tr>
    <!-- <tr>
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
   <td> ✓  </td>
  </tr> -->
  
</table>


    

 ---
 
###  EN

<h1 align="center"> Pipegene Services</h1><br>


**Este projeto de iniciação Científica é uma continuação de um projeto relizado em frontend e backend de uma plataforma que tem por objetivo realizar análise de datasets da área da saúde.** <br><br>
Neste trabalho pipelines foram desenvolvidas para integrar o front e backend com finalidade de processar grandes conjuntos de dados para gerar insigths. Com os serviços aqui descritos, é possível prover análises de mutações em genes de qualquer variação de mutação gênica.


O projeto foi realizado em três partes até o momento:
- [BackEnd](https://github.com/viniciuslsilva/ifsp-prj-pipegene)
- [FrontEnd](https://github.com/LucasGTeixeira/pipegene-frontend)
- [Services and Pipelines](https://github.com/lucas-ifsp/pipegene-services)
<br>
 
 --- 


<h2 align="center"> Services and pipelines that build PipeGene</h2><br>

Os serviços que compõem a PipeGene estão todos na tabela abaixo. Cada qual tem seu ID; descrição do que o seviço realizado; tipo, seja Pump, Filter ou Sink; a entrada que pode ser TSV ou json; sua saída, png ou CSV e o próximo serviço que será usado na sequência para finalizar uma pipeline.


<h3 align="center"> Table with services that build PipeGene</h3><br>
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
    <td> Filter </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S2, S4, S6, S8, S10 </td>
  </tr>
   <tr>
    <td> S2 </td>
    <td> Compute gene incidence </td>
    <td> Filter </td>
    <td> TSV </td>
    <td> TSV </td>
    <td> S3 </td>
  </tr>
   <tr>
    <td> S3 </td>
    <td> Plot gene bar chart </td>
    <td> Sink </td>
    <td> json </td>
    <td> png </td>
    <td> - </td>
  </tr>
   <tr>
    <td> S4 </td>
    <td> Compute mutation incidence</td>
    <td> Filter </td>
    <td> TSV </td>
    <td> json </td>
    <td> S5 </td>
  </tr>
   <tr>
    <td> S5 </td>
    <td> Plot mutation barchart snv </td>
    <td> Sink </td>
    <td> json </td>
    <td> png </td>
    <td> - </td>
  </tr>  
   <tr>
    <td> S6 </td>
    <td> Compute top ten mutation </td>
    <td> Filter </td>
    <td> TSV </td>
    <td> json </td>
    <td> S7 </td>
  </tr>
   <tr>
    <td> S7 </td>
    <td> Plot composite bar chart </td>
    <td> Sink </td>
    <td> json </td>
    <td> png </td>
    <td> - </td>
  </tr>
    <tr>
    <td> S8 </td>
    <td> Compute mutation per patient <br> (with and without outliers) </td>
    <td> Filter </td>
    <td> TSV </td>
    <td> json </td>
    <td> S9 </td>
  </tr>
    <tr>
    <td> S9 </td>
    <td> Plot histogram of mutations </td>
    <td> Sink </td>
    <td> json </td>
    <td> png </td>
    <td> - </td>
  </tr>
    <tr>
    <td> S10 </td>
    <td> Compute indicators from dataset  </td>
    <td> Filter </td>
    <td> TSV </td>
    <td> json </td>
    <td> S11 </td>
  </tr>
    <tr>
    <td> S11 </td>
    <td> Create CSV with original and preprocess data </td>
    <td> Sink </td>
    <td> json </td>
    <td> CSV </td>
    <td> - </td>
  </tr> 
</table>
<br><br>

A tabelas que seguem possuem as pipelines geradas pelo conjunto de serviços acima descritos. A primeira tabela temos as pipelines e suas descrições, a segunda temos um overview de como cada serviço pode ser usado em cada pipeline.
<br><br>

<h3 align="center"> Pipelines descriptions </h3>


<table align="center">
  <tr>
    <th>Pipeline</th>
    <th> Descrição </th>
  </tr>
  <tr>
  <td> PA </td>
   <td> Plot gene bar chart with variant classification </td>
  </tr>
 
  <tr>
  <td> PB </td>
   <td> Plot gene bar chart with variant type </td>
  </tr>
 
  <tr>
  <td> PC </td>
   <td> Plot composite bar chart with mutation incidences </td>
  </tr>
 
  <tr>
  <td> PD </td>
   <td> Create CSV with original and preprocess data </td>
  </tr>
 
  <tr>
  <td> PE </td>
   <td> Plot histogram of mutations  with top10 mutations </td>
  </tr>

</table>
<br><br>

<h3 align="center">  Services overview and its reuse in distinct pipelines </h3>

<table align="center">
 
  <tr>
    <th>Pipeline</th>
    <th> S1 </th>
    <th> S2 </th>
    <th> S3 </th>
    <th> S4 </th>
    <th> S5 </th>
    <th> S6 </th>
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
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
  </tr>
    <tr>
   <td> Pipeline B </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>  </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
  </tr>
    <tr>
   <td> Pipeline C </td>
   <td> ✓  </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td> ✓  </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
  </tr>
    <tr>
   <td> Pipeline D </td>
   <td> ✓  </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
  </tr>
    <tr>
   <td> Pipeline E </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td>  </td>
   <td>   </td>
   <td>   </td>
  </tr>
    <tr>
   <td> Pipeline F </td>
   <td> ✓  </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td>   </td>
   <td> ✓  </td>
   <td> ✓  </td>
   <td>   </td>
  </tr>
    <!-- <tr>
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
   <td> ✓  </td>
  </tr> -->
  
</table>


    
