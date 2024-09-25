# # import streamlit as st
# # import pandas as pd
# # import instaloader
# # import time
# # from random import choice
# # import requests

# # # Load proxies


# # def load_proxies():
# #     url = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=ipport&format=text"
# #     response = requests.get(url)
# #     if response.status_code == 200:
# #         proxies = response.text.strip().split("\n")
# #         return proxies
# #     else:
# #         st.error("Failed to retrieve proxies")
# #         return []

# # # Set proxy for Instaloader


# # def set_proxy_session(L, proxy):
# #     session = requests.Session()
# #     session.proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
# #     L.context._session = session

# # # Engagement rate calculation function


# # def calculate_engagement_rate(profile, proxies, L):
# #     proxy = choice(proxies)
# #     set_proxy_session(L, proxy)
# #     time.sleep(10)

# #     # Simulate calculating engagement rate (mockup)
# #     posts = profile.get_posts()
# #     engagement_sum = 0
# #     post_count = 0
# #     for post in posts:
# #         if post_count >= 5:
# #             break
# #         engagement_sum += post.likes
# #         post_count += 1

# #     # Engagement calculation
# #     if post_count > 0:
# #         engagement_rate = (engagement_sum / post_count) / \
# #             profile.followers * 100
# #     else:
# #         engagement_rate = 0

# #     return engagement_rate

# # # Streamlit app


# # def main():
# #     st.title('Instagram Engagement Rate Calculator')

# #     # Upload CSV file
# #     uploaded_file = st.file_uploader(
# #         "Upload a CSV file with Instagram usernames", type="csv")

# #     if uploaded_file is not None:
# #         df = pd.read_csv(uploaded_file)
# #         st.write("Uploaded CSV file:")
# #         st.dataframe(df)

# #         if 'Username' in df.columns:
# #             L = instaloader.Instaloader()
# #             proxies = load_proxies()

# #             results = []
# #             for username in df['Username']:
# #                 try:
# #                     profile = instaloader.Profile.from_username(
# #                         L.context, username)
# #                     engagement_rate = calculate_engagement_rate(
# #                         profile, proxies, L)
# #                     follower_count = profile.followers
# #                     following_count = profile.followees
# #                     real_or_fake = "Real" if engagement_rate > 0.2 or follower_count / \
# #                         following_count >= 0.5 else "Fake"
# #                     results.append(
# #                         [username, follower_count, following_count, profile.mediacount, engagement_rate, real_or_fake])
# #                 except Exception as e:
# #                     st.error(f"Failed to process {username}: {str(e)}")
# #                     continue

# #             # Convert results to DataFrame
# #             result_df = pd.DataFrame(results, columns=[
# #                                      'Username', 'Followers', 'Following', 'Posts', 'Engagement Rate', 'Real/Fake'])

# #             st.write("Processed Results:")
# #             st.dataframe(result_df)

# #             # Convert DataFrame to CSV for download
# #             csv = result_df.to_csv(index=False)
# #             st.download_button(
# #                 label="Download Processed CSV",
# #                 data=csv,
# #                 file_name='processed_instagram_data.csv',
# #                 mime='text/csv'
# #             )
# #         else:
# #             st.error("CSV file must contain a 'Username' column")


# # if __name__ == "__main__":
# #     main()


# import streamlit as st
# import pandas as pd
# import instaloader
# import time

# # Engagement rate calculation function


# def calculate_engagement_rate(profile, L):
#     time.sleep(10)

#     # Simulate calculating engagement rate (mockup)
#     posts = profile.get_posts()
#     engagement_sum = 0
#     post_count = 0
#     for post in posts:
#         if post_count >= 5:
#             break
#         engagement_sum += post.likes
#         post_count += 1

#     # Engagement calculation
#     if post_count > 0:
#         engagement_rate = (engagement_sum / post_count) / \
#             profile.followers * 100
#     else:
#         engagement_rate = 0

#     return engagement_rate

# # Streamlit app


# def main():
#     st.title('Instagram Engagement Rate Calculator')

#     # Upload CSV file
#     uploaded_file = st.file_uploader(
#         "Upload a CSV file with Instagram usernames", type="csv")

#     if uploaded_file is not None:
#         df = pd.read_csv(uploaded_file)
#         st.write("Uploaded CSV file:")
#         st.dataframe(df)

#         if 'Username' in df.columns:
#             L = instaloader.Instaloader()

#             results = []
#             for username in df['Username']:
#                 try:
#                     profile = instaloader.Profile.from_username(
#                         L.context, username)
#                     engagement_rate = calculate_engagement_rate(profile, L)
#                     follower_count = profile.followers
#                     following_count = profile.followees
#                     real_or_fake = "Real" if engagement_rate > 0.2 or follower_count / \
#                         following_count >= 0.5 else "Fake"
#                     results.append([username, follower_count, following_count,
#                                    profile.mediacount, engagement_rate, real_or_fake])
#                 except Exception as e:
#                     st.error(f"Failed to process {username}: {str(e)}")
#                     continue

#             # Convert results to DataFrame
#             result_df = pd.DataFrame(results, columns=[
#                                      'Username', 'Followers', 'Following', 'Posts', 'Engagement Rate', 'Real/Fake'])

#             st.write("Processed Results:")
#             st.dataframe(result_df)

#             # Convert DataFrame to CSV for download
#             csv = result_df.to_csv(index=False)
#             st.download_button(
#                 label="Download Processed CSV",
#                 data=csv,
#                 file_name='processed_instagram_data.csv',
#                 mime='text/csv'
#             )
#         else:
#             st.error("CSV file must contain a 'Username' column")


# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
import instaloader
import os
import time

# Engagement rate calculation function


def calculate_engagement_rate(profile, L):
    time.sleep(10)  # To avoid Instagram's rate limiting

    # Simulate calculating engagement rate (mockup)
    posts = profile.get_posts()
    engagement_sum = 0
    post_count = 0
    for post in posts:
        if post_count >= 5:
            break
        engagement_sum += post.likes
        post_count += 1

    # Engagement calculation
    if post_count > 0:
        engagement_rate = (engagement_sum / post_count) / \
            profile.followers * 100
    else:
        engagement_rate = 0

    return engagement_rate

# Login function


def login_instagram(L):
    session_file = "instaloader_session"

    # Prompt for username
    username = st.text_input("Instagram Username", type="default")

    # Check if session file exists and load it
    if os.path.exists(session_file):
        try:
            L.load_session_from_file(username, session_file)
            st.success("Logged in using the saved session!")
        except Exception as e:
            st.error(
                f"Session file exists but could not be loaded. Error: {str(e)}")
    else:
        # Login to Instagram and save session
        password = st.text_input("Instagram Password", type="password")

        if st.button("Login"):
            try:
                L.login(username, password)
                L.save_session_to_file(session_file)  # Save session to file
                st.success("Successfully logged in and session saved!")
            except Exception as e:
                st.error(f"Login failed: {str(e)}")

# Streamlit app


def main():
    st.title('Instagram Engagement Rate Calculator')

    L = instaloader.Instaloader()

    # Login or load session
    login_instagram(L)

    # Upload CSV file
    uploaded_file = st.file_uploader(
        "Upload a CSV file with Instagram usernames", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded CSV file:")
        st.dataframe(df)

        if 'Username' in df.columns:
            results = []
            for username in df['Username']:
                try:
                    username = username.strip()
                    profile = instaloader.Profile.from_username(
                        L.context, username)
                    engagement_rate = calculate_engagement_rate(profile, L)
                    follower_count = profile.followers
                    following_count = profile.followees
                    real_or_fake = "Real" if engagement_rate > 0.2 or follower_count / \
                        following_count >= 0.5 else "Fake"
                    results.append([username, follower_count, following_count,
                                   profile.mediacount, engagement_rate, real_or_fake])
                except Exception as e:
                    st.error(f"Failed to process {username}: {str(e)}")
                    continue

            # Convert results to DataFrame
            result_df = pd.DataFrame(results, columns=[
                                     'Username', 'Followers', 'Following', 'Posts', 'Engagement Rate', 'Real/Fake'])

            st.write("Processed Results:")
            st.dataframe(result_df)

            # Convert DataFrame to CSV for download
            csv = result_df.to_csv(index=False)
            st.download_button(
                label="Download Processed CSV",
                data=csv,
                file_name='processed_instagram_data.csv',
                mime='text/csv'
            )
        else:
            st.error("CSV file must contain a 'Username' column")


if __name__ == "__main__":
    main()
