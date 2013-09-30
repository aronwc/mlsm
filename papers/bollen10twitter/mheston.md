####Overview####
The authors present a series of experiments to test whether or not Twitter
sentiment can be used as a predictive measure of the stock market.

####Algorithm####
The analysis uses both OpinionFinder and Google-Proﬁle of Mood States to
get sentiment scores. To compare these time series, they were normalized
to z-scores on the basis of a local mean and standard deviation within a
sliding window of k days before and after the particular date.

####Hypothesis####
Public sentiment as measured by Twitter is correlated with changes in the
Dow Jones Industrial average.

####Data####
9,853,498 tweets by apprixmately 2.7M users from February 28 to December 19, 2008
were collected. Stop words and punctuation were removed, and tweets were grouped by
the date submitted. Only tweets that match certain feeling expressions such as
"I feel" were used, and tweets that contain "http:" or "www." were removed.

####Experiments####
- First, the authors use OF and GPOMS on tweets around Thanksgiving and the 2008
U.S. presidential election to test their ability to capture changes in mood. They
also use a regression model to obtain a relationship between OF moods and the
different mood dimensions of GPOMS.
- They use Granger causality analysis to test the relationship between the
sentiment time series and changes in the stock market.
- They then test a Self-organizing Fuzzy NeuralNetwork with the inputs of past
DIJA values and permutations of the mood time series data to predict DIJA values.

####Results####
- Some mood dimensions from the GPOMS overlap more with OF scores and are more
predictive in these types of analyses. In particular, the Calm attribute seems
very important.
- Their initial mood time series does correlate with changes in the DIJA.
- Their SOFNN model improves the accuracy of DIJA prediction.

####Assumptions####
I'm not entirely sure how the positive/negative lexicon for OF is established, or
if they're updating that lexicon based on the domain they are attempting to apply it
to. If they're not though, there is an assumption that the way people talk about
the stock market is the same way people talk about other things, at least as far
as measuring sentiment goes.


####Synthesis####
There are areas in their initial causality analysis of incongruence between sentiment
and the market, in particular, they point out the bank bailout. I think these particularly
extreme anomalies need to be studied in more detail. For example, given that they were
using the GPMOS, I wonder if these could be identified by a certain mood configuration,
i.e. difference tends to occur when anxiety is high and anger is high.

####Related Papers####
- Bollen, Johan, Huina Mao, and Alberto Pepe. "Modeling public mood and emotion: Twitter sentiment and socio-economic phenomena." ICWSM. 2011.
  - A paper by the same authors that describes more generally the relationship between Twitter sentiment and various cultural events.
- Gilbert, Eric, and Karrie Karahalios. "Widespread Worry and the Stock Market." ICWSM. 2010.
  - Similar to this paper, these authors use LiveJournal data and apply sentiment analysis techniques in predicting stock market changes.
