from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Product, Review
from main.serializers import ProductListSerializer, ProductDetailsSerializer, ReviewSerializer


@api_view(['GET'])
def products_list_view(request):
    try:
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)

        return Response(serializer.data)
    except Exception as e:
        return Response({"message": str(e)}, status=500)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
            serializer = ProductDetailsSerializer(product)

            return Response(serializer.data)
        except ObjectDoesNotExist as e:
            return Response({"message": str(e)}, status=404)
        except Exception as e:
            return Response({"message": str(e)}, status=500)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        mark = request.GET.get("mark", "")

        if len(mark) == 0:
            reviews = Review.objects.filter(product=product_id)
        elif mark.isdigit():
            reviews = Review.objects.filter(product=product_id, mark=mark)
        else:
            return Response({"message": "Invalid parameter \"mark\"."})

        serializer = ReviewSerializer(reviews, many=True)

        return Response(serializer.data)
