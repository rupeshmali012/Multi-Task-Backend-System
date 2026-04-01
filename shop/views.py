import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer

# --- Task 4: AI Recommendation Engine Logic ---

@api_view(['GET'])
def get_recommendations(request, product_id):
    """
    AI Engine: Suggests products based on description similarity.
    Uses TF-IDF Vectorization and Cosine Similarity.
    """
    products = Product.objects.all()
    if not products.exists():
        return Response({"error": "No products found"}, status=404)

    # 1. Data Preparation: Converting Django Queryset to a Pandas DataFrame
    df = pd.DataFrame(list(products.values('id', 'name', 'description')))
    
    # 2. Feature Extraction (TF-IDF):
    # Converting text descriptions into numerical vectors, ignoring common 'English' stop words.
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['description'])
    
    # 3. Similarity Calculation:
    # Computing the Cosine Similarity score between all product vectors.
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    try:
        # Finding the index of the product the user is currently viewing
        idx = df[df['id'] == int(product_id)].index[0]
        
        # 4. Sorting: Finding top products with the highest similarity scores
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Selecting top 3 recommendations (excluding the product itself)
        product_indices = [i[0] for i in sim_scores[1:4]]
        recommended_products = df.iloc[product_indices]
        
        return Response(recommended_products.to_dict(orient='records'))
    except Exception as e:
        return Response({"error": "Product not found or logic error"}, status=404)


# --- Task 3: E-commerce Logic (CRUD & Stock Management) ---

class ProductViewSet(viewsets.ModelViewSet):
    """Standard API Viewset for managing the Product Inventory."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """Custom ViewSet for Order processing with inventory validation."""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        """
        Overriding the create method to handle Stock Verification and 
        Automated Price Calculation.
        """
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity', 1))
        
        try:
            product = Product.objects.get(id=product_id)
            
            # 1. Inventory Check: Ensure enough stock is available
            if product.stock >= quantity:
                # 2. Automated Total Price Calculation
                total_price = product.price * quantity
                
                # 3. Create the Order record
                order = Order.objects.create(
                    user=request.user,
                    product=product,
                    quantity=quantity,
                    total_price=total_price
                )
                
                # 4. Stock Reduction: Updating inventory after successful order
                product.stock -= quantity
                product.save()
                
                return Response({'message': 'Order placed successfully!'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Out of stock!'}, status=status.HTTP_400_BAD_REQUEST)
                
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)