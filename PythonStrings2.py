# 2. Product Review Analysis
# Objective:
# The aim of this assignment is to extract insights from product reviews by using string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter
# Write a program that searches through a series of product reviews for keywords such as "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords in uppercase so they stand out.

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review. Use a predefined list of positive and negative words to check against. The function should return the count of positive and negative words for each review.

# Task 3: Review Summary
# Implement a script that takes the first 50 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

def highlight_keywords_in_reviews(reviews, keywords):
    
    for review in reviews:
        modified_review = review
        for keyword in keywords:
            # Check if the keyword is in the review
            if keyword in review.lower():
                # Replace keyword with uppercase version
                modified_review = modified_review.replace(keyword, keyword.upper())
                modified_review = modified_review.replace(keyword.capitalize(), keyword.upper())
        print(modified_review)

reviews = [
    "I thought the product was good but could be improved.",
    "This is an excellent product, and I highly recommend it!",
    "Unfortunately, my experience was bad due to a manufacturing defect.",
    "The quality is average, not what I expected at this price point.",
    "Received a damaged item, poor service from the company."
]

keywords = {"good", "excellent", "bad", "poor", "average"}

highlight_keywords_in_reviews(reviews, keywords)

def tally_sentiment(reviews, positive_words, negative_words):

    results = []

    for review in reviews:
        # Initialize counts for this review
        positive_count = 0
        negative_count = 0
        # Normalize the review to lowercase to make comparison case-insensitive
        words = review.lower().split()
        # Count positive and negative words
        for word in words:
            if word in positive_words:
                positive_count += 1
            elif word in negative_words:
                negative_count += 1
        
        results.append((positive_count, negative_count))

    return results

reviews = [
    "I thought the product was good and the quality excellent.",
    "This is an excellent product, and I highly recommend it!",
    "Unfortunately, my experience was bad due to a manufacturing defect.",
    "The quality is average, not what I expected at this price point.",
    "Received a damaged item, poor service from the company."
]

positive_words = {"good", "excellent", "recommend", "highly", "loved"}
negative_words = {"bad", "poor", "damaged", "defect", "average"}

sentiment_counts = tally_sentiment(reviews, positive_words, negative_words)

for review, (pos_count, neg_count) in zip(reviews, sentiment_counts):
    print(f"Review: \"{review}\" \nPositive words: {pos_count}, Negative words: {neg_count}\n")

def summarize_review(review):
    # Check if the review is shorter than or exactly 50 characters
    if len(review) <= 50:
        return review
    # If the review is longer than 50 characters, find the last space within the first 50 characters
    cutoff_point = review[:50].rfind(' ')
    # If there is no space, use the full 50 characters; otherwise, cut off at the last complete word
    if cutoff_point == -1:
        summary = review[:50]
    else:
        summary = review[:cutoff_point]
    
    return summary + "…"

reviews = [
    "I thought the product was good and the quality excellent. Really loved it!",
    "This is an excellent product, and I highly recommend it! Five stars.",
    "Unfortunately, my experience was bad due to a manufacturing defect. Not happy.",
    "The quality is average, not what I expected at this price point. Could be better.",
    "Received a damaged item, poor service from the company. Very disappointed."
]

for review in reviews:
    print(summarize_review(review))