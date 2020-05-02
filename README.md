# knowledge_discovery_WHP
Repository for the experiment ""Knowledge discovery in Workplace Health Promotion Practices"

# Experiment outline

### Objective
To explore how scientific knowledge about Workplace Health Promotion is related, and potential gaps for further research.

### Methods
- Gather all article summaries from JOEM in Pubmed (adv search by Journal w. journal title)
- Parse XML data into a table with columns: `article_id`,`article_title` and `abstract`
- Apply NLP process: Tokenize and remove stopwords, apply Bag of Words and TF-IDF
- Run a clustering algorithm to "label" classes
- Analyze cluster results to manually add a class descriptor
- Apply t-sne to see visual representation of knowledge
- Comment t-sne results

### Preliminary Results
- 4814 titles extracted

### Expected results
- Cluster analysis with topic aggregations
- Visual representation of knowledge
- Research gap analysis
