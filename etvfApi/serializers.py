from rest_framework import serializers
from django.contrib.auth.models import User
from  etvf.models import *


class KristianaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kristiana
        fields = (
            "id", "kody_kristiana", "anarana_kristiana", "fanampiny_kristiana", "finday_kristiana",
            "mailaka_kristiana", "daty_nandraisana", "sary_kristiana", "vola_vina", "gender", "asa", "mpandray", "maty"
        )


class SondageSerializer(serializers.ModelSerializer):
    kristiana = KristianaSerializer(required=False)

    class Meta:
        model = Sondage
        fields = (
            "id", "mamaky_boky", "mahay_mivavaka", "kristiana"
        )


class SondagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sondage
        fields = (
            "id", "mamaky_boky", "mahay_mivavaka", "kristiana"
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "username"
        )


class ToeranaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toerana
        fields = (
            "id", "anarana_toerana"
        )

    def update(self, instance, validated_data):
        instance.anarana_toerana = validated_data.get('anarana_toerana', instance.anarana_toerana)
        instance.save()
        return instance


class TossaafiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tossaafi
        fields = (
            "id", "kody_tossaafi", "anarana_tossaafi", "daty_nipoirany", "color"
        )

    def update(self, instance, validated_data):
        instance.kody_tossaafi = validated_data.get('kody_tossaafi', instance.kody_tossaafi)
        instance.anarana_tossaafi = validated_data.get('anarana_tossaafi', instance.anarana_tossaafi)
        instance.daty_nipoirany = validated_data.get('daty_nipoirany', instance.daty_nipoirany)
        instance.save()
        return instance


class MpikambanaSerializer(serializers.ModelSerializer):
    kristiana = KristianaSerializer(required=False)
    tossaafi = TossaafiSerializer(required=False)
    toerana = ToeranaSerializer(required=False)

    class Meta:
        model = Mpikambana
        fields = (
            "id", "daty_nahampikambana", "kristiana", "tossaafi", "toerana", "daty_nahampikambana",
        )


class MpikambanaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mpikambana
        fields = (
            "id", "daty_nahampikambana", "kristiana", "tossaafi", "toerana", "daty_nahampikambana",
        )


class AdidySerializer(serializers.ModelSerializer):
    kristiana = KristianaSerializer(required=False)

    class Meta:
        model = Adidy
        fields = (
            "id", "rosia_adidy", "daty_adidy_1", "daty_adidy_2"
            , "daty_nandoavana_adidy", "vola_adidy", "totaly_adidy", "kristiana",
            "toby_voalohany", "toby_faharoa"
        )


class AdidyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adidy
        fields = (
            "id", "rosia_adidy", "daty_adidy_1", "daty_adidy_2"
            , "daty_nandoavana_adidy", "vola_adidy", "totaly_adidy", "kristiana",
            "toby_voalohany", "toby_faharoa"
        )


class KitapoSerializer(serializers.ModelSerializer):
    kristiana = KristianaSerializer(required=False)

    class Meta:
        model = Kitapo
        fields = (
            "id", "rosia_kitapo", "daty_kitapo_1", "daty_kitapo_2",
            "daty_nandoavana_kitapo", "vola_kitapo", "kristiana", 'totaly_vola',
            "toby_voalohany", "toby_faharoa"
        )


class KitapoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitapo
        fields = (
            "id", "rosia_kitapo", "daty_kitapo_1", "daty_kitapo_2",
            "daty_nandoavana_kitapo", "vola_kitapo", "kristiana", "totaly_vola",
            "toby_voalohany", "toby_faharoa"
        )


class LaminasaSerializer(serializers.ModelSerializer):
    tossaafi = TossaafiSerializer(required=False)

    class Meta:
        model = Laminasa
        fields = (
            "id", "daty_laminasa", "asa", "toerana", "tossaafi"
        )


class LaminasaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laminasa
        fields = (
            "id", "daty_laminasa", "asa", "toerana", "tossaafi"
        )
