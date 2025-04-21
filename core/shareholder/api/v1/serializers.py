from rest_framework import serializers
from ...models import ShareholdersHistory
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from ...documents import ShareholdersDocument

class ShareholdersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShareholdersHistory
        fields = [
            "id", 
            "date",
            "shareholder_id",
            "shareholder_name",
            "shareholder_percentage",
            "shareholder_shares",
            "change",
            "symbol",
            "shareholder_instrument_id",
            "created_at",
            "updated_at"
        ]
        read_only_fields = fields

class ShareholdersDocumentSerializer(DocumentSerializer):

    class Meta:
        document = ShareholdersDocument
        fields = [
            "id", 
            "date",
            "shareholder_id",
            "shareholder_name",
            "shareholder_percentage",
            "shareholder_shares",
            "change",
            "symbol",
            "shareholder_instrument_id",
            "created_at",
            "updated_at"
        ]
        read_only_fields = fields








