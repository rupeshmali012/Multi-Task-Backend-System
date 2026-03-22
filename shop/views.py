import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product

@api_view(['GET'])
def get_recommendations(request, product_id):
    products = Product.objects.all()
    if not products.exists():
        return Response({"error": "No products found"}, status=404)

    # 1. Database ko AI-readable format mein badlo
    df = pd.DataFrame(list(products.values('id', 'name', 'description')))
    
    # 2. TF-IDF Vectorizer (Text ko numbers mein convert karega)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['description'])
    
    # 3. Cosine Similarity (Dono products kitne similar hain check karega)
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    try:
        # Current product ka index dhundo
        idx = df[df['id'] == int(product_id)].index[0]
        
        # Similar products ke scores nikal lo
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Pehle 3 similar products (khud ko chhod kar)
        product_indices = [i[0] for i in sim_scores[1:4]]
        recommended_products = df.iloc[product_indices]
        
        return Response(recommended_products.to_dict(orient='records'))
    except Exception as e:
        return Response({"error": "Product not found or logic error"}, status=404)

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity', 1))
        
        try:
            product = Product.objects.get(id=product_id)
            
            # Stock Check Karo
            if product.stock >= quantity:
                total_price = product.price * quantity
                
                # Order Save Karo
                order = Order.objects.create(
                    user=request.user,
                    product=product,
                    quantity=quantity,
                    total_price=total_price
                )
                
                # Stock Update Karo (Automatic)
                product.stock -= quantity
                product.save()
                
                return Response({'message': 'Order placed successfully!'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Out of stock!'}, status=status.HTTP_400_BAD_REQUEST)
                
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)