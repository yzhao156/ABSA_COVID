# ABSA as a Sentence Pair Classification Task
### Dataset for Covid-19 Country Image:
https://github.com/thunlp/COVID19-CountryImage

aspects : ['politics', 'economy', 'foreign', 'culture','situation', 'measures', 'racism', 'overall']

sentiment : ['unrelated', 'negative', 'neutral', 'positive']

### Results: 
Accuracy: 84%

![alt text](http://https://github.com/yzhao156/ABSA_BERT_PAIR/edit/master/images/Score.png)

The data is extremely imbalance and for most aspects, the data isn't enough. Compare with the Author's approach(BERT), BERT-PAIR didn't perform better. Futher work include research on differet ways to handle the imblance data.
