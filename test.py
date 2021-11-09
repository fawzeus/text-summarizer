from summerizer import calculate_sentences_score,calculate_word_frequency, normalize,summerize
import spacy
text ="""Machine learning (ML) is the scientific study of algorithms and statistical models
that computer systems use to progressively improve their performance on a specific task.
Machine learning algorithms build a mathematical model of sample data, known as "training data",
in order to make predictions or decisions without being explicitly programmed to perform the task.
Machine learning algorithms are used in the applications of email filtering, detection of network intruders,
and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task.
Machine learning is closely related to computational statistics, which focuses on making predictions using computers.
The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning.
Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.
In its application across business problems, machine learning is also referred to as predictive analytics."""

nlp=spacy.load("en_core_web_sm")
docx=nlp(text)
words_freaquency=calculate_word_frequency(docx)
normalize(words_freaquency)
sentences_score=calculate_sentences_score(docx,words_freaquency)
print(summerize(sentences_score))
