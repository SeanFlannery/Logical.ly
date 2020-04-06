# Logical.ly
Automated Logical Fallacy Detection (Purdue CS 577 NLP Final Project)


### 1 Problem Description
Detect logical fallacies in raw text.

First, identify if they are logically consistent or contradictory statements at all. This will involve using
currently-existent datasets pertaining to text entailment, and potentially leveraging knowledge graphs.

Second, we seek to identify particular logical fallacies from the text. Examples include “Appeal to Authority”, “Ad Hominem”, and “Strawman”. We have found a suitable corpus for us to scrape examples of logical fallacies
from and will use this to create a tool that can be used to detect particular types of fallacy.


### 2 Literature Review
There exists substantial recent interest in automated fallacy detection both in online forums [2] and when ensuring consistency in formal engineering specifications [7].

Many of the topics related to this work can be found within recent publications of Stanford’s NLP group. After performing our paper critiques within the domain of knowledge graphs, we noticed the works especially of one Gabor Angeli that pertained to extraction of conclusions into the form of KG triplets [4] as well as leveraging this for some shallow reasoning tasks [3]. 

One paper that was especially helpful for identifying features of a good argument was their work pertaining to Argument Quality Assessment [8]. They provide useful methods to evaluate the general quality of arguments that were indispensable in deciding to hone in on identifying particular logical fallacies as a useful additional feature.


### 3 Technical Details

We will start by using simple features like n-grams, word2vec, and TF-IDF with a neural network to classify if a statement is logical/illogical, as well as what type of fallacy it encompasses. Later we will switch to a BERT-like model since they report decent results in reading comprehension [6].

### 4 Evaluation
The dataset we are most likely to use will be the Stanford Natural Language Inference dataset [5]. Examples of entries from the dataset include pairs of text and hypotheses based on those entries. Each has the judgments of five mechanical Turk workers and a consensus judgment as to whether or not the hypothesis is entailed from, contradicted by, or has no effect on the actual hypothesis.

We would be most interested in selecting examples where there exist contradictions or entailments from the original text, so we will use these pairs.

Another option for datasets to use include study guide questions from SAT, GRE, or AP Exam preparation books. These are usually isolated examples that require either minimal or limited external knowledge.

For the part of the project that pertains to identifying particular fallacies, we have chosen to use the website “arguman.org” [1], which is a platform where people analyze the merits of arguments and assign logical fallacies to any contradictory ones. We will use the definitions of logical fallacies from here for our fallacy-labeling tasks.


### 5 Work Plan
#### 5.1 Team Members and Work Distribution
Sean Flannery (sflanner@purdue.edu)
- Training Models
- Knowledge Graph Integration (if the stage is achieved) 
- Final Report Outline + Bulk of Writing

Elnard Utiushev (eutiushe@purdue.edu)
- Website scraping
- Dataset Preparation
- Model Evaluation
- Interactive Website (if we have time)

#### 5.2 Outline
We have broken down the project into several stages that we wish to accomplish, with Stage 1 being the minimum viable product for us to have considered the project successful.
1. Mimic HW1 for political framing, but apply it to detect different types of fallacies.
- Use simple features like n-grams, word2vec, etc.
- Create baseline minimum viable product, classifying statements that are fallacious and non-fallacious (binary decision problem)
- RESULT: Binary classifier for logical/illogical
2. Extend the initial model to multiple types of fallacies.
3. Detection of Consistency/Truth of Statements with Knowledge Graphs
- Apply Stanford Open Information Extraction [4] to create Entity → Relation → Entity triplets
- Use existence of a triplet as a way to measure if a statement was fallacious
- RESULT: Affirm that we can use Knowledge Graphs to validate the truth of statements from the raw text (essential for us to check logical fallacies)
4. Identify Graphical Motifs within Knowledge Graphs Related to Logical Fallacies
- Are there graphical structures inherent inside of knowledge graphs that correspond to common logical fallacies?
- RESULT: Method to go from a series of Entity → Relation triplets to identifying if they correspond to a type of logical fallacy
5. Web tool to identify logical fallacies in raw text
- Service like Grammarly, only name it “Logical.ly” or something akin to that!
- RESULT: Flag probable logical fallacies in one’s own text data
- BONUS: If time allows, even identify the particular fact that was inconsistent.


### References
[1] https://en.arguman.org/fallacies.

[2] The skeptic’s guide to the universe, Jun 2016.

[3] Gabor Angeli, Neha Nayak, and Christopher D Manning. Combining natural logic and shallow reasoning for question answering. In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 442–452, 2016.

[4] Gabor Angeli, Melvin Jose Johnson Premkumar, and Christopher D Manning. Leveraging linguistic structure for open domain information extraction. In Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pages 344–354, 2015.

[5] Samuel R Bowman, Gabor Angeli, Christopher Potts, and Christopher D Manning. A large annotated corpus for learning natural language inference. arXiv preprint arXiv:1508.05326, 2015.

[6] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of Deep Bidirec- tional Transformers for Language Understanding. (Mlm), oct 2018.

[7] Laura G ́omez Rodr ́ıguez. A tool-supported method for fallacies detection in process-based argumentation, 2018.

[8] Henning Wachsmuth, Benno Stein, Graeme Hirst, Vinodkumar Prabhakaran, Yonatan Bilu, Yufang Hou, Nona Naderi, and Tim Alberdingk Thijm. Computational argumentation quality assessment in natural language. In EACL, 2017.
