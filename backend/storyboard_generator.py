def generate_storyboard(text):

    lines = text.split("\n")

    topics = []

    for line in lines:

        line = line.strip()

        if len(line) > 5 and len(line) < 60:

            if line not in topics:

                topics.append(line)

        if len(topics) >= 5:

            break

    if not topics:

        return "No topics found."

    storyboard = ""

    for i, topic in enumerate(topics):

        storyboard += (
            f"🎬 Scene {i+1}: "
            f"{topic}\n"
        )

    return storyboard