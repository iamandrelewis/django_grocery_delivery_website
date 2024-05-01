from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample data (Product ID, Product Name, Product Description)
products = [
    (1, 'Apple', 'Fresh and juicy apples'),
    (2, 'Banana', 'Ripe bananas with a yellow peel'),
    (3, 'Orange', 'Sweet and tangy oranges'),
    (4, 'Carrot', 'Crunchy carrots, perfect for snacking'),
    (5, 'Broccoli', 'Nutrient-rich broccoli florets'),
]

# Convert the data into a DataFrame for easier manipulation
import pandas as pd
df = pd.DataFrame(products, columns=['ProductID', 'ProductName', 'Description'])

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the product descriptions
tfidf_matrix = tfidf_vectorizer.fit_transform(df['Description'])

# Calculate the cosine similarity between products
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to get product recommendations
def get_recommendations(product_id, cosine_similarities=cosine_similarities):
    # Get the index of the product with the given ID
    product_index = df.index[df['ProductID'] == product_id].tolist()[0]

    # Get the cosine similarity scores for the product
    sim_scores = list(enumerate(cosine_similarities[product_index]))

    # Sort the products based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top N similar products (excluding the product itself)
    top_n = 3
    similar_products = sim_scores[1:1+top_n]

    # Get the indices of the similar products
    similar_product_indices = [x[0] for x in similar_products]

    # Get the product names of the recommended products
    recommended_products = df['ProductName'].iloc[similar_product_indices].tolist()

    return recommended_products

# Example: Get recommendations for 'Banana' (ProductID = 2)
product_id_to_recommend = 2
recommendations = get_recommendations(product_id_to_recommend)

# Display the recommendations
print(f"Top recommendations for {df['ProductName'].iloc[product_id_to_recommend-1]}:")
for i, product in enumerate(recommendations, 1):
    print(f"{i}. {product}")
