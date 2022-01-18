Implemented the Analogy-reasoning in python using 50-dim , 400K Vocab-size pre-trained GLove vectors as word-embeddings.
Experimented cosine-similarity, euclid-distance-similarity as similarity measures.

Some results:
* india-->delhi as japan-->tokyo
* small-->smaller as large-->larger

Also observed the biases in the above model which need to be addressed.
Eg. 
* man-->doctor as woman-->nurse
* woman-->doctor as man-->colleague