from fastapi import FastAPI, HTTPException
from app.schemas import NewPost

app = FastAPI()

text_posts_data = {
    1: {
        "title": "Testing Display",
        "content": "Just testing how this looks on the screen. Nothing important here."
    },
    2: {
        "title": "Formatting Check",
        "content": "Another sample post to check formatting and spacing."
    },
    3: {
        "title": "Placeholder Content",
        "content": "Lorem ipsum but make it simple—just a placeholder post."
    },
    4: {
        "title": "Text Length Test",
        "content": "Trying out different text lengths in this test message."
    },
    5: {
        "title": "Minimal Post",
        "content": "Short post. Clean and minimal."
    },
    6: {
        "title": "Longer Paragraph Test",
        "content": "This is a slightly longer test post to see how paragraphs behave when there is more content involved."
    },
    7: {
        "title": "Line Break Test",
        "content": "Testing line breaks.\nDoes this go to the next line properly?"
    },
    8: {
        "title": "Random Thoughts",
        "content": "Random thoughts: coffee, code, sleep, repeat."
    },
    9: {
        "title": "Emoji Support",
        "content": "Checking how emojis work 🙂🔥 (if supported)."
    },
    10: {
        "title": "Backend Test",
        "content": "Backend test post for API response validation."
    },
    11: {
        "title": "Frontend Rendering",
        "content": "Frontend rendering test with plain text content."
    },
    12: {
        "title": "Debug Mode",
        "content": "Debugging post: if you see this, things are working fine."
    },
    13: {
        "title": "Blog Preview",
        "content": "Sample content for blog preview testing."
    },
    14: {
        "title": "Special Characters",
        "content": "Testing edge cases with symbols !@#$%^&*()"
    },
    15: {
        "title": "Final Check",
        "content": "Final test post to confirm everything is functioning correctly."
    }
}

@app.get("/text-posts")
def text_posts(limit : int = None):
    if limit :
        return list(text_posts_data.values())[:limit]
    return text_posts_data

@app.get("/posts/{id}")
def get_post(id : int):
    if id not in text_posts_data:
        raise HTTPException(status_code=404, detail="Post Not Found")
    return text_posts_data.get(id) 

@app.post("/create-post")
def create_post(post: NewPost):
    new_post= {"title": post.title, "content": post.content,}
    text_posts_data[max(text_posts_data.keys()) + 1] = new_post
    return new_post