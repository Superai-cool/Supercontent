import streamlit as st
import openai
import os

# Streamlit app title
st.title("LinkedIn Engagement Tools")

# Fetch the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("Error: OpenAI API key not found. Please set it as an environment variable.")
else:
    # Tool Selection
    tool = st.selectbox("Select a tool:", ["LinkedIn Comment Creator", "LinkedIn Viral Content Creator"])

    if tool == "LinkedIn Comment Creator":
        st.header("LinkedIn Comment Creator")
        # User input: LinkedIn Post Content
        post_content = st.text_area("Enter the LinkedIn post content:")
        comment_tone = st.selectbox("Choose comment tone:", ["Professional", "Funny", "Formal", "Sarcasm"])

        if st.button("Generate Comment"):
            if post_content.strip():
                def generate_linkedin_comment(api_key, post_content, comment_tone):
                    """
                    Generates a LinkedIn comment based on the provided post content and tone.

                    Parameters:
                        api_key (str): OpenAI API key.
                        post_content (str): The content of the LinkedIn post.
                        comment_tone (str): The tone of the comment.

                    Returns:
                        str: A generated LinkedIn comment.
                    """
                    openai.api_key = api_key

                    prompt = (
                        f"Write a LinkedIn comment in a {comment_tone} tone that is positive, engaging, and concise. Acknowledge the post meaningfully, add value with a relevant thought or question. Limit to 200 characters.\n"
                        f"Post Content: {post_content}\n"
                        "Comment:"
                    )

                    try:
                        response = openai.ChatCompletion.create(
                            model="gpt-4o",
                            messages=[
                                {"role": "system", "content": "You are an expert LinkedIn commenter."},
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=150
                        )

                        comment = response.choices[0].message.content.strip()
                        return comment

                    except openai.error.OpenAIError as e:
                        return f"Error generating comment: {str(e)}"

                # Generate and display the comment
                comment = generate_linkedin_comment(api_key, post_content, comment_tone)
                st.subheader("Generated Comment:")
                st.write(comment)
            else:
                st.error("Post content cannot be empty. Please enter some content.")

    elif tool == "LinkedIn Viral Content Creator":
        st.header("LinkedIn Short, Engaging, Viral Content Creator")
        # User input: Content topic or idea
        content_topic = st.text_area("Enter the topic or idea for the LinkedIn post:")
        post_tone = st.selectbox("Choose post tone:", ["Professional", "Formal", "Funny", "Sarcasm"])

        if st.button("Generate Post"):
            if content_topic.strip():
                def generate_viral_content(api_key, content_topic, post_tone):
                    """
                    Generates a short, engaging, and viral LinkedIn post based on the provided topic or idea and tone.

                    Parameters:
                        api_key (str): OpenAI API key.
                        content_topic (str): The topic or idea for the post.
                        post_tone (str): The tone of the post.

                    Returns:
                        str: A generated LinkedIn post.
                    """
                    openai.api_key = api_key

                    prompt = (
                        f"You are an expert LinkedIn post creator. Generate a short, engaging, and {post_tone} LinkedIn post based on the topic provided."
                        " Use a bold title, concise messaging, clear pointers (using arrows →), and include a call-to-action. Add 5-7 relevant hashtags. Limit to 100 words."
                        f"\nTopic: {content_topic}\nPost:"
                    )

                    try:
                        response = openai.ChatCompletion.create(
                            model="gpt-4o",
                            messages=[
                                {"role": "system", "content": "You are an expert LinkedIn post creator."},
                                {"role": "user", "content": prompt}
                            ],
                            max_tokens=200
                        )

                        post = response.choices[0].message.content.strip()
                        return post

                    except openai.error.OpenAIError as e:
                        return f"Error generating post: {str(e)}"

                # Generate and display the post
                post = generate_viral_content(api_key, content_topic, post_tone)
                st.subheader("Generated Post:")
                st.write(post)
            else:
                st.error("Topic cannot be empty. Please enter a topic or idea.")
