======================================================================================
=================================Lab 1 Spam Email Filter==============================
======================================================================================

Name: 	Sui Huang
NetID: 	sh4507
UnivID: N13944024
Email:	sh4507@nyu.edu

======================================================================================
=====================================File System======================================
./data				Contain all the data set in the lab
./eval				Contain eval data for result testing
lab1_report.pdf			Lab report
lab1_report.tex			Lab report LaTex code
precisiontable.tex		Precision table transformed from datafram to LaTex table
recalltable.tex			Recall table transformed from datafram to LaTex table
Spam_Filter_NB.ipynb		Jupyter notebook for NB classifiers and eval results
Spam_Filter_SVM.ipynb		Jupyter notebook for SVM classifier
Adverserial_Spam_Filter.ipynb	Jupyter notebook code for extra credit
README.txt			Instruction guide

=======================================================================================
==============================How to reproduce the result==============================

Activate Jupyter Notebook.


To print the Top-N features from ig:
->Open Spam_Filter_NB.ipynb -> run the first few blocks.


For recision and recall matrix of these three classifiers:
a.Bernoulli NB classifier with binary features;
b.Multinomial NB with binary features; and
c.Multinomial NB with term frequency (TF) features
->Open Spam_Filter_NB.ipynb ->Run all the code to the end


For Eval results:
The results are saved in 'results_new.txt' in ./eval
->Open Spam_Filter_NB.ipynb ->Run all the code to the end
Codes for eval are in the last block


For SVM classifier:
->Open Spam_Filter_SVM.ipynb ->Run all the code to the end


For extra credit:
->Open Adverserial_Spam_Filter.ipynb->Run all the code to the end
False Negative rate of the baseline NB classifier before and after the attacker¡¯s 
modifications are printed in the process.
False Negative and False Positive rate of the updated NB classifier are printed at the 
end.

=======================================================================================
=======================================================================================