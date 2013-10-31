**Overview**
	Using two different versions of writing samples and the analysis of features contained within, predict the creators’ location on a scale of High and Low Extraversion and Neuroticism.

**Algorithm**
	This paper identified several possible metrics that the researchers believe could be indicative of the subjects’ extraversion or neuroticism levels. The features either related to the prevalence of function words in the texts or to rules created by Systemic Functional Grammar (SFG). The researchers also analyzed oppositions prevalent within the SFG features in an effort to illustrate the qualities of the features which are more highly indicative of each personality trait.

**Hypothesis**
	A prediction can be made about the author’s extraversion and neuroticism levels from stream-of-consciousness (SOC) and deep self-analysis texts. 

**Data**
	1157 stream-of-consciousness essays and 1106 self-analysis essays were written by students at UTAustin, who then completed a Big Five personality test. The personality results were divided into thirds (High, Middle, Low) and the students were classified accordingly. Data about Function Words, Conjunction, Modality, and Appraisal were collected from the supplied texts as features. 

**Experiments**
	A SMO learning algorithm was applied to the data collected from the essays and personality test, which was then tested with 10-fold cross-validation.

**Results**
	Stream-of-consciousness (SOC) performed better than deep self-analysis (DSA) in most features, which is unsurprising. Appraisal qualified by far as the most indicative of High/Low Neuroticism at 58.2% accuracy (SOC)/ 58.0% accuracy (DSA). A combined-feature approach produced similar accuracy for High/Low Extraversion prediction, but only for the SOC texts. 

**Assumptions**
	The primary assumption in this paper, beyond the idea that personality impacts writing, is that the selected features can identify the selected personality traits. 

**Synthesis**
	It might be more effective to have multiple stream-of-consciousness essays taken over several sessions, to weed out current worries in favor to more persistent, personality-specific thoughts.
 
**Related Papers**
Mairesse, François, et al. "Using Linguistic Cues for the Automatic Recognition of Personality in Conversation and Text." J. Artif. Intell. Res.(JAIR) 30 (2007): 457-500.
	Expands the issue to all Big Five personality traits and utilizes both conversation and text, both self-reported and observed. Also analyzes with classification, regression, and ranking to compare models.
Iacobelli, Francisco, et al. "Large scale personality classification of bloggers." Affective Computing and Intelligent Interaction. Springer Berlin Heidelberg, 2011. 568-577.
	Runs analysis on social media text (blogs) rather than specifically-generated documents using SVM and several linguistic features, some duplicates and some not, to provide best accuracies.
