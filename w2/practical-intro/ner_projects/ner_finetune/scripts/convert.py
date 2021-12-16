
"""Convert LitBank data to spaCy v3
.spacy format."""
import srsly
import typer
import warnings
from pathlib import Path

import spacy
from spacy.tokens import DocBin
from spacy.util import filter_spans
from sklearn.model_selection import train_test_split



def convert(lang: str, test_size:float):
    entities_path = Path.cwd() / 'assets' / 'litbank' / 'entities' / 'brat'
    assert entities_path.exists()
    
    text_files = [f for f in entities_path.iterdir() if f.suffix == '.txt']

    docs = []

    #note: not using pretrained model because it adds predictions, just want LitBank data
    nlp = spacy.blank(lang)

    for text_file in text_files:
        doc = nlp.make_doc(text_file.read_text())
        annotation_file = (entities_path / (text_file.stem +'.ann'))
        annotations = annotation_file.read_text().split('\n')
        ents = []
        for annotation in annotations[:-1]:
            label, start, end = annotation.split('\t')[1].split()
            span = doc.char_span(int(start), int(end), label=label)
            if span: # when start and end do not match a valid string, spaCy returns a NoneType span
                ents.append(span)

        filtered = filter_spans(ents)
        doc.ents = filtered
        docs.append(doc)

    train_set, validation_set = train_test_split(docs, test_size=test_size)
    print(f'Created {len(train_set)} training docs')
    print(f'Created {len(validation_set)} validation docs')
    
    # the DocBin will store the training documents
    train_db = DocBin()
    for doc in train_set:
        train_db.add(doc)
    train_db.to_disk((Path.cwd() / 'corpus' /"train.spacy"))

    # Save the validation Docs to disk 
    validation_db = DocBin()
    for doc in validation_set:
        validation_db.add(doc)

    validation_db.to_disk((Path.cwd() / 'corpus' / "dev.spacy"))


if __name__ == "__main__":
    typer.run(convert)
