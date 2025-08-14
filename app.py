import streamlit as st
from scraper import get_amazon_reviews, get_flipkart_reviews, get_ebay_reviews
from sentiment import get_best_review

st.title("🔍 Smart Product Review Comparison")
st.write("Type a product name to find top reviews from Amazon, Flipkart, and eBay!")

product_name = st.text_input("Enter a product name:")

if st.button("Find Reviews"):
    if not product_name.strip():
        st.warning("Please enter a product name.")
    else:
        try:
            # Get reviews
            amazon = get_amazon_reviews(product_name)
            flipkart = get_flipkart_reviews(product_name)
            ebay = get_ebay_reviews(product_name)

            # Get best review from each
            best_amazon = get_best_review(amazon)
            best_flipkart = get_best_review(flipkart)
            best_ebay = get_best_review(ebay)

            # Show results
            st.subheader("⭐ Best Reviews:")

            st.markdown("### 🛒 Amazon")
            st.write(best_amazon)

            st.markdown("### 🛒 Flipkart")
            st.write(best_flipkart)

            st.markdown("### 🛒 eBay")
            st.write(best_ebay)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
