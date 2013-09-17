####Overview####
This paper tried to find and make use of inner relationships between people’s tweets and their heath conditions. The paper proved reports that extracted form tweets have high correlation with reports that announced by medical organizations, so by mining tweets, geographic syndrome surveillance for multiple ailments will be able to implemented in a low cost and efficient way.

####Algorithm####
- Aliment Topic Aspect Model (ATAM), they use this method to determine and analyze tweets that talk about certain disase. 
- Latent Dirichlet allocation (LDA). 
- ATAM+ is the improved version of ATAM, which use a new method to calculate the precision parameters.

####Hypothesis####
-	People are what they are tweet.Authors think that the tweet people sent have inner relationship with their health conditions and their treatment for certain disease.
-	All the ATAM assumptions (relationships between words and certain ailments or treatments). 

####Data####
- 20 disease articles related to this research.
- 2 billion tweets collected from May 2009 to October 2010
- 1.63 million on topic tweets filtered by SVM.

####Experimental####
- Using Paul and Dredze’s high precision SVM binary classifier to filter tweets, and got 1.63 million on topic tweets. Trained ATAM and ATAM+ by these data.
- For the accuracy issue ailment output was annotated by two people not involved in running the models. The result is relatively favorable, most of the answers matches, but there are still several problems need to be noted. Such as clusters are more general and confusion between similar symptoms and treatments. 
- To further confirm the accuracy of the mining result, they compare the reports to the public health articles, each article was paired with its corresponding ailment in the model output, and these pairings serve as their gold standard alignments. It shows that ATAM+ outperforms ATAM, showing that the priors produced more coherent ailments.
####Results####
The data that author extract from tweets have high correlation rates with reports which published by medical organizations, which means their mining report got really high accuracy, and their hypothesis stands well.

####Assumptions####
- They assume other use of their research method, they think that twitter clearly contains many different types of information of value to public health research on many different ailments.



####Synthesis####
-	To think about the main user of twitter are relatively young and full of energy, the analysis result may be not very accurate for certain disease, for example heart attack.
-	What I really want to do with this method is using the result to help local hospitals to get prepared for burst of certain disease, how to implement rolling forecast is another problem. 
- Or officer of public health can monitor epidemic disease's treatment of normal people, then provide best practice or redress people's method timely.
- Set some alert mechanism on twitter, since it will be more faster than get reports from local medical organization, quicker is always better.

####Related Papers####
- The Use of Twitter to Track Levels of Disease Activity and Public Concern in the U.S. during the Influenza A H1N1 Pandemic
Alessio Signorini, Alberto Maria Segre, Philip M. Polgreen mail
This paper got a brand new concept called disease activity level, measure the Severity of certain disease and set appropriate priority to deal with burst diseases more than one.
- Validating models for disease detection using twitter
Marcel Salathé, Todd Bodnar
This paper analyzed several methods related to disease surveillance, and do some improvements to the methods.
 
