#### Overview
The authors describe a techniques that can be used to detect bullying on social networking sites, as well
as means to help deter it from taking place.

#### Algorithm
To detect what they call "direct forms" of bullying, the authors use standard classification methods. They
label messages as bullying or not, and train four types of classifiers: Naive Bayes, JRip, J48, and SVM.

They also work to develop what they call "common sense reasoning." This works using ConceptNet, a graph
representaton of common sense knowledge where concepts are represented as nodes and their relationship
is representated as edges. They represent this as a matrix where the rows are concepts and the columns
represent relation edges. They are then able to calculate a degree of similarity between concepts using
the dot product of their concept/feature matrix. In building their BullySpace knowledge base, they use
a blending technique to combine matrices.

#### Hypothesis
Because bullying is personalized and contextual, standard statistical approaches for detection are not
enough, and a common sense model can be used to detect instances of bullying.

#### Data
Comments from a variety of types of YouTube videos were collected. They were annotated along three
labels. 1500 comments under each category where kappa > 0.4 were kept.

The second dataset came from the website FormSpring, and included instances of bullying that were
either user flagged or caught by the moderators.

#### Experiment
Feature design took into account features specific to each label as well as general features. These
included: tf-idf, Ortony lexicon, POS tags, and unigrams and bigrams specific to each label.

YouTube data was divided into 50% training, 30% validation, and 10% test data. They trained and tested
several different classifiers.

Using thei BullySpace knowledge base, concepts are extracted from comments and a similarity score
is computed for these concepts.

#### Results
The supervised machine learning method do pretty well for the direct attacks dataset, achieving
up to .80 accuracy. The classifiers for each individual label outperform the classifier trained
on a mixture. Binary classifiers performed better than multiclass classifiers.

The fifty instances of cyberbullying were given scores on the concepts of "boy" and "girl."
Three annotators then verified the results. They agreed with between 34-38 of the scores.

#### Assumptions
They assume instance of bullying can be understood in terms of these concept relatonships.
In their example of bullying that relies on making comments about a person's sexuality, it
makes sense to look at concepts such as "boy" and "girl" and make an assumption about
what someone's intentions are. For other forms of bullying, I'm not sure this is as straight
forward.

#### Synthesis
As mentioned above, the main problem I have with this paper is that I'm not sure their
model makes sense for all cases of cyberbullying, since they focuses especially on sexuality
based comments. They also applied their knowledge base to comments that had been flagged as
bullying. It would be useful to apply this to an existing social network, and see how well
this method performs at detecting hurtful messages.

#### Related Papers
- Mancilla-Caceres, Juan Fernando, et al. "Identifying Bullies with a Computer Game." AAAI. 2012.
  - Looks at virtual social network dynamics to discover latent characteristics of real world network. A virtual game is analyzed to detect bullies inside the classroom.
