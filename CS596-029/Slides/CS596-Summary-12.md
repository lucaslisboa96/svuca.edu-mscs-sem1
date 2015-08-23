# Chapter 12: Information Retrieval

[TOC]

> IR (Information Retrieval) are techniques used in pre-processing text documents, for text mining tasks, or web search.

![](https://i.imgur.com/feCvXCb.png)

## Purposes or Applications of IR

* Document or information classification
* Website/blog/news recommending system (by group article/document into different interest groups)
* Spam filtering (by classification SPAM / NOT SPAM)
* Sentiment analysis for marketing
* Email routing & prioritization (important, not important)
* Email advertisement

## IR Queries
Queries can be any of these forms:

* Keyword 
* Boolean (`AND`, `OR`, `NOT`)
* Phrase
* Proximity
* Full document
* Natural Language Questions


## IR Models

These are the popular IR models: Boolean, Naive Bayes, Vector Space, Statistical language model [^statmodel]

### General Terms

#### Document
> **Document** is a phrase, a sentence, or a paragraph that contains multiple words that will be used for future analysis.

#### Document Space
> **Document space** is a set of all documents used for analysis.

#### Vocabulary 
> **Vocabulary** is a list of all the _words_ that come from _all the documents_ in the document space. Vocabulary _must be unique_ (i.e. not duplicated).
> \\( V = {t1, t2, ...,t_{ |V|}} \\)

#### Query
> Query is a set of words (can be combined with logic `AND`, `OR`), which used as search conditions for a document (or multiple documents) in the document space.


### Boolean Model
**Algorithm / Process**

1. Build vocabulary list containing all the terms in the document space  
1. Define each document by a 1-D weight matrix of the corresponding appearance (not frequency) of each term in V. 

	**Example:**
	![](https://i.imgur.com/byNCbgu.png)
	* Combining all documents produces a 2-D matrix defining 
1. Base on the query, try exact matching in each document, if it matches, return it.

**Notes:**

* _Performance of Boolean model is quite poor_ as it does not count duplication of the term in the document, i.e. only 0 or 1, not 2, nor 3... as frequency.
* Looks like this model is good for searching.

### Naive Bayes Model 
**Algorithm / Process**

* **_Objective_**: Classify the **category** of a _query_ (i.e. a test document) base on the _existing classified data_ (training documents).
	1. Calculate probability of each category in D, using formula \\( P(c_i) = \frac{count\_of\_documents\_belong\_to\_c_i}{total\_no\_of\_documents}  \\)
	1. For each word in the vocabulary, calculate *the conditional probability of the word j given the category i*, using this formula \\( P(w_j | c_i) = \frac{n_{ij} + 1}{n_i + |V|} \\), where: 
		* \\( n_{ij} \\) is *total number* of that word *in all documents in category*  \\( c_i \\); and 
		* \\( n_i \\) is the total number of words *in this category/class*.
		* This formular uses *Laplacian Smoothing* *by adding 1 to the dividend*, and *total no of **distinct** element* (\\( |V| \\)) to the divisor, in case the word does not appear in that category.
	1. Now, to calculate the probability if a test document X is in category \\( c_i \\), we use this formular \\( P(X|c_i) = \Pi_{i=1}^n P(w_i | c_i) \\), where:
		* \\( w_i \\) is each word in test document X. 
		* The result of \\( P(w_i | c_i) \\) is taken from calculation in the previous step. Duplication is also considered.
		* Instead of using multiplication as in the formula, which makes the result much smaller and harder to store (since we multiply all <1 numbers), we can sum all \\(log\\) of each prob result. Because \\( x < y \iff log(x) < log(y) \\), and \\( log(xy) = log(x) + log(y) \\)
		* Class result with highest probability score is the most probable.

**Example**
![](https://i.imgur.com/a7gc7eB.png)
![](https://i.imgur.com/xOKC9jR.png)



### Vector Space Model
**Algorithm / Process**

1. Generate the vocabulary of the document space \\( V = \{T_1, T_2, T_3, ... T_n\} \\).

2. Base on the vocabulary, generate a **geometrical vector** of each document which maps the document to the vocabulary, for example \\( D_1 = 2T_1 + 3T_2 + 5T_3, D2 = 3T_1 + 7T_2 + 0T_3\\), etc.

	* If your documents are assigned into different categories, for example: c1={D1, D2} and c2={D3,D4}, you can use a resultant vector [^resultant_vector] to represent all vectors (documents) belong to that category. *The cosine similarity calculation will be much simpler and faster since you just need to compare Query vector with Resultant vector instead with each vectors belong to the category*. 
[^resultant_vector]: Resultant vector is the vector sum of two or more vectors - [Reference](http://www.mathwarehouse.com/vectors/resultant-vector.php).

3. Use **cosine** formular to calculate "proximity" of **query q** to each document \\(d_i\\) (or category's resultant vector), the result that has **biggest value** is the **"closest" to the query**:

	\\( cosine(d_i, q) = \frac{d \cdot q}{||d_j|| * ||q||} \\)
	
	**Note**: You may use Python function `cosine(u,v)` in package `scipy.spatial.distance` to do this calculation. **However**, be careful when using this function it will result in a slightly different computation from the above formula. The result will be  \\( 1 - cosine(d_i, q) = 1 - \frac{d \cdot q}{||d_j|| * ||q||} \\), this measures the **_distance between 2 vectors_**. And thus **the smaller this number is the closer (more similar) the 2 vectors are**. 
	
#### TF-IDF
TF-IDF is a special technique/scheme used in Cosine Similarity method to normalize (tweaking) the weight matrix of document space, for a better [^tf-idf] normalized vector space.

[^tf-idf]: The process weighs up importance word, weighs down common word. 

* **TF (Term Frequency) – \\(tf_{ij}\\)**: if a term \\(t_i\\) appears more requently in document \\(d_j\\) than any other term in all documents, we use it as the normalizing factor, i.e. _divide each freq of each term in a document by this freq_. For example:
		
			| Term-1 | Term-2 | Term-3
			--- | --- | --- | ---
			Doc-1 | 5 | 3 | 2
			Doc-2 | 1 | 2 | 4
			
	We divide each freq in the matrix by 5 since it is the most frequent term. 
	
* **IDF (Inverse Document Frequency) – \\(idf_{i}\\)**: 
			
	\\(idf_i = \log_2 \frac{Total\_no\_of\_documents}{Number\_of\_documents\_containing\_term\_i} \\)
		
* **TF-IDF Weighting**: is calculated base on **TF** and **IDF**, using this formula
		
	\\( w_{ij} = tf{ij} * idf_i = tf_{ij} * \log_2(\frac{N}{df_i})\\)
	
	The main idea behind TF-IDF is to (a) increase the effect of a term that appears more frequent in a document, i.e. **weigh up the important terms**, and at the same time (b) reducing the effect of a term that seems to be too common (appearing too frequent in all documents), i.e. **weigh down the common terms**.
		
	**Example:** 
		
	![](https://i.imgur.com/FFOzCKg.png)

### Example - Compare Boolean vs Cosine vs TF-IDF

![](https://i.imgur.com/XVPFBuL.png)


### Text Pre-Processing Techniques
There are some techniques we can apply to trim  the document content before applying the IR modeling, or even before TF-IDF.

#### Stopwords Removal
> Stop words are usually conjunction or preposition in English, such as *the, of, and, to*...

**Benefits**: 
Removal of stopwords may **reduce the document size significantly**, as well as the indexing table (weight matrix). It **reduces confusion** in retrieval process, and thus **improves** the **efficiency and effectiveness**. 

#### Stemming
> Stemming is a technique used to find the root (or stem) of a word.

**Example:** {users, used, using, user} -> use

**Benefits**: increase matching rate of similar words (after stemming) thus improve recall, and combining words with same roots may reduce indexing size as much as 40-50%. Hence, steming also improves the effectiveness of IR and text mining. 


[^statmodel]: Will not be mentioned in this document.


### Relevance Feedback / Rocchio Text Classifier


