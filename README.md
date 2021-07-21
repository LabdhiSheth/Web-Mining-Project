# Web-Mining-Project - Knowledge discovery and pattern mining in World Wide Web

**Problem Statement**
Explosive Growth of Information sources thus creating the need to utilize automated tools to get desired information. Necessity to mine effectively on server and client side for knowledge, in doing so on server side unique and important issues have risen.

**Scope**
1. Pattern Analysis using technologies like AI, data mining, psychology and information theory.
2. Discovering and analysing patterns of web transactions.
3. Describing Web Usage mining architecture.
4. Research directions on data pre-processing and mining process

There are a few problem gaps that we came across:

1. As we have used indegenious languages input, it can happen that at times not all text is perfectly translated.
2. There are some edges cases like not all stop words relating to indigenious languages are included.
3. Dataset can be very large which would need terabytes of storage and strong servers
4. Limited query interface to individual users

Recent Tweets from within 500km radius of Delhi, India were mined using ‘snscrape’.
Tweets have been taken to find the trending topic in and around Delhi, India.
The data had to be cleaned by deleting unnecessary data, normalizing whitespace, removing stopwordsfor both Hindi and Hinglish, stemming and detecting the language.

● We have used the LDA text mining algorithm.

● Working : LDA assumes all words in a document to be related. They are randomly assigned a topic, and it assumes that except the current assignment, the rest of them are correct.

● Say, proportion of words in document is ‘d’ which are currently assigned a topic ‘t’ is p(topict| documentd) and proportion of assignments topic ‘t’ over all documents that belong to word ‘w’ is p(wordw|topict).

● The probability is found by multiplying the two proportions and then the current word is assigned a topic.

Our implementation was done using:
1. Python language
2. Kaggleinterface for coding
3. Twitter data csvfile
4. Google translator
5. Various libraries for prepossessing and scraping the tweets

**Performance**
The model appropriately assigns a topic and a score to a given test document.
We have defined the number of topics to be 10.
Our model assigns the appropriate topic to the given test document.
