from django.db import transaction
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import *
from rest_framework import status
from django.db.models import Q
from datetime import date, datetime
from math import *
from etvfApi.serializers import \
    KristianaSerializer, \
    MpikambanaSerializer, \
    MpikambanaPostSerializer, \
    ToeranaSerializer, \
    TossaafiSerializer, \
    AdidySerializer, \
    KitapoSerializer, \
    KitapoPostSerializer, \
    UserSerializer, \
    AdidyPostSerializer, \
    LaminasaSerializer, \
    LaminasaPostSerializer, \
    SondageSerializer, \
    SondagePostSerializer

from etvf.models import *
from rest_framework.decorators import permission_classes, detail_route, api_view
from rest_framework import permissions
from etvfApi.permissions import HasGroupPermission


# ******** START USER  **************

class CurrentUserAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__']
    }

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class SondageLisitraAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'POST': ['__all__'],
    }

    def get(self, request, format=None):
        sondages = Sondage.objects.all()
        serializer = SondageSerializer(sondages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SondagePostSerializer(data=request.data)
        if serializer.is_valid():
            print('manao akory ', serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SondageAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'PUT': ['__all__'],
        'DELETE': ['__all__'],
    }

    def get(self, request, pk, format=None):
        sondage = Sondage.objects.get(pk=pk)
        serializer = SondageSerializer(sondage)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        sondage = Sondage.objects.get(id=pk)
        sondage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        tossaafi = Tossaafi.objects.get(pk=pk)

        serializer = SondageSerializer(tossaafi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KristianaLisitraAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__']
    }

    def get(self, request, format=None):
        kristianas = Kristiana.objects.all()
        serializer = KristianaSerializer(kristianas, many=True)
        return Response(serializer.data)


class KristianaAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'POST': ['__all__'],
        'PUT': ['__all__'],
        'DELETE': ['__all__'],
    }

    def get(self, request, pk, format=None):
        kristiana = Kristiana.objects.get(pk=pk)
        serializer = KristianaSerializer(kristiana)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KristianaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.data['user'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        kristiana = Kristiana.objects.get(id=pk)
        kristiana.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        kristiana = Kristiana.objects.get(pk=pk)

        serializer = KristianaSerializer(kristiana, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KristianaByKodyAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
    }

    def get(self, reques, pk, format=None):
        kristiana = Kristiana.objects.get(kody_kristiana=pk)
        serializer = KristianaSerializer(kristiana)
        return Response(serializer.data)


class TossaafiLisitraAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__']
    }

    def get(self, request, format=None):
        tossaafis = Tossaafi.objects.all()
        serializer = TossaafiSerializer(tossaafis, many=True)
        return Response(serializer.data)


class TossaafiAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'POST': ['__all__'],
        'PUT': ['__all__'],
        'DELETE': ['__all__'],
    }

    def get(self, request, pk, format=None):
        tossaafi = Tossaafi.objects.get(pk=pk)
        serializer = TossaafiSerializer(tossaafi)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TossaafiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.data['user'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tossaafi = Tossaafi.objects.get(id=pk)
        tossaafi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        tossaafi = Tossaafi.objects.get(pk=pk)

        serializer = TossaafiSerializer(tossaafi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MpikambanaLisitraAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__']
    }

    def get(self, request, format=None):
        mpikambanas = Mpikambana.objects.all()
        serializer = MpikambanaSerializer(mpikambanas, many=True)
        return Response(serializer.data)


class MpikambanaAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'POST': ['__all__'],
        'PUT': ['__all__'],
        'DELETE': ['__all__'],
    }

    def get(self, request, pk, format=None):
        mpikambana = Mpikambana.objects.get(pk=pk)
        serializer = MpikambanaSerializer(mpikambana)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MpikambanaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.data['user'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        mpikambana = Mpikambana.objects.get(id=pk)
        mpikambana.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        mpikambana = Mpikambana.objects.get(pk=pk)

        serializer = MpikambanaSerializer(mpikambana, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MpikambanaByKristianaAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__']
    }

    def get(self, request, kristiana, format=None):
        mpikambanas = Mpikambana.objects.filter(kristiana_id=kristiana)
        serializer = MpikambanaSerializer(mpikambanas, many=True)
        return Response(serializer.data)


class KitapoLisitraAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'POST': ['__all__']
    }

    def get(self, request, format=None):
        kitapos = Kitapo.objects.all()
        serializer = KitapoSerializer(kitapos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KitapoPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KitapoAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'PUT': ['__all__'],
        'DELETE': ['__all__'],
    }

    def get(self, request, pk, format=None):
        kitapo = Kitapo.objects.get(pk=pk)
        serializer = KitapoSerializer(kitapo)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        kitapo = Kitapo.objects.get(id=pk)
        kitapo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        kitapo = Kitapo.objects.get(pk=pk)

        serializer = KitapoSerializer(kitapo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KitapoHamarininaAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
    }

    def get(self, request, format=None):
        daty = date.today()
        user = request.user
        if Kitapo.objects.filter(daty_nandoavana_kitapo=daty.isoformat()).exists():
            kitapos = Kitapo.objects.filter(daty_nandoavana_kitapo=daty.isoformat())
            for kitapo in kitapos:
                # UPDATE DETTE
                newKitapo = {
                    'kristiana': kitapo.kristiana.id,
                    'toby_voalohany': kitapo.toby_voalohany,
                    'toby_faharoa': user.username,
                    'rosia_kitapo': kitapo.rosia_kitapo,
                    'daty_nandoavana_kitapo': kitapo.daty_nandoavana_kitapo,
                    'daty_kitapo_1': kitapo.daty_kitapo_1,
                    'daty_kitapo_2': kitapo.daty_kitapo_2,
                    'vola_kitapo': kitapo.vola_kitapo,
                    'totaly_vola': kitapo.totaly_vola
                }
                serializer = KitapoPostSerializer(kitapo, data=newKitapo)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializers = KitapoSerializer(kitapos, many=True)
            print(serializers)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class KitapoByDatyAnioAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
    }

    def get(self, format=None):
        daty = date.today()
        if Kitapo.objects.filter(daty_nandoavana_kitapo=daty.isoformat()).exists():
            kitapos = Kitapo.objects.filter(daty_nandoavana_kitapo=daty.isoformat())
            serializers = KitapoSerializer(kitapos, many=True)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class KitapoByKristianaAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__']
    }

    def get(self, request, kristiana, format=None):
        kitapos = Kitapo.objects.filter(kristiana_id=kristiana)
        serializer = KitapoPostSerializer(kitapos, many=True)
        return Response(serializer.data)


class KitapoLastAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
    }

    def get(self, request, kristiana, rosia, format=None):
        kitapos = Kitapo.objects.filter(kristiana_id=kristiana, daty_kitapo_1__year=rosia)
        for kitapo in kitapos:
            serializer = KitapoPostSerializer(kitapo)
        return Response(serializer.data)


class KitapoLastByRosiaAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
    }

    def get(self, request, format=None):
        kitapos = Kitapo.objects.filter(rosia_kitapo__startswith='20/')
        print(kitapos)
        for kitapo in kitapos:
            serializer = KitapoPostSerializer(kitapo)
        return Response(serializer.data)


class AdidyLisitraAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'POST': ['__all__']
    }

    def get(self, request, format=None):
        adidy = Adidy.objects.all()
        serializer = AdidySerializer(adidy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdidyPostSerializer(data=request.data)

        print('ireo serializer', serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdidyAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'PUT': ['__all__'],
        'DELETE': ['__all__'],
    }

    def get(self, request, pk, format=None):
        adidy = Adidy.objects.get(pk=pk)
        serializer = AdidySerializer(adidy)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        adidy = Adidy.objects.get(id=pk)
        adidy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        adidy = Adidy.objects.get(pk=pk)

        serializer = AdidySerializer(adidy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdidyByKristianaAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__']
    }

    def get(self, request, kristiana, format=None):
        adidys = Adidy.objects.filter(kristiana_id=kristiana)
        serializer = AdidyPostSerializer(adidys, many=True)
        return Response(serializer.data)


class AdidyLastAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
    }

    def get(self, request, kristiana, rosia, format=None):
        adidys = Adidy.objects.filter(kristiana_id=kristiana, daty_adidy_1__year=rosia)
        for adidy in adidys:
            serializer = AdidyPostSerializer(adidy)
        return Response(serializer.data)


class AdidyLastByRosiaAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
    }

    def get(self, request, format=None):
        adidys = Adidy.objects.filter(rosia_adidy__startswith='20/')
        print(adidys)
        for adidy in adidys:
            serializer = AdidyPostSerializer(adidy)
        return Response(serializer.data)


class AdidyHamarininaAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
    }

    def get(self, request, format=None):
        daty = date.today()
        user = request.user
        if Adidy.objects.filter(daty_nandoavana_adidy=daty.isoformat()).exists():
            adidys = Adidy.objects.filter(daty_nandoavana_adidy=daty.isoformat())
            for adidy in adidys:
                # UPDATE DETTE
                newAdidy = {
                    'kristiana': adidy.kristiana.id,
                    'toby_voalohany': adidy.toby_voalohany,
                    'toby_faharoa': user.username,
                    'rosia_adidy': adidy.rosia_adidy,
                    'daty_nandoavana_adidy': adidy.daty_nandoavana_adidy,
                    'daty_adidy_1': adidy.daty_adidy_1,
                    'daty_adidy_2': adidy.daty_adidy_2,
                    'vola_adidy': adidy.vola_adidy,
                    'totaly_adidy': adidy.totaly_adidy
                }
                serializer = AdidyPostSerializer(adidy, data=newAdidy)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializers = AdidySerializer(adidys, many=True)
            print(serializers)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class AdidyByDatyAnioAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
    }

    def get(self, format=None):
        daty = date.today()
        if Adidy.objects.filter(daty_nandoavana_adidy=daty.isoformat()).exists():
            adidys = Adidy.objects.filter(daty_nandoavana_adidy=daty.isoformat())
            serializers = AdidySerializer(adidys, many=True)
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class LaminasaLisitraAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'POST': ['__all__']
    }

    def get(self, request, format=None):
        laminasas = Laminasa.objects.all()
        serializer = LaminasaSerializer(laminasas, many=True)
        return Response(serializer.data)


class LaminasaAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'PUT': ['__all__'],
        'POST': ['__all__'],
        'DELETE': ['__all__'],
    }

    def get(self, request, pk, format=None):
        laminasa = Laminasa.objects.get(pk=pk)
        serializer = LaminasaSerializer(laminasa)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LaminasaPostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        laminasa = Laminasa.objects.get(id=pk)
        laminasa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        laminasa = Laminasa.objects.get(pk=pk)

        serializer = LaminasaSerializer(kitapo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LaminasaAfterDayAPIView(APIView):
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['__all__'],
        'POST': ['None'],
    }

    def get(self, request, format=None):
        laminasas = []
        firstLaminasas = Laminasa.objects.all().order_by('-id')
        for laminasa in firstLaminasas:
            if laminasa.daty_laminasa is None:
                break
            else:
                dateCount = date.today() - datetime.date(laminasa.daty_laminasa)
                number = dateCount.days
                if number < 0:
                    laminasas.append(laminasa)
        serializer = LaminasaSerializer(laminasas, many=True)
        return Response(serializer.data)
