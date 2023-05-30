# MUSER

## How to set up
* Python3.7 
* Install all packages in requirement.txt.
```shell script
pip3 install -r requirements.txt
```

## Index a list of documents:
```
python multi_step_retriever.py --index example_docs.jsonl
```

## Train NLI models
* Run *train.py* and specify what Transformer model you would like to fine tune:
```shell script
python train.py --bert_type bert-large --check_point 1
```
Option "--check_point 1" means that we will use the checkpoint technique
during training.

The trained model (that has the best performance on the dev set)
will be saved to directory *output/*.

## Test the performance of the trained models
* To test the performance of a trained model, run the command below:
```shell script
python test_trained_model.py --bert_type bert-large
```


1) Download the model weights and extract them into the `output/nli_model` folder:

 - <a href="https://drive.google.com/drive/folders/1-aPX4HBxe8U3ErzOyoYfs-V5lpmGsVWw?usp=share_link">NLI model</a>


## Main experiment setup parameters

| |PolitiFact| Gossipcop| Weibo|
|-|-|-|-|
| Sequence_length | 512|512 |512 |
| Max_encoder_length | 512|512 |512 |
| Min_decoder_length | 64|64 |64 |
| Max_decoder_length | 128|128 |128 |
| Embedding_dimension | 200| 200| 200|
| k(number of paragraphs retrieved) |30 |30 |30 |
| MSR| 0.3| 0.3| 0.3|
|$lambda$ |0.9 |0.9 |0.9 |
| Retrieve_steps | 2| 3| 3|
| Batch_size |64 |64 |32 |
| Maximum_epochs |10 |10 |10 |
| Vocabulary_size | 30522|30522 | 21128 |
| Learning_rate | 1e-5| 1e-5| 1e-5|





