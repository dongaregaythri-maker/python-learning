#Write a program to find out weather a given post is taking about "Gaythri" or not.
post = input("Enter the post: ")

if "gaythri" in post.lower():
    print("The post is about Gaythri.")
else:
    print("The post is not about Gaythri.")