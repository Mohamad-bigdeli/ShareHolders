from rest_framework import serializers
from ...models import Shareholder

class ShareholdersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shareholder
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