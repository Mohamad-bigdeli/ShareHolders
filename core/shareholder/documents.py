from django_elasticsearch_dsl import Document, Index, fields
from .models import ShareholdersHistory

SHAREHOLDER_INDEX = Index("shareholders")

SHAREHOLDER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=0,
analysis={
        'analyzer': {
            'persian_analyzer': {
                'type': 'custom',
                'tokenizer': 'standard',
                'filter': [
                    'lowercase',
                    'persian_stop',
                    'persian_normalization' 
                ]
            },
            'fuzzy_analyzer': {
                'type': 'custom',
                'tokenizer': 'standard',
                'filter': [
                    'lowercase',
                    'persian_normalization',
                    'edge_ngram_filter' 
                ]
            }
        },
        'filter': {
            'persian_stop': {
                'type': 'stop',
                'stopwords': '_persian_'
            },
            'edge_ngram_filter': {
                'type': 'edge_ngram',
                'min_gram': 2,
                'max_gram': 10
            }
        }
    }
)
@SHAREHOLDER_INDEX.doc_type
class ShareholdersDocument(Document):

    shareholder_name = fields.TextField(
        analyzer='persian_analyzer',
        fields={
            'raw': fields.KeywordField(),
            'suggest': fields.CompletionField(),
            'fuzzy': fields.TextField(analyzer='fuzzy_analyzer')
        }
    )

    symbol = fields.TextField(
        analyzer='persian_analyzer',
        fields={
            'raw': fields.KeywordField(),
            'suggest': fields.CompletionField(),
            'fuzzy': fields.TextField(analyzer='fuzzy_analyzer')
        }
    )

    class Django:
        model = ShareholdersHistory
        fields = [
            "id",
            "date",
            "shareholder_id",
            "shareholder_shares",
            "shareholder_percentage",
            "change",
            "created_at",
            "updated_at"
        ]
    