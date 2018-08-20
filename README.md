# NYTimes Corpus: Crowdsourcing Topical Relevance

This repository contains the crowdsourcing annotations for topical relevance referenced in the following paper:

* Oana Inel, Giannis Haralabopoulos, Dan Li, Christophe Van Gysel, Zoltán Szlávik, Elena Simperl, Evangelos Kanoulas and Lora Aroyo: **[Studying Topical Relevance with Evidence-based Crowdsourcing](https:...)**. [CIKM 2018](http://www.cikm2018.units.it).


If you find this data useful in your research, please consider citing:

```
@inproceedings{inel2018studying,
  title={Studying Topical Relevance with Evidence-based Crowdsourcing},
  author={Inel, Oana and Haralabopoulos, Giannis and Li, Dan and Van Gysel, Christophe and Szlávik, Zoltán and Simperl, Elena and Kanoulas, Evangelos and Aroyo, Lora},
  booktitle={To Appear in the Proceedings of the 27th ACM International Conference on Information and Knowledge Management (CIKM)},
  year={2018},
  organization={ACM}
}
```

## Crowdsourcing Templates
The following crowdsourcing templates have been used in the aforementioned article. We use the same experiment notation as in the article. To check each crowdsourcing annotation template, click on the small template icon. The image will open in a new tab.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;border-color:#ccc;}
.tg td{font-family:Arial, sans-serif;font-size:12px;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;border-top-width:1px;border-bottom-width:1px;border-color:#ccc;color:#333;background-color:#fff;}
.tg th{font-family:Arial, sans-serif;font-size:12px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:0px;overflow:hidden;word-break:normal;border-top-width:1px;border-bottom-width:1px;border-color:#ccc;color:#333;background-color:#f0f0f0;}
.tg .tg-s6z2{text-align:center}
.tg .tg-baqh{text-align:center;vertical-align:top}
</style>
<table class="tg" style="undefined;table-layout: fixed; width: 1002px">
<colgroup>
<col style="width: 41px">
<col style="width: 130px">
<col style="width: 114px">
<col style="width: 88px">
<col style="width: 230px">
<col style="width: 125px">
<col style="width: 122px">
<col style="width: 152px">
</colgroup>
  <tr>
    <td class="tg-s6z2" rowspan="2">Type</td>
    <td class="tg-s6z2" rowspan="2">Experiment</td>
    <td class="tg-baqh" colspan="2">Input Data</td>
    <td class="tg-baqh" colspan="4">Crowdsourcing Annotation Template</td>
  </tr>
  <tr>
    <td class="tg-baqh">Topic-Document Pairs</td>
    <td class="tg-baqh">Document Length</td>
    <td class="tg-baqh">Relevance Annotation Values</td>
    <td class="tg-baqh">Document Granularity</td>
    <td class="tg-baqh">Document Paragraph Order</td>
    <td class="tg-baqh">Annotation</td>
  </tr>
  <tr>
    <td class="tg-s6z2" rowspan="8">Pilot</td>
    <td class="tg-s6z2">3P-Doc-NoHigh</td>
    <td class="tg-baqh">120</td>
    <td class="tg-baqh">Bin1&amp;Bin2</td>
    <td class="tg-baqh">3-point scale (Highly Relevant,<br>Relevant, Not Relevant)<br></td>
    <td class="tg-baqh">Full <br>Document</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">Relevance Value</td>
  </tr>
  <tr>
    <td class="tg-s6z2">3P-Doc-High</td>
    <td class="tg-baqh">120</td>
    <td class="tg-baqh">Bin1&amp;Bin2</td>
    <td class="tg-baqh">3-point scale (Highly Relevant,Relevant, Not Relevant)</td>
    <td class="tg-baqh">Full <br>Document</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">Relevance Value +<br>Text Highlight</td>
  </tr>
  <tr>
    <td class="tg-s6z2">2P-Doc-NoHigh</td>
    <td class="tg-baqh">120</td>
    <td class="tg-baqh">Bin1&amp;Bin2</td>
    <td class="tg-baqh">2-point scale <br>(Relevant, Not Relevant)</td>
    <td class="tg-baqh">Full <br>Document</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">Relevance Value</td>
  </tr>
  <tr>
    <td class="tg-s6z2">2P-Doc-High</td>
    <td class="tg-baqh">120</td>
    <td class="tg-baqh">Bin1&amp;Bin2</td>
    <td class="tg-baqh">2-point scale <br>(Relevant, Not Relevant)</td>
    <td class="tg-baqh">Full <br>Document</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">Relevance Value +<br>Text Highlight</td>
  </tr>
  <tr>
    <td class="tg-s6z2">2P-OrdPar-NoHigh</td>
    <td class="tg-baqh">116</td>
    <td class="tg-baqh">Bin1&amp;Bin2</td>
    <td class="tg-baqh">2-point scale <br>(Relevant, Not Relevant)</td>
    <td class="tg-baqh">Document<br>Paragraphs</td>
    <td class="tg-baqh">Ordered</td>
    <td class="tg-baqh">Relevance Value</td>
  </tr>
  <tr>
    <td class="tg-s6z2">2P-OrdPar-High</td>
    <td class="tg-baqh">116</td>
    <td class="tg-baqh">Bin1&amp;Bin2</td>
    <td class="tg-baqh">2-point scale <br>(Relevant, Not Relevant)</td>
    <td class="tg-baqh">Document<br>Paragraphs</td>
    <td class="tg-baqh">Ordered</td>
    <td class="tg-baqh">Relevance Value +<br>Text Highlight</td>
  </tr>
  <tr>
    <td class="tg-s6z2">2P-RndPar-NoHigh</td>
    <td class="tg-baqh">116</td>
    <td class="tg-baqh">Bin1&amp;Bin2</td>
    <td class="tg-baqh">2-point scale <br>(Relevant, Not Relevant)</td>
    <td class="tg-baqh">Document<br>Paragraphs</td>
    <td class="tg-baqh">Random</td>
    <td class="tg-baqh">Relevance Value</td>
  </tr>
  <tr>
    <td class="tg-s6z2">2P-RndPar-High</td>
    <td class="tg-baqh">116</td>
    <td class="tg-baqh">Bin1&amp;Bin2</td>
    <td class="tg-baqh">2-point scale <br>(Relevant, Not Relevant)</td>
    <td class="tg-baqh">Document<br>Paragraphs</td>
    <td class="tg-baqh">Random</td>
    <td class="tg-baqh">Relevance Value +<br>Text Highlight</td>
  </tr>
  <tr>
    <td class="tg-s6z2">Main</td>
    <td class="tg-s6z2">2P-RndPar-High</td>
    <td class="tg-baqh">23,554</td>
    <td class="tg-baqh">Bin1&amp;Bin2</td>
    <td class="tg-baqh">2-point scale <br>(Relevant, Not Relevant)</td>
    <td class="tg-baqh">Document<br>Paragraphs</td>
    <td class="tg-baqh">Random</td>
    <td class="tg-baqh">Relevance Value +<br>Text Highlight</td>
  </tr>
</table>

