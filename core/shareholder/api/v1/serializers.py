from __future__ import annotations

from rest_framework import serializers

from ...models import ShareholdersHistory


class ShareholdersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShareholdersHistory
        fields = [
            "id", 
            "date",
            "jalali_date",
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

class ShareholderChangeSerializer(serializers.Serializer):
    shareholder_id = serializers.IntegerField()
    shareholder_name = serializers.CharField(max_length=255)
    current_shares = serializers.IntegerField(required=False)
    previous_shares = serializers.IntegerField(required=False)
    change_shares = serializers.IntegerField(required=False)
    current_percentage = serializers.FloatField(required=False)
    previous_percentage = serializers.FloatField(required=False)
    change_percentage = serializers.FloatField(required=False)
    changes = serializers.CharField(max_length=100)







