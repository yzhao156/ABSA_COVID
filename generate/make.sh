# generate datasets

python generate_${1}_NLI_M.py
python generate_${1}_QA_M.py
python generate_${1}_NLI_B_QA_B.py
python generate_${1}_BERT_single.py



python generate_semeval_NLI_M.py
python generate_semeval_QA_M.py
python generate_semeval_NLI_B_QA_B.py
python generate_semeval_BERT_single.py
python generate_sentihood_NLI_M.py
python generate_sentihood_QA_M.py
python generate_sentihood_NLI_B_QA_B.py
python generate_sentihood_BERT_single.py

python generate_semeval_NLI_M.py
python generate_semeval_NLI_B_QA_B.py
#T:\OneDrive - University of Toronto\桌面\ABSA-BERT-pair-master\generate>python generate_semeval_NLI_B_QA_B.py
#Traceback (most recent call last):
#  File "generate_semeval_NLI_B_QA_B.py", line 4, in <module>
#    with open(data_dir+"test_NLI_M.csv","r",encoding="utf-8") as f, \
#FileNotFoundError: [Errno 2] No such file or directory: '../data/semeval2014/bert-pair/test_NLI_M.csv'