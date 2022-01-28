data_dir='../data/covid/bert-pair/'

labels=['unrelated', 'neutral', 'negative', 'positive']
with open(data_dir+"test_NLI_M.csv","r",encoding="utf-8") as f, \
    open(data_dir+"test_NLI_B.csv","w",encoding="utf-8") as g_nli, \
    open(data_dir+"test_QA_B.csv","w",encoding="utf-8") as g_qa:
    s=f.readline().strip()
    while s:
        print(s)
        tmp=s.split("\t")
        # print(tmp)
        # print(tmp[2])
        # print('\n')
        for label in labels:
            t_nli = label + " - " + tmp[2]
            t_qa = "the polarity of the aspect " + tmp[2] + " is " + label + " ."
            if tmp[1]==label:
                g_nli.write(tmp[0]+"\t1\t"+t_nli+"\t"+tmp[3]+"\n")
                g_qa.write(tmp[0]+"\t1\t"+t_qa+"\t"+tmp[3]+"\n")
            else:
                g_nli.write(tmp[0]+"\t0\t"+t_nli+"\t"+tmp[3]+"\n")
                g_qa.write(tmp[0]+"\t0\t"+t_qa+"\t"+tmp[3]+"\n")
        s = f.readline().strip()


with open(data_dir+"train_NLI_M.csv","r",encoding="utf-8") as f, \
    open(data_dir+"train_NLI_B.csv","w",encoding="utf-8") as g_nli, \
    open(data_dir+"train_QA_B.csv","w",encoding="utf-8") as g_qa:
    s=f.readline().strip()
    while s:
        print(s)
        tmp=s.split("\t")
        print(tmp)
        print(tmp[2])
        print('\n')
        for label in labels:
            t_nli = label + " - " + tmp[2]
            t_qa = "the polarity of the aspect " + tmp[2] + " is " + label + " ."
            if tmp[1]==label:
                g_nli.write(tmp[0]+"\t1\t"+t_nli+"\t"+tmp[3]+"\n")
                g_qa.write(tmp[0]+"\t1\t"+t_qa+"\t"+tmp[3]+"\n")
            else:
                g_nli.write(tmp[0]+"\t0\t"+t_nli+"\t"+tmp[3]+"\n")
                g_qa.write(tmp[0]+"\t0\t"+t_qa+"\t"+tmp[3]+"\n")
        s = f.readline().strip()